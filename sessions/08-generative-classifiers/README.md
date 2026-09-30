# Sesión 08 — Building Classifiers with Generative Models
*Creación de clasificadores con modelos generativos*

**RAE asociados:** RAE 1, RAE 2, RAE 3 · **Duración:** 3 horas (virtual)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. Contrastar clasificadores **generativos** (Naive Bayes) y **discriminativos** (regresión logística) con la regla de Bayes y anticipar cuándo gana cada uno según la cantidad de datos (Ng y Jordan, 2002).
2. Entrenar Naive Bayes, regresión logística y una red MLP en **PyTorch** sobre *embeddings* de oraciones, y leer una curva de aprendizaje.
3. Usar un LLM como clasificador **zero-shot** puntuando la log-verosimilitud de cada etiqueta (verbalizadores), sin generar texto libre.
4. Diseñar un experimento de **aumento con datos sintéticos** sin fugas hacia el conjunto de prueba, y revisar la **calibración** de las probabilidades.
5. Recomendar un clasificador según restricciones de **costo, latencia y privacidad**.

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Tres preguntas de repaso de la Sesión 07 (intents y slots, agentes, métricas de chatbots) |
| Teoría | 60' | Generativos vs. discriminativos · simulador de fronteras de decisión · Ng y Jordan con datos reales · VAE y LLM como clasificadores generativos · simulador de suma vs. media de log-probabilidades · datos sintéticos · calibración · calculadora de costos · sala de grupos: recomendar un clasificador para 3 restricciones |
| Descanso | 10' | — |
| Lab guiado | 60' | Tuits financieros: NB vs. regresión logística con curva de aprendizaje, MLP en PyTorch (y su versión en Keras), zero-shot con Qwen2.5-0.5B por log-verosimilitud, aumento sintético de la clase bajista y tabla resumen |
| Challenge | 40' | Challenge individual calificado (se entrega hasta las 23:59) |

## Antes de la clase (≈2 h)

- **Lectura principal:** Tunstall, von Werra y Wolf (2022), capítulo 2 (clasificación de texto).
- **Repaso breve:** Jurafsky y Martin (2023), primeras secciones del capítulo 4 (Naive Bayes) y del capítulo 5 (regresión logística).
- **Repasa tus notebooks** de la Sesión 02 (el codificador de un VAE) y de la Sesión 03 (clasificación zero-shot y few-shot con un LLM): hoy los conectamos.
- **Kaggle:** verifica que tu cuenta tenga el teléfono verificado para poder activar la GPU.

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/08-generative-classifiers/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/08-generative-classifiers/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/08-generative-classifiers/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/08-generative-classifiers/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/08-generative-classifiers/challenge.ipynb) · [archivo](challenge.ipynb) |
| Guía de Kaggle | [configuracion-kaggle.md](../../docs/configuracion-kaggle.md) |

**Datos y modelos:** [`zeroshot/twitter-financial-news-sentiment`](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment) (tuits en inglés etiquetados como bajista, alcista o neutral), `sentence-transformers/all-MiniLM-L6-v2` y `Qwen/Qwen2.5-0.5B-Instruct`. En Kaggle activa **Internet** y, si puedes, la **GPU T4 x2** (en CPU también corre, solo que las partes con el LLM son más lentas).

## Challenge de la sesión (evaluación)

Challenge **individual** y **personalizado**: tu código estudiantil define cuántos ejemplos etiquetados tienes (`n_train` entre 30 y 240), qué clase minoritaria vas a aumentar (bajista o alcista), tu porción de 60 tuits de prueba y el perfil de restricción de tu cliente (presupuesto, latencia o privacidad).

| Tarea | Qué haces | Componente |
|---|---|---|
| 1 | Naive Bayes vs. regresión logística vs. LLM zero-shot en tu porción: accuracy, macro-F1, F1 de tu clase minoritaria y latencia | Ejecución técnica |
| 2 | Aumento sintético de tu clase minoritaria con el LLM: lees los ejemplos, reentrenas y comparas antes y después | Análisis e interpretación |
| 3 | **Explica y decide:** recomiendas un clasificador para tu cliente con tus números de calidad, latencia y costo | Análisis e interpretación |
| 4 | **Crítica a la IA:** encuentras, explicas y corriges tres fugas de datos en un código generado por un asistente | Análisis e interpretación |

- **Rúbrica:** Ejecución técnica 40% · Análisis e interpretación 40% · Reflexión y registro de IA 20% (ver [evaluación](../../docs/evaluacion.md)).
- **Entrega:** ejecuta todo en orden, descarga el notebook (`File → Download notebook`) y súbelo a **e-Aulas** como **`S08_<codigo>.ipynb`** antes de las **23:59** de hoy.
- **Uso de IA:** permitido con registro obligatorio al final del notebook ([política de uso de IA](../../docs/politica-uso-ia.md)). Puede haber **micro-sustentaciones**: si no puedes explicar tu entrega, la nota se limita a 3.0.

## Después de la clase (trabajo independiente ≈7 h)

- **Cierra el challenge** y entrégalo antes de las 23:59 (≈1 h si no lo terminaste en clase).
- **Proyecto final (≈4 h):** entrena o afina el primer modelo de tu grupo y compáralo con una **línea base simple** (por ejemplo, TF-IDF + regresión logística o un zero-shot) con al menos dos métricas justificadas. Si tu caso es de clasificación, incluye la curva de aprendizaje y revisa la calibración.
- **Práctica autónoma (≈1 h):** resuelve los ejercicios 🧪 *Try it* del lab (conteos para Naive Bayes, pesos de clase en la MLP, calibración contextual del LLM, temperatura en la generación sintética).
- **Lectura (≈1 h):** Ng y Jordan (2002) y la sección de resultados de Møller et al. (2024).
- **Prepara la Sesión 09:** trae una idea de caso de uso de tu sector para el canvas del proyecto (hito formativo de S09).

## Lecturas y recursos

- Ng, A. Y., & Jordan, M. I. (2002). On discriminative vs. generative classifiers: A comparison of logistic regression and naive Bayes. En *Advances in Neural Information Processing Systems 14*.
- Jurafsky, D., & Martin, J. H. (2023). *Speech and language processing* (3.ª ed., borrador), caps. 4 y 5. [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/)
- Tunstall, L., von Werra, L., & Wolf, T. (2022). *Natural language processing with transformers: Building language applications with Hugging Face* (ed. rev.), cap. 2. O'Reilly Media.
- Kingma, D. P., Rezende, D. J., Mohamed, S., & Welling, M. (2014). Semi-supervised learning with deep generative models. En *Advances in Neural Information Processing Systems 27*. [https://arxiv.org/abs/1406.5298](https://arxiv.org/abs/1406.5298)
- Zhao, Z., Wallace, E., Feng, S., Klein, D., & Singh, S. (2021). Calibrate before use: Improving few-shot performance of language models. En *ICML 2021*. [https://arxiv.org/abs/2102.09690](https://arxiv.org/abs/2102.09690)
- Holtzman, A., West, P., Shwartz, V., Choi, Y., & Zettlemoyer, L. (2021). Surface form competition: Why the highest probability answer isn't always right. En *EMNLP 2021*. [https://aclanthology.org/2021.emnlp-main.564/](https://aclanthology.org/2021.emnlp-main.564/)
- Møller, A. G., Pera, A., Dalsgaard, J., & Aiello, L. (2024). The parrot dilemma: Human-labeled vs. LLM-augmented data in classification tasks. En *EACL 2024 (short papers)*. [https://aclanthology.org/2024.eacl-short.17/](https://aclanthology.org/2024.eacl-short.17/)
- Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. En *ICML 2017*. [https://arxiv.org/abs/1706.04599](https://arxiv.org/abs/1706.04599)
- Pérez, J. M., Rajngewerc, M., Giudici, J. C., Furman, D. A., Luque, F., Alonso Alemany, L., & Martínez, M. V. (2023). pysentimiento: A Python toolkit for opinion mining and social NLP tasks. [https://arxiv.org/abs/2106.09462](https://arxiv.org/abs/2106.09462) — herramienta de análisis de sentimiento desarrollada en Argentina, con modelos para tuits en español.
- Hugging Face. Curso de LLM en español: [https://huggingface.co/learn/llm-course/es/chapter1/1](https://huggingface.co/learn/llm-course/es/chapter1/1)
