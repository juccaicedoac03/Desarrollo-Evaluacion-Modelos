# Evaluación del curso

*Desarrollo y Evaluación de Modelos Propios · Especialización en Inteligencia Artificial Generativa y Desarrollo de Negocios · Universidad del Rosario*

Este documento explica **cómo se calcula tu nota**, qué se espera en cada entrega y cómo funcionan las micro-sustentaciones, la personalización de los challenges y la huella de resultados. Léelo junto con la [política de uso de IA](politica-uso-ia.md).

---

## 1. Resumen

- **Escala:** 0.0 a 5.0. **Se aprueba con 3.0.**
- **No hay parciales ni examen final:** la evaluación es continua (un challenge por sesión) y cierra con un proyecto integrador.

| Componente | Peso | Cómo se obtiene |
|---|---|---|
| Challenges de sesión (S01–S11) | **70%** | 11 challenges individuales. Cuentan tus **mejores 10**; cada uno vale **7%** |
| Proyecto final (grupos de 3) | **30%** | Entregable técnico **15%** · Socialización y demo **10%** · Defensa individual **5%** |
| Factor de coevaluación | **×0.7–1.0** | Multiplica tu nota individual del proyecto según la evaluación de pares de tu grupo |

## 2. Cómo se calcula tu nota final

```text
Nota challenges      = promedio de tus 10 mejores challenges                   (0.0–5.0)
Nota proyecto        = (15 × Entregable + 10 × Socialización + 5 × Defensa) / 30   (0.0–5.0)
Proyecto individual  = Nota proyecto × Factor de coevaluación (0.7–1.0)
Nota final           = 0.70 × Nota challenges + 0.30 × Proyecto individual
```

**Ejemplo.** Una estudiante obtiene en sus 11 challenges: 4.5, 4.0, 3.8, 0.0 (no entregó el S04), 4.2, 4.6, 3.9, 4.4, 4.1, 4.3 y 4.7.

1. Se descarta la nota más baja (0.0). El promedio de las otras 10 es **4.25**.
2. En el proyecto, su grupo obtiene 4.0 en el entregable técnico y 4.5 en la socialización; ella obtiene 3.8 en su defensa individual: (15 × 4.0 + 10 × 4.5 + 5 × 3.8) / 30 = **4.13**.
3. Su factor de coevaluación es 0.9: 4.13 × 0.9 = **3.72**.
4. Nota final: 0.70 × 4.25 + 0.30 × 3.72 = 2.975 + 1.116 = **4.09**.

## 3. Challenges de sesión (70%)

### 3.1 Qué es un challenge

En los últimos 40 minutos de cada sesión (S01 a S11) resuelves de forma **individual** un notebook de Kaggle (`challenge.ipynb`) con 3 o 4 tareas. Todos los challenges incluyen:

- una configuración **personal** (datos, hiperparámetros o escenario asignados a partir de tu código estudiantil; ver la sección 6);
- una tarea **"Explica y decide"**: una decisión técnica o de negocio que debes justificar con *tus* números;
- una tarea **"Crítica a la IA"**: un texto o código "generado por un asistente" con errores sembrados que debes encontrar, explicar y corregir;
- una **reflexión** y el **registro de uso de IA**.

### 3.2 Entrega

1. Ejecuta el notebook completo, en orden, y verifica que aparezcan **"Tu configuración personal"** y la **huella de resultados** al final.
2. Descárgalo desde Kaggle: `File → Download notebook`.
3. Renómbralo como **`S<NN>_<codigo>.ipynb`** (por ejemplo, `S05_123456.ipynb` para la Sesión 05 si tu código es 123456).
4. Súbelo a **e-Aulas** antes de las **23:59 (hora de Colombia) del mismo día** de la sesión.

Revisa que subiste el challenge y no el lab, y que el archivo conserva las salidas: se califican tanto el código como los resultados impresos. Las instrucciones detalladas de Kaggle están en [configuracion-kaggle.md](configuracion-kaggle.md).

### 3.3 Mejores 10 de 11

De los 11 challenges se descarta automáticamente la nota más baja, sea cual sea la razón (una entrega que no hiciste, un mal día, un problema de conexión). **Guárdalo para una emergencia real**: no hay un segundo descarte. Las situaciones de fuerza mayor que vayan más allá de ese descarte se tramitan según el reglamento de la Universidad.

### 3.4 Entregas tardías

| Momento de la entrega | Consecuencia |
|---|---|
| Hasta las 23:59 del día de la sesión | Sin penalización |
| Hasta 24 horas después del plazo | **−0.5** sobre la nota obtenida |
| Más de 24 horas después del plazo | **0.0** (ese challenge puede ser el que se descarta en la regla de mejores 10 de 11) |

## 4. Rúbrica del challenge

Cada challenge se califica con tres componentes:

| Componente | Peso | Pregunta clave |
|---|---|---|
| **Ejecución técnica** | 40% | ¿El notebook corre con tu configuración personal y las tareas están completas? |
| **Análisis e interpretación** | 40% | ¿Tus respuestas usan tus propios números y tus decisiones están justificadas? |
| **Reflexión y registro de IA** | 20% | ¿Tu reflexión es específica y tu registro de uso de IA es verificable? |

### 4.1 Descriptores por nivel

| Componente | 5.0 · Excelente | 4.0 · Bueno | 3.0 · Aceptable | < 3.0 · Insuficiente |
|---|---|---|---|---|
| **Ejecución técnica (40%)** | El notebook corre de principio a fin con tu configuración personal. Todas las tareas están completas, el código es claro y se generan los resultados y la huella. | Corre completo y las tareas están completas, con fallas menores (una salida faltante, código poco legible, un valor mal redondeado). | Corre, pero una tarea está incompleta o tiene errores que afectan parte de los resultados. | No corre, no usa tu configuración personal, faltan varias tareas o no aparece la huella de resultados. |
| **Análisis e interpretación (40%)** | Las respuestas citan tus números y explican por qué ocurren. Las decisiones comparan alternativas (calidad, costo, riesgo, tiempo) y llegan a una recomendación clara. En la "Crítica a la IA" identificas, explicas y corriges todos los errores. | Usas tus números y justificas tus decisiones, con alguna interpretación superficial o un error de la IA sin detectar o sin explicar. | Las respuestas son genéricas o citan pocos de tus números. La decisión está poco justificada y la crítica a la IA es parcial. | No hay respuestas, son genéricas (podrían ser de cualquier estudiante) o contradicen tus resultados. No hay una decisión. |
| **Reflexión y registro de IA (20%)** | La reflexión es específica y honesta, y la autoevaluación está argumentada. El registro de IA está completo y es verificable: herramienta, propósito, prompt principal y qué verificaste o corregiste. | La reflexión es adecuada y el registro está completo, pero la verificación está poco detallada. | La reflexión es breve o genérica, o el registro está incompleto (por ejemplo, no dice qué verificaste). | La reflexión falta o no es pertinente. **Si falta el registro de IA, este componente vale 0.0.** |

Se pueden asignar notas intermedias (por ejemplo, 4.5 o 3.5) cuando el trabajo está entre dos niveles.

### 4.2 Cálculo de la nota del challenge

```text
Nota del challenge = 0.40 × Ejecución + 0.40 × Análisis + 0.20 × Reflexión y registro de IA
```

Después de aplicar la rúbrica, se aplican estas reglas, en este orden:

1. **Registro de IA ausente:** el componente de reflexión y registro de IA vale 0.0 (la nota máxima posible queda en 4.0). Si no usaste IA, escribe *"No usé asistentes de IA en este challenge."*: esa frase cuenta como registro.
2. **Micro-sustentación no aprobada:** la nota del challenge se limita a **3.0** (sección 5).
3. **Entrega tardía:** −0.5 si llega dentro de las 24 horas siguientes al plazo (sección 3.4).

**Ejemplos:**

| Ejecución | Análisis | Reflexión y registro | Situación | Nota |
|---|---|---|---|---|
| 4.5 | 4.0 | 5.0 | Entrega a tiempo | 0.4 × 4.5 + 0.4 × 4.0 + 0.2 × 5.0 = **4.4** |
| 4.5 | 4.0 | — | Sin registro de IA | 0.4 × 4.5 + 0.4 × 4.0 + 0.2 × 0.0 = **3.4** |
| 4.5 | 4.0 | 5.0 | No explicó su entrega en la micro-sustentación | 4.4 → tope → **3.0** |
| 4.5 | 4.0 | 5.0 | Entregó 10 horas tarde | 4.4 − 0.5 = **3.9** |

## 5. Micro-sustentaciones

Las micro-sustentaciones comprueban que **entiendes lo que entregas**, uses o no asistentes de IA. Son cortas, no son un examen oral y no buscan que recuerdes la sintaxis de memoria.

**Protocolo**

1. **Selección.** En cada sesión, durante el bloque de challenge, se eligen al azar 3 o 4 estudiantes. En el semestre, **cada estudiante pasa al menos 2 veces**; el sorteo da prioridad a quienes aún no completan sus dos turnos.
2. **Formato.** Compartes pantalla con tu notebook en vivo durante **2–3 minutos**. El profesor señala una celda o una respuesta de tu trabajo y te pregunta, por ejemplo:
   - ¿Qué hace esta celda y por qué la escribiste así?
   - ¿Qué significa este resultado para el caso que te tocó?
   - ¿Qué pasaría si cambias este parámetro?
   - ¿Qué error encontraste en el texto de la IA y cómo lo verificaste?
3. **Sin ayudas.** Durante la micro-sustentación no puedes consultar asistentes de IA ni recibir ayuda de otras personas. Sí puedes mirar tu notebook.
4. **Criterio.** Se aprueba si explicas con tus palabras qué hace tu código, qué significan tus resultados y por qué tomaste tus decisiones. Se valora el razonamiento, no la memoria.
5. **Resultado.**
   - **Aprobada:** no cambia tu nota.
   - **No aprobada:** la nota de ese challenge se limita a **3.0**.
6. **Problemas de conexión.** Si no puedes compartir pantalla por razones técnicas, la micro-sustentación se reprograma para la siguiente sesión o para el horario de atención.

Además de las micro-sustentaciones por sorteo, el profesor puede citarte a una conversación de verificación si encuentra inconsistencias en una entrega (por ejemplo, resultados que no coinciden con la huella o notebooks muy parecidos entre estudiantes). En esa conversación se aplica el mismo criterio.

## 6. Personalización y huella de resultados

### 6.1 Tu configuración personal

La primera celda de cada challenge te pide tu **código estudiantil** (`STUDENT_ID`, tal como aparece en e-Aulas). A partir de ese código, el notebook elige de forma automática y reproducible tu **configuración personal**: por ejemplo, qué subconjunto de datos usas, qué hiperparámetros pruebas o qué escenario de negocio analizas. La verás impresa bajo el título **"Tu configuración personal"**.

¿Qué implica esto para ti?

- Tus números van a ser **distintos** de los de tus compañeros, y tus respuestas deben basarse en **tus** números.
- Si ejecutas de nuevo el notebook con el mismo código, obtienes la misma configuración.
- Puedes discutir ideas y conceptos con tus compañeros; lo que no sirve es copiar respuestas, porque no corresponden a tu configuración.

### 6.2 La huella de resultados

La última celda del challenge imprime tu configuración, tus resultados principales y un código corto llamado **huella de resultados** (🔏). La huella resume en un solo código tu código estudiantil, tu configuración y tus resultados. Sirve para comprobar que los resultados que reportas salen de **tu** ejecución: el profesor puede volver a ejecutar tu notebook con tu código y comparar.

**Buenas prácticas**

- Escribe tu código estudiantil **exactamente** como aparece en e-Aulas, antes de ejecutar cualquier otra celda.
- No modifiques las celdas marcadas como *no editar*.
- Ejecuta todo en orden. Si te equivocaste de código, corrígelo y **vuelve a ejecutar todo desde el principio**.
- Escribe en tus respuestas los mismos números que imprimió tu notebook; no los cambies a mano.

Si al volver a ejecutar tu notebook ves variaciones mínimas en algunos números (por ejemplo, por diferencias entre GPU), es normal y se tiene en cuenta en la revisión. Lo que se revisa es la coherencia entre tu configuración, tus resultados y tus respuestas.

## 7. Proyecto final (30%)

El proyecto final se desarrolla en **grupos de 3** a lo largo del semestre: diseñar, entrenar o afinar, evaluar y mejorar un modelo propio para un problema contextualizado, y exponerlo en una app (Gradio) o un agente (Startti). El enunciado completo está en [proyecto-final/README.md](../proyecto-final/README.md) y los criterios detallados en la [rúbrica del proyecto](../proyecto-final/rubrica.md).

| Componente | Peso | Nota |
|---|---|---|
| Entregable técnico | 15% | Grupal |
| Socialización y demo (S12) | 10% | Grupal |
| Defensa individual | 5% | Individual |
| **Factor de coevaluación** | ×0.7–1.0 | Individual: multiplica tu nota del proyecto |

- **Factor de coevaluación.** Al final del proyecto, cada integrante evalúa el aporte de sus compañeros con la [plantilla de coevaluación](../proyecto-final/plantillas/coevaluacion.md). Si el aporte fue equitativo, el factor es 1.0; si la evaluación de pares muestra un aporte menor, puede bajar hasta 0.7. La fórmula está en la rúbrica del proyecto.
- **Hitos formativos (obligatorios).** No tienen nota propia, pero reciben retroalimentación y su calidad se refleja en la entrega final:

  | Sesión | Hito |
  |---|---|
  | S03 | Grupos conformados |
  | S05 → S06 | Propuesta del proyecto ([canvas](../proyecto-final/plantillas/propuesta.md)) |
  | S09 | Canvas de caso de uso |
  | S11 | Iteración de mejora documentada |
  | S12 | Entrega y socialización |

- **Socialización en S12.** Cada grupo tiene 8 minutos de pitch, 3 de demo y 4 de preguntas. Se acepta una demo pregrabada como respaldo.
- **Uso de IA en el proyecto.** El grupo documenta su uso de IA con la [plantilla de registro](../proyecto-final/plantillas/registro-uso-ia.md), bajo las mismas reglas de la [política de uso de IA](politica-uso-ia.md).

## 8. Tipos de evaluación

| Tipo | Instrumento | ¿Afecta la nota? |
|---|---|---|
| **Diagnóstica** | Quiz de calentamiento al inicio de cada sesión (en S01 incluye un diagnóstico de entrada) | No |
| **Formativa** | *Checkpoints* del lab, hitos del proyecto con retroalimentación, autoevaluación en las reflexiones | No, pero prepara las evaluaciones sumativas |
| **Sumativa** | Challenges de sesión (70%) y proyecto final (30%) | Sí |

| Agente evaluador | Cómo se aplica |
|---|---|
| **Autoevaluación** | En cada challenge propones y justificas tu propia nota en la reflexión; el grupo se autoevalúa en el proyecto |
| **Coevaluación** | Evaluación de pares dentro del grupo (factor 0.7–1.0) y [retroalimentación entre grupos](../proyecto-final/plantillas/retroalimentacion-pares.md) en S12 |
| **Heteroevaluación** | El profesor califica challenges y proyecto con las rúbricas publicadas |

## 9. Matriz RAE ↔ actividades

**Resultados de aprendizaje esperados (RAE) del curso:**

1. **RAE 1 — Diseñar y entrenar** modelos generativos y preentrenados, utilizando herramientas y frameworks avanzados para desarrollar modelos adaptados a necesidades específicas en diversos contextos.
2. **RAE 2 — Evaluar el desempeño** de los modelos, implementando métricas de evaluación estándar para garantizar la precisión, eficiencia y robustez de los modelos entrenados, aplicando principios éticos en su desarrollo.
3. **RAE 3 — Desarrollar aplicaciones prácticas** de inteligencia artificial: crear prototipos funcionales como chatbots, clasificadores y otras soluciones basadas en IA, ajustadas a requerimientos reales del mercado.
4. **RAE 4 — Integrar modelos en escenarios reales**, analizando casos de uso para aplicar modelos generativos en problemas concretos, considerando factores sociales, económicos y tecnológicos.
5. **RAE 5 — Fomentar la innovación** en la implementación de IAG, identificando oportunidades para la incorporación de modelos generativos en contextos empresariales y sociales, impulsando la transformación digital.
6. **RAE 6 — Gestionar riesgos y asegurar la calidad**, anticipando y mitigando riesgos asociados a la implementación de modelos generativos, garantizando sostenibilidad, escalabilidad y cumplimiento regulatorio.

**Dónde se trabaja y se evalúa cada RAE** (● = se evalúa en el challenge de la sesión o en el proyecto):

| RAE | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | S09 | S10 | S11 | Proyecto (S12) |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 · Diseñar y entrenar | ● | ● | ● | ● | | | | ● | | | | ● |
| 2 · Evaluar el desempeño | | ● | | ● | ● | | | ● | | ● | ● | ● |
| 3 · Desarrollar aplicaciones | | | ● | | | ● | ● | ● | | | | ● |
| 4 · Integrar en escenarios reales | ● | | | | | ● | ● | | ● | | | ● |
| 5 · Fomentar la innovación | ● | | | | | | | | ● | | | ● |
| 6 · Gestionar riesgos y calidad | | | | | | | ● | | ● | ● | ● | ● |

**Evidencias principales por RAE**

| RAE | Evidencias en los challenges | Evidencias en el proyecto |
|---|---|---|
| 1 | Muestreo y parámetros de generación (S01); entrenamiento de un VAE (S02); transferencia con embeddings y *few-shot* (S03); afinamiento completo y LoRA (S04); clasificadores generativos (S08) | Modelo entrenado o afinado por el grupo |
| 2 | Curvas de pérdida (S02); comparación de configuraciones (S04); BLEU, ROUGE, chrF y validación cruzada (S05); métricas y aumento sintético (S08); métricas de disparidad (S10); pruebas de robustez y bitácora de mejora (S11) | Línea base, al menos 2 métricas justificadas y análisis de errores |
| 3 | Clasificación con modelos preentrenados (S03); app en Gradio y agente (S06); chatbot evaluado con 12 conversaciones (S07); clasificador con recomendación de costo y latencia (S08) | Demo funcional (Gradio o Startti) |
| 4 | Análisis del escenario de negocio asignado: costo, datos, privacidad y control (S01); umbral de confianza con costos de negocio (S06); ¿listo para producción? (S07); prototipo sectorial y ROI (S09) | Problema contextualizado en Colombia o Latinoamérica |
| 5 | Recomendación en el espectro de adaptación, del *prompting* al modelo propio (S01); canvas de caso de uso y decisión *go / no-go* (S09) | Propuesta de valor y socialización |
| 6 | Política de escalamiento a humanos (S07); verificación de afirmaciones y estadísticas (S09); auditoría de sesgo y clasificación regulatoria (S10); decisión de despliegue con restricciones (S11) | Análisis ético y de sostenibilidad, *model card* e iteración de mejora |

## 10. Publicación y revisión de notas

- Las notas y la retroalimentación de cada challenge se publican en **e-Aulas**.
- Si tienes dudas sobre una calificación, escríbele primero al profesor por los canales del curso (ver la sección de canales de soporte en la [metodología](metodologia.md)), indicando la sesión, el componente de la rúbrica y tu argumento. Las solicitudes formales de revisión siguen el reglamento académico de la Universidad.
