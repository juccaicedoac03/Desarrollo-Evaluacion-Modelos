# Desarrollo y Evaluación de Modelos Propios

**Guía de asignatura** · Escuela de Administración (Rosario GSB) · Universidad del Rosario

*Última actualización: septiembre de 2026*

> Versión en Markdown de [`guia-de-asignatura.docx`](guia-de-asignatura.docx), diligenciada sobre el formato institucional *Formato Guía de Asignatura*. Ambos archivos tienen el mismo contenido.

## 1. Información general

| Campo | Detalle |
|---|---|
| **Nombre de la asignatura** | Desarrollo y Evaluación de Modelos Propios – Gr. 1 |
| **Escuela o facultad** | Escuela de Administración (Rosario GSB) |
| **Programa** | Especialización en Inteligencia Artificial Generativa y Desarrollo de Negocios |
| **Código** | 75220005 |
| **Tipo de asignatura** | Obligatoria (tipo de saber: básico) |
| **Número de créditos** | 3 |
| **Tipo de crédito** | Asignatura virtual (teórico-práctica) |
| **Horas de trabajo semanal con acompañamiento directo del profesor** | 36 horas: 12 sesiones sincrónicas de 3 horas, en 8 encuentros (4 viernes con una sesión de 3 horas y 4 sábados con dos sesiones consecutivas de 3 horas). |
| **Horas semanales de trabajo independiente del estudiante** | 9 horas por sesión (108 horas en el periodo académico). Total del curso: 144 horas. |
| **Prerrequisitos** | Ninguno |
| **Correquisitos** | Ninguno |
| **Horario** | Del 2 al 24 de octubre de 2026 (hora de Colombia): viernes 2, 9, 16 y 23 de octubre, de 18:00 a 21:00 (una sesión); sábados 3, 10, 17 y 24 de octubre, de 7:00 a 13:00 (dos sesiones consecutivas: 7:00–10:00 y 10:00–13:00). |
| **Salón** | Aula virtual (enlace de videoconferencia publicado en e-Aulas) |

## 2. Información del profesor

| Campo | Detalle |
|---|---|
| **Nombre del profesor** | Julian Camilo Caicedo Acosta |
| **Perfil profesional** | Ingeniero electrónico, magíster en Ingeniería con énfasis en automatización industrial y doctor en Ingeniería con énfasis en automatización basada en inteligencia artificial (tesis laureada) de la Universidad Nacional de Colombia, sede Manizales. Tiene más de 7 años de experiencia en el desarrollo de soluciones de ciencia de datos y aprendizaje automático en la empresa y la academia, con énfasis en IA generativa, visión por computador y despliegue en la nube (AWS, GCP y Azure). Es CEO y cofundador de Startti AI, empresa dedicada a la creación y orquestación de agentes de IA autónomos para la automatización de procesos de negocio. Ha dirigido las áreas de ciencia y analítica de datos de ALTIPAL, Sumatec y BIOS (Centro de Bioinformática y Biología Computacional de Colombia), y lideró el desarrollo de una plataforma de medición del espectro electromagnético con la Universidad Nacional de Colombia y la Agencia Nacional del Espectro. Fue profesor e investigador en IA y automatización en la Universidad Autónoma de Manizales (2020–2023) y es autor de publicaciones científicas sobre aprendizaje automático aplicado a señales EEG, neurociencia y visión por computador. |
| **Correo electrónico institucional** | [julian.caicedo@urosario.edu.co](mailto:julian.caicedo@urosario.edu.co) |
| **Lugar y horario de atención** | Virtual (videoconferencia), con cita previa solicitada al correo institucional. Respuesta en máximo 2 días hábiles. |
| **Página web u otros medios (opcional)** | Portal del curso: [https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/)<br>Repositorio de materiales: [https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos](https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos) |

## 3. Resumen y propósitos del curso

### Resumen

El curso *Desarrollo y Evaluación de Modelos Propios* ofrece a los estudiantes las competencias necesarias para entrenar, ajustar y evaluar modelos generativos y preentrenados, como GPT, BERT y los autoencoders variacionales (VAE). A lo largo del curso, los participantes exploran técnicas de afinamiento y métricas de evaluación, y las aplican en el desarrollo de soluciones prácticas como chatbots, agentes, clasificadores de texto y otros sistemas de IA orientados a problemas reales.

Con un enfoque de aprendizaje experiencial, el curso analiza casos de uso en sectores como salud, finanzas, educación y servicio al cliente, e integra las prácticas éticas, la reducción de sesgos, la privacidad y la sostenibilidad de los modelos, así como su impacto social. Los estudiantes culminan con un proyecto final en el que diseñan, entrenan o afinan, evalúan y mejoran un modelo propio adaptado a un problema contextualizado, lo que fortalece su capacidad de innovar con inteligencia artificial.

El curso es virtual y eminentemente práctico. Cada una de las 12 sesiones sincrónicas de 3 horas combina una exposición interactiva, una práctica guiada en notebooks de Kaggle y un *challenge* evaluado al final de la sesión. Así, el aprendizaje se evalúa de forma continua —en cada sesión y no mediante exámenes parciales— y el estudiante recibe retroalimentación frecuente sobre su progreso. Las actividades parten de reconocer que los estudiantes usan asistentes de IA (ChatGPT, Claude, Codex, entre otros): su uso se permite de forma transparente y con registro, y la evaluación se centra en el análisis, en la justificación de decisiones con resultados propios y en la capacidad de explicar el trabajo entregado.

El curso se fundamenta en bibliografía reciente y validada, lo que garantiza su pertinencia y su alineación con los avances actuales en IA generativa y aprendizaje automático.

### Propósitos de formación

El curso tiene como propósito formar profesionales capaces de diseñar, entrenar, evaluar y adaptar modelos de inteligencia artificial generativa y preentrenados para resolver problemas específicos en diversos contextos. A través del desarrollo de habilidades técnicas y conceptuales, los estudiantes aprenden a aplicar herramientas de aprendizaje automático, integrar métricas de evaluación y desarrollar soluciones prácticas como chatbots y clasificadores, todo enmarcado en principios éticos y sostenibles.

Asimismo, el curso busca fomentar un pensamiento crítico e innovador, a partir de una comprensión integral de casos de uso reales, y promover la capacidad de implementar modelos de IA que tengan un impacto positivo en la sociedad y en las organizaciones.

## 4. Conceptos fundamentales

El curso se organiza alrededor de los siguientes conceptos clave. Entre paréntesis se indican las sesiones (S) en las que se trabajan con mayor profundidad; todos se integran en el proyecto final.

- **Modelos generativos y discriminativos:** modelar la distribución de los datos, p(x) o p(x, y), frente a modelar directamente la decisión, p(y | x); familias autorregresivas, autoencoders, VAE, GAN y modelos de difusión (S1, S8).
- **Modelos preentrenados y fundacionales:** modelos entrenados a gran escala (BERT, GPT, T5) que se reutilizan y adaptan; decisión entre construir, adaptar o comprar (*build vs. buy*) y licencias de uso (S1, S3).
- **Arquitectura Transformer:** mecanismo de atención, tokenización y *embeddings*; variantes codificador, decodificador y codificador-decodificador (S3).
- **Entrenamiento y optimización:** funciones de pérdida, optimizadores, tasa de aprendizaje, preprocesamiento de datos, sobreajuste, regularización y fuga de datos (S2).
- **Autoencoders variacionales (VAE):** espacio latente, cota inferior de la evidencia (ELBO) y truco de reparametrización (S2, S8).
- **Transferencia de aprendizaje:** extracción de características, aprendizaje *zero-shot* y *few-shot*, y selección de modelos según los datos disponibles (S3).
- **Afinamiento completo y eficiente:** *fine-tuning* completo frente a métodos eficientes en parámetros como LoRA y QLoRA; ajuste por instrucciones, hiperparámetros, datasets propios y olvido catastrófico; cuándo usar *prompting*, RAG o afinamiento (S4).
- **Métricas de evaluación:** perplejidad, BLEU, ROUGE, chrF, similitud semántica y LLM como juez; exactitud, precisión, exhaustividad (*recall*) y F1 para clasificación (S5).
- **Validación y análisis de errores:** particiones de datos, validación cruzada (*k-fold*), análisis por segmentos y pruebas de robustez (S5, S11).
- **Aplicaciones: clasificadores, chatbots y agentes:** del modelo al producto; umbrales de confianza y humano en el ciclo; flujos conversacionales (Rasa, Dialogflow CX), RAG y agentes (S6, S7, S8).
- **Ética, sesgo, privacidad y sostenibilidad:** equidad, protección de datos personales, marcos regulatorios, huella de carbono y documentación con *model cards* y *datasheets* (S10).
- **Mejora continua y MLOps:** ciclo iterativo de evaluación y mejora, seguimiento de experimentos, optimización de hiperparámetros, eficiencia (cuantización, destilación), monitoreo y deriva de datos (S11).

## 5. Resultados de aprendizaje esperados (RAE)

Al finalizar el curso, el estudiante estará en capacidad de:

**RAE 1.** **Diseñar** modelos generativos y preentrenados adaptados a necesidades específicas en diversos contextos, entrenándolos y afinándolos con herramientas y *frameworks* actuales (PyTorch, TensorFlow/Keras y Hugging Face).

**RAE 2.** **Evaluar** el desempeño de los modelos entrenados mediante métricas estándar y métodos de validación, para verificar su precisión, eficiencia y robustez, aplicando principios éticos en su desarrollo.

**RAE 3.** **Desarrollar** prototipos funcionales de aplicaciones de inteligencia artificial —como chatbots, agentes y clasificadores— ajustados a requerimientos reales del mercado.

**RAE 4.** **Analizar** casos de uso reales para integrar modelos generativos en problemas concretos, considerando factores sociales, económicos y tecnológicos.

**RAE 5.** **Identificar** oportunidades para incorporar modelos generativos en contextos empresariales y sociales que impulsen la innovación y la transformación digital.

**RAE 6.** **Gestionar** los riesgos y la calidad en la implementación de modelos generativos, anticipando y mitigando riesgos para garantizar su sostenibilidad, escalabilidad y cumplimiento regulatorio.

La relación entre cada RAE, las sesiones y las actividades de evaluación se presenta en las secciones de actividades de evaluación y de programación de actividades.

## 6. Modalidad del curso

**Virtual.** El curso se desarrolla en su totalidad de forma remota y sincrónica: 12 sesiones de 3 horas por videoconferencia, los viernes y sábados entre el 2 y el 24 de octubre de 2026, cuyo enlace se publica en e-Aulas. El aula virtual e-Aulas concentra la guía, los enlaces a los materiales, las entregas, los foros y los anuncios del curso.

Las prácticas se realizan en notebooks de Kaggle, que ofrece GPU gratuita (con Google Colab como alternativa), y en las sesiones 6, 7 y 9 en la plataforma de agentes Startti ADP, siempre con una alternativa en Python que no requiere cuenta. Todos los materiales están disponibles en el portal del curso ([https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/)) y en su repositorio público.

**Idiomas.** Las presentaciones y los notebooks de práctica guiada están en inglés (lectura técnica); los challenges, las rúbricas, el proyecto final y los documentos del curso están en español.

**Requisitos técnicos.** Computador con navegador actualizado, conexión estable a internet, cámara y micrófono (se usan en las micro-sustentaciones y en la socialización del proyecto), cuenta de Kaggle con verificación telefónica y cuenta en Startti ADP (licencia sin costo entregada por el curso). No se requiere instalar software ni contar con un computador de alto desempeño.

## 7. Estrategias de aprendizaje

El curso privilegia metodologías activas y centradas en el estudiante, en coherencia con el Proyecto Educativo Institucional. Las estrategias transversales son:

- **Aprendizaje activo con clases interactivas:** la teoría se presenta con una interacción cada 10 minutos, aproximadamente: preguntas en vivo, simuladores, encuestas y salas de grupos con temporizador.
- **Aula invertida ligera:** antes de cada sesión el estudiante dedica cerca de 2 horas a lecturas y recursos cortos, para aprovechar el tiempo sincrónico en práctica y discusión.
- **Aprendizaje basado en proyectos:** un proyecto grupal atraviesa el curso, con hitos formativos entre S3 y S10 (grupos, propuesta, canvas de caso de uso e iteración de mejora), y culmina con la socialización en S12.
- **Aprendizaje experiencial con casos reales:** laboratorios, challenges y discusiones trabajan casos de salud, finanzas, educación y servicio al cliente, con organizaciones ficticias y datos abiertos.
- **Laboratorios prácticos en la nube:** notebooks en Kaggle con GPU gratuita (Google Colab como alternativa), sin instalaciones locales.
- **IA como copiloto, con uso transparente:** se promueve el uso de asistentes de IA para programar, explicar y depurar, siempre con registro, verificación y responsabilidad sobre lo entregado.
- **Evaluación continua:** cada sesión cierra con un challenge individual y retroalimentación, de modo que el estudiante conoce su progreso sesión a sesión.

### Estructura de cada sesión (180 minutos)

| Bloque | Minutos | Actividad |
|---|---|---|
| **Calentamiento** | 10 | Quiz de repaso de la sesión anterior (diagnóstico, no calificado). |
| **Teoría** | 60 | Exposición interactiva: una interacción cada ~10 minutos (quiz, simulador, encuesta o sala de grupos con temporizador). |
| **Descanso** | 10 | — |
| **Práctica guiada** | 60 | Programación en vivo en Kaggle con puntos de control (*checkpoints*). |
| **Challenge** | 40 | Evaluación individual calificada y micro-sustentaciones en vivo; entrega hasta las 23:59 del mismo día. |

Durante la práctica guiada, el profesor programa en vivo y el grupo avanza con él; los puntos de control (*checkpoints*) permiten verificar que todos avanzan antes de continuar. En el bloque de challenge, el profesor acompaña el trabajo individual y realiza las micro-sustentaciones.

## 8. Actividades de evaluación

La evaluación es continua y está alineada con los RAE. No hay exámenes parciales: cada sesión (1 a 11) termina con un challenge individual calificado y el curso culmina con un proyecto final grupal. La escala de calificación es de 0.0 a 5.0 y la nota aprobatoria es 3.0.

### Composición de la nota final

- **Challenges de sesión (S1–S11): 70%.** Cuentan las mejores 10 de 11 notas y cada una vale 7%. Esta regla absorbe una ausencia o una entrega fallida.
- **Proyecto final en grupos de 3: 30%.** Entregable técnico 15%, socialización y demo 10% y defensa individual 5%.
- **Factor de coevaluación (0.7–1.0).** La nota del proyecto de cada estudiante se multiplica por un factor que resulta de la evaluación de pares dentro del grupo.

*Nota final = 0.07 × (suma de las 10 mejores notas de challenge) + factor de coevaluación × (0.15 × entregable técnico + 0.10 × socialización y demo + 0.05 × defensa individual).*

### El challenge de cada sesión

El challenge es un notebook de Kaggle que se trabaja en los últimos 40 minutos de la sesión y se entrega en e-Aulas hasta las 23:59 del mismo día, con el nombre `S<NN>_<codigo>.ipynb`. Su diseño anticipa el uso de asistentes de IA:

- **Personalización:** el código estudiantil genera una semilla que asigna a cada estudiante datos, hiperparámetros, dominio o escenario propios; una huella de resultados al final del notebook permite detectar entregas copiadas o resultados inventados.
- **Preguntas “Explica y decide”:** decisiones técnicas o de negocio que exigen citar los resultados propios.
- **Crítica a la IA:** encontrar, explicar y corregir errores sembrados en código o en textos “generados por un asistente”, o verificar la respuesta del propio asistente.
- **Registro de uso de IA obligatorio:** herramienta, prompts principales y qué se verificó o corrigió de cada respuesta.
- **Micro-sustentaciones:** en cada sesión, 3 o 4 estudiantes elegidos al azar explican en vivo una celda de su notebook (2–3 minutos, con cámara y pantalla compartida); cada estudiante pasa al menos dos veces durante el curso. Si el estudiante no puede explicar su propia entrega, la nota de ese challenge se limita a 3.0.

Cada challenge se califica con la siguiente rúbrica general:

- **Ejecución técnica (40%):** el notebook corre con la configuración personal y las tareas están completas.
- **Análisis e interpretación (40%):** las respuestas usan los números propios y las decisiones están justificadas.
- **Reflexión y registro de IA (20%):** reflexión metacognitiva y registro de uso de IA verificable. Si falta el registro de IA, este componente se califica con 0.

### Proyecto final

En grupos de 3, los estudiantes diseñan, entrenan o afinan, evalúan y mejoran un modelo propio para un problema contextualizado (de preferencia colombiano o latinoamericano) y lo exponen mediante una app (Gradio) o un agente (Startti ADP). Los mínimos técnicos son: modelo afinado o entrenado por el grupo; línea base y comparación; al menos dos métricas justificadas; análisis de errores; una iteración de mejora documentada; análisis ético y de sostenibilidad; *model card*; y demo funcional.

Los hitos formativos son obligatorios y reciben retroalimentación: conformación de grupos (S3), propuesta en formato canvas (entrega hasta el miércoles 14 de octubre a las 23:59, con retroalimentación escrita en S7), canvas de caso de uso (S9), iteración de mejora (documentada en el informe técnico y entregada con la entrega final, el viernes 23 de octubre a las 23:59) y socialización (S12: 8 minutos de pitch, 3 de demo y 4 de preguntas por grupo; se acepta una demo pregrabada como respaldo). Los hitos no tienen nota propia, pero cada hito (H1–H4) que no se entregue en su plazo descuenta 0.3 de la nota del entregable técnico (máximo −1.2).

### Autoevaluación, coevaluación y heteroevaluación

- **Autoevaluación:** en la reflexión de cada challenge el estudiante propone y justifica su nota; al cierre del proyecto, cada estudiante valora su propio aporte.
- **Coevaluación:** evaluación de pares dentro de cada grupo (base del factor de coevaluación) y retroalimentación entre grupos durante la socialización de S12.
- **Heteroevaluación:** el profesor califica los challenges y el proyecto con rúbricas conocidas de antemano y retroalimenta cada entrega.

### Actividades según el propósito de la evaluación

La siguiente tabla resume las actividades según su propósito (diagnóstico, formativo o sumativo), el momento del curso, los RAE asociados y su peso en la nota final.

| Propósito de evaluación | Corte del semestre | Actividad de evaluación | RAE asociado | Porcentaje |
|---|---|---|---|---|
| **Evaluación diagnóstica** | Sesión 1 y calentamiento de cada sesión | Diagnóstico de entrada (perfil, experiencia previa y alfabetización en IA) en S1 y quiz de repaso al inicio de cada sesión. | RAE 1–6 | No calificada |
| **Evaluación formativa** | Sesiones 1–11 | Checkpoints del lab guiado, quizzes y simuladores en clase; reflexión y autoevaluación en cada challenge; retroalimentación de cada entrega con la rúbrica. | RAE 1–6 | No calificada |
| **Evaluación formativa** | Sesiones 3–10 (diálogo formativo: sesiones 4 a 7) | Hitos del proyecto con retroalimentación: grupos (S3), propuesta (después de S6, con retroalimentación en S7), canvas de caso de uso (S9) e iteración de mejora (con la entrega final, antes de S11). | RAE 1–6 | No calificada (obligatoria; −0.3 en el entregable técnico por hito no entregado, máximo −1.2) |
| **Evaluación sumativa** | Sesiones 1–11 | Challenges de sesión, individuales y personalizados (rúbrica 40/40/20); cuentan las mejores 10 de 11 notas, con un peso de 7% cada una. | RAE 1–6, según la sesión (ver programación) | 70% |
| **Evaluación sumativa** | Sesión 12 | Proyecto final: entregable técnico (15%), socialización y demo (10%) y defensa individual (5%), multiplicado por el factor de coevaluación (0.7–1.0). | RAE 1–6 | 30% |
| **Total nota final** |  |  |  | **100%** |

## 9. Programación de actividades

La programación organiza las 12 sesiones del curso, entre el 2 y el 24 de octubre de 2026: los viernes de 18:00 a 21:00 hay una sesión y los sábados de 7:00 a 13:00 hay dos sesiones consecutivas (7:00–10:00 y 10:00–13:00). Cada sesión sincrónica dura 3 horas (calentamiento 10 min, teoría 60 min, descanso 10 min, práctica guiada 60 min y challenge 40 min). A cada sesión le corresponden cerca de 9 horas de trabajo independiente: preparación previa (≈2 h), cierre y entrega del challenge (≈2 h), práctica autónoma (≈2 h) y proyecto final (≈3 h). Como las sesiones del sábado son consecutivas, la preparación de S2–S3, S5–S6, S8–S9 y S11–S12 se hace antes del viernes correspondiente.

Los títulos de las sesiones se presentan en español y, entre paréntesis, en inglés, idioma de las presentaciones y de los notebooks de práctica guiada. Los materiales de cada sesión (presentación, lab, challenge y guía de la sesión) están en el portal del curso: [https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/). En la columna de recursos, las referencias remiten a la sección de bibliografía.

| Sesión | Temas o conceptos fundamentales | Trabajo con acompañamiento directo del profesor (3 h) | Trabajo independiente del estudiante (9 h) | Recursos y e-recursos (herramientas, plataformas, bibliografía) |
|---|---|---|---|---|
| **S1**<br>Viernes 2 oct.<br>18:00–21:00 | **Introducción a los modelos generativos y preentrenados** (*Introduction to Generative and Pretrained Models*)<br>Generativo vs. discriminativo; familias de modelos (autorregresivos, autoencoders, VAE, GAN, difusión); modelos fundacionales; espectro construir, adaptar o comprar; PyTorch, TensorFlow/Keras y Hugging Face; aplicaciones de la IA.<br>*RAE 1, 4, 5* | **Calentamiento:** diagnóstico de entrada; presentación del curso, la evaluación y la política de uso de IA.<br>**Teoría:** simulador de muestreo (temperatura y top-k) y simulador *build vs. buy*; sala de grupos: ubicar 5 casos de negocio en el espectro de adaptación.<br>**Lab:** tensores y autograd en PyTorch, el mismo modelo en Keras, pipelines de Hugging Face, tokenización y parámetros de generación.<br>**Challenge:** muestreo con temperaturas asignadas, diversidad distinct-n, recomendación *build vs. buy* y crítica a la IA. | Crear la cuenta de Kaggle con verificación telefónica y revisar e-Aulas.<br>Cerrar y entregar el challenge (23:59).<br>Lectura: Goodfellow et al. (2016), caps. 1 y 5.<br>Práctica autónoma con los ejercicios del lab. | Presentación S01<br>Lab y challenge en Kaggle (alternativa: Colab)<br>Guía de configuración de Kaggle<br>Goodfellow et al. (2016); McKinsey & Company (2023); Hugging Face (s. f.) |
| **S2**<br>Sábado 3 oct.<br>7:00–10:00 | **Entrenamiento de modelos generativos** (*Training Generative Models*)<br>Ciclo de entrenamiento; funciones de pérdida y optimizadores; tasa de aprendizaje; sobreajuste y regularización; preprocesamiento y fuga de datos; autoencoders y VAE (ELBO, reparametrización); VAE vs. GAN vs. difusión.<br>*RAE 1, 2* | **Teoría:** simuladores de tasa de aprendizaje y de sobreajuste; sala de grupos: errores de preprocesamiento en un conjunto de datos de CRM.<br>**Lab:** VAE en Fashion-MNIST con PyTorch: curvas de pérdida, reconstrucción, muestreo e interpolación en el espacio latente.<br>**Challenge:** VAE con dimensión latente, β y tasa de aprendizaje asignados; comparación con la línea base; corrección de errores sembrados en el ciclo de entrenamiento. | Cerrar y entregar el challenge.<br>Lectura: Kingma y Welling (2014); Goodfellow et al. (2016), caps. 8 y 14.<br>Repetir el lab con otra configuración y comparar. | Presentación S02<br>Lab y challenge en Kaggle (GPU)<br>Kingma y Welling (2014); Goodfellow et al. (2016); Google (2023) |
| **S3**<br>Sábado 3 oct.<br>10:00–13:00 | **Modelos preentrenados y transferencia de aprendizaje** (*Pretrained Models and Transfer Learning*)<br>Por qué funciona el preentrenamiento; arquitectura Transformer y atención; BERT, GPT y T5; tokenización y su costo en español; estrategias de transferencia; selección de modelos y licencias; modelos en español (BETO).<br>*RAE 1, 3* | **Teoría:** mapa de atención interactivo y calculadora de costo por tokens; sala de grupos: elegir una estrategia de transferencia para 4 escenarios.<br>**Lab:** tokenización EN vs. ES, fill-mask con BERT, embeddings con regresión logística y clasificación zero-shot y few-shot con un LLM pequeño.<br>**Challenge:** curva de aprendizaje con el k asignado, few-shot y decisión según los datos disponibles.<br>Conformación de los grupos del proyecto final. | Cerrar y entregar el challenge.<br>Proyecto: conformar el grupo (3 personas) y explorar ideas.<br>Lectura: Vaswani et al. (2017); Devlin et al. (2019); Cañete et al. (2020). | Presentación S03<br>Lab y challenge en Kaggle<br>Vaswani et al. (2017); Devlin et al. (2019); Cañete et al. (2020); Jurafsky y Martin (2023) |
| **S4**<br>Viernes 9 oct.<br>18:00–21:00 | **Afinamiento de modelos generativos** (*Fine-Tuning Generative Models*)<br>Afinamiento completo vs. eficiente (LoRA, QLoRA); ajuste por instrucciones (SFT) y plantillas de chat; hiperparámetros; construcción de datasets propios; olvido catastrófico; prompt, RAG o afinamiento.<br>*RAE 1, 2* | **Teoría:** calculadora de parámetros LoRA y juego de hiperparámetros; sala de grupos: guía de etiquetado para un dataset de servicio al cliente.<br>**Lab:** DistilBERT afinado en Banking77 con Trainer y LoRA sobre SmolLM2 con un dataset propio.<br>**Challenge:** intents y configuraciones asignados; comparación de dos configuraciones; decisión entre afinamiento, RAG y prompting.<br>Inicio del diálogo formativo: balance de los challenges S1–S3. | Cerrar y entregar el challenge.<br>Lectura: Hu et al. (2021); OpenAI (2023).<br>Proyecto: redactar la propuesta (canvas). | Presentación S04<br>Lab y challenge en Kaggle (GPU)<br>Hu et al. (2021); Dettmers et al. (2023); OpenAI (2023)<br>Plantilla de propuesta del proyecto |
| **S5**<br>Sábado 10 oct.<br>7:00–10:00 | **Evaluación de modelos generativos** (*Evaluating Generative Models*)<br>Por qué es difícil evaluar la generación; perplejidad, BLEU, ROUGE, chrF, similitud semántica y LLM como juez; métricas de clasificación; validación cruzada y fuga de datos; análisis de errores; relación con KPI de negocio.<br>*RAE 2* | **Teoría:** calculadora BLEU/ROUGE y explorador de umbrales; sala de grupos: elegir métricas para 4 productos.<br>**Lab:** perplejidad, BLEU y chrF en traducción EN→ES, ROUGE en resúmenes, similitud semántica, validación cruzada estratificada y análisis de confusiones.<br>**Challenge:** métricas sobre muestras asignadas, un caso en el que la métrica falla y un plan de evaluación de negocio. | Cerrar y entregar el challenge.<br>Proyecto: avanzar en la propuesta (canvas).<br>Activar la licencia de Startti antes de S6.<br>Lectura: Jurafsky y Martin (2023), apartados de evaluación; Google (2023), métricas de clasificación. | Presentación S05<br>Lab y challenge en Kaggle<br>Jurafsky y Martin (2023); Google (2023) |
| **S6**<br>Sábado 10 oct.<br>10:00–13:00 | **Introducción al desarrollo de aplicaciones básicas** (*Introduction to Basic Application Development*)<br>Del modelo al producto; diseño conceptual de clasificadores y chatbots; patrones de arquitectura; UX para IA; umbrales de confianza y humano en el ciclo; Gradio frente a plataformas no-code (Startti ADP); latencia y costo.<br>*RAE 3, 4* | **Teoría:** simulador de umbral de enrutamiento (automatizar o escalar a un humano); sala de grupos: AI Product Canvas.<br>**Lab:** app en Gradio (clasificador con umbral de confianza y generador de texto) y primer agente en Startti llamado por API desde Kaggle.<br>**Challenge:** caso asignado; umbral de mínimo costo esperado; versión en Startti o alternativa en Python; comparación código vs. no-code.<br>Diálogo formativo: orientaciones para la propuesta del proyecto. | Cerrar y entregar el challenge.<br>Guardar la clave de API de Startti en Kaggle Secrets, lista para S7.<br>Proyecto: entregar la propuesta (canvas) en e-Aulas hasta el miércoles 14 de octubre, 23:59. | Presentación S06<br>Lab y challenge en Kaggle<br>Guía de configuración de Startti; Startti (s. f.)<br>Hugging Face (s. f.): demos con Gradio |
| **S7**<br>Viernes 16 oct.<br>18:00–21:00 | **Implementación de chatbots y agentes básicos** (*Implementing Basic Chatbots and Agents*)<br>De los bots basados en reglas a Rasa y Dialogflow CX (intents, entidades, slots, flujos); chatbots con LLM y RAG; agentes con herramientas; Startti ADP; diseño conversacional, escalamiento a humano e inyección de prompts; evaluación de chatbots.<br>*RAE 3, 4, 6* | **Teoría:** máquina de estados conversacional interactiva; sala de grupos: diseño del flujo de un caso asignado.<br>**Lab:** bot en Python (NLU, slots, estado y LLM de respaldo) y agente en Startti con base de conocimiento, evaluado desde Kaggle con conversaciones de prueba.<br>**Challenge:** dominio y FAQ asignados; 12 conversaciones de prueba; métricas por tipo; una iteración de mejora; ¿está listo para producción?<br>Diálogo formativo: devolución de la retroalimentación escrita de las propuestas. | Cerrar y entregar el challenge.<br>Lectura: Lewis et al. (2020); documentación de [Rasa](https://rasa.com/docs/) y de [Dialogflow CX](https://cloud.google.com/dialogflow/cx/docs).<br>Proyecto: ajustar el alcance según la retroalimentación y preparar los datos y la línea base. | Presentación S07<br>Lab y challenge en Kaggle<br>Startti ADP (alternativa en Python sin cuenta)<br>Lewis et al. (2020) |
| **S8**<br>Sábado 17 oct.<br>7:00–10:00 | **Creación de clasificadores con modelos generativos** (*Building Classifiers with Generative Models*)<br>Clasificadores generativos vs. discriminativos (Naive Bayes vs. regresión logística); características latentes de VAE; clasificación por verosimilitud con LLM; zero-shot; datos sintéticos; calibración; costo, latencia y privacidad.<br>*RAE 1, 2, 3* | **Teoría:** visualizador de fronteras de decisión y calculadora de costos; sala de grupos: recomendar un clasificador para 3 restricciones de negocio.<br>**Lab (PyTorch):** Naive Bayes vs. regresión logística con curva de aprendizaje, red MLP sobre embeddings, zero-shot por log-verosimilitud y aumento con datos sintéticos.<br>**Challenge:** tamaño de entrenamiento y clase minoritaria asignados; experimento de aumento; recomendación según restricciones; detección de fuga de datos sembrada. | Cerrar y entregar el challenge.<br>Lectura: Tunstall et al. (2022), capítulo de clasificación de texto.<br>Proyecto: entrenar o afinar el primer modelo y compararlo con la línea base. | Presentación S08<br>Lab y challenge en Kaggle<br>Tunstall et al. (2022); Kingma y Welling (2014); Goodfellow et al. (2016) |
| **S9**<br>Sábado 17 oct.<br>10:00–13:00 | **Casos de uso: modelos generativos en contextos reales** (*Use Cases: Generative Models in Real Contexts*)<br>Marcos para analizar casos de uso (valor × factibilidad, riesgo, KPI, ROI); salud, finanzas y educación; casos de éxito y fracasos documentados; contexto colombiano y latinoamericano.<br>*RAE 4, 5, 6* | **Teoría:** matriz valor × factibilidad y calculadora de ROI; sala de grupos: canvas de un caso por sector.<br>**Lab:** prototipos de sentimiento financiero, orientación de síntomas (salud, sin fines diagnósticos) y generación de preguntas (educación); agente sectorial en Startti.<br>**Challenge:** sector y caso asignados; prototipo, canvas y ROI; decisión go/no-go; verificación de una estadística inventada. | Cerrar y entregar el challenge.<br>Proyecto (hito formativo): canvas de caso de uso.<br>Lectura: McKinsey & Company (2023). | Presentación S09<br>Lab y challenge en Kaggle<br>McKinsey & Company (2023); Stanford University (2023) |
| **S10**<br>Viernes 23 oct.<br>18:00–21:00 | **Ética y sostenibilidad en modelos generativos** (*Ethics and Sustainability in Generative Models*)<br>Taxonomía de riesgos; sesgo y equidad; privacidad y datos personales (Ley 1581 de 2012); marcos y regulación (HLEG, Reglamento de IA de la UE, NIST AI RMF, UNESCO, CONPES 4144); huella de carbono; model cards y datasheets.<br>*RAE 2, 6* | **Teoría:** demo de sesgo contrafactual y calculadora de huella de carbono; sala de grupos: clasificar casos por nivel de riesgo del Reglamento de IA de la UE.<br>**Lab:** sondeo de sesgo con fill-mask, prueba contrafactual, detección y anonimización de datos personales (datos sintéticos), medición con CodeCarbon y model card.<br>**Challenge:** auditoría de sesgo con el atributo asignado; mitigación; clasificación regulatoria del caso y controles. | Cerrar y entregar el challenge.<br>Lectura: HLEG (2019); Bender et al. (2021); Mitchell et al. (2019).<br>Proyecto: análisis ético y de sostenibilidad y model card.<br>**Entrega final del proyecto:** viernes 23 de octubre, 23:59 (repositorio o notebook, informe técnico con la iteración de mejora documentada, model card, demo y registro de uso de IA). | Presentación S10<br>Lab y challenge en Kaggle<br>HLEG (2019); Reglamento (UE) 2024/1689; NIST (2023); UNESCO (2021); CONPES 4144 (2025); Ley 1581 de 2012<br>Luccioni et al. (2024); Gebru et al. (2021) |
| **S11**<br>Sábado 24 oct.<br>7:00–10:00 | **Evaluación y mejora continua de modelos** (*Evaluation and Continuous Model Improvement*)<br>Ciclo de mejora continua (MLOps); análisis de errores, hipótesis y correcciones; mejora centrada en datos; seguimiento de experimentos; optimización de hiperparámetros (Optuna); robustez (CheckList); eficiencia (cuantización, destilación); monitoreo y deriva.<br>*RAE 2, 6* | **Teoría:** diagrama del ciclo de mejora y demo de cuantización; sala de grupos: hoja de ruta de mejora del proyecto.<br>**Lab:** línea base con ruido de etiquetas, análisis por segmentos, limpieza y aumento, búsqueda con Optuna, pruebas de robustez, cuantización int8 y bitácora de experimentos.<br>**Challenge:** presupuesto de mejora asignado; bitácora con al menos dos iteraciones; reporte de robustez; decisión de despliegue con restricciones. | Cerrar y entregar el challenge.<br>Proyecto: ensayar la socialización de S12 (misma mañana, 10:00). | Presentación S11<br>Lab y challenge en Kaggle<br>Huyen (2022); Ribeiro et al. (2020)<br>Plantillas de informe técnico y model card |
| **S12**<br>Sábado 24 oct.<br>10:00–13:00 | **Proyecto integrador: desarrollo de solución completa** (*Integrative Project: Complete Solution*)<br>Integración de los conceptos del curso en un modelo propio funcional para un contexto aplicado; presentación y evaluación de los proyectos finales; cierre del curso.<br>*RAE 1–6* | **Socialización por grupo:** 8 min de pitch, 3 min de demo (se acepta demo pregrabada como respaldo) y 4 min de preguntas.<br>**Defensa individual:** preguntas a cada integrante sobre el trabajo del grupo.<br>Retroalimentación entre grupos y cierre del curso. | La entrega final se realizó el viernes 23 de octubre (ver S10).<br>Después de la sesión: coevaluación de pares y autoevaluación del proyecto. | Presentación de facilitación S12<br>Enunciado y rúbrica del proyecto final<br>Plantillas de coevaluación y de retroalimentación entre pares |

### Diálogo formativo (sesiones 4 a 7)

Entre las sesiones 4 y 7 se abre un espacio de diálogo formativo para que cada estudiante conozca su desempeño y ajuste su estrategia antes de la segunda mitad del curso: (a) en S4 (viernes 9 de octubre), cada estudiante revisa el balance de sus challenges S1–S3 (notas, comentarios de la rúbrica y su autoevaluación); (b) cada grupo entrega su propuesta de proyecto hasta el miércoles 14 de octubre y recibe retroalimentación escrita en S7 (viernes 16 de octubre); y (c) los estudiantes o grupos que lo requieran acuerdan una conversación breve con el profesor en el horario de atención.

## 10. Factores de éxito para este curso

Estas recomendaciones te ayudarán a gestionar tu autonomía y a aprovechar al máximo el curso:

- **Prepara tus herramientas antes de la primera sesión (viernes 2 de octubre):** crea tu cuenta de Kaggle y verifica tu número de teléfono (sin verificación no se habilitan la GPU ni el acceso a internet en los notebooks); activa tu licencia de Startti antes de la sesión 6 (sábado 10 de octubre) y guarda tu clave de API en Kaggle Secrets, nunca en el código.
- **Asegura tu conexión y tu espacio de trabajo:** internet estable, cámara y micrófono funcionando, y un plan alterno (por ejemplo, datos móviles) para las sesiones y las entregas.
- **Planifica cerca de 9 horas de trabajo independiente por sesión:** unas 2 h de preparación, 2 h para cerrar el challenge, 2 h de práctica autónoma y 3 h de proyecto. Como las sesiones se concentran los viernes y sábados, reserva tiempo de lunes a jueves y bloquéalo en tu agenda.
- **Llega preparado a cada sesión:** revisa las lecturas y la guía de la sesión; el quiz de calentamiento te indicará qué repasar.
- **Usa la IA de forma transparente y verifica todo:** registra herramientas y prompts, contrasta las respuestas con tus propios resultados y con fuentes confiables. Eres responsable de todo lo que entregas.
- **Comprende tu propio notebook:** cualquier estudiante puede ser llamado a una micro-sustentación con cámara encendida y pantalla compartida; practica explicar tus decisiones con tus números.
- **Entrega a tiempo, aunque no esté perfecto:** una entrega parcial con buen análisis vale más que ninguna. Recuerda que cuentan tus mejores 10 de 11 challenges.
- **Forma tu grupo de proyecto temprano:** conforma tu grupo en la sesión 3, acuerda con tus compañeros los roles y un canal de comunicación, y aprovecha los hitos formativos para recibir retroalimentación.
- **Pide ayuda a tiempo:** usa los foros de e-Aulas, el horario de atención y el diálogo formativo de las sesiones 4 a 7; si un error técnico te bloquea por más de 20 minutos, pregunta.
- **Aprende de la retroalimentación:** revisa la rúbrica y los comentarios de cada challenge y ajusta tu estrategia para la siguiente sesión.

## 11. Bibliografía y recursos

Bibliografía básica del sílabo, en formato APA (7.ª ed.). En la programación de actividades se indica la sesión en la que se usa cada referencia.

- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. En *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies* (Vol. 1, pp. 4171–4186). Association for Computational Linguistics. [https://doi.org/10.18653/v1/N19-1423](https://doi.org/10.18653/v1/N19-1423)
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press. [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/)
- Google. (2023). *Machine Learning Crash Course*. Google for Developers. [https://developers.google.com/machine-learning/crash-course](https://developers.google.com/machine-learning/crash-course)
- High-Level Expert Group on Artificial Intelligence. (2019). *Ethics guidelines for trustworthy AI*. Comisión Europea. [https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai)
- Jurafsky, D., & Martin, J. H. (2023). *Speech and language processing* (3.ª ed., borrador). Disponible en línea sin costo en [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/)
- Kingma, D. P., & Welling, M. (2014). Auto-encoding variational Bayes. En *2nd International Conference on Learning Representations (ICLR 2014)*. [https://arxiv.org/abs/1312.6114](https://arxiv.org/abs/1312.6114)
- McKinsey & Company. (2023). *The economic potential of generative AI: The next productivity frontier*. McKinsey Global Institute. [https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier)
- OpenAI. (2023). *Fine-tuning* [Guía de la documentación de la plataforma]. [https://platform.openai.com/docs/guides/fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)
- Stanford University. (2023). *CS230: Deep learning* [Materiales del curso]. [https://cs230.stanford.edu/](https://cs230.stanford.edu/)
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

## 12. Bibliografía y recursos complementarios

Referencias para ampliar los temas del curso, con fuentes internacionales y nacionales, obras de autoras y documentos en español.

- Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? En *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* (pp. 610–623). ACM. [https://doi.org/10.1145/3442188.3445922](https://doi.org/10.1145/3442188.3445922)
- Cañete, J., Chaperon, G., Fuentes, R., Ho, J.-H., Kang, H., & Pérez, J. (2020). Spanish pre-trained BERT model and evaluation data. En *PML4DC Workshop at ICLR 2020*. [https://github.com/dccuchile/beto](https://github.com/dccuchile/beto)
- Congreso de la República de Colombia. (2012). *Ley Estatutaria 1581 de 2012, por la cual se dictan disposiciones generales para la protección de datos personales*.
- Consejo Nacional de Política Económica y Social y Departamento Nacional de Planeación. (2025). *Documento CONPES 4144: Política Nacional de Inteligencia Artificial*. DNP.
- Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2023). QLoRA: Efficient finetuning of quantized LLMs. *Advances in Neural Information Processing Systems, 36*. [https://arxiv.org/abs/2305.14314](https://arxiv.org/abs/2305.14314)
- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12), 86–92. [https://doi.org/10.1145/3458723](https://doi.org/10.1145/3458723)
- Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. (2021). *LoRA: Low-rank adaptation of large language models* (arXiv:2106.09685). arXiv. [https://arxiv.org/abs/2106.09685](https://arxiv.org/abs/2106.09685)
- Hugging Face. (s. f.). *LLM Course*. [https://huggingface.co/learn/llm-course](https://huggingface.co/learn/llm-course)
- Huyen, C. (2022). *Designing machine learning systems: An iterative process for production-ready applications*. O'Reilly Media.
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems, 33*. [https://arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)
- Luccioni, A. S., Jernite, Y., & Strubell, E. (2024). Power hungry processing: Watts driving the cost of AI deployment? En *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency*. ACM. [https://doi.org/10.1145/3630106.3658542](https://doi.org/10.1145/3630106.3658542)
- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. En *Proceedings of the Conference on Fairness, Accountability, and Transparency* (pp. 220–229). ACM. [https://doi.org/10.1145/3287560.3287596](https://doi.org/10.1145/3287560.3287596)
- National Institute of Standards and Technology. (2023). *Artificial intelligence risk management framework (AI RMF 1.0)* (NIST AI 100-1). [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)
- Parlamento Europeo y Consejo de la Unión Europea. (2024). Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024, por el que se establecen normas armonizadas en materia de inteligencia artificial (Reglamento de Inteligencia Artificial). *Diario Oficial de la Unión Europea*. [https://eur-lex.europa.eu/eli/reg/2024/1689/oj](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Ribeiro, M. T., Wu, T., Guestrin, C., & Singh, S. (2020). Beyond accuracy: Behavioral testing of NLP models with CheckList. En *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 4902–4912). Association for Computational Linguistics. [https://doi.org/10.18653/v1/2020.acl-main.442](https://doi.org/10.18653/v1/2020.acl-main.442)
- Startti. (s. f.). *Documentación de Startti ADP*. [https://adp.startti.ai/docs](https://adp.startti.ai/docs)
- Tunstall, L., von Werra, L., & Wolf, T. (2022). *Natural language processing with transformers: Building language applications with Hugging Face* (ed. rev.). O'Reilly Media.
- UNESCO. (2021). *Recomendación sobre la ética de la inteligencia artificial*. UNESCO.

## 13. Acuerdos para el desarrollo del curso

Para el buen desarrollo del curso se establecen los siguientes acuerdos, en el marco del [Reglamento Formativo-Preventivo y Disciplinario](https://www.urosario.edu.co/Reglamento-Formativo-Preventivo-Disciplinario/Inicio/) de la Universidad:

- **Asistencia:** se registra la asistencia en cada sesión sincrónica. La cámara debe estar encendida en los momentos de evaluación (bloque de challenge, micro-sustentaciones y socialización del proyecto) y se recomienda durante toda la sesión. Las ausencias justificadas se tramitan según el reglamento académico.
- **Puntualidad:** las sesiones inician a la hora programada con el quiz de calentamiento; se espera conectarse unos minutos antes para resolver problemas técnicos.
- **Entregas:** los challenges se entregan en e-Aulas hasta las 23:59 del día de la sesión, como archivo `S<NN>_<codigo>.ipynb` descargado desde Kaggle. Los entregables del proyecto se entregan en las fechas publicadas en e-Aulas.
- **Entregas tardías:** hasta 24 horas después del plazo se descuentan 0.5 puntos de la nota; después de 24 horas la nota es 0.0. La regla de las mejores 10 de 11 notas absorbe una ausencia o una entrega fallida.
- **Comunicación:** los canales oficiales son los foros y la mensajería de e-Aulas y el correo institucional. Las dudas generales se publican en el foro para que todo el grupo se beneficie de la respuesta.
- **Respeto en la interacción virtual:** en el chat, los foros y las salas de grupos se mantiene un trato respetuoso; se pide la palabra y se valoran las distintas trayectorias (perfiles técnicos y de negocio).
- **Integridad académica y uso de IA:** el uso de asistentes de IA se rige por la [política de uso de IA del curso](https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/docs/politica-uso-ia.md). Todo uso se declara en el registro de IA; están prohibidos la suplantación, los resultados inventados y compartir las salidas personalizadas de un challenge. Los casos de plagio o fraude se tratan según el reglamento de la Universidad.
- **Datos personales y confidencialidad:** no se cargan datos personales ni información sensible o confidencial de organizaciones en Kaggle, Startti ni en asistentes de IA; en el curso se usan datos abiertos o sintéticos.
- **Grabaciones de clase:** las sesiones pueden grabarse solo con fines académicos y de acuerdo con las políticas de la Universidad, previo aviso al grupo. Las grabaciones se comparten únicamente en e-Aulas y no pueden difundirse fuera del curso; los estudiantes no deben grabar las sesiones sin autorización.

## 14. Respeto y no discriminación

Si tiene alguna discapacidad, sea este visible o no, y requiere algún tipo de apoyo para estar en igualdad de condiciones con los(as) demás estudiantes, por favor informar a su profesor(a) para que puedan realizarse ajustes razonables al curso a la mayor brevedad posible. De igual forma, si no cuenta con los recursos tecnológicos requeridos para el desarrollo del curso, por favor informe de manera oportuna a la Secretaría Académica de su programa o a la Dirección de Estudiantes, de manera que se pueda atender a tiempo su requerimiento.

Recuerde que es deber de todas las personas respetar los derechos de quienes hacen parte de la comunidad Rosarista. Cualquier situación de acoso, acoso sexual, discriminación o matoneo, sea presencial o virtual, es inaceptable. Quien se sienta en alguna de estas situaciones puede denunciar su ocurrencia contactando al equipo de la Coordinación de Psicología y Calidad de Vida de la Decanatura del Medio Universitario (Teléfono o WhatsApp 322 2485756).
