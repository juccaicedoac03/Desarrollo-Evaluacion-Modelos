# Sesión 03 — Pretrained Models and Transfer Learning
*Modelos preentrenados y transferencia de aprendizaje*

**RAE asociados:** RAE 1, RAE 3 · **Duración:** 3 horas (virtual) · **Fecha:** sábado 3 de octubre de 2026, 10:00–13:00 (hora de Colombia)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. **Explicar** por qué el preentrenamiento autosupervisado (predecir el siguiente token o un token enmascarado) produce conocimiento reutilizable, con sus sesgos incluidos. *(RAE 1)*
2. **Describir** la autoatención, softmax(QKᵀ/√d_k)·V, y contrastar BERT (codificador), GPT (decodificador) y T5 (codificador-decodificador). *(RAE 1)*
3. **Medir** cuántos tokens más ocupa el español con distintos tokenizadores y traducirlo a costo, contexto y latencia. *(RAE 3)*
4. **Construir** un clasificador con embeddings congelados y regresión logística, y **compararlo** con clasificación *zero-shot* y *few-shot* con un LLM pequeño. *(RAE 1, RAE 3)*
5. **Elegir** una estrategia de transferencia y un modelo (tamaño, licencia, idioma) para un caso de negocio. *(RAE 3)*

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Tres preguntas de repaso de la S02: ciclo de entrenamiento, sobreajuste y β en un VAE |
| Teoría interactiva | 60' | Por qué funciona el preentrenamiento · Transformer: tokens, embeddings y atención (simulador de mapa de atención) · BERT, GPT y T5 · tokenización y costo en español (calculadora de tokens) · estrategias de transferencia (sala de trabajo: 4 escenarios) · elegir un modelo y modelos en español (BETO) |
| Descanso | 10' | — |
| Lab guiado | 60' | Tokenizadores BERT vs. GPT-2 (y Qwen2.5) en inglés y español · *fill-mask* con BERT · embeddings + regresión logística en AG News · *zero-shot* y *few-shot* con Qwen2.5-0.5B-Instruct · tabla comparativa · conformación de grupos |
| Challenge | 40' | ¿Cuántos datos necesitas? (individual, evaluado) |

## Antes de la clase (≈2 h)

La S02 y la S03 son seguidas (sábado 3 de octubre, 7:00 y 10:00): haz esta preparación antes del sábado.

1. **Lectura 1:** Alammar, J. (2018), [*The Illustrated Transformer*](https://jalammar.github.io/illustrated-transformer/): la explicación visual de la atención que usaremos en clase. *(≈40 min)*
2. **Lectura 2:** Hugging Face, [*LLM Course*, capítulo 2, en español](https://huggingface.co/learn/llm-course/es/chapter2/1): modelos, tokenizadores y cómo se conectan. *(≈45 min)*
3. **Lectura 3 (rápida):** el [repositorio de BETO](https://github.com/dccuchile/beto) (Universidad de Chile): qué es, con qué datos se entrenó y qué dice sobre su licencia. *(≈15 min)*
4. **Proyecto final:** habla con posibles compañeros. **Hoy se conforman los grupos de 3** (hito H1); lee la sección 3 del [enunciado del proyecto](../../proyecto-final/README.md), con el bloque de registro del grupo. *(≈20 min)*

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/03-transfer-learning/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/03-transfer-learning/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/03-transfer-learning/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/03-transfer-learning/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/03-transfer-learning/challenge.ipynb) · [archivo](challenge.ipynb) |
| Proyecto final (hito H1) | [Enunciado y bloque de registro del grupo](../../proyecto-final/README.md) |

Modelos y datos de hoy (abiertos, sin registro): `google-bert/bert-base-uncased`, `openai-community/gpt2`, `sentence-transformers/all-MiniLM-L6-v2`, `Qwen/Qwen2.5-0.5B-Instruct` y el dataset [`fancyzhx/ag_news`](https://huggingface.co/datasets/fancyzhx/ag_news) (noticias en 4 temas: World, Sports, Business, Sci/Tech).

**Kaggle:** activa Internet. La GPU (*GPU T4 x2*) es recomendable para la parte del LLM, pero todo corre también en CPU. Las slides y el lab están en inglés; el challenge y esta guía, en español. En las slides, presiona `S` para ver las notas del presentador.

## Challenge de la sesión (evaluación)

**¿Cuántos datos necesitas?** Tu configuración personal (a partir de tu código estudiantil) te asigna `k_train` (16, 64, 256 o 1.024 ejemplos etiquetados por clase), `n_shots` (1, 2 o 4 ejemplos por clase en el prompt), un corte personal de noticias de prueba y un caso de negocio de una empresa ficticia.

| Tarea | Qué haces | Componente |
|---|---|---|
| 1 · Curva de aprendizaje | Embeddings congelados de MiniLM + regresión logística con tu `k_train` y con 16, 64 y 256 ejemplos por clase; graficas e interpretas la curva | Ejecución técnica (40%) |
| 2 · Few-shot vs. clasificador | Clasificas 40 noticias de tu corte con Qwen2.5-0.5B en *zero-shot* y *few-shot* y comparas exactitud, latencia, tokens de prompt y errores de formato con tu clasificador | Ejecución técnica (40%) · Análisis (40%) |
| 3 · Explica y decide | Recomiendas estrategia de transferencia y modelo (tamaño, idioma, licencia) para tu caso de negocio, con tus números, un riesgo y qué te haría cambiar de opinión | Análisis e interpretación (40%) |
| 4 · Crítica a la IA | Encuentras, explicas y corriges 3 errores en una explicación "generada por IA" sobre atención y transferencia, con dos evidencias en código | Análisis e interpretación (40%) |
| Reflexión y registro de IA | Reflexión breve y tabla de uso de asistentes de IA | Reflexión y registro de IA (20%) |

- **Rúbrica:** ejecución técnica 40% · análisis e interpretación 40% · reflexión y registro de IA 20% (descriptores por nivel en la [evaluación del curso](../../docs/evaluacion.md)).
- **Entrega:** ejecuta todo el notebook, descárgalo (`Archivo → Descargar notebook`) y súbelo a **e-Aulas** como `S03_<codigo>.ipynb` antes de las **23:59 de hoy**. Verifica que se vean "Tu configuración personal" y la huella de resultados.
- **Reglas de IA:** puedes usar asistentes de IA, pero debes registrarlos (sin registro, ese 20% vale 0.0) y eres responsable de lo que entregas. En las **micro-sustentaciones** (2–3 minutos, sin IA) explicas una celda de tu trabajo; si no puedes hacerlo, la nota máxima del challenge es 3.0. Detalles en la [política de uso de IA](../../docs/politica-uso-ia.md).

## Proyecto final: hito H1 (hoy)

- Conformen **grupos de 3** (idealmente con perfiles de negocio y técnicos). Solo con autorización del profesor puede haber grupos de 2 o de 4.
- Un integrante sube el registro del grupo a e-Aulas como **`PF_H1_<codigo>`** (con su propio código estudiantil) antes de las **23:59 de hoy**. El bloque que deben copiar y completar está en la sección 3 del [enunciado del proyecto](../../proyecto-final/README.md).
- El hito es formativo pero obligatorio: si no se entrega a tiempo, descuenta 0.3 de la nota del entregable técnico. A quien no tenga grupo al cierre, el profesor le asigna uno.
- Pista para la idea preliminar: piensen qué estrategia de transferencia de hoy encaja con los datos que podrían conseguir.

## Después de la clase (trabajo independiente ≈7 h)

1. **Termina y entrega el challenge** (23:59) y el **registro del grupo** `PF_H1_<codigo>`. *(≈1.5 h)*
2. **Repite el lab por tu cuenta** y resuelve los ejercicios 🧪 *Try it* antes de abrir las soluciones; en especial, cambia `K_PER_CLASS` y `SHOTS_PER_CLASS` y observa la tabla comparativa. *(≈1.5 h)*
3. **Mide tu propio texto:** toma 10 frases reales de tu trabajo en español y cuenta sus tokens con los tokenizadores del lab. ¿Cuál es tu razón ES/EN? *(≈30 min)*
4. **Lecturas de profundización** (elige dos): Vaswani et al. (2017), secciones 3.1–3.3; Devlin et al. (2019), secciones 3 y 5; Cañete et al. (2020); Jurafsky y Martin, capítulos sobre Transformers y modelos de lenguaje grandes. *(≈2.5 h)*
5. **Proyecto:** reúnanse como grupo, acuerden su idea preliminar y busquen en el Hugging Face Hub dos modelos candidatos (idioma, tamaño y licencia de su *model card*). *(≈1 h)*
6. **Prepara la S04 (afinamiento, viernes 9 de octubre):** revisa tu cuota de GPU en Kaggle; el lab de la próxima sesión la necesita.

## Lecturas y recursos

**Lecturas de la sesión**

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *NeurIPS*. https://arxiv.org/abs/1706.03762
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *NAACL*. https://arxiv.org/abs/1810.04805
- Cañete, J., Chaperon, G., Fuentes, R., Ho, J.-H., Kang, H., & Pérez, J. (2020). Spanish pre-trained BERT model and evaluation data. *PML4DC Workshop, ICLR 2020*. Modelo y documentación: https://github.com/dccuchile/beto
- Alammar, J. (2018). *The illustrated transformer*. https://jalammar.github.io/illustrated-transformer/

**Fuentes primarias citadas en clase**

- Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). *Language models are unsupervised multitask learners*. OpenAI.
- Brown, T. B., et al. (2020). Language models are few-shot learners. *NeurIPS*. https://arxiv.org/abs/2005.14165
- Raffel, C., et al. (2020). Exploring the limits of transfer learning with a unified text-to-text transformer. *JMLR*. https://arxiv.org/abs/1910.10683
- Sennrich, R., Haddow, B., & Birch, A. (2016). Neural machine translation of rare words with subword units. *ACL*. https://arxiv.org/abs/1508.07909
- Petrov, A., La Malfa, E., Torr, P. H. S., & Bibi, A. (2023). Language model tokenizers introduce unfairness between languages. *NeurIPS*.
- Howard, J., & Ruder, S. (2018). Universal language model fine-tuning for text classification. *ACL*. https://arxiv.org/abs/1801.06146
- Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. *EMNLP*. https://arxiv.org/abs/1908.10084
- Gururangan, S., Marasović, A., Swayamdipta, S., Lo, K., Beltagy, I., Downey, D., & Smith, N. A. (2020). Don't stop pretraining: Adapt language models to domains and tasks. *ACL*. https://arxiv.org/abs/2004.10964
- Zhao, Z., Wallace, E., Feng, S., Klein, D., & Singh, S. (2021). Calibrate before use: Improving few-shot performance of language models. *ICML*. https://arxiv.org/abs/2102.09690
- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. *FAT\**. https://arxiv.org/abs/1810.03993
- Conneau, A., et al. (2020). Unsupervised cross-lingual representation learning at scale. *ACL*. https://arxiv.org/abs/1911.02116

**Libros de referencia**

- Jurafsky, D., & Martin, J. H. *Speech and language processing* (3.ª ed., borrador en línea), capítulos sobre Transformers y modelos de lenguaje grandes. https://web.stanford.edu/~jurafsky/slp3/
- Tunstall, L., von Werra, L., & Wolf, T. (2022). *Natural language processing with Transformers*. O'Reilly.

**Modelos para español y contexto latinoamericano**

- BETO (Universidad de Chile): https://github.com/dccuchile/beto
- Gutiérrez-Fandiño, A., et al. (2022). MarIA: Spanish language models. *Procesamiento del Lenguaje Natural*, 68.
- Pérez, J. M., Furman, D. A., Alonso Alemany, L., & Luque, F. (2022). RoBERTuito: A pre-trained language model for social media text in Spanish. *LREC*.
- Hugging Face. *LLM Course* (edición en español): https://huggingface.co/learn/llm-course/es/chapter1/1

**Documentación y tarjetas de modelo**

- Hugging Face, plantillas de chat: https://huggingface.co/docs/transformers/main/en/chat_templating
- `sentence-transformers/all-MiniLM-L6-v2`: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- `Qwen/Qwen2.5-0.5B-Instruct`: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct
- AG News en Hugging Face: https://huggingface.co/datasets/fancyzhx/ag_news
