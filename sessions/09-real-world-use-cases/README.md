# Sesión 09 — Use Cases: Generative Models in Real Contexts
*Casos de uso: modelos generativos en contexto real*

**RAE asociados:** RAE 4, RAE 5, RAE 6 · **Duración:** 3 horas (virtual) · **Fecha:** sábado 17 de octubre de 2026, 10:00–13:00 (hora de Colombia)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. Analizar un caso de uso de IA generativa como una **tarea** (no como una tecnología) con cuatro lentes: cadena de valor, valor × factibilidad, riesgo × impacto y escalera de KPI (RAE 4).
2. Estimar el ROI y el *payback* de un caso con supuestos explícitos, incluido el costo del retrabajo, y tomar una decisión *go / no-go* (RAE 4, RAE 5).
3. Leer la evidencia con criterio: estimaciones económicas de alto nivel, experimentos de campo y fallas documentadas, y saber qué se puede transferir a tu caso (RAE 4).
4. Prototipar y medir soluciones sectoriales en finanzas, salud y educación con modelos abiertos pequeños (RAE 5).
5. Anticipar los riesgos de cada sector (responsabilidad, seguridad del paciente, privacidad) y elegir controles (RAE 6).

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Tres preguntas de repaso de la S08 (Ng y Jordan, clasificación *zero-shot* por verosimilitud, fuga de datos) |
| Teoría | 60' | Del caso de uso a la tarea · valor × factibilidad · riesgo × impacto · KPI · ROI y *payback* · evidencia (McKinsey, Brynjolfsson et al., Dell'Acqua et al.) · salud, finanzas y educación · fallas documentadas (Moffatt v. Air Canada, chatbot MyCity) · contexto colombiano. Simuladores: matriz valor × factibilidad y calculadora de ROI. Sala de trabajo: canvas de un caso por sector |
| Descanso | 10' | — |
| Lab guiado | 60' | FinBERT vs. LLM *zero-shot* en titulares financieros · recuperación síntoma → condición con *top-3* (no es consejo médico) · generación de preguntas con verificación de respondibilidad · agente con base de conocimiento (Startti o Python) evaluado con preguntas dentro y fuera de alcance |
| Challenge | 40' | Tu sector, tu caso ficticio y tus parámetros de ROI: prototipo, canvas, decisión *go / no-go* y verificación de un resumen escrito por IA |

**Hito del proyecto (formativo):** hoy cada grupo entrega el **canvas de caso de uso (H3)**: Parte A actualizada + Parte B de la [plantilla de propuesta](../../proyecto-final/plantillas/propuesta.md) (valor × factibilidad, KPI, ROI base y pesimista, riesgos y decisión). Una persona del grupo lo sube a e-Aulas como `PF_G<NN>_H3_canvas` antes de las **23:59**. Es formativo: recibirán comentarios antes de la S10 ([detalles del proyecto](../../proyecto-final/README.md)).

## Antes de la clase (≈2 h)

Esta sesión va justo después de la S08 (7:00–10:00), así que esta preparación se hace **antes del sábado a las 7:00**, junto con la de la S08.

- [ ] Lee el resumen y la introducción de Brynjolfsson, Li y Raymond, *Generative AI at Work* ([NBER w31161](https://www.nber.org/papers/w31161)) (≈30 min). Fíjate en **quiénes** ganan más con el asistente.
- [ ] Lee el resumen de Dell'Acqua et al. (2023), *Navigating the Jagged Technological Frontier* (HBS Working Paper 24-013) (≈20 min).
- [ ] Revisa la Parte B de la [plantilla de propuesta](../../proyecto-final/plantillas/propuesta.md) con tu grupo y traigan una primera versión de B2 (línea base) y B3 (valor × factibilidad) (≈45 min).
- [ ] Si vas a usar Startti en el lab o en el challenge: verifica que tu clave esté en Kaggle Secrets como `STARTTI_API_KEY` y que sabes publicar un agente con base de conocimiento ([guía, secciones 3 a 7](../../docs/configuracion-startti.md)). Si prefieres no usar cuenta, la alternativa en Python cubre todo.
- [ ] Repasa la clasificación *zero-shot* por verosimilitud y la fuga de datos de la S08.

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/09-real-world-use-cases/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/09-real-world-use-cases/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/09-real-world-use-cases/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/09-real-world-use-cases/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/09-real-world-use-cases/challenge.ipynb) · [archivo](challenge.ipynb) |
| Manual del estudiante de Colibrí Online University (base de conocimiento del lab, ficticio) | [data/colibri_handbook.md](data/colibri_handbook.md) |
| Casos del challenge (9 organizaciones ficticias, 3 por sector) | [data/casos/](data/casos/) |
| Plantilla del canvas de caso de uso (H3, Parte B) | [proyecto-final/plantillas/propuesta.md](../../proyecto-final/plantillas/propuesta.md) |
| Guía de configuración de Startti | [docs/configuracion-startti.md](../../docs/configuracion-startti.md) |
| Guía de Kaggle (Secrets) | [docs/configuracion-kaggle.md](../../docs/configuracion-kaggle.md) |

**Kaggle:** Internet activado. La GPU T4 es opcional (acelera la parte de finanzas y la de educación); con CPU también funciona. Para Startti: *Add-ons → Secrets* → `STARTTI_API_KEY`, adjunto al notebook.

> ⚠️ Todas las organizaciones de la sesión son **ficticias**. Los prototipos son ejercicios de clase: **no son consejo médico, financiero ni académico**.

## Challenge de la sesión (evaluación)

Tu código estudiantil te asigna un **sector** (salud, finanzas o educación), un **caso** de una organización ficticia y tus **parámetros de ROI** (volumen, adopción, fracción de ahorro, costo por hora, costo de implementación y costo mensual).

1. **Prototipo del sector y asistente del caso (ejecución técnica):** corre el prototipo de tu sector sobre tu muestra personal y mide su calidad *q* (exactitud, exactitud *top-3* o tasa de preguntas respondibles); luego prueba un asistente que responde con el documento de tu caso (agente de Startti **o** alternativa en Python) con preguntas dentro y fuera del documento.
2. **Canvas del caso (análisis):** valor, factibilidad, riesgos con controles, KPI y *guardrail*, cada puntaje justificado con tus números o con el documento del caso.
3. **Explica y decide (análisis):** ROI, *payback* y *q* de equilibrio en un escenario base y uno pesimista, con la misma fórmula de las slides → *go*, *go* condicionado o *no-go*, con un criterio para detener el proyecto.
4. **Crítica a la IA (análisis):** un resumen ejecutivo escrito por IA con una estadística inventada, una afirmación legal falsa y datos que no coinciden con tus resultados: verifica cada afirmación con fuentes y corrígela.

- **Rúbrica:** ejecución técnica 40% · análisis e interpretación 40% · reflexión y registro de IA 20% ([evaluación](../../docs/evaluacion.md)).
- **IA permitida con registro obligatorio**: sin registro, ese componente vale 0.0 ([política de uso de IA](../../docs/politica-uso-ia.md)). **Micro-sustentaciones** al azar: si no puedes explicar tu entrega, la nota máxima es 3.0.
- **Startti es opcional:** sin clave de API, el notebook usa la alternativa en Python y la rúbrica es la misma.
- **Entrega:** `Archivo → Descargar notebook` → súbelo a e-Aulas como **`S09_<codigo>.ipynb`** antes de las **23:59** de hoy.

## Después de la clase (trabajo independiente ≈7 h)

- [ ] Termina y entrega el challenge (23:59).
- [ ] **Proyecto (≈4 h):** terminen y entreguen en grupo el **canvas de caso de uso (H3)** antes de las 23:59: línea base medida (B2), valor × factibilidad con evidencia (B3), KPI y *guardrail* (B4), ROI base y pesimista con la fórmula de la sesión y supuestos explícitos (B5), riesgos (B6) y decisión (B7). **No inventen cifras:** si un valor es una estimación, díganlo y expliquen de dónde sale.
- [ ] Aplica las cuatro preguntas de transferencia (¿misma tarea, mismos usuarios, misma medida de calidad, mismo contexto?) a la fuente principal que cite tu grupo.
- [ ] Practica con los ejercicios 🧪 del lab: cambia el verbalizador, el número de vecinos *k*, el nivel de las preguntas y el umbral de similitud del agente.
- [ ] Lectura para la S10 (viernes 23 de octubre, 18:00): Bender, Gebru et al. (2021), *On the Dangers of Stochastic Parrots* (resumen y secciones 4–6).

## Lecturas y recursos

- Brynjolfsson, E., Li, D., & Raymond, L. R. (2023). *Generative AI at work* (NBER Working Paper 31161). https://www.nber.org/papers/w31161 — versión publicada en *The Quarterly Journal of Economics*, 140(2), 2025.
- Dell'Acqua, F., McFowland, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). *Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality* (Harvard Business School Working Paper 24-013).
- McKinsey & Company. (2023). *The economic potential of generative AI: The next productivity frontier*.
- Singhal, K., Azizi, S., Tu, T., Mahdavi, S. S., et al. (2023). Large language models encode clinical knowledge. *Nature, 620*, 172–180. https://doi.org/10.1038/s41586-023-06291-2
- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences, 122*(26).
- Araci, D. (2019). *FinBERT: Financial sentiment analysis with pre-trained language models*. arXiv:1908.10063.
- *Moffatt v. Air Canada*, 2024 BCCRT 149 (Civil Resolution Tribunal de British Columbia, 14 de febrero de 2024).
- Lecher, C. (2024, 29 de marzo). NYC's AI chatbot tells businesses to break the law. *The Markup*.
- Welbl, J., Liu, N. F., & Gardner, M. (2017). Crowdsourcing multiple choice science questions. *Workshop on Noisy User-generated Text (W-NUT)* (dataset SciQ).
- **En español y contexto colombiano:**
  - Congreso de Colombia. (2012). *Ley Estatutaria 1581 de 2012*, por la cual se dictan disposiciones generales para la protección de datos personales.
  - Superintendencia de Industria y Comercio. (2024). *Circular Externa 002 de 2024*: tratamiento de datos personales en sistemas de inteligencia artificial.
  - Departamento Nacional de Planeación. (2025). *Documento CONPES 4144: Política Nacional de Inteligencia Artificial*.
  - CENIA y CEPAL. (2025). *Índice Latinoamericano de Inteligencia Artificial (ILIA)*.
- Datasets del lab y del challenge: `zeroshot/twitter-financial-news-sentiment`, `gretelai/symptom_to_diagnosis` y `allenai/sciq` (Hugging Face).
