# --- Course setup (do not edit) ---
import os, sys, random, subprocess, importlib
FAST_DEV_RUN = os.environ.get("COURSE_FAST_DEV_RUN") == "1"  # used by the course smoke test
IN_KAGGLE = "KAGGLE_KERNEL_RUN_TYPE" in os.environ
IN_COLAB = "google.colab" in sys.modules

def ensure(package, import_name=None):
    """Install a package only if it is missing (Kaggle already ships most of them)."""
    try:
        importlib.import_module(import_name or package)
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", package], check=True)

import socket
if os.environ.get("HF_HUB_OFFLINE") != "1":  # models and datasets come from the Hugging Face Hub
    try:
        socket.create_connection(("huggingface.co", 443), timeout=10).close()
    except OSError:
        raise RuntimeError(
            "No internet connection: this notebook downloads models and datasets from Hugging Face.\n"
            "Kaggle: in the right-hand panel open Settings (Session options) and switch Internet on. "
            "The switch only appears once your account is phone-verified (kaggle.com/settings). "
            "Then run this cell again. Colab has internet by default."
        ) from None

import numpy as np
import torch
SEED = 42
random.seed(SEED); np.random.seed(SEED); torch.manual_seed(SEED)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device: {DEVICE} | Kaggle: {IN_KAGGLE} | Colab: {IN_COLAB} | Fast dev run: {FAST_DEV_RUN}")
# --- end of course setup ---
