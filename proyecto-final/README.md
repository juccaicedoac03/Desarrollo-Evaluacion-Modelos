# Proyecto final — Un modelo propio, de la idea a la demo

*Desarrollo y Evaluación de Modelos Propios · Especialización en Inteligencia Artificial Generativa y Desarrollo de Negocios · Rosario GSB, Universidad del Rosario*

| | |
|---|---|
| **Modalidad** | Grupos de 3 personas (se recomienda mezclar perfiles de negocio y técnicos) |
| **Peso en la nota final** | 30%: entregable técnico 15% · socialización y demo 10% · defensa individual 5%, multiplicado por el factor de coevaluación (0.7–1.0) |
| **Duración** | Del 3 al 24 de octubre de 2026 (de la S3 a la S12) |
| **Hitos formativos (obligatorios)** | H1: S3 (sábado 3 oct.) · H2: miércoles 14 oct. · H3: S9 (sábado 17 oct.) · H4: con la entrega final (viernes 23 oct.) |
| **Entrega final** | Viernes 23 de octubre, 23:59 |
| **Socialización** | Sesión 12 (sábado 24 de octubre, 10:00–13:00) |
| **Rúbrica** | [rubrica.md](rubrica.md) |
| **Plantillas** | [propuesta](plantillas/propuesta.md) · [informe técnico](plantillas/informe-tecnico.md) · [model card](plantillas/model-card.md) · [registro de uso de IA](plantillas/registro-uso-ia.md) · [coevaluación](plantillas/coevaluacion.md) · [retroalimentación entre grupos](plantillas/retroalimentacion-pares.md) |

---

## 1. El reto

Su grupo va a **diseñar, afinar o entrenar, evaluar y mejorar un modelo propio** que resuelva un problema concreto, de preferencia de una organización colombiana o latinoamericana, y lo va a mostrar funcionando en una **app de Gradio** o en un **agente de Startti**.

La pregunta que el proyecto debe responder con evidencia es:

> **¿Nuestro modelo propio resuelve el problema mejor que la alternativa más simple, con un costo y un riesgo aceptables?**

Un **modelo propio** es un modelo cuyos pesos el grupo adaptó (fine-tuning completo o LoRA) o entrenó, y que el mismo grupo evaluó. Escribir prompts para un modelo servido por API (ChatGPT, Claude, un agente de Startti) **no cuenta por sí solo** como modelo propio. Un LLM por API sí puede ser la línea base, una herramienta para generar datos sintéticos, un juez de evaluación o la capa conversacional de la demo.

No es obligatorio que el modelo supere a la línea base. Se califica la calidad de la evaluación y la honestidad del análisis: un resultado negativo bien explicado vale más que uno positivo sin evidencia.

---

## 2. Alcance mínimo

Todo proyecto debe cumplir estos ocho mínimos. Si falta alguno, el criterio correspondiente de la [rúbrica](rubrica.md) se califica como *Insuficiente*.

| # | Mínimo | Qué significa en la práctica | Dónde se evidencia |
|---|---|---|---|
| 1 | **Modelo afinado o entrenado por el grupo** | Fine-tuning completo de un modelo pequeño (p. ej., DistilBERT o BETO para clasificación), LoRA sobre un LLM pequeño (SmolLM2, Qwen2.5-0.5B) o un modelo entrenado desde cero. Un clasificador entrenado sobre embeddings es válido si se justifica. **Solo prompting no cuenta.** | Código · informe §3 |
| 2 | **Línea base y comparación** | Al menos una alternativa simple evaluada con el mismo conjunto de prueba: clase mayoritaria, TF-IDF + regresión logística, reglas, zero-shot o el modelo base sin afinar. | Informe §4 |
| 3 | **Al menos 2 métricas justificadas** | Una métrica técnica y otra ligada al negocio o al riesgo. Ejemplos: F1 macro + recall de la clase crítica; ROUGE-L + evaluación humana de fidelidad; exactitud + latencia o costo por consulta. | Informe §4 · model card |
| 4 | **Análisis de errores** | Revisión manual de una muestra de errores (sugerido: 20 o más), agrupados en categorías, con conteos, ejemplos y una hipótesis por categoría. | Informe §4 |
| 5 | **Al menos 1 iteración de mejora documentada** | Hipótesis → cambio → resultado → decisión. La decisión se toma con el conjunto de validación; al final se reportan todas las versiones en el mismo conjunto de prueba, **sin ajustar nada sobre él**. | Informe §5 (bitácora) |
| 6 | **Análisis ético y de sostenibilidad** | Sesgos, privacidad (Ley 1581 de 2012), usos indebidos, emisiones del entrenamiento (medidas con CodeCarbon o estimadas con un método citado), clasificación de riesgo y mitigaciones. | Informe §7 · model card |
| 7 | **Model card** | Documento del modelo según Mitchell et al. (2019), con la [plantilla](plantillas/model-card.md). | Repositorio o notebook |
| 8 | **Demo funcional** | App de Gradio o agente de Startti integrado con el modelo propio (ver §4). El modelo del grupo debe tener un papel verificable en la demo. | Socialización |

**Carga de trabajo.** El proyecto está dimensionado para unas **3 horas por persona por cada sesión** entre la S3 y la S12, dentro de las 9 horas de trabajo independiente que le corresponden a cada sesión del curso. Los ocho mínimos caben en ese presupuesto. Dos elementos del nivel *Excelente* de la [rúbrica](rubrica.md) son **metas de alcance extendido**, para hacer solo si el tiempo les alcanza (sin ellos, esos criterios pueden llegar al nivel *Bueno*):

- la variabilidad de los resultados con varias semillas o intervalos (criterio 4 del entregable técnico);
- la prueba empírica por subgrupo o contrafactual (criterio 6).

---

## 3. Hitos y calendario

Los hitos son **formativos y obligatorios**: no tienen nota propia, pero sirven para recibir retroalimentación a tiempo. **Cada hito (H1–H4) que no se entregue en su plazo descuenta 0.3 de la nota del entregable técnico** (escala 0.0–5.0; máximo −1.2), salvo excusa válida aceptada por el profesor según el reglamento. Un hito tardío puede recibir comentarios si hay tiempo, pero de todas formas cuenta como no entregado para el descuento.

| Hito | Sesión | Qué entrega el grupo | Plantilla | Plazo | Retroalimentación |
|---|---|---|---|---|---|
| **H1 · Conformación del grupo** | S3 (sábado 3 oct.) | Registro del grupo (ver el bloque de abajo), como `PF_H1_<codigo>` | — | 23:59 del día de la S3 | Confirmación y número de grupo (`G01`, `G02`…) |
| **H2 · Propuesta (canvas)** | Después de la S6 | Parte A de la propuesta: canvas de 1 página | [propuesta.md](plantillas/propuesta.md) | Miércoles 14 de octubre, 23:59 | Retroalimentación escrita en la S7 (viernes 16 oct.) |
| **H3 · Canvas de caso de uso** | S9 (sábado 17 oct.) | Parte A actualizada (1 página) + Parte B (máximo 2 páginas adicionales): valor × factibilidad, KPI, ROI, riesgos, primeros resultados de la línea base | [propuesta.md](plantillas/propuesta.md) (Parte B) | 23:59 del día de la S9 | Comentarios antes de la S10 |
| **H4 · Iteración de mejora** | Día de la S10 (viernes 23 oct.) | Sección 5 del informe técnico (bitácora con al menos una iteración), entregada dentro del informe de la entrega final | [informe-tecnico.md](plantillas/informe-tecnico.md) §5 | Viernes 23 de octubre, 23:59 (con la entrega final) | Revisión en la S11 y calificación con la rúbrica |
| **Entrega final** | Día de la S10 (viernes 23 oct.) | Todos los entregables de la §4 | Todas | Viernes 23 de octubre, 23:59 | Calificación con la rúbrica |
| **Socialización** | S12 (sábado 24 oct.) | Pitch + demo + preguntas | — | En clase | Retroalimentación del profesor y de los demás grupos |
| **Coevaluación** | S12 | Formulario individual y confidencial, como `PF_G<NN>_coev_<codigo>` | [coevaluacion.md](plantillas/coevaluacion.md) | 23:59 del día de la S12 | — |
| **Retroalimentación entre grupos** | S12 | Formulario individual sobre los grupos que el profesor asigna a cada estudiante, como `PF_retro_<codigo>` | [retroalimentacion-pares.md](plantillas/retroalimentacion-pares.md) | 23:59 del día de la S12 | Consolidada y anónima |

**Cómo se entrega:** un integrante sube el archivo del grupo a la actividad correspondiente de e-Aulas, en PDF o Markdown. En el H1 el grupo aún no tiene número, así que el registro se llama `PF_H1_<codigo>`, con el código estudiantil de quien lo sube (p. ej., `PF_H1_123456.md`). Desde el H2, los archivos se llaman `PF_G<NN>_<hito>` (p. ej., `PF_G03_H2_propuesta.pdf`). La coevaluación (`PF_G<NN>_coev_<codigo>`) y la retroalimentación entre grupos (`PF_retro_<codigo>`) son individuales: cada estudiante sube su propio archivo.

### Bloque para el registro del grupo (H1)

Copien este bloque, complétenlo y súbanlo a e-Aulas:

```text
Nombre del grupo:
Integrantes (nombre completo · código · perfil: negocio / técnico / mixto):
  1.
  2.
  3.
Canal de comunicación del grupo:
Dónde vivirá el código (repositorio de GitHub o notebook de Kaggle):
Idea preliminar (1–2 líneas):
Acuerdos de trabajo:
  - Frecuencia y horario de reuniones:
  - Cómo tomamos decisiones:
  - Qué hacemos si alguien no cumple un compromiso:
```

- Los grupos son de 3 personas. Solo con autorización del profesor puede haber grupos de 2 o de 4.
- El profesor asigna un grupo a quien no tenga uno al cierre del H1.
- **Roles sugeridos** (cada persona lidera un frente, pero todos programan y todos deben poder explicar todo):
  - *Producto y negocio:* problema, usuarios, KPI, ROI, pitch.
  - *Datos y evaluación:* datos, particiones, métricas, análisis de errores, ética.
  - *Modelado y demo:* entrenamiento, iteraciones, app de Gradio o agente de Startti.
- Si hay problemas de participación, háblenlo primero en el grupo según sus acuerdos. Si persisten, informen al profesor **antes de la S10** (viernes 23 de octubre), con evidencia, para que haya margen de actuar antes de la entrega final; no esperen a la coevaluación.

---

## 4. Entregables finales (Sesión 12)

Plazo: **viernes 23 de octubre, 23:59** (el día de la S10). Se califica la versión disponible al cierre del plazo: el último commit o la última versión guardada del notebook de Kaggle antes de la hora límite.

| # | Entregable | Formato y condiciones |
|---|---|---|
| 1 | **Código** | Repositorio de GitHub o notebook de Kaggle, público o privado compartido con el profesor. Debe correr de principio a fin (`Run All` o las instrucciones del README), con semilla fija, versiones de librerías registradas, acceso a los datos documentado (p. ej., un Kaggle Dataset privado) y **sin claves en el código** (usen Kaggle Secrets). El profesor no tiene acceso a sus Secrets, así que el notebook también debe correr completo **sin claves** (ver la opción B de la demo). |
| 2 | **Informe técnico** | PDF de **máximo 8 páginas**, sin contar portada, referencias ni anexos, con la [plantilla](plantillas/informe-tecnico.md). Lo que pase de la página 8 no se califica. Incluye el **Anexo A. Declaración de contribuciones** (obligatorio, no cuenta en las 8 páginas). |
| 3 | **Model card** | Con la [plantilla](plantillas/model-card.md): `MODEL_CARD.md` en el repositorio, sección final del notebook o tarjeta del modelo en Hugging Face Hub. |
| 4 | **Demo** | **Opción A — Gradio:** app en el notebook (`demo.launch(share=True)` genera un enlace público temporal) o, si quieren un enlace estable, en Hugging Face Spaces. **Opción B — Agente de Startti integrado:** el agente funciona como capa conversacional y se orquesta desde el notebook junto con el modelo propio (p. ej., el modelo clasifica o extrae y el agente responde con su base de conocimiento). El agente por sí solo no cumple el mínimo. Como el profesor no puede usar sus Kaggle Secrets, el notebook entregado debe funcionar **sin la clave de Startti**: las celdas del agente se omiten sin error y muestran una transcripción o capturas grabadas de conversaciones reales con el agente, o ejecutan la alternativa en Python. El agente en vivo se muestra en la socialización de la S12. Ver [configuración de Startti](../docs/configuracion-startti.md). |
| 5 | **Registro de uso de IA** | Con la [plantilla](plantillas/registro-uso-ia.md). Es obligatorio y se califica. |
| 6 | **Diapositivas del pitch** | PDF. |
| 7 | **Video de respaldo** *(opcional)* | Máximo 3 minutos: la demo grabada, por si la demo en vivo falla. Se entrega como enlace (no suban el video a e-Aulas). |

Un integrante sube a e-Aulas: `PF_G<NN>_informe.pdf` (con el Anexo A de contribuciones), `PF_G<NN>_slides.pdf`, `PF_G<NN>_model-card.md` y `PF_G<NN>_registro-ia.md`. La portada del informe reúne los enlaces al código, la demo y el video. Después de la S12, cada estudiante sube su coevaluación (`PF_G<NN>_coev_<codigo>`) y su retroalimentación entre grupos (`PF_retro_<codigo>`).

**Compartir con el profesor:** si el repositorio de GitHub es privado, agreguen como colaborador al usuario `juccaicedoac03`. Si el notebook de Kaggle es privado, compártanlo con el usuario de Kaggle que el profesor publicará en e-Aulas.

---

## 5. Socialización en la Sesión 12

Cada grupo tiene **15 minutos: 8' de pitch + 3' de demo + 4' de preguntas**. El tiempo se controla con temporizador; al minuto 8 el profesor pide pasar a la demo. La logística de la sesión está en la [guía de la Sesión 12](../sessions/12-integrative-project/README.md).

- **Orden aleatorio:** el orden se sortea en clase. Todos los grupos deben estar listos desde el inicio, con la pantalla compartida probada. Si un grupo no está listo cuando lo llaman, pasa una sola vez al final de la lista.
- **Todos hablan:** cada integrante presenta una parte del pitch o de la demo.
- **Defensa individual:** en los 4' de preguntas, el profesor dirige al menos una pregunta a cada integrante, sobre cualquier parte del proyecto y no solo sobre "su" parte. Si el tiempo no alcanza, la defensa puede completarse en un espacio breve al final de la sesión. Durante la defensa no se pueden consultar asistentes de IA ni leer respuestas preparadas.
- **Cámara encendida** durante la propia intervención y la defensa individual.
- **Ausencias:** quien falte a la S12 sin excusa válida obtiene 0.0 en socialización y en defensa individual. Con excusa válida según el reglamento, conserva la nota de socialización del grupo y presenta su defensa individual en otra fecha.

**Estructura sugerida del pitch (8')**

| Minutos | Contenido |
|---|---|
| 1' | Problema, usuario y por qué importa (con un dato o un caso) |
| 1.5' | Solución y datos |
| 1.5' | Modelo y entrenamiento: qué afinaron y por qué |
| 2' | Evaluación: resultados frente a la línea base, errores típicos y la iteración de mejora |
| 1' | Ética, sostenibilidad y limitaciones |
| 1' | Valor de negocio, recomendación (go / no-go) y siguiente paso |

**Demo (3'):** preparen 2 o 3 casos: uno típico, uno difícil y uno en el que el modelo falla, explicando por qué. Muestren las decisiones de producto: umbral de confianza, escalamiento a una persona, mensajes de incertidumbre. Si la demo en vivo falla por causas técnicas, proyecten el video de respaldo; presentar solo el video, sin intentar la demo en vivo, limita la nota de la demo ([rúbrica](rubrica.md), sección 3).

Mientras presentan los demás grupos, cada estudiante diligencia la [retroalimentación entre grupos](plantillas/retroalimentacion-pares.md) (formativa, no calificada).

---

## 6. Evaluación

El proyecto vale **30% de la nota final**. El esquema completo del curso está en [evaluación del curso](../docs/evaluacion.md) y los descriptores de cada nivel están en la [rúbrica](rubrica.md).

| Componente | Peso en la nota final | Tipo de nota |
|---|---|---|
| Entregable técnico | 15% | Grupal (menos los descuentos por hitos) |
| Socialización y demo | 10% | Grupal |
| Defensa individual | 5% | Individual |
| **Factor de coevaluación** | **× 0.7–1.0** | Individual: se aplica a la nota del proyecto de cada estudiante |

```text
Nota del proyecto (0.0–5.0)   = (15 × Técnico + 10 × Socialización + 5 × Defensa) / 30
Nota individual del proyecto  = Nota del proyecto × F
Aporte a la nota final        = 0.30 × Nota individual del proyecto

F = 0.7 + 0.3 × (P − 1) / 3, con tope en 1.0
P = promedio de los puntajes (1–5) que cada estudiante recibe de sus compañeros de grupo en la coevaluación (sin su autoevaluación)
```

Con P = 1.0, F = 0.70; con P = 3.0, F = 0.90; con **P ≥ 4.0, F = 1.00**. F se redondea a dos decimales. En el entregable técnico se aplican primero los descuentos por hitos (−0.3 por hito, máximo −1.2) y luego los topes (p. ej., 3.0 si solo hay prompting). La rúbrica trae un ejemplo completo y las reglas para casos extremos: el profesor puede revisar el factor con evidencia.

---

## 7. Reglas de uso de IA en el proyecto

Aplica la [política de uso de IA del curso](../docs/politica-uso-ia.md). En resumen:

1. **Los asistentes de IA están permitidos y se espera que los usen** (ChatGPT, Claude, Codex, Copilot, etc.) para programar, depurar, redactar y revisar.
2. **Todo uso se declara** en el [registro de uso de IA](plantillas/registro-uso-ia.md): herramienta, para qué, prompt principal y qué verificaron o corrigieron. Si no hay registro, ese criterio de la rúbrica vale 0.
3. **Cada integrante debe poder explicar cualquier parte del proyecto**, incluido lo que generó una IA. La defensa individual lo comprueba.
4. **Resultados fabricados.** Métricas, tablas, gráficas, citas o datos que no provengan de ejecutar su propio código, o que hayan sido alterados, se tramitan conforme al reglamento académico de la Universidad del Rosario; el componente afectado puede calificarse con **0.0**.
5. **No compartan datos personales ni confidenciales** de ninguna organización con asistentes de IA externos ni con agentes de Startti.
6. Si la IA forma parte de la solución (datos sintéticos, LLM como juez, traducción automática, agente conversacional), se documenta además en el informe y en la model card, con la forma en que se validó.

---

## 8. Datos: fuentes y privacidad

### Fuentes válidas

1. **Datasets públicos** de Hugging Face o Kaggle. Revisen la licencia y los términos de uso.
2. **Datos abiertos**, como el [Portal de Datos Abiertos de Colombia](https://www.datos.gov.co). Verifiquen la licencia y que no incluyan datos personales.
3. **Datos de su organización**, solo con autorización escrita, anonimizados y sin secretos empresariales. Guárdenlos como Kaggle Dataset **privado** o en un repositorio privado.
4. **Datos sintéticos** generados con un LLM o con reglas. Documenten modelo, prompt, cantidad y revisión humana. El conjunto de prueba debe ser revisado por personas y, si es posible, con datos reales: evaluar solo sobre datos sintéticos del mismo generador infla las métricas.
5. **Contenido web público**, respetando los términos de uso del sitio, los derechos de autor y `robots.txt`, sin datos personales y citando la fuente.

### Reglas de privacidad (Ley 1581 de 2012)

La [Ley 1581 de 2012](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981) regula el tratamiento de datos personales en Colombia; la reglamenta el Decreto 1377 de 2013.

- **No usen datos personales sin autorización previa, expresa e informada de sus titulares.** Lo más seguro es no usarlos.
- **No usen datos sensibles** (salud, vida sexual, origen racial o étnico, orientación política, convicciones religiosas, pertenencia a sindicatos, datos biométricos), salvo datasets públicos preparados para investigación y siempre con fines académicos.
- **Anonimicen antes de procesar:** eliminen o reemplacen nombres, números de cédula, teléfonos, correos, direcciones y números de cuenta o de tarjeta. Luego revisen una muestra a mano, como en el laboratorio de la [Sesión 10](../sessions/10-ethics-and-sustainability/README.md).
- No publiquen datos de una organización en notebooks o repositorios públicos.
- Documenten en el informe y en la model card el origen, la licencia, el consentimiento y la anonimización.

### Datasets verificados en Hugging Face

Todos cargan con `datasets.load_dataset("<id>")`. Si su caso es en español y el dataset está en inglés, pueden traducir un subconjunto con `Helsinki-NLP/opus-mt-en-es`, revisar a mano una muestra y reportar el efecto de la traducción.

| Dataset | Contenido | Tamaño (particiones) | Ideas relacionadas |
|---|---|---|---|
| `SetFit/amazon_reviews_multi_es` | Reseñas de productos **en español**; columnas `text`, `label` (0–4 = 1 a 5 estrellas) | 200 000 train · 5 000 validation · 5 000 test | 4 |
| `legacy-datasets/banking77` | Consultas de clientes bancarios en inglés, 77 intenciones | 10 003 train · 3 080 test | 1, 2 |
| `zeroshot/twitter-financial-news-sentiment` | Tweets de noticias financieras en inglés; `label`: 0 bajista, 1 alcista, 2 neutral | 9 543 train · 2 388 validation (**sin test**: usen validation como prueba y separen su propia validación de train) | 10 |
| `fancyzhx/ag_news` | Noticias en inglés, 4 temas (World, Sports, Business, Sci/Tech) | 120 000 train · 7 600 test | 7 |
| `allenai/sciq` | Preguntas de ciencias en inglés con respuesta correcta, 3 distractores y párrafo de soporte | 11 679 train · 1 000 validation · 1 000 test | 6 |
| `gretelai/symptom_to_diagnosis` | Descripciones de síntomas en inglés (`input_text`) y diagnóstico (`output_text`) | 853 train · 212 test | Proyectos de salud: solo con fines educativos, **nunca como diagnóstico real** |
| `stanfordnlp/imdb` | Reseñas de películas en inglés, sentimiento binario | 25 000 train · 25 000 test | Practicar el flujo de clasificación de sentimiento |

---

## 9. Cómputo y modelos de partida

El proyecto debe poder hacerse con los recursos **gratuitos de Kaggle**: GPU T4 de 16 GB (acelerador *GPU T4 x2*), con una cuota semanal de aproximadamente 30 horas de GPU por cuenta. Kaggle define y puede cambiar esa cuota; revísenla en su perfil. Cada integrante tiene su propia cuota: coordínense. Guía paso a paso: [configuración de Kaggle](../docs/configuracion-kaggle.md).

**Recomendaciones**

- Usen modelos de **≤ ~1B de parámetros**; para modelos generativos, **LoRA** ([Hu et al., 2021](https://arxiv.org/abs/2106.09685)).
- Iteren con subconjuntos pequeños y escalen solo la versión final.
- Limiten la longitud de secuencia (p. ej., 128–256 tokens para clasificación) y usen acumulación de gradientes si la memoria no alcanza.
- Precisión numérica: con modelos pequeños, entrenen en fp32 (la opción por defecto), que es la más estable. `fp16=True` puede ahorrar memoria y tiempo en GPU con los modelos más grandes de la lista; si la pérdida se vuelve `NaN`, vuelvan a fp32. **No usen fp16 con modelos de la familia T5** (p. ej., `google/flan-t5-small`): suelen producir pérdidas `NaN`.
- Guarden checkpoints en `/kaggle/working`. Para entrenamientos largos, usen *Save Version → Save & Run All*, que ejecuta el notebook en segundo plano.
- Registren `transformers.__version__` y fijen versiones: Kaggle puede traer versiones distintas entre sesiones. Usen `eval_strategy` (no `evaluation_strategy`).
- Midan las emisiones del entrenamiento con [CodeCarbon](https://codecarbon.io) o, si no es posible, estímenlas con un método citado (p. ej., [Lacoste et al., 2019](https://arxiv.org/abs/1910.09700)).

**Modelos de partida sugeridos** (abiertos y sin acceso restringido)

| Modelo | Tipo | Parámetros (aprox.) | Idioma | Útil para |
|---|---|---|---|---|
| `distilbert/distilbert-base-uncased` | Codificador | 67M | Inglés | Clasificación rápida |
| `google-bert/bert-base-uncased` | Codificador | 110M | Inglés | Clasificación, extracción |
| `dccuchile/bert-base-spanish-wwm-cased` (BETO) | Codificador | ~110M (tamaño BERT-base) | **Español** | Clasificación y extracción en español ([Cañete et al., 2020](https://arxiv.org/abs/2308.02976)); revisen su licencia antes de un uso comercial |
| `distilbert/distilbert-base-multilingual-cased` | Codificador | 135M | Multilingüe | Clasificación en español |
| `dslim/bert-base-NER` | Codificador (entidades) | 108M | Inglés | Punto de partida para extracción de entidades |
| `ProsusAI/finbert` | Codificador (sentimiento financiero) | ~110M (tamaño BERT-base) | Inglés | Sentimiento financiero |
| `sentence-transformers/all-MiniLM-L6-v2` | Embeddings | 23M | Inglés | Clasificador sobre embeddings, búsqueda semántica |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | Embeddings | 118M | Multilingüe | Lo mismo, en español |
| `google/flan-t5-small` | Codificador-decodificador | 77M | Principalmente inglés | Resumen, texto → JSON |
| `HuggingFaceTB/SmolLM2-135M-Instruct` · `SmolLM2-360M-Instruct` | LLM (decodificador) | 135M · 362M | Principalmente inglés | SFT con LoRA: estilo, formato |
| `Qwen/Qwen2.5-0.5B-Instruct` | LLM (decodificador) | 494M | Multilingüe (incluye español) | SFT con LoRA en español |
| `Helsinki-NLP/opus-mt-en-es` | Traducción | — | Inglés → español | Traducir datasets en inglés |

---

## 10. Diez ideas de proyecto

Pueden tomar una de estas ideas, adaptarla o proponer la suya. Un problema real de su organización es bienvenido, siempre que cumpla las reglas de datos de la §8. Para elegir, pregúntense:

- ¿El problema tiene **valor** medible para alguien?
- ¿Tenemos o podemos construir **datos** suficientes y legales?
- ¿Es **factible** en Kaggle gratis y en el tiempo que va del 3 al 24 de octubre (de la S3 a la S12)?
- ¿El **riesgo** es manejable?

Las organizaciones de los ejemplos son genéricas o ficticias.

### 1. Clasificador de PQRS para una empresa de servicios públicos

- **Contexto:** una empresa de acueducto o de energía recibe peticiones, quejas, reclamos y sugerencias (PQRS) por web, correo y redes, y debe responderlas dentro de los plazos legales. Clasificarlas y enrutarlas a mano es lento.
- **Tarea:** clasificación de texto por tipo de PQRS y área responsable (opcional: urgencia).
- **Datos:** PQRS propias anonimizadas y con autorización, o un corpus sintético generado con LLM y revisado por el grupo; el conjunto de prueba se revisa a mano. Para practicar el flujo: `legacy-datasets/banking77`.
- **Modelo de partida:** BETO o DistilBERT multilingüe afinado; alternativa: clasificador sobre embeddings multilingües.
- **Línea base:** reglas por palabras clave; TF-IDF + regresión logística.
- **Métricas sugeridas:** F1 macro, recall de los reclamos urgentes y porcentaje de enrutamiento correcto a la primera.
- **Demo:** Gradio con umbral de confianza; si el modelo duda, el caso pasa a revisión humana.
- **Ojo con:** datos personales en el texto; desempeño desigual según el canal o la forma de escribir (errores ortográficos, lenguaje coloquial).

### 2. Asistente de soporte para un banco digital con base de conocimiento

- **Contexto:** *Andes Bank*, un banco digital ficticio (el mismo de la guía de configuración de Startti y del lab de la S07), atiende por chat preguntas repetitivas sobre tarjetas, transferencias y recargas.
- **Tarea:** detectar la intención, responder con una base de conocimiento y escalar a una persona cuando corresponda.
- **Datos:** `legacy-datasets/banking77` (pueden traducir un subconjunto al español y revisarlo) + una FAQ ficticia escrita por el grupo para la base de conocimiento.
- **Modelo de partida:** DistilBERT o BETO afinado para la intención; opcional: LoRA sobre `Qwen/Qwen2.5-0.5B-Instruct` para el tono de marca. El agente de Startti puede ser la capa conversacional.
- **Línea base:** zero-shot con un LLM, o el agente de Startti sin el clasificador.
- **Métricas sugeridas:** exactitud y F1 macro de la intención; tasa de resolución correcta en un set de conversaciones de prueba; tasa de escalamiento correcto.
- **Demo:** Gradio, o agente de Startti orquestado desde el notebook.
- **Ojo con:** no dar asesoría financiera; nunca pedir claves ni datos de tarjetas; errores costosos en temas de fraude.

### 3. Resumen de actas de reunión

- **Contexto:** comités, juntas directivas o asambleas de copropietarios (propiedad horizontal) producen actas largas; los asistentes necesitan decisiones, responsables y fechas.
- **Tarea:** generar resúmenes estructurados (decisiones, compromisos, responsables, fechas).
- **Datos:** actas propias anonimizadas y con autorización, o actas sintéticas escritas por el grupo, con resúmenes de referencia escritos o revisados por personas.
- **Modelo de partida:** LoRA sobre `Qwen/Qwen2.5-0.5B-Instruct` (español) o `google/flan-t5-small` (inglés).
- **Línea base:** las primeras oraciones del acta (*lead-k*); el modelo base sin afinar, con el mismo prompt.
- **Métricas sugeridas:** ROUGE-L; porcentaje de decisiones y responsables extraídos correctamente (verificado a mano); errores de hecho por resumen.
- **Ojo con:** compromisos inventados (alucinaciones); confidencialidad de lo discutido.

### 4. Sentimiento en reseñas en español

- **Contexto:** una cadena de restaurantes o un comercio electrónico quiere monitorear lo que dicen sus clientes.
- **Tarea:** clasificar el sentimiento (negativo / neutral / positivo) o predecir las estrellas.
- **Datos:** `SetFit/amazon_reviews_multi_es`, complementado con reseñas públicas en español colombiano recolectadas por el grupo (sin nombres de usuarios) para medir el cambio de dominio. Úsenlo solo con fines académicos y revisen sus términos de uso.
- **Modelo de partida:** BETO o DistilBERT multilingüe afinado.
- **Línea base:** TF-IDF + regresión logística; zero-shot con un LLM.
- **Métricas sugeridas:** F1 macro, error absoluto medio en estrellas y matriz de confusión (la clase neutral suele ser la difícil).
- **Ojo con:** ironía, regionalismos y caída de desempeño fuera del dominio de entrenamiento.

### 5. Generador de descripciones de producto para e-commerce

- **Contexto:** una tienda en línea ficticia de café, artesanías o moda tiene cientos de productos sin descripción.
- **Tarea:** generación condicionada: atributos del producto → descripción con el tono de la marca.
- **Datos:** pares atributos → descripción escritos o revisados por el grupo; desde unas decenas hasta algunos cientos de pares.
- **Modelo de partida:** LoRA sobre `HuggingFaceTB/SmolLM2-360M-Instruct` (inglés) o `Qwen/Qwen2.5-0.5B-Instruct` (español).
- **Línea base:** plantilla con reglas; el modelo base con *few-shot prompting*.
- **Métricas sugeridas:** fidelidad a los atributos (porcentaje de atributos correctos y de atributos inventados, verificable de forma automática); chrF contra referencias; evaluación humana del tono con rúbrica y dos evaluadores.
- **Ojo con:** atributos inventados que pueden constituir publicidad engañosa (Estatuto del Consumidor, Ley 1480 de 2011).

### 6. Tutor para un curso

- **Contexto:** una institución educativa quiere un tutor que genere preguntas de práctica y explique las respuestas.
- **Tarea:** generar preguntas de opción múltiple con distractores y explicación, o responder preguntas sobre el material del curso.
- **Datos:** `allenai/sciq`, o material propio de un curso con permiso de su autor.
- **Modelo de partida:** LoRA sobre `Qwen/Qwen2.5-0.5B-Instruct`, o `google/flan-t5-small` (párrafo de soporte → pregunta).
- **Línea base:** el modelo base con prompting; distractores elegidos al azar.
- **Métricas sugeridas:** exactitud de las respuestas del tutor; calidad de los distractores (plausibles pero incorrectos) con rúbrica humana; porcentaje de preguntas bien formadas.
- **Demo:** quiz en Gradio o agente de Startti con el material del curso como base de conocimiento.
- **Ojo con:** errores conceptuales presentados con seguridad; accesibilidad.

### 7. Triage de correos corporativos

- **Contexto:** el buzón de servicio al cliente o la mesa de ayuda de una empresa recibe correos de temas y urgencias muy distintos.
- **Tarea:** clasificar el área responsable y la prioridad.
- **Datos:** correos propios anonimizados y con autorización, o correos sintéticos. Para practicar la clasificación por tema: `fancyzhx/ag_news`.
- **Modelo de partida:** BETO o DistilBERT afinado; o embeddings multilingües + regresión logística o un MLP.
- **Línea base:** reglas por remitente y palabras clave.
- **Métricas sugeridas:** F1 macro, recall de los urgentes y costo esperado de los errores (matriz de costos definida con el negocio).
- **Ojo con:** los correos están llenos de datos personales: anonimicen antes de cualquier uso y nunca los peguen en un asistente de IA.

### 8. Extracción de información de facturas en texto

- **Contexto:** el área contable de una pyme recibe facturas en PDF o en texto y digita a mano proveedor, NIT, fecha, subtotal, IVA y total.
- **Tarea:** extracción de información: reconocimiento de entidades o texto → JSON.
- **Datos:** facturas **sintéticas** generadas por el grupo con datos ficticios y formatos variados. No usen facturas reales con datos de personas.
- **Modelo de partida:** afinar BETO o `dslim/bert-base-NER` con etiquetas propias (clasificación de tokens), o LoRA sobre `Qwen/Qwen2.5-0.5B-Instruct` o `google/flan-t5-small` para texto → JSON.
- **Línea base:** expresiones regulares.
- **Métricas sugeridas:** coincidencia exacta por campo, F1 por entidad, porcentaje de facturas con todos los campos correctos y porcentaje de JSON válidos.
- **Ojo con:** errores en montos (costo alto) y formatos no vistos en el entrenamiento.

### 9. Chatbot de admisiones universitarias

- **Contexto:** una universidad recibe preguntas repetitivas sobre fechas, requisitos, costos y proceso de admisión. Usen una universidad ficticia, o información pública identificada claramente como prototipo académico.
- **Tarea:** detectar la intención, responder desde una base de conocimiento y escalar lo que esté fuera de alcance.
- **Datos:** FAQ construida por el grupo a partir de información pública, con paráfrasis por intención (humanas y sintéticas revisadas) y un set de conversaciones de prueba.
- **Modelo de partida:** clasificador afinado (BETO o DistilBERT multilingüe) o sobre embeddings multilingües; agente de Startti con base de conocimiento.
- **Línea base:** reglas por palabras clave; el agente sin clasificador.
- **Métricas sugeridas:** exactitud de la intención, tasa de respuestas correctas y completas en las conversaciones de prueba, y escalamiento correcto de los casos fuera de alcance.
- **Ojo con:** información desactualizada (fechas, costos); políticas inventadas; recolección de datos personales de aspirantes.

### 10. Análisis de noticias financieras

- **Contexto:** el área de riesgo de *Banco Andino*, un banco ficticio, quiere monitorear el tono de las noticias sobre sectores y emisores.
- **Tarea:** clasificar el sentimiento financiero (bajista / alcista / neutral).
- **Datos:** `zeroshot/twitter-financial-news-sentiment` + titulares en español recolectados por el grupo (solo titulares, citando la fuente) para medir la transferencia al español.
- **Modelo de partida:** `ProsusAI/finbert` como modelo preentrenado de referencia (hay que mapear sus etiquetas a las del dataset) frente a DistilBERT o BETO afinado por el grupo.
- **Línea base:** FinBERT sin afinar; clase mayoritaria.
- **Métricas sugeridas:** F1 macro, recall de la clase bajista y desempeño en los titulares en español.
- **Ojo con:** esto **no** es asesoría de inversión; no se usa para decisiones automáticas de compra o venta.

---

## 11. Dónde repasar

| Tema del proyecto | Sesión |
|---|---|
| Fine-tuning y LoRA | [S04 — Fine-Tuning Generative Models](../sessions/04-fine-tuning/README.md) |
| Métricas, línea base y análisis de errores | [S05 — Evaluating Generative Models](../sessions/05-evaluating-generative-models/README.md) |
| App de Gradio, umbrales, primer agente de Startti | [S06 — Introduction to Basic Application Development](../sessions/06-basic-ai-applications/README.md) |
| Chatbots, agentes y evaluación conversacional | [S07 — Implementing Basic Chatbots and Agents](../sessions/07-chatbots-and-agents/README.md) |
| Canvas de caso de uso, KPI y ROI | [S09 — Use Cases: Generative Models in Real Contexts](../sessions/09-real-world-use-cases/README.md) |
| Sesgo, privacidad, emisiones, model cards | [S10 — Ethics and Sustainability](../sessions/10-ethics-and-sustainability/README.md) |
| Iteraciones de mejora, bitácora, robustez | [S11 — Evaluation and Continuous Model Improvement](../sessions/11-continuous-improvement/README.md) |
| Socialización | [S12 — Integrative Project](../sessions/12-integrative-project/README.md) |

---

## 12. Preguntas frecuentes

**¿Podemos usar datos de nuestra empresa?**
Sí, con autorización escrita de la organización, anonimizados, sin secretos empresariales y guardados de forma privada (§8).

**¿Podemos usar ChatGPT, Claude o Startti dentro de la solución?**
Sí: como línea base, para generar datos sintéticos (documentados y revisados), como juez de evaluación (validado con una muestra humana) o como capa conversacional. Pero el modelo afinado o entrenado por el grupo debe tener un papel verificable.

**¿El modelo tiene que ganarle a la línea base?**
No. Se califica que la comparación sea justa y que el análisis sea honesto. Si no le gana, expliquen por qué y qué harían después.

**¿En qué idioma trabajamos?**
Los datos pueden estar en inglés. El informe, la model card y la socialización van en español. El código y sus comentarios pueden estar en inglés.

**¿Podemos cambiar de idea?**
Sí, hasta el H3 (S9), justificando el cambio en la Parte B del canvas. Después, solo con aprobación del profesor.

**¿Y si se nos acaba la GPU?**
Usen subconjuntos y modelos más pequeños, repartan el entrenamiento entre las cuentas del grupo, entrenen en CPU los clasificadores sobre embeddings o usen Colab como respaldo ([configuración de Kaggle](../docs/configuracion-kaggle.md)).

**¿Qué pasa si un integrante no aporta?**
Aplíquenle los acuerdos del grupo; si el problema persiste, avisen al profesor antes de la S10 con evidencia. La coevaluación ajusta la nota individual (§6 y [rúbrica](rubrica.md)).

---

## 13. Plantillas

| Plantilla | Para qué | Cuándo |
|---|---|---|
| [propuesta.md](plantillas/propuesta.md) | Canvas de propuesta (Parte A) y canvas de caso de uso (Parte B) | H2 (miércoles 14 oct.) · H3 (S9) |
| [informe-tecnico.md](plantillas/informe-tecnico.md) | Estructura del informe técnico (≤ 8 páginas) y bitácora de mejora | H4 (§5, con la entrega final del viernes 23 oct.) |
| [model-card.md](plantillas/model-card.md) | Model card (Mitchell et al., 2019) | Entrega final |
| [registro-uso-ia.md](plantillas/registro-uso-ia.md) | Registro grupal de uso de IA + reflexión | Durante todo el proyecto · entrega final |
| [coevaluacion.md](plantillas/coevaluacion.md) | Evaluación confidencial de los compañeros de grupo | S12 (individual) |
| [retroalimentacion-pares.md](plantillas/retroalimentacion-pares.md) | Retroalimentación a otros grupos durante la socialización | S12 (individual, formativa) |
