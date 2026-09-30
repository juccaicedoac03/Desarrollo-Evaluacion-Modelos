# Sesión 01 — Introduction to Generative and Pretrained Models
*Introducción a modelos generativos y preentrenados*

**RAE asociados:** RAE 1, RAE 4, RAE 5 · **Duración:** 3 horas (virtual) · **Fecha:** viernes 2 de octubre de 2026, 18:00–21:00 (hora de Colombia)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. **Diferenciar** los modelos discriminativos, que aprenden p(y | x), de los generativos, que aprenden p(x) o p(x, y), y nombrar las principales familias: autorregresivos (GPT), autoencoders enmascarados (BERT), secuencia a secuencia (T5), VAE, GAN y modelos de difusión. *(RAE 1)*
2. **Explicar** cómo un modelo de lenguaje genera texto token a token y cómo la temperatura, top-k y top-p cambian sus respuestas. *(RAE 1)*
3. **Ejecutar** modelos preentrenados con PyTorch, Keras 3 y Hugging Face en Kaggle. *(RAE 1)*
4. **Ubicar** un caso de negocio en el espectro de adaptación (*prompting* → RAG → *fine-tuning* → entrenamiento desde cero), con argumentos de costo, datos, privacidad y control. *(RAE 4)*
5. **Identificar** oportunidades de IA generativa en tu sector. *(RAE 5)*

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Diagnóstico del grupo y dos preguntas de alfabetización en IA |
| Teoría interactiva | 60' | ¿Qué es la IA generativa? · familias de modelos y modelos fundacionales · modelos propios vs. APIs (simulador *build vs. buy* y salas de trabajo) · herramientas, sectores, ruta del curso y evaluación |
| Descanso | 10' | — |
| Lab guiado | 60' | PyTorch (tensores, autograd y descenso de gradiente) · el mismo modelo en Keras 3 · *pipelines* de Hugging Face y chat con SmolLM2 · tokens y parámetros de generación |
| Challenge | 40' | Temperatura, diversidad y decisión (individual, evaluado) |

## Antes de la clase (≈2 h)

1. **Crea tu cuenta de Kaggle y verifica tu número de celular** (sin verificación no puedes activar Internet ni la GPU en los notebooks). Sigue la [guía de configuración de Kaggle](../../docs/configuracion-kaggle.md). *(≈20 min)*
2. **Lee la [política de uso de IA](../../docs/politica-uso-ia.md)** y la sección de challenges de la [evaluación del curso](../../docs/evaluacion.md): desde hoy cada challenge termina con un registro de uso de IA. *(≈20 min)*
3. **Lectura 1:** Hugging Face, [*LLM Course*, capítulo 1, en español](https://huggingface.co/learn/llm-course/es/chapter1/1): introducción a los Transformers, qué tareas resuelven y cómo funcionan. *(≈45 min)*
4. **Lectura 2:** Bommasani et al. (2021), [*On the Opportunities and Risks of Foundation Models*](https://arxiv.org/abs/2108.07258), sección 1 (introducción: emergencia y homogeneización). *(≈30 min)*
5. Piensa en **un proceso de tu organización** donde la IA generativa podría ayudar: lo usaremos en clase y es la semilla de tu proyecto final.

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/01-intro-generative-models/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/01-intro-generative-models/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/01-intro-generative-models/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/01-intro-generative-models/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/01-intro-generative-models/challenge.ipynb) · [archivo](challenge.ipynb) |

Modelos que usamos hoy (abiertos y pequeños; corren en CPU): `HuggingFaceTB/SmolLM2-135M-Instruct`, `distilbert/distilbert-base-uncased-finetuned-sst-2-english` y `google-bert/bert-base-uncased`.

Las slides y el lab están en inglés; el challenge y esta guía, en español. En las slides, presiona `S` para ver las notas del presentador y `Esc` para ver todas las diapositivas.

## Challenge de la sesión (evaluación)

**Temperatura, diversidad y decisión.** Tu configuración personal (a partir de tu código estudiantil) te asigna 3 prompts de negocio, 2 temperaturas y un escenario de una empresa ficticia.

| Tarea | Qué haces | Componente |
|---|---|---|
| 1 · Ejecución | Generas 5 muestras por prompt × temperatura con SmolLM2-135M-Instruct y mides distinct-1, distinct-2 y la longitud promedio | Ejecución técnica (40%) |
| 2 · Análisis | Interpretas cómo cambiaron la diversidad y la calidad con *tus* números y eliges la mejor temperatura por prompt | Análisis e interpretación (40%) |
| 3 · Explica y decide | Ubicas tu escenario en el espectro de adaptación (costo, datos, privacidad, control, al menos un riesgo) usando tu estimación de tokens | Análisis e interpretación (40%) |
| 4 · Crítica a la IA | Encuentras, explicas y corriges 3 errores en un párrafo "generado por IA" que compara BERT y GPT | Análisis e interpretación (40%) |
| Reflexión y registro de IA | Reflexión breve y tabla de uso de asistentes de IA | Reflexión y registro de IA (20%) |

- **Rúbrica:** ejecución técnica 40% · análisis e interpretación 40% · reflexión y registro de IA 20% (descriptores por nivel en la [evaluación del curso](../../docs/evaluacion.md)).
- **Entrega:** ejecuta todo el notebook, descárgalo (`Archivo → Descargar notebook`) y súbelo a **e-Aulas** como `S01_<codigo>.ipynb` antes de las **23:59 de hoy**. Verifica que se vean "Tu configuración personal" y la huella de resultados.
- **Reglas de IA:** puedes usar asistentes de IA, pero debes registrarlos (sin registro, ese 20% vale 0.0) y eres responsable de lo que entregas. En las **micro-sustentaciones** (2–3 minutos, sin IA) explicas una celda de tu trabajo; si no puedes hacerlo, la nota máxima del challenge es 3.0. Detalles en la [política de uso de IA](../../docs/politica-uso-ia.md).

## Después de la clase (trabajo independiente ≈7 h)

1. **Termina y entrega el challenge** si no alcanzaste en clase (hasta las 23:59). *(≈1 h)*
2. **Repite el lab por tu cuenta** y resuelve los ejercicios 🧪 *Try it* antes de abrir las soluciones. *(≈1.5 h)*
3. **Explora el Hugging Face Hub:** para un caso de uso de tu organización, encuentra 3 modelos candidatos y anota para cada uno la tarea, el tamaño, el idioma y la licencia de su *model card*. *(≈1 h)*
4. **Lecturas de profundización** (elige dos): Vaswani et al. (2017); Devlin et al. (2019); el capítulo 20 de Goodfellow, Bengio y Courville (2016); Bender et al. (2021). *(≈2.5 h)*
5. **Proyecto final:** lee el [enunciado del proyecto](../../proyecto-final/README.md) y empieza a conversar con posibles compañeros. **Los grupos de 3 se conforman en la Sesión 03** (hito H1); se recomienda mezclar perfiles de negocio y técnicos. *(≈1 h)*
6. **Prepara las sesiones 02 y 03 antes del sábado a las 7:00:** el sábado 3 de octubre hay dos sesiones seguidas (7:00–10:00 y 10:00–13:00), así que haz antes la sección "Antes de la clase" de ambas guías ([Sesión 02](../02-training-generative-models/README.md) y [Sesión 03](../03-transfer-learning/README.md)).

## Lecturas y recursos

**Lecturas de la sesión**

- Bommasani, R., Hudson, D. A., Adeli, E., et al. (2021). *On the opportunities and risks of foundation models*. arXiv:2108.07258. https://arxiv.org/abs/2108.07258
- Hugging Face. *LLM Course*, capítulo 1 (edición en español). https://huggingface.co/learn/llm-course/es/chapter1/1

**Fuentes primarias citadas en clase**

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *NeurIPS*. https://arxiv.org/abs/1706.03762
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *NAACL*. https://arxiv.org/abs/1810.04805
- Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). *Language models are unsupervised multitask learners*. OpenAI.
- Sanh, V., Debut, L., Chaumond, J., & Wolf, T. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. arXiv:1910.01108. https://arxiv.org/abs/1910.01108
- Raffel, C., et al. (2020). Exploring the limits of transfer learning with a unified text-to-text transformer. *JMLR*. https://arxiv.org/abs/1910.10683
- Brown, T. B., et al. (2020). Language models are few-shot learners. *NeurIPS*. https://arxiv.org/abs/2005.14165
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press. https://www.deeplearningbook.org/
- Kingma, D. P., & Welling, M. (2014). Auto-encoding variational Bayes. *ICLR*. https://arxiv.org/abs/1312.6114
- Goodfellow, I., et al. (2014). Generative adversarial nets. *NeurIPS*. https://arxiv.org/abs/1406.2661
- Ho, J., Jain, A., & Abbeel, P. (2020). Denoising diffusion probabilistic models. *NeurIPS*. https://arxiv.org/abs/2006.11239
- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS*.
- Hu, E. J., et al. (2022). LoRA: Low-rank adaptation of large language models. *ICLR*.
- Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2020). The curious case of neural text degeneration. *ICLR*. https://arxiv.org/abs/1904.09751
- Li, J., Galley, M., Brockett, C., Gao, J., & Dolan, B. (2016). A diversity-promoting objective function for neural conversation models. *NAACL*. https://arxiv.org/abs/1510.03055 *(origen de la métrica distinct-n del challenge)*
- Allal, L. B., et al. (2025). SmolLM2: When smol goes big — data-centric training of a small language model. arXiv:2502.02737. https://arxiv.org/abs/2502.02737

**Negocio, riesgos y contexto latinoamericano**

- McKinsey & Company (2023). *The economic potential of generative AI: The next productivity frontier*. https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier
- Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *FAccT*. https://doi.org/10.1145/3442188.3445922
- CENIA. *Índice Latinoamericano de Inteligencia Artificial (ILIA)*. https://indicelatam.cl/

**Documentación de herramientas**

- PyTorch, *Learn the basics*: https://pytorch.org/tutorials/beginner/basics/intro.html
- Keras 3 (multi-backend): https://keras.io/keras_3/
- Hugging Face, plantillas de chat: https://huggingface.co/docs/transformers/main/en/chat_templating
- Hugging Face, estrategias de generación: https://huggingface.co/docs/transformers/generation_strategies
- Kaggle Notebooks: https://www.kaggle.com/docs/notebooks
