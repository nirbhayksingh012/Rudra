import os
import math
# pyrefly: ignore [missing-import]
import torch
import matplotlib.pyplot as plt
from tqdm import tqdm
from tokenizer import CharacterTokenizer
from model import Rudra
import config

# Set random seed for reproducibility
torch.manual_seed(1337)

def get_lr(iter_num):
    """Learning rate schedule: linear warmup then cosine decay."""
    # Linear warmup
    if iter_num < config.warmup_iters:
        return config.learning_rate * (iter_num + 1) / config.warmup_iters
    # Cosine decay
    if iter_num > config.lr_decay_iters:
        return config.min_lr
    decay_ratio = (iter_num - config.warmup_iters) / (config.lr_decay_iters - config.warmup_iters)
    coeff = 0.5 * (1.0 + math.cos(math.pi * decay_ratio))
    return config.min_lr + coeff * (config.learning_rate - config.min_lr)

def main():
    # 1. Load the dataset
    data_path = config.data_path
    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"Dataset not found at {data_path}. Please verify it was downloaded."
        )

    with open(data_path, 'r', encoding='utf-8') as f:
        text = f.read()

    print(f"Loaded dataset: {data_path}")
    print(f"Dataset length in characters: {len(text):,}")
    print(f"Dataset size: {len(text) / 1024:.1f} KB")

    # 2. Build the tokenizer
    tokenizer = CharacterTokenizer(text)
    vocab_size = tokenizer.vocab_size
    print(f"Vocabulary size: {vocab_size}")

    # 3. Encode the text data and split into train/val
    data = torch.tensor(tokenizer.encode(text), dtype=torch.long)
    n = int(0.9 * len(data)) # 90% train, 10% validation
    train_data = data[:n]
    val_data = data[n:]
    print(f"Train tokens: {len(train_data):,} | Val tokens: {len(val_data):,}")

    # 4. Data loading function
    def get_batch(split):
        # generate a small batch of data of inputs x and targets y
        data_split = train_data if split == 'train' else val_data
        ix = torch.randint(len(data_split) - config.block_size, (config.batch_size,))
        x = torch.stack([data_split[i:i+config.block_size] for i in ix])
        y = torch.stack([data_split[i+1:i+config.block_size+1] for i in ix])
        x, y = x.to(config.device), y.to(config.device)
        return x, y

    # 5. Helper function to estimate loss on train & val splits
    @torch.no_grad()
    def estimate_loss(model):
        out = {}
        model.eval()
        for split in ['train', 'val']:
            losses = torch.zeros(config.eval_iters)
            for k in range(config.eval_iters):
                X, Y = get_batch(split)
                logits, loss = model(X, Y)
                losses[k] = loss.item()
            out[split] = losses.mean().item()
        model.train()
        return out

    # 6. Instantiate the model
    print(f"\nInitializing Rudra on device: {config.device}")
    print(f"Architecture: {config.n_layer} layers, {config.n_head} heads, {config.n_embd} embed dim, {config.block_size} context")
    model = Rudra(vocab_size)
    model.to(config.device)

    # Print number of parameters
    num_params = sum(p.numel() for p in model.parameters()) / 1e6
    print(f"Model size: {num_params:.2f}M parameters")

    # 7. Optimizer (AdamW with weight decay)
    optimizer = torch.optim.AdamW(model.parameters(), lr=config.learning_rate, weight_decay=0.01)

    # Variables to track loss history for plotting
    iters = []
    train_losses = []
    val_losses = []
    best_val_loss = float('inf')

    # 8. Training Loop
    print(f"\nStarting training for {config.max_iters} iterations...")
    print(f"LR schedule: warmup {config.warmup_iters} steps -> cosine decay to {config.min_lr}")
    print(f"Gradient clipping: max_norm={config.max_grad_norm}")
    print("=" * 60)

    for iter in tqdm(range(config.max_iters), desc="Training"):
        # Update learning rate
        lr = get_lr(iter)
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr

        # Periodically evaluate loss on train and val sets
        if iter % config.eval_interval == 0 or iter == config.max_iters - 1:
            losses = estimate_loss(model)
            print(f"\nStep {iter}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}, lr {lr:.6f}")
            
            iters.append(iter)
            train_losses.append(losses['train'])
            val_losses.append(losses['val'])

            # Save best model checkpoint
            if losses['val'] < best_val_loss:
                best_val_loss = losses['val']
                torch.save(model.state_dict(), config.checkpoint_path)
                print(f"  [OK] Saved best checkpoint (val loss {best_val_loss:.4f})")

        # Get batch and run step
        xb, yb = get_batch('train')
        logits, loss = model(xb, yb)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()

        # Gradient clipping for training stability
        torch.nn.utils.clip_grad_norm_(model.parameters(), config.max_grad_norm)
        optimizer.step()

    print("\n" + "=" * 60)
    print(f"Training complete! Best val loss: {best_val_loss:.4f}")

    # 9. Plot the loss curves
    plt.figure(figsize=(10, 6))
    plt.plot(iters, train_losses, label='Train Loss', color='#FF6B6B', linewidth=2)
    plt.plot(iters, val_losses, label='Val Loss', color='#4D96FF', linewidth=2)
    plt.xlabel('Iteration')
    plt.ylabel('Cross Entropy Loss')
    plt.title('Rudra Training and Validation Loss (Scaled Model)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig('loss_plot.png', dpi=150)
    plt.close()
    print("Loss plot saved to loss_plot.png")

    # 10. Generate sample text to verify it runs
    print("\nGenerating sample text from the best checkpoint...")
    model.load_state_dict(torch.load(config.checkpoint_path, weights_only=True))
    model.eval()

    test_prompts = [
        "hello",
        "what is your name?",
        "What is the capital of India?",
        "45 + 12",
        "What will happen tomorrow?",
    ]

    stop_seq = tokenizer.encode("<|end|>")

    for prompt_text in test_prompts:
        formatted = f"<|user|>{prompt_text}\n<|assistant|>"
        encoded = tokenizer.encode(formatted)
        x = torch.tensor([encoded], dtype=torch.long, device=config.device)
        
        with torch.no_grad():
            generated = model.generate(x, max_new_tokens=200, temperature=0.7, top_k=50, stop_sequence=stop_seq)
            full_output = tokenizer.decode(generated[0].tolist())

        # Extract response
        response = full_output[len(formatted):]
        if response.endswith("<|end|>"):
            response = response[:-7]

        print(f"\n{'-' * 50}")
        print(f"  Q: {prompt_text}")
        print(f"  A: {response.strip()}")
    
    print(f"{'-' * 50}")

if __name__ == "__main__":
    main()
