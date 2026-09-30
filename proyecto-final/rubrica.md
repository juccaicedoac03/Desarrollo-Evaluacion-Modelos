# Rúbrica del proyecto final

*Desarrollo y Evaluación de Modelos Propios · Rosario GSB, Universidad del Rosario*

Esta rúbrica califica el proyecto descrito en el [enunciado del proyecto](README.md). El esquema de evaluación de todo el curso está en [evaluación del curso](../docs/evaluacion.md) y las reglas sobre asistentes de IA, en la [política de uso de IA](../docs/politica-uso-ia.md).

---

## 1. Cómo se calcula la nota

| Componente | Peso en la nota final | Peso dentro del proyecto | Tipo de nota |
|---|---|---|---|
| Entregable técnico (T) | 15% | 50% | Grupal, después de descuentos por hitos y topes (sección 2) |
| Socialización y demo (S) | 10% | 33.3% | Grupal |
| Defensa individual (D) | 5% | 16.7% | Individual |
| **Factor de coevaluación (F)** | **× 0.7–1.0** | — | Individual |

```text
Nota del proyecto             N  = (15 × T + 10 × S + 5 × D) / 30
Nota individual del proyecto  NI = N × F
Aporte a la nota final           = 0.30 × NI
```

**Niveles de desempeño.** Cada criterio recibe una nota de 0.0 a 5.0 dentro de la franja del nivel que mejor describe el trabajo:

| Nivel | Franja |
|---|---|
| Excelente | 4.5–5.0 |
| Bueno | 4.0–<4.5 |
| Aceptable | 3.0–<4.0 |
| Insuficiente | <3.0 |

La nota de cada componente es el promedio ponderado de sus criterios.

**Redondeo.** El único valor intermedio que se redondea es el factor de coevaluación F (a dos decimales). Los demás cálculos intermedios (notas de componente, T después de ajustes, N) no se redondean; la nota individual del proyecto se reporta con dos decimales y la nota definitiva del curso se redondea según el reglamento académico.

---

## 2. Entregable técnico (15%) — nota grupal

Se califica con el código, el informe técnico, la model card y el registro de uso de IA.

| Criterio (peso) | Excelente (4.5–5.0) | Bueno (4.0–<4.5) | Aceptable (3.0–<4.0) | Insuficiente (<3.0) |
|---|---|---|---|---|
| **1. Problema y contexto** (10%) | Problema de negocio concreto y relevante, con usuario, situación actual, costo del problema y KPI de éxito definidos. Justifica por qué un modelo propio es mejor opción que solo prompting o reglas. | Problema claro, con usuario y KPI. La justificación del modelo propio es general. | Problema genérico; usuario o KPI poco definidos. No se discute la alternativa sin modelo propio. | Problema ausente, confuso o sin relación con la solución construida. |
| **2. Datos** (15%) | Fuente, licencia, tamaño y distribución de clases documentados. Particiones de entrenamiento, validación y prueba sin fuga, y la ausencia de fuga se verificó. Preprocesamiento justificado; calidad revisada con ejemplos. Privacidad y anonimización (Ley 1581 de 2012) resueltas y documentadas. Si hay datos sintéticos, su generación y revisión son trazables. | Datos documentados y particiones correctas; la revisión de calidad o de privacidad es superficial en algún aspecto. | Descripción incompleta (falta la licencia, la distribución o cómo se partieron los datos); el riesgo de fuga no se analiza. | Origen desconocido, fuga evidente (p. ej., evaluar con datos de entrenamiento) o datos personales usados sin autorización. |
| **3. Modelo y entrenamiento** (15%) | Modelo base elegido con criterios explícitos (tarea, idioma, tamaño, licencia, cómputo). Afinamiento o entrenamiento correcto (fine-tuning completo, LoRA o desde cero), con hiperparámetros, curvas de pérdida y cómputo usado reportados. Decisiones justificadas con evidencia. | Entrenamiento correcto y documentado; algunas decisiones no se justifican del todo. | El entrenamiento funciona, pero con la configuración por defecto sin justificar, sin curvas o con problemas no diagnosticados (sobreajuste, pérdida que no baja). | No hay modelo afinado ni entrenado por el grupo (solo prompting), o el entrenamiento no corre. **Activa el tope de 3.0 (ver abajo).** |
| **4. Evaluación: métricas, línea base y análisis de errores** (20%) | Dos o más métricas justificadas desde el negocio y el riesgo. Comparación con la línea base en el mismo conjunto de prueba reservado. Reporta la variabilidad cuando es posible (varias semillas o intervalos; meta de alcance extendido). El análisis de errores tiene categorías, conteos y ejemplos, y lleva a conclusiones accionables. | Métricas y línea base adecuadas; el análisis de errores tiene ejemplos, pero pocas categorías o conteos. | Métricas sin justificar o línea base débil (p. ej., solo la clase mayoritaria, sin discusión); análisis de errores anecdótico. | Una sola métrica, sin línea base, evaluación con datos de entrenamiento o sin análisis de errores. |
| **5. Mejora iterativa** (10%) | Al menos una iteración con una hipótesis que sale del análisis de errores, un cambio controlado, comparación antes/después en igualdad de condiciones y una decisión explícita. Bitácora completa. La decisión se tomó con validación, no con el conjunto de prueba. | Iteración documentada y comparada; la hipótesis está poco conectada con el análisis de errores. | Se reportan cambios sin una hipótesis clara o sin comparar en igualdad de condiciones. | No hay iteración documentada, o la mejora se obtuvo ajustando sobre el conjunto de prueba. |
| **6. Ética, sostenibilidad y model card** (15%) | Riesgos específicos del caso (sesgo, privacidad, uso indebido, impacto en las personas usuarias), con al menos una prueba empírica (p. ej., desempeño por subgrupo o prueba contrafactual; meta de alcance extendido) y mitigaciones. Emisiones o energía del entrenamiento medidas con CodeCarbon o estimadas con un método citado. Clasificación de riesgo razonada. Model card completa y coherente con el informe. | Análisis específico y model card completa, pero sin prueba empírica o con la medición de emisiones incompleta. | Análisis genérico ("puede haber sesgos"); model card con secciones vacías o superficiales. | Sin análisis ético o sin model card. |
| **7. Calidad del código y reproducibilidad** (10%) | El notebook o repositorio corre de principio a fin siguiendo sus instrucciones, también sin claves de API: si la demo usa Startti, las celdas del agente se omiten sin error y muestran una transcripción o capturas grabadas, o ejecutan la alternativa en Python. Semilla, versiones y acceso a los datos documentados. Código ordenado y comentado; secretos fuera del código. Los resultados del informe coinciden con los que produce el código. | Corre con ajustes menores; la documentación es suficiente. | Corre de forma parcial o requiere que el profesor lo arregle (p. ej., falla sin la clave de Startti); documentación mínima. | No corre, faltan partes esenciales, hay claves de API expuestas o los resultados del informe no se pueden reproducir. |
| **8. Registro de uso de IA** (5%) | Registro completo por fase, con prompts resumidos y lo que se verificó o corrigió en cada caso. Reflexión crítica con ejemplos concretos. Distingue la IA como herramienta de trabajo de la IA como componente de la solución. | Registro completo, con la verificación descrita; reflexión general. | Registro incompleto o genérico ("usamos ChatGPT para el código"). | Sin registro (el criterio vale 0) o registro que contradice la evidencia. |

**Ajustes a la nota del entregable técnico**

Los ajustes se aplican en este orden: **primero los descuentos** por hitos y **luego los topes**. Por ejemplo, un grupo con subtotal 4.40, un hito no entregado y sin modelo propio obtiene 4.40 − 0.30 = 4.10 → tope → **T = 3.00**.

- **Hitos:** −0.3 por cada hito formativo (H1–H4) no entregado en su plazo, salvo excusa válida aceptada por el profesor; máximo −1.2. La nota no baja de 0.0.
- **Tope por falta de modelo propio:** si el grupo no afinó ni entrenó un modelo propio (solo prompting de un API), la nota del entregable técnico no puede superar 3.0. El tope se aplica después de los descuentos por hitos.
- **Extensión:** el informe tiene máximo 8 páginas, sin contar portada, referencias ni anexos. Lo que pase de la página 8 no se califica.
- **Resultados fabricados:** cualquier resultado que no provenga de ejecutar el código del grupo, o que haya sido alterado, se tramita conforme al reglamento académico de la Universidad del Rosario; el componente afectado puede calificarse con **0.0**.

---

## 3. Socialización y demo (10%) — nota grupal

Formato: 8' de pitch + 3' de demo + 4' de preguntas; orden aleatorio.

| Criterio (peso) | Excelente (4.5–5.0) | Bueno (4.0–<4.5) | Aceptable (3.0–<4.0) | Insuficiente (<3.0) |
|---|---|---|---|---|
| **1. Claridad del pitch y valor de negocio** (35%) | Historia clara para un público mixto: problema → solución → evidencia (resultados frente a la línea base) → valor de negocio cuantificado o bien argumentado → limitaciones y siguiente paso. Visuales legibles y al servicio del mensaje. | Clara y bien estructurada; el valor de negocio aparece, pero poco cuantificado, o las limitaciones son poco explícitas. | Estructura confusa, o demasiado técnica o demasiado superficial; resultados sin comparación con la línea base. | No se entiende qué problema resuelve ni qué se logró. |
| **2. Demo funcional** (30%) | Demo en vivo del modelo propio con casos preparados (típico, difícil y un fallo explicado). Muestra decisiones de producto: umbral de confianza, escalamiento a una persona, manejo de la incertidumbre. | Demo en vivo funcional con casos típicos; explora poco los límites del modelo. | La demo falla en parte, o el papel del modelo propio no se ve con claridad. | Sin demo, o la demo no usa el modelo del grupo. |
| **3. Manejo del tiempo** (15%) | Pitch y demo dentro de 8' y 3'; transiciones fluidas; el grupo está listo cuando lo llaman. | Se desvía hasta 1 minuto en total, sin afectar el contenido. | Se excede y el profesor debe interrumpir, o quedan partes clave sin presentar. | El grupo no está listo cuando lo llaman, o la presentación queda muy incompleta por el tiempo. |
| **4. Participación equitativa** (20%) | Todos los integrantes hablan, con tiempos equilibrados y dominio de lo que presentan; se apoyan entre sí en las respuestas. | Todos hablan, con un desequilibrio moderado. | Una persona concentra la mayor parte; las demás intervienen muy poco. | Algún integrante presente no interviene. |

**Reglas**

- **Video de respaldo:** si la demo en vivo falla por causas técnicas, se proyecta el video de respaldo (≤ 3 min) sin penalización, y el profesor verifica después que la demo funcione con lo entregado. Presentar solo el video, sin intentar la demo en vivo, limita el criterio 2 al nivel Bueno (menos de 4.5).
- **Demo con Startti:** el profesor no puede usar los Kaggle Secrets del grupo, así que el agente en vivo se muestra en la S12 desde la cuenta del grupo. El notebook entregado debe funcionar sin la clave (criterio 7 del entregable técnico).
- **Ausencias:** quien falte sin excusa válida obtiene 0.0 en socialización y en defensa individual. Su ausencia no afecta la nota de participación equitativa del grupo. Con excusa válida según el reglamento, conserva la nota de socialización del grupo y presenta su defensa individual en otra fecha.

---

## 4. Defensa individual (5%) — nota individual

En los 4' de preguntas, el profesor dirige al menos una pregunta a cada integrante, sobre cualquier parte del proyecto. No se pueden consultar asistentes de IA ni leer respuestas preparadas. Responder "no lo sé, pero lo verificaría así…" es mejor que improvisar.

| Criterio (peso) | Excelente (4.5–5.0) | Bueno (4.0–<4.5) | Aceptable (3.0–<4.0) | Insuficiente (<3.0) |
|---|---|---|---|---|
| **1. Comprensión técnica de su parte y del todo** (40%) | Explica con precisión su parte y cualquier otra parte del proyecto (datos, modelo, métricas, resultados), usando los números del grupo. | Domina su parte y explica el resto a nivel general. | Explica su parte con imprecisiones; desconoce aspectos importantes del resto. | No puede explicar su propia parte. |
| **2. Capacidad de justificar decisiones** (35%) | Justifica las decisiones con evidencia y con las alternativas consideradas (costo, riesgo, desempeño); reconoce limitaciones. | Da razones válidas, pero sin discutir alternativas. | Justificaciones vagas ("porque así venía en el tutorial"). | No justifica, o su respuesta contradice la evidencia del proyecto. |
| **3. Uso crítico de IA** (25%) | Describe con ejemplos cómo usó la IA, qué verificó y un error de la IA que detectó y corrigió; distingue lo que entiende de lo que delegó. | Describe el uso de la IA y la verificación en términos generales. | Describe el uso de forma vaga, con poca evidencia de verificación. | No puede explicar partes generadas con IA que presenta como propias, o su respuesta contradice el registro de uso de IA. |

---

## 5. Factor de coevaluación

Al cerrar el proyecto, cada integrante califica de forma confidencial a sus compañeros de grupo en 5 criterios, con una escala de 1 a 5 ([plantilla de coevaluación](plantillas/coevaluacion.md)).

**Definiciones**

- **P** = promedio de todos los puntajes que **tus compañeros** te asignan (5 criterios × número de evaluadores). Tu autoevaluación se recoge como insumo formativo, pero **no entra en P**.
- **F** = factor que multiplica tu nota del proyecto:

```text
F = 0.7 + 0.3 × (P − 1) / 3, con tope en 1.0
  (equivale a F = 0.7 + 0.1 × (P − 1); F se redondea a dos decimales)
```

| P (promedio recibido) | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | ≥ 4.0 |
|---|---|---|---|---|---|---|---|
| **F** | 0.70 | 0.75 | 0.80 | 0.85 | 0.90 | 0.95 | **1.00** |

En la práctica, quien recibe en promedio "aporte sólido" (4) o más conserva el 100% de la nota del proyecto; por debajo de 4, cada punto menos resta 0.1 al factor, hasta un mínimo de 0.7.

**Ejemplo de cálculo de P.** Ana recibe de Bruno 4, 4, 3, 4 y 4 (promedio 3.8) y de Carla 3, 4, 3, 3 y 4 (promedio 3.4). Entonces P = 36 / 10 = 3.6 y F = 0.7 + 0.3 × 2.6 / 3 = 0.96.

**Reglas**

1. **La coevaluación es obligatoria.** Quien no entregue su formulario a tiempo recibe −0.05 en su propio F (sin bajar de 0.7). En ese caso, el P de sus compañeros se calcula solo con las evaluaciones disponibles.
2. **Grupos de 2 o de 4** (solo con autorización): P se calcula con los evaluadores disponibles (1 o 3).
3. **Confidencialidad:** solo el profesor ve los puntajes y comentarios individuales. El grupo no conoce quién calificó qué.
4. **Revisión por el profesor en casos extremos.** El profesor revisa el factor, con evidencia, cuando:
   - algún integrante recibe P < 3.0 (F < 0.90);
   - los promedios que dos compañeros asignan a la misma persona difieren en 1.5 puntos o más;
   - los comentarios reportan una situación grave (no participación, conflicto serio, conducta inapropiada);
   - los puntajes contradicen la evidencia (p. ej., todos 5 aunque un integrante no tenga aportes verificables) o hay indicios de acuerdos para inflar o castigar notas.

   La evidencia incluye: historial de commits o de versiones de Kaggle, la declaración de contribuciones del informe, el registro de uso de IA, los hitos, la participación en la socialización y la defensa individual. El profesor puede pedir una reunión breve con el grupo o con cada integrante. Puede confirmar F, ajustarlo dentro del rango 0.7–1.0 o descartar evaluaciones puntuales, y comunica su decisión con la justificación. Las reclamaciones siguen el reglamento académico.
5. **No participación total.** Si la evidencia muestra que un integrante no hizo ningún aporte verificable al proyecto, el profesor puede calificar su entregable técnico de forma individual, según su aporte real (incluso con 0.0), conforme al reglamento.
6. **Alerta temprana.** Los problemas de participación deben informarse al profesor antes de la S10 (viernes 23 de octubre), para que haya margen de actuar antes de la entrega final. La coevaluación no reemplaza la conversación oportuna dentro del grupo.

---

## 6. Ejemplo completo

**Grupo G03** (Ana, Bruno y Carla). Entregó H1 y H3 a tiempo, y el H4 llegó dentro del informe de la entrega final; **el H2 no se entregó en su plazo**: la propuesta llegó el jueves 15 de octubre, después del cierre del miércoles 14 a las 23:59, así que cuenta como no entregada para el descuento.

**Entregable técnico**

| Criterio | Peso | Nota | Aporte |
|---|---|---|---|
| 1. Problema y contexto | 10% | 4.5 | 0.450 |
| 2. Datos | 15% | 4.2 | 0.630 |
| 3. Modelo y entrenamiento | 15% | 4.6 | 0.690 |
| 4. Evaluación | 20% | 4.3 | 0.860 |
| 5. Mejora iterativa | 10% | 4.0 | 0.400 |
| 6. Ética, sostenibilidad y model card | 15% | 4.4 | 0.660 |
| 7. Código y reproducibilidad | 10% | 4.8 | 0.480 |
| 8. Registro de uso de IA | 5% | 4.6 | 0.230 |
| **Subtotal** | | | **4.40** |
| Descuento por H2 no entregado en su plazo | | | −0.30 |
| **T** | | | **4.10** |

**Socialización y demo:** pitch 4.6 (35%) + demo 4.6 (30%) + tiempo 4.2 (15%) + participación 4.4 (20%) → **S = 1.61 + 1.38 + 0.63 + 0.88 = 4.50**.

**Defensa individual, coevaluación y nota individual**

| | Ana | Bruno | Carla |
|---|---|---|---|
| D (defensa individual) | 4.00 | 4.60 | 3.40 |
| N = (15 × 4.10 + 10 × 4.50 + 5 × D) / 30 | 4.2167 | 4.3167 | 4.1167 |
| P (promedio recibido) | 3.6 | 4.3 | 2.4 |
| F | 0.96 | 1.00 | 0.84 |
| **NI = N × F** | **4.05** | **4.32** | **3.46** |
| Aporte a la nota final (0.30 × NI) | 1.214 | 1.295 | 1.037 |

Como Carla recibió P = 2.4 (< 3.0), el profesor revisa su caso con la evidencia antes de confirmar F = 0.84 (regla 4).

La defensa de Ana, por ejemplo, se calcula así: comprensión 4.5 (40%) + justificación 4.0 (35%) + uso crítico de IA 3.2 (25%) = 1.80 + 1.40 + 0.80 = 4.00.

---

## 7. Hoja de calificación

*Para uso del profesor; se comparte con el grupo junto con la retroalimentación.*

**Grupo:** G__ · **Proyecto:** ______________________ · **Hitos no entregados:** ___ × (−0.3), máximo −1.2

| Componente | Criterio | Peso | Nota | Comentario |
|---|---|---|---|---|
| Técnico | 1. Problema y contexto | 10% | | |
| Técnico | 2. Datos | 15% | | |
| Técnico | 3. Modelo y entrenamiento | 15% | | |
| Técnico | 4. Evaluación | 20% | | |
| Técnico | 5. Mejora iterativa | 10% | | |
| Técnico | 6. Ética, sostenibilidad y model card | 15% | | |
| Técnico | 7. Código y reproducibilidad | 10% | | |
| Técnico | 8. Registro de uso de IA | 5% | | |
| **T** (primero descuentos por hitos, luego topes) | | | | |
| Socialización | 1. Pitch y valor de negocio | 35% | | |
| Socialización | 2. Demo funcional | 30% | | |
| Socialización | 3. Manejo del tiempo | 15% | | |
| Socialización | 4. Participación equitativa | 20% | | |
| **S** | | | | |

| Integrante | D: comprensión (40%) | D: justificación (35%) | D: uso crítico de IA (25%) | D | P | F | N | NI |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
