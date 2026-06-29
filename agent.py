import re
import torch
import config
from tools import calculate, web_search

# Regex to parse tool calls: <|tool_call|>tool_name("argument")<|end_tool|>
TOOL_CALL_RE = re.compile(r"<\|tool_call\|>(\w+)\((.*?)\)<\|end_tool\|>")

def build_context_with_memory(tokenizer, prompt: str, history=None) -> str:
    """
    Constructs the prompt context from history and the current prompt.
    Trims older history entries if the context exceeds the available context size.
    """
    if history is None:
        history = []
        
    # We want to leave at least 150 tokens for output generation.
    # So max context length = block_size - 150
    max_context_len = config.block_size - 150
    
    # We start with the full history and reduce it if it's too long
    active_history = list(history)
    
    while True:
        # Build context string
        context_parts = []
        for msg in active_history:
            role = msg.get("role")
            text = msg.get("text", "")
            if role == "user":
                context_parts.append(f"<|user|>{text}\n")
            elif role == "assistant":
                context_parts.append(f"<|assistant|>{text}<|end|>\n")
                
        # Append current user prompt
        context_parts.append(f"<|user|>{prompt}\n<|assistant|>")
        context_str = "".join(context_parts)
        
        # Check token length
        encoded = tokenizer.encode(context_str)
        if len(encoded) <= max_context_len or len(active_history) == 0:
            return context_str
            
        # Too long! Drop the oldest message
        active_history.pop(0)

def run_agent_loop(model, tokenizer, prompt: str, history=None, num_tokens: int = 300, temperature: float = 0.7, top_k: int = 50):
    """
    Executes a custom agent loop. Runs Rudra generation. If it emits a tool call, 
    executes it using tools.py, feeds the result back, and runs generation again.
    """
    # Track which tools were executed for UI indicators
    tool_activities = []
    
    # Build context using historical memory window
    current_context = build_context_with_memory(tokenizer, prompt, history)
    
    # We allow up to 3 tool calls per turn to prevent infinite loops
    max_loops = 3
    
    for loop_idx in range(max_loops):
        # Encode current context
        encoded = tokenizer.encode(current_context)
        if not encoded:
            encoded = tokenizer.encode("\n")
            
        x = torch.tensor([encoded], dtype=torch.long, device=config.device)
        stop_seq = tokenizer.encode("<|end|>")
        
        # Run generation
        with torch.no_grad():
            generated_idx = model.generate(
                x, 
                max_new_tokens=num_tokens, 
                temperature=temperature, 
                top_k=top_k,
                stop_sequence=stop_seq
            )
            full_output = tokenizer.decode(generated_idx[0].tolist())
            
        # Extract what was generated in this turn
        generated_part = full_output[len(current_context):]
        
        # Check if there is a tool call inside the generated part
        match = TOOL_CALL_RE.search(generated_part)
        if match:
            tool_name = match.group(1)
            # Clean up the argument
            tool_arg = match.group(2).strip().strip('"').strip("'")
            
            # Execute the tool
            print(f"Agent Loop [Turn {loop_idx+1}]: Executing '{tool_name}' with arg '{tool_arg}'")
            if tool_name == "calculate":
                result = calculate(tool_arg)
            elif tool_name == "web_search":
                result = web_search(tool_arg)
            else:
                result = f"Error: Tool '{tool_name}' is not recognized."
                
            # Log the activity
            tool_activities.append({
                "tool": tool_name,
                "query": tool_arg,
                "result": result
            })
            
            # Formulate the updated context including the tool result
            generated_call_str = generated_part[:match.end()]
            current_context = (
                current_context + 
                generated_call_str + 
                f"\n<|tool_result|>{result}<|end_tool_result|>\n<|assistant|>"
            )
            continue
        else:
            # No tool call generated. This is our final response!
            final_response = generated_part
            if final_response.endswith("<|end|>"):
                final_response = final_response[:-7]
                
            return {
                "response": final_response.strip(),
                "tool_activities": tool_activities
            }
            
    # If we exceeded max loops, return whatever we generated last
    final_response = generated_part
    if final_response.endswith("<|end|>"):
        final_response = final_response[:-7]
    return {
        "response": final_response.strip(),
        "tool_activities": tool_activities
    }
