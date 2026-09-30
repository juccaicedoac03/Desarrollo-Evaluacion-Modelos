# Sesión 11 — Evaluation and Continuous Model Improvement
*Evaluación y mejora continua de modelos*

**RAE asociados:** RAE 2, RAE 6 · **Duración:** 3 horas (virtual)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. Recorrer el ciclo de mejora continua de un modelo (análisis de errores → hipótesis → cambio puntual → nueva medición → decisión) y registrarlo en una bitácora de experimentos reproducible (RAE 2).
2. Distinguir la mejora centrada en los datos de la centrada en el modelo, y detectar etiquetas probablemente erróneas con probabilidades de validación cruzada, inspirado en *confident learning* (RAE 2).
3. Buscar hiperparámetros con Optuna usando solo validación, fijar la regla de decisión antes de experimentar y comprobar con un *bootstrap* si una ganancia supera el ruido de la evaluación (RAE 2).
4. Medir la robustez de un clasificador con pruebas de comportamiento al estilo CheckList (invariancia, funcionalidad mínima, direccionales) y reportar tasas de aprobación (RAE 2, RAE 6).
5. Comparar versiones por exactitud, latencia, tamaño y robustez (incluida la cuantización int8) y decidir cuál desplegar con restricciones de negocio y un plan de monitoreo (RAE 6).

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Tres preguntas de repaso de la S10 (criterios de equidad, huella de carbono, pruebas contrafactuales como pruebas de invariancia) |
| Teoría | 60' | El ciclo de mejora y la deuda técnica · análisis de errores y mejora centrada en datos · experimentos confiables (bitácora, validación vs. prueba, búsqueda de hiperparámetros) · robustez, *drift* y eficiencia (cuantización, destilación) · mejora en producción (monitoreo, *shadow*, *canary*, A/B, LLMOps). Simuladores: ciclo de mejora y cuantización. Sala de grupos: hoja de ruta de mejora del proyecto |
| Descanso | 10' | — |
| Lab guiado | 60' | Banking77 con 10% de etiquetas erróneas: línea base y bitácora, análisis de errores por segmento, etiquetas sospechosas y aumento de datos, Optuna, pruebas CheckList, cuantización int8 de DistilBERT y reporte final en prueba |
| Challenge | 40' | Mejora con al menos 2 iteraciones, reporte de robustez, decisión de despliegue con tus restricciones y crítica a un plan de mejora propuesto por una IA |

**Hito H4 del proyecto (grupal, formativo):** hoy a las 23:59 cada grupo **documenta una iteración de mejora** de su modelo en la bitácora de la sección 5 del [informe técnico](../../proyecto-final/plantillas/informe-tecnico.md) (hipótesis → cambio → resultado en validación → decisión) y entrega el enlace al código. En la sala de grupos de hoy planean esa iteración.

## Antes de la clase (≈2 h)

- [ ] Lee Sculley et al. (2015), *Hidden technical debt in machine learning systems* (8 páginas, ≈40 min): quédate con la idea de que el modelo es la caja pequeña del sistema.
- [ ] Lee las secciones 1 a 3 de Ribeiro et al. (2020), *Beyond accuracy: Behavioral testing of NLP models with CheckList* (≈30 min).
- [ ] Recorre el [tutorial de primeros pasos de Optuna](https://optuna.readthedocs.io/en/stable/tutorial/index.html) (≈20 min).
- [ ] Trae a clase **un error frecuente del modelo de tu proyecto**, con un conteo de tu línea base (lo usarás en la sala de grupos).
- [ ] Repasa la separación entrenamiento / validación / prueba de la S05 y las pruebas contrafactuales de la S10.

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/11-continuous-improvement/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/11-continuous-improvement/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/11-continuous-improvement/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/11-continuous-improvement/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/11-continuous-improvement/challenge.ipynb) · [archivo](challenge.ipynb) |
| Plantilla del informe técnico (§5, bitácora de mejora) | [informe-tecnico.md](../../proyecto-final/plantillas/informe-tecnico.md) |
| Hitos y entregas del proyecto final | [proyecto-final/README.md](../../proyecto-final/README.md) |

**Kaggle:** *Settings → Internet: On* · *Accelerator: None*. Hoy la CPU es parte del ejercicio: las restricciones de latencia del challenge se miden en CPU. No necesitas claves ni Secrets.

## Challenge de la sesión (evaluación)

Tu código estudiantil te asigna un **grupo de 10 intenciones** de Banking77, una **tasa de errores de etiqueta** del proveedor (5%, 10% o 20%), un **presupuesto de Optuna** (10, 15 o 20 ensayos) y un **caso de despliegue** con restricciones de latencia, exactitud y tamaño (escenarios ficticios de Andes Bank, Banco Andino, NovaTel Pagos o la Cooperativa Horizonte).

1. **Mejora con bitácora:** parte de tu línea base y corre al menos **2 iteraciones documentadas** (etiquetas sospechosas con validación cruzada y búsqueda con Optuna), con hipótesis que salgan de tus números y una regla de decisión fijada antes de experimentar. Verifica con un intervalo *bootstrap* si la ganancia supera el ruido.
2. **Reporte de robustez:** tasas de aprobación de pruebas de invariancia (errores de tipeo, mayúsculas, frase irrelevante, sin puntuación) para la línea base y tu campeón, con un ejemplo fallido explicado.
3. **Explica y decide:** compara TF-IDF y MiniLM (float32 e int8) por exactitud, latencia, tamaño y robustez, y escribe un memo para el comité: qué versión despliegas con **tus** restricciones y qué monitorearías el primer mes.
4. **Crítica a la IA:** encuentra, explica y corrige los 3 pasos equivocados de un plan de mejora escrito por un asistente de IA.

- **Rúbrica:** ejecución técnica 40% · análisis e interpretación 40% · reflexión y registro de IA 20% ([evaluación](../../docs/evaluacion.md)).
- **IA permitida con registro obligatorio**: sin registro, ese componente vale 0.0 ([política de uso de IA](../../docs/politica-uso-ia.md)). **Micro-sustentaciones** al azar: si no puedes explicar tu entrega, la nota máxima es 3.0.
- **Entrega:** `File → Download notebook` → súbelo a e-Aulas como **`S11_<codigo>.ipynb`** antes de las **23:59** de hoy.

## Después de la clase (trabajo independiente ≈7 h)

- [ ] Termina y entrega el challenge (23:59).
- [ ] **Proyecto · hito H4 (≈3 h, hoy 23:59):** documenten en grupo **una iteración de mejora** del modelo del proyecto en la sección 5 del [informe técnico](../../proyecto-final/plantillas/informe-tecnico.md): hipótesis con evidencia de su análisis de errores, **un** cambio, métricas de validación antes y después, decisión según una regla escrita antes de experimentar, y enlace al código o *commit*. No usen el conjunto de prueba para decidir. Súbanlo a e-Aulas como `PF_G<NN>_H4` (por ejemplo, `PF_G03_H4_bitacora.pdf`); reciben comentarios antes de la S12 ([detalles del hito](../../proyecto-final/README.md)).
- [ ] **Proyecto (≈2 h):** agreguen al informe al menos una prueba de comportamiento (INV o MFT) de su modelo y una medición de latencia o tamaño en el hardware de su demo; empiecen a preparar el *pitch* y la demo de la S12.
- [ ] Practica con los ejercicios 🧪 del lab: nuevos segmentos de error, datos dirigidos para la intención más débil, búsqueda aleatoria frente a TPE y n-gramas de caracteres para la robustez.
- [ ] Lectura recomendada (opcional): Sambasivan et al. (2021) sobre las cascadas de datos, o las *Reglas del aprendizaje automático* de Google (en español).

## Lecturas y recursos

**Ciclo de vida y deuda técnica**
- Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., Chaudhary, V., Young, M., Crespo, J.-F., & Dennison, D. (2015). Hidden technical debt in machine learning systems. *NeurIPS*.
- Amershi, S., Begel, A., Bird, C., DeLine, R., Gall, H., Kamar, E., Nagappan, N., Nushi, B., & Zimmermann, T. (2019). Software engineering for machine learning: A case study. *ICSE-SEIP*.
- Huyen, C. (2022). *Designing machine learning systems*. O'Reilly.
- Sambasivan, N., Kapania, S., Highfill, H., Akrong, D., Paritosh, P., & Aroyo, L. M. (2021). "Everyone wants to do the model work, not the data work": Data cascades in high-stakes AI. *CHI 2021*. https://doi.org/10.1145/3411764.3445518

**Datos, etiquetas y experimentos**
- Northcutt, C., Jiang, L., & Chuang, I. (2021). Confident learning: Estimating uncertainty in dataset labels. *Journal of Artificial Intelligence Research, 70*, 1373–1411.
- Northcutt, C., Athalye, A., & Mueller, J. (2021). Pervasive label errors in test sets destabilize machine learning benchmarks. *NeurIPS Datasets and Benchmarks*.
- Wei, J., & Zou, K. (2019). EDA: Easy data augmentation techniques for boosting performance on text classification tasks. *EMNLP-IJCNLP*.
- Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). Optuna: A next-generation hyperparameter optimization framework. *KDD*.
- Bergstra, J., & Bengio, Y. (2012). Random search for hyper-parameter optimization. *JMLR, 13*, 281–305.
- Casanueva, I., Temčinas, T., Gerz, D., Henderson, M., & Vulić, I. (2020). Efficient intent detection with dual sentence encoders. *NLP4ConvAI workshop, ACL*. arXiv:2003.04807 (dataset Banking77).

**Robustez, eficiencia y producción**
- Ribeiro, M. T., Wu, T., Guestrin, C., & Singh, S. (2020). Beyond accuracy: Behavioral testing of NLP models with CheckList. *ACL*.
- Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., & Bouchachia, A. (2014). A survey on concept drift adaptation. *ACM Computing Surveys, 46*(4).
- Hinton, G., Vinyals, O., & Dean, J. (2015). Distilling the knowledge in a neural network. arXiv:1503.02531.
- Sanh, V., Debut, L., Chaumond, J., & Wolf, T. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. arXiv:1910.01108.
- Jacob, B., et al. (2018). Quantization and training of neural networks for efficient integer-arithmetic-only inference. *CVPR*.
- Dettmers, T., Lewis, M., Belkada, Y., & Zettlemoyer, L. (2022). LLM.int8(): 8-bit matrix multiplication for transformers at scale. *NeurIPS*.
- Kohavi, R., Tang, D., & Xu, Y. (2020). *Trustworthy online controlled experiments: A practical guide to A/B testing*. Cambridge University Press.
- Documentación de [Optuna](https://optuna.readthedocs.io/) y guía de [cuantización de PyTorch](https://pytorch.org/docs/stable/quantization.html).
- **En español:** Zinkevich, M. [*Reglas del aprendizaje automático: prácticas recomendadas para la ingeniería de AA*](https://developers.google.com/machine-learning/guides/rules-of-ml?hl=es) (Google for Developers), y el [Curso intensivo de aprendizaje automático](https://developers.google.com/machine-learning/crash-course?hl=es) de Google, módulos sobre conjuntos de datos, generalización y sistemas de AA en producción.
