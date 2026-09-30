# Sesión 10 — Ethics and Sustainability in Generative Models
*Ética y sostenibilidad en modelos generativos*

**RAE asociados:** RAE 2, RAE 6 · **Duración:** 3 horas (virtual) · **Fecha:** viernes 23 de octubre de 2026, 18:00–21:00 (hora de Colombia)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. Mapear los principales riesgos de los modelos generativos (sesgo, privacidad, alucinación, propiedad intelectual, seguridad, usos indebidos, impacto ambiental e impacto laboral) y asignar a cada uno un responsable y un control.
2. Medir el sesgo de un modelo con pruebas contrafactuales y métricas de equidad: paridad demográfica, igualdad de oportunidades y tasa de cambio.
3. Detectar y redactar datos personales (nombres, cédula, celular, correo), distinguir seudonimización de anonimización y explicar qué exige la **Ley 1581 de 2012**.
4. Clasificar un caso de uso según el **Reglamento de IA de la UE** y el marco colombiano, y proponer controles.
5. Estimar la energía y las emisiones de un modelo con **CodeCarbon** y documentarlo en una ***model card***.

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Dos preguntas sobre los casos reales de la S09 (frontera irregular y responsabilidad por un chatbot) y tu propio caso de uso |
| Teoría | 60' | Mapa de riesgos · sesgo y equidad (simulador contrafactual) · privacidad y regulación (sala de grupos: clasificar 5 casos según el Reglamento de IA de la UE) · huella de carbono (calculadora), *model cards* y gobernanza |
| Pausa | 10' | — |
| Lab guiado | 60' | Sondeo de sesgo con *fill-mask* · prueba contrafactual de un clasificador · detección y redacción de datos personales (datos sintéticos) · medición con CodeCarbon · *model card* |
| Challenge | 40' | Auditoría de sesgo con tu atributo asignado, mitigación, clasificación regulatoria y crítica a la IA |

## Antes de la clase (≈2 h)

- Lee el resumen y las secciones 4 a 6 de Bender, Gebru, McMillan-Major y Shmitchell (2021), *On the dangers of stochastic parrots* (≈45 min).
- Revisa el capítulo 2 de las *Directrices éticas para una IA fiable* del Grupo de Expertos de Alto Nivel (HLEG, 2019): los siete requisitos (≈30 min).
- Lee Mitchell et al. (2019), *Model cards for model reporting*, secciones 1 a 4 (≈30 min).
- Trae a clase el caso de uso de tu proyecto (canvas del H3): lo usarás en el calentamiento.
- **Proyecto:** la entrega final vence **hoy a las 23:59**. Lleguen a clase con el informe técnico casi completo, incluida la iteración de mejora del hito H4 (sección 5), y con un primer borrador del análisis ético (sección 7) y de la *model card*, para ajustarlos con lo de hoy.

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/10-ethics-and-sustainability/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/10-ethics-and-sustainability/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/10-ethics-and-sustainability/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/10-ethics-and-sustainability/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/10-ethics-and-sustainability/challenge.ipynb) · [archivo](challenge.ipynb) |
| Plantilla de *model card* del proyecto | [model-card.md](../../proyecto-final/plantillas/model-card.md) |

**Configuración de Kaggle:** *Settings → Internet: On*. No necesitas GPU ni claves: todos los modelos son pequeños y corren en CPU. Todos los datos personales de los notebooks son **sintéticos**.

## Challenge de la sesión (evaluación)

Tu código estudiantil te asigna un **atributo** (género, nacionalidad o edad), **6 plantillas** de frases de un banco de 15, un **modelo** (clasificador de sentimiento o BERT *fill-mask*) y un **caso de uso** ficticio.

1. **Auditoría de sesgo contrafactual:** brecha media con intervalo de confianza *bootstrap*, diferencia de paridad demográfica, diferencia de igualdad de oportunidades, tasa de cambio y exactitud.
2. **Mitigación y nueva medición:** umbral por grupo y aumento contrafactual en inferencia, probados también con pares reservados.
3. **Explica y decide:** clasifica tu caso de uso según el Reglamento de IA de la UE y el marco colombiano (Ley 1581 de 2012, CONPES 4144, Circular Externa 002 de 2024 de la SIC), propone controles conectados con tus números y completa una mini *model card*.
4. **Crítica a la IA:** encuentra, explica y corrige los 3 errores de una declaración ética escrita por un asistente de IA.

**Rúbrica:** Ejecución técnica 40% · Análisis e interpretación 40% · Reflexión y registro de IA 20% (ver [evaluación](../../docs/evaluacion.md)).
**Entrega:** `File → Download notebook` → renómbralo `S10_<codigo>.ipynb` → súbelo a e-Aulas antes de las **23:59** de hoy.
**Uso de IA:** permitido, con el registro obligatorio al final del notebook ([política de uso de IA](../../docs/politica-uso-ia.md)). Puedes ser seleccionado(a) para una micro-sustentación: si no puedes explicar tu entrega, la nota máxima es 3.0.

## Después de la clase (trabajo independiente ≈7 h)

- Termina y entrega el challenge (≈1 h, hasta las 23:59).
- **Proyecto · entrega final y H4, hoy a las 23:59:** cierren el análisis ético y de sostenibilidad del proyecto (informe §7): riesgos específicos del caso, al menos una prueba empírica (desempeño por subgrupo o prueba contrafactual, como en el lab), anonimización de datos según la Ley 1581, clasificación de riesgo razonada y emisiones del entrenamiento medidas con CodeCarbon o estimadas con un método citado. Completen la [*model card*](../../proyecto-final/plantillas/model-card.md) (la del lab sirve de punto de partida) y verifiquen que la sección 5 del informe documenta la iteración de mejora (H4). Una persona del grupo sube la entrega final a e-Aulas antes de las 23:59 ([detalles](../12-integrative-project/README.md#entrega-final-viernes-23-de-octubre-2359)).
- Lecturas (≈2 h): Gebru et al. (2021), *Datasheets for datasets*; Luccioni, Jernite y Strubell (2024); y el documento CONPES 4144.
- **Prepara la S11 y la S12 antes del sábado 24 de octubre a las 7:00:** son seguidas (7:00–10:00 y 10:00–13:00). Haz las lecturas de la S11 ([guía](../11-continuous-improvement/README.md)) y ensayen el *pitch* y la demo de la S12 ([guía](../12-integrative-project/README.md)).

## Lecturas y recursos

**Riesgos y sesgo**
- Bender, E. M., Gebru, T., McMillan-Major, A., y Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *FAccT '21*. https://doi.org/10.1145/3442188.3445922
- Weidinger, L., et al. (2021). *Ethical and social risks of harm from language models*. arXiv. https://arxiv.org/abs/2112.04359
- Buolamwini, J., y Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. *FAT\* 2018*, PMLR 81. https://proceedings.mlr.press/v81/buolamwini18a.html
- Suresh, H., y Guttag, J. (2021). A framework for understanding sources of harm throughout the machine learning life cycle. *EAAMO '21*. https://arxiv.org/abs/1901.10002
- Hardt, M., Price, E., y Srebro, N. (2016). Equality of opportunity in supervised learning. *NeurIPS*. https://arxiv.org/abs/1610.02413
- Barocas, S., Hardt, M., y Narayanan, A. (2023). *Fairness and machine learning: Limitations and opportunities*. MIT Press. Libro abierto: https://fairmlbook.org
- Kiritchenko, S., y Mohammad, S. M. (2018). Examining gender and race bias in two hundred sentiment analysis systems. *\*SEM 2018*. https://aclanthology.org/S18-2005/

**Privacidad y seguridad**
- Carlini, N., et al. (2021). Extracting training data from large language models. *USENIX Security*. https://arxiv.org/abs/2012.07805
- Greshake, K., et al. (2023). Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. https://arxiv.org/abs/2302.12173
- OWASP GenAI Security Project. *Top 10 for LLM Applications*. https://genai.owasp.org/llm-top-10/

**Marcos y regulación**
- Congreso de Colombia. [Ley 1581 de 2012](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981), por la cual se dictan disposiciones generales para la protección de datos personales.
- Superintendencia de Industria y Comercio (2024). [Circular Externa 002 de 2024: lineamientos sobre el tratamiento de datos personales en sistemas de inteligencia artificial](https://sedeelectronica.sic.gov.co/sites/default/files/normativa/Circular%20Externa%20No.%20002%20del%2021%20de%20agosto%20de%202024.pdf).
- Departamento Nacional de Planeación (2025). [Documento CONPES 4144: Política Nacional de Inteligencia Artificial](https://colaboracion.dnp.gov.co/CDT/Conpes/Econ%C3%B3micos/4144.pdf).
- Grupo de Expertos de Alto Nivel sobre IA (2019). [Directrices éticas para una IA fiable](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai) (disponible en español).
- [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) (Reglamento de IA). Sus plazos de aplicación para sistemas de alto riesgo fueron modificados por el [Reglamento (UE) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj) ("Ómnibus digital sobre IA"); consulta siempre la versión consolidada vigente.
- NIST (2023). [AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework).
- UNESCO (2021). [Recomendación sobre la ética de la inteligencia artificial](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics).
- OCDE (2019, actualizada en 2024). [Principios de IA](https://oecd.ai/en/ai-principles).

**Sostenibilidad y documentación**
- Strubell, E., Ganesh, A., y McCallum, A. (2019). Energy and policy considerations for deep learning in NLP. *ACL*. https://arxiv.org/abs/1906.02243
- Luccioni, A. S., Jernite, Y., y Strubell, E. (2024). Power hungry processing: Watts driving the cost of AI deployment? *FAccT '24*. https://arxiv.org/abs/2311.16863
- Lacoste, A., Luccioni, A., Schmidt, V., y Dandres, T. (2019). *Quantifying the carbon emissions of machine learning*. https://arxiv.org/abs/1910.09700
- [CodeCarbon](https://codecarbon.io): medición de energía y emisiones en Python.
- Mitchell, M., et al. (2019). Model cards for model reporting. *FAT\* '19*. https://arxiv.org/abs/1810.03993
- Gebru, T., et al. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12). https://arxiv.org/abs/1803.09010
- Hugging Face. [Model Cards](https://huggingface.co/docs/hub/model-cards) (documentación).

> Este material es formativo y no constituye asesoría jurídica. Para un despliegue real, involucra al equipo legal y de protección de datos de tu organización.
