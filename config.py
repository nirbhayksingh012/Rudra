import torch

# Training settings (Optimized for GTX 1650 4GB VRAM)
batch_size = 16       # Reduced batch size to fit in 4GB VRAM
block_size = 384      # Context window (up from 256, but not 512 to save VRAM)
max_iters = 8000      # More iterations for larger dataset
eval_interval = 400   # Evaluate every 400 steps
learning_rate = 3e-4  # Standard learning rate for transformers
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 100      # Number of validation batches to average over

# Learning rate schedule
warmup_iters = 500    # Linear warmup for first 500 steps
lr_decay_iters = 8000 # Cosine decay over full training
min_lr = 1e-5         # Minimum learning rate after decay

# Gradient clipping
max_grad_norm = 1.0   # Clip gradients to prevent exploding gradients

# Model architecture settings (Fits in GTX 1650 4GB VRAM)
n_embd = 256          # Embedding dimension (keep at 256 for VRAM safety)
n_head = 8            # More attention heads (256 / 8 = 32 per head)
n_layer = 8           # Deeper network for better reasoning (8 layers)
dropout = 0.2         # Dropout rate

# Data path
data_path = 'data/input.txt'
checkpoint_path = 'rudra.pth'
