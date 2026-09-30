# ✏️ Escribe tu código estudiantil (como aparece en e-Aulas) y tu nombre completo.
STUDENT_ID = ""
STUDENT_NAME = ""

# --- Configuración del curso (no editar) ---
import os, sys, random, subprocess, importlib, hashlib, json
SESSION = "S01"
FAST_DEV_RUN = os.environ.get("COURSE_FAST_DEV_RUN") == "1"
IN_KAGGLE = "KAGGLE_KERNEL_RUN_TYPE" in os.environ
IN_COLAB = "google.colab" in sys.modules
if FAST_DEV_RUN and not STUDENT_ID.strip():
    STUDENT_ID, STUDENT_NAME = "000000", "Prueba automática"
assert STUDENT_ID.strip(), "⚠️ Escribe tu STUDENT_ID en la primera línea de esta celda y vuelve a ejecutarla."

def ensure(package, import_name=None):
    """Instala un paquete solo si falta."""
    try:
        importlib.import_module(import_name or package)
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", package], check=True)

PERSONAL_SEED = int(hashlib.sha256(f"{SESSION}:{STUDENT_ID.strip()}".encode()).hexdigest()[:8], 16)
rng = random.Random(PERSONAL_SEED)

def pick(options):
    """Elige una opción de forma determinística a partir de tu código estudiantil."""
    return rng.choice(list(options))

import numpy as np
import torch
random.seed(PERSONAL_SEED); np.random.seed(PERSONAL_SEED % (2**32)); torch.manual_seed(PERSONAL_SEED)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Sesión {SESSION} | Estudiante: {STUDENT_NAME} ({STUDENT_ID}) | Semilla personal: {PERSONAL_SEED} | Dispositivo: {DEVICE}")
# --- fin de la configuración ---
