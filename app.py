from contextlib import asynccontextmanager
import os
import random
from typing import List, Optional
import torch
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from tokenizer import CharacterTokenizer
from model import Rudra
from agent import run_agent_loop
import config

# Global variables for model and tokenizer
model = None
tokenizer = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model, tokenizer
    print("Loading tokenizer and dataset...")
    if not os.path.exists(config.data_path):
        raise RuntimeError(f"Dataset file '{config.data_path}' is missing.")
    
    with open(config.data_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    tokenizer = CharacterTokenizer(text)
    vocab_size = tokenizer.vocab_size

    print(f"Loading Rudra model from checkpoint: {config.checkpoint_path}")
    if not os.path.exists(config.checkpoint_path):
        raise RuntimeError(f"Model checkpoint file '{config.checkpoint_path}' not found. Please train the model first.")

    model = Rudra(vocab_size)
    model.load_state_dict(torch.load(config.checkpoint_path, map_location=config.device, weights_only=True))
    model.to(config.device)
    model.eval()
    print(f"Rudra successfully loaded on device: {config.device}")
    yield

# Initialize FastAPI App with lifespan handler
app = FastAPI(
    title="Rudra API Server",
    description="Backend API serving text generation requests from the trained Rudra model.",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for Next.js development server (default port 3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Predefined seed prompts/presets
PRESETS = [
    "hi",
    "hello",
    "what is your name?",
    "who created you?",
    "45 + 12",
    "95 - 40",
    "bye"
]

class HistoryMessage(BaseModel):
    role: str
    text: str

class GenerationRequest(BaseModel):
    prompt: str = Field(default="", description="Prompt text to start generation. If empty, a random seed is selected.")
    history: Optional[List[HistoryMessage]] = Field(default=None, description="Recent conversation history list.")
    num_tokens: int = Field(default=300, ge=1, le=1000, description="Number of tokens to generate.")
    temperature: float = Field(default=0.8, ge=0.1, le=2.0, description="Sampling temperature.")
    top_k: int = Field(default=50, ge=1, le=200, description="Top-k vocabulary options to restrict sampling.")

@app.post("/api/generate")
async def generate_text(req: GenerationRequest):
    global model, tokenizer
    if model is None or tokenizer is None:
        raise HTTPException(status_code=503, detail="Model is not loaded yet.")

    try:
        # Check if prompt is empty or whitespace. If so, pick a random seed preset
        prompt_to_use = req.prompt.strip()
        if not prompt_to_use:
            prompt_to_use = random.choice(PRESETS)

        # Run the agent loop
        # Convert history objects to standard dictionaries for agent loop
        history_dicts = []
        if req.history:
            history_dicts = [{"role": h.role, "text": h.text} for h in req.history]

        agent_result = run_agent_loop(
            model=model,
            tokenizer=tokenizer,
            prompt=prompt_to_use,
            history=history_dicts,
            num_tokens=req.num_tokens,
            temperature=req.temperature,
            top_k=req.top_k
        )

        return {
            "prompt": prompt_to_use,
            "generated_text": agent_result["response"],
            "tool_activities": agent_result["tool_activities"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent loop execution failed: {str(e)}")

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "device": config.device,
        "model_loaded": model is not None
    }

if __name__ == "__main__":
    import uvicorn
    # Start the server on port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)
