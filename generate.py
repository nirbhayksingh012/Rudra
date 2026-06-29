import os
import torch
import argparse
from tokenizer import CharacterTokenizer
from model import Rudra
import config

def main():
    # 1. Argument parsing
    parser = argparse.ArgumentParser(description="Generate text using trained Rudra model.")
    parser.add_argument(
        "--prompt", 
        type=str, 
        default="\n", 
        help="Prompt to seed the text generator. Default is a newline."
    )
    parser.add_argument(
        "--num_tokens", 
        type=int, 
        default=500, 
        help="Number of characters to generate."
    )
    parser.add_argument(
        "--temp", 
        type=float, 
        default=0.8, 
        help="Sampling temperature. Lower is more conservative, higher is more creative/random."
    )
    parser.add_argument(
        "--top_k", 
        type=int, 
        default=50, 
        help="Top-k filtering parameter. If specified, crops logits to top-k options."
    )
    args = parser.parse_args()

    # 2. Check if checkpoint file exists
    if not os.path.exists(config.checkpoint_path):
        print(f"Error: Checkpoint file '{config.checkpoint_path}' not found.")
        print("Please train the model first by running: python train.py")
        return

    # 3. Load text to rebuild tokenizer (to ensure exact match with training vocabulary)
    if not os.path.exists(config.data_path):
        print(f"Error: Training dataset not found at '{config.data_path}' to construct tokenizer.")
        return

    with open(config.data_path, 'r', encoding='utf-8') as f:
        text = f.read()

    tokenizer = CharacterTokenizer(text)
    vocab_size = tokenizer.vocab_size

    # 4. Instantiate and load model
    print(f"Loading Rudra model from checkpoint: {config.checkpoint_path}")
    model = Rudra(vocab_size)
    model.load_state_dict(torch.load(config.checkpoint_path, map_location=config.device,weights_only=True))
    model.to(config.device)
    model.eval()

    # 5. Encode the prompt
    print(f"Generating {args.num_tokens} characters seeded with prompt: {repr(args.prompt)}")
    encoded_prompt = tokenizer.encode(args.prompt)
    if not encoded_prompt:
        # Fallback to newline if prompt mapping is completely empty
        encoded_prompt = tokenizer.encode("\n")

    # Shape: (1, T)
    x = torch.tensor([encoded_prompt], dtype=torch.long, device=config.device)

    # 6. Generate and decode
    print("=" * 60)
    with torch.no_grad():
        generated_idx = model.generate(
            x, 
            max_new_tokens=args.num_tokens, 
            temperature=args.temp, 
            top_k=args.top_k
        )
        # generated_idx is shape (1, T + max_new_tokens)
        output_text = tokenizer.decode(generated_idx[0].tolist())
        print(output_text)
    print("=" * 60)

if __name__ == "__main__":
    main()
