# Ejecutar los notebooks en tu propio computador

*Guía opcional. La forma recomendada de trabajar en el curso es [Kaggle](configuracion-kaggle.md): tiene GPU gratuita y no requiere instalar nada.*

Los labs y los challenges también corren en tu computador, con Jupyter. Esta opción te sirve si ya trabajas con Python, si tu conexión a Kaggle es inestable o si quieres seguir practicando después del curso. Todo lo que se califica es igual: entregas el mismo archivo `.ipynb` en e-Aulas.

---

## 1. Antes de empezar: ¿te conviene?

| Situación | Recomendación |
|---|---|
| Nunca has instalado Python o no tienes permisos de administrador | Usa Kaggle |
| Tienes un computador con GPU NVIDIA y drivers CUDA | Local funciona muy bien |
| Tienes un Mac (Intel o Apple Silicon) o un portátil sin GPU | Local funciona en CPU; ver los tiempos de la sección 5 |
| Tienes menos de 8 GB de RAM o menos de 10 GB libres en disco | Usa Kaggle |

**Requisitos mínimos:** Python 3.11 o 3.12, 8 GB de RAM, unos 10 GB libres en disco (librerías y modelos que se descargan la primera vez) e internet para la primera ejecución de cada notebook.

## 2. Instalación (una sola vez)

1. **Descarga el repositorio.** Con git:

   ```bash
   git clone https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos.git
   ```

   o descarga el ZIP desde GitHub (*Code → Download ZIP*) y descomprímelo. Trabaja siempre dentro de esa carpeta: los notebooks buscan sus archivos de datos en la carpeta `data/` de cada sesión.

2. **Crea un entorno virtual** dentro de la carpeta del repositorio.

   macOS / Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Windows (PowerShell):

   ```powershell
   py -3.12 -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Instala las librerías del curso:**

   ```bash
   pip install -r requirements.txt
   ```

   La instalación descarga PyTorch y Transformers, así que puede tardar varios minutos. Si tienes GPU NVIDIA, instala primero la versión de PyTorch con CUDA siguiendo [pytorch.org](https://pytorch.org/get-started/locally/) y después ejecuta el comando anterior.

4. **Abre Jupyter:**

   ```bash
   jupyter lab
   ```

   y abre `sessions/NN-<tema>/lab.ipynb` o `challenge.ipynb`. También puedes usar VS Code o Cursor con la extensión de Jupyter, eligiendo el intérprete de `.venv`.

> Los notebooks traen una función `ensure(...)` que instala con `pip` cualquier librería que falte. Aun así, instala `requirements.txt` antes: así evitas instalaciones a mitad de clase.

## 3. Cada vez que trabajes

1. Activa el entorno (`source .venv/bin/activate` o `.venv\Scripts\Activate.ps1`).
2. Actualiza los materiales antes de cada sesión: `git pull` (o vuelve a descargar el ZIP). Los notebooks pueden recibir correcciones durante el curso.
3. Abre `jupyter lab` y ejecuta el notebook desde la primera celda.

**Challenges: trabaja sobre una copia.** Antes de empezar un challenge, duplica el archivo (por ejemplo, `S03_<codigo>.ipynb`) para que `git pull` no choque con tus cambios. Ese mismo archivo, guardado con sus salidas, es el que subes a e-Aulas.

## 4. Startti fuera de Kaggle

En Kaggle la API key se guarda en *Secrets*. En tu computador se guarda como **variable de entorno** `STARTTI_API_KEY`, definida **antes** de abrir Jupyter en la misma terminal:

macOS / Linux:

```bash
export STARTTI_API_KEY="pega-aqui-tu-clave"
jupyter lab
```

Windows (PowerShell):

```powershell
$env:STARTTI_API_KEY = "pega-aqui-tu-clave"
jupyter lab
```

La celda del cliente de Startti debe imprimir `Startti key found ✅`. **Nunca escribas la clave dentro del notebook**: el archivo se entrega y queda en e-Aulas. Si no tienes clave, los notebooks usan la alternativa en Python, igual que en Kaggle. Cómo obtener la clave: [configuración de Startti](configuracion-startti.md).

## 5. GPU, CPU y tiempos

- **GPU NVIDIA:** los notebooks la detectan solos (`Dispositivo: cuda` en la primera celda).
- **Mac y equipos sin GPU NVIDIA:** los notebooks corren en CPU (`Dispositivo: cpu`). El curso no usa la GPU de Apple (MPS) a propósito, porque varias librerías todavía fallan con ella.
- **Tiempos en CPU:** la mayoría de labs y challenges termina en pocos minutos en un portátil. Los más pesados son S04 (afinamiento de DistilBERT y LoRA), S08 (clasificación con Qwen2.5-0.5B) y S09 (varios modelos). Para ellos, si tu equipo es lento, usa Kaggle con GPU.
- **Primera ejecución:** cada modelo se descarga una vez (de decenas de MB a 1 GB) y queda guardado en la caché de Hugging Face (`~/.cache/huggingface`).

## 6. Sin internet

Cada notebook comprueba al inicio que puede llegar a Hugging Face y, si no puede, se detiene con un mensaje. Si ya ejecutaste antes ese notebook y los modelos están en la caché, puedes trabajar sin conexión definiendo `HF_HUB_OFFLINE=1` antes de abrir Jupyter:

```bash
export HF_HUB_OFFLINE=1        # Windows PowerShell: $env:HF_HUB_OFFLINE = "1"
jupyter lab
```

Algunos notebooks descargan datasets o archivos del repositorio que quizá no estén en tu caché. Si una celda falla sin conexión, conéctate y vuelve a ejecutarla.

## 7. No uses el modo de prueba en tus entregas

El repositorio usa la variable `COURSE_FAST_DEV_RUN=1` para probar automáticamente los notebooks con datos muy reducidos. **No la definas en tu computador:** cambia los tamaños de los datos, rellena un código estudiantil de prueba y tus resultados no coincidirían con tu configuración personal ni con la huella de resultados.

## 8. Problemas frecuentes

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| `No module named ...` | El notebook no está usando el entorno `.venv` | En Jupyter, *Kernel → Change kernel* y elige el de `.venv`; o abre `jupyter lab` con el entorno activado |
| `No internet connection` / `Sin conexión a internet` al inicio | Sin conexión, o un proxy o firewall bloquea `huggingface.co` | Revisa la conexión o la red; si los modelos ya están en caché, usa `HF_HUB_OFFLINE=1` (sección 6) |
| `STARTTI_API_KEY not found` | La variable no estaba definida al abrir Jupyter | Ciérralo, define la variable en la misma terminal y vuelve a abrirlo (sección 4) |
| El kernel se reinicia o se queda sin memoria | RAM insuficiente para el modelo | Cierra otros programas, reinicia el kernel y ejecuta de nuevo; si persiste, usa Kaggle |
| Una celda tarda mucho en CPU | Modelo o entrenamiento pesado (S04, S08, S09) | Espera o usa Kaggle con GPU |
| `pip install` falla al instalar `torch` | Versión de Python no soportada | Usa Python 3.11 o 3.12 |
| La app de Gradio no abre | Bloqueo del navegador o de la red | Usa el enlace local (`http://127.0.0.1:7860`) que imprime la celda |

Si nada de esto funciona, vuelve a Kaggle y pregunta en el foro del curso: la ejecución local es opcional y no cambia los plazos de entrega.
