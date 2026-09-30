# Sesión 02 — Training Generative Models
*Entrenamiento de modelos generativos*

**RAE asociados:** RAE 1, RAE 2 · **Duración:** 3 horas (virtual) · **Fecha:** sábado 3 de octubre de 2026, 7:00–10:00 (hora de Colombia)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. Escribir el ciclo de entrenamiento en PyTorch (*forward* → pérdida → *backward* → paso del optimizador) y explicar qué hace cada línea (RAE 1).
2. Elegir una función de pérdida (entropía cruzada, MSE, divergencia KL) y un optimizador (SGD, *momentum*, Adam, AdamW), y diagnosticar problemas de tasa de aprendizaje (RAE 1).
3. Leer curvas de entrenamiento y validación para detectar sobreajuste y decidir cuándo detener el entrenamiento (RAE 2).
4. Identificar errores de preprocesamiento y fugas de datos (*data leakage*) en datos de negocio (RAE 2).
5. Explicar cómo aprende un autoencoder variacional (ELBO, truco de reparametrización, β-VAE) y entrenar uno en Fashion-MNIST (RAE 1).

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Tres preguntas de repaso de la Sesión 01: temperatura, espectro de adaptación y familias de modelos |
| Teoría | 60' | Parte 1: el ciclo de entrenamiento, pérdidas, optimizadores y **simulador de tasa de aprendizaje**. Parte 2: generalización y datos, **simulador de sobreajuste** y **sala de grupos**: encontrar 5 errores de preprocesamiento en un conjunto de datos de CRM. Parte 3: de los autoencoders a los VAE; VAE vs. GAN vs. difusión |
| Descanso | 10' | Activar la GPU en Kaggle |
| Lab guiado | 60' | VAE en Fashion-MNIST con PyTorch: datos, modelo y ELBO, ciclo de entrenamiento y curvas, reconstrucción, muestreo, interpolación y mapa del espacio latente, SGD vs. Adam |
| Challenge | 40' | Tu propio VAE con configuración asignada, comparación con una línea base, decisión de negocio y crítica a la IA |

## Antes de la clase (≈2 h)

La S02 y la S03 son seguidas (sábado 3 de octubre, 7:00 y 10:00): haz la preparación de ambas antes del sábado.

- **Kaggle con GPU:** verifica tu número de celular en Kaggle; sin verificación no puedes activar la GPU ni Internet. El lab y el challenge funcionan en CPU, pero con GPU son más rápidos. Guía: [configuración de Kaggle](../../docs/configuracion-kaggle.md).
- **Lectura principal:** Goodfellow, Bengio y Courville (2016), [*Deep Learning*](https://www.deeplearningbook.org/), capítulo 8 (optimización: secciones 8.1, 8.3 y 8.5) y capítulo 14 (autoencoders: sección 14.1).
- **Práctica guiada:** el tutorial oficial de PyTorch [Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html), en especial *Datasets & DataLoaders*, *Autograd* y *Optimization*.
- **Repaso:** la Parte 1 del lab de la [Sesión 01](../01-intro-generative-models/README.md) (tensores y *autograd*): hoy usamos las mismas ideas a mayor escala.

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/02-training-generative-models/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/02-training-generative-models/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/02-training-generative-models/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/02-training-generative-models/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/02-training-generative-models/challenge.ipynb) · [archivo](challenge.ipynb) |

**Kaggle:** *Settings → Accelerator → GPU T4 x2* (recomendado) e *Internet → On*. Los datos ([`zalando-datasets/fashion_mnist`](https://huggingface.co/datasets/zalando-datasets/fashion_mnist)) se descargan del Hugging Face Hub al ejecutar el notebook.

## Challenge de la sesión (evaluación)

Individual, 40 minutos en clase y entrega hasta las **23:59 del mismo día**. Tu código estudiantil define tu configuración personal: dimensión latente (2, 4, 8 o 16), β (0.5, 1, 2 o 4), tasa de aprendizaje (0.001 o 0.003) y 3 de las 10 prendas de Fashion-MNIST.

| Tarea | Qué haces | Componente |
|---|---|---|
| 1 · Entrena tu VAE | Entrenas el VAE con tu configuración; reportas reconstrucción, KL, −ELBO y dimensiones activas; comparas la reconstrucción de tus 3 prendas | Ejecución técnica |
| 2 · Compara con la línea base | Entrenas la línea base (latente 8, β = 1) e interpretas el equilibrio entre reconstrucción y KL con **tus** números | Análisis e interpretación |
| 3 · Explica y decide | Recomiendas una configuración para el generador de bocetos de Hilo Norte (empresa ficticia) y argumentas VAE vs. GAN vs. difusión | Análisis e interpretación |
| 4 · Crítica a la IA | Encuentras, explicas y corriges 3 errores en un ciclo de entrenamiento escrito por una IA, y vuelves a entrenar | Ejecución técnica + análisis |

- **Rúbrica:** ejecución técnica 40% · análisis e interpretación 40% · reflexión y registro de IA 20% ([evaluación del curso](../../docs/evaluacion.md)).
- **Uso de IA:** permitido con **registro obligatorio** en la tabla final del notebook; sin registro, ese componente vale 0.0 ([política de uso de IA](../../docs/politica-uso-ia.md)).
- **Micro-sustentaciones:** si te seleccionan y no puedes explicar tu entrega, la nota máxima del challenge es 3.0.
- **Entrega:** ejecuta todo en orden → *File → Download notebook* → súbelo a e-Aulas como **`S02_<codigo>.ipynb`**. Verifica que aparezcan "Tu configuración personal" y la huella de resultados (🔏).

## Después de la clase (trabajo independiente ≈7 h)

- **Cierra y entrega el challenge** antes de las 23:59.
- **Repite el lab con otra configuración y compara:** por ejemplo, `LATENT_DIM = 2` (puedes dibujar el espacio latente directamente, sin PCA) o β = 4 en el entrenamiento. Anota cómo cambian la reconstrucción, el KL, las muestras y las dimensiones activas.
- **Lectura:** Kingma y Welling (2014), secciones 1–3, apoyándote en Kingma y Welling (2019), capítulos 1 y 2, que explican lo mismo con más detalle; y Higgins et al. (2017) sobre β-VAE.
- **Proyecto final:** busca a tus compañeros de grupo (3 personas; idealmente perfiles de negocio y técnicos). Los grupos se registran hoy mismo en la **Sesión 03** (hito **H1**, hasta las 23:59). Revisa el [enunciado del proyecto final](../../proyecto-final/README.md) y empieza a pensar en qué datos de tu organización podrías usar… sin fugas de datos.
- **La Sesión 03** (modelos preentrenados y transferencia de aprendizaje) empieza hoy a las 10:00, después de un breve descanso; su preparación ya debía quedar lista antes del sábado.

## Lecturas y recursos

**Lecturas principales**

- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press. Caps. 8 (optimización), 14 (autoencoders) y 20 (modelos generativos profundos; secciones 20.10.3 sobre VAE y 20.10.4 sobre GAN). [deeplearningbook.org](https://www.deeplearningbook.org/)
- Kingma, D. P., & Welling, M. (2014). Auto-encoding variational Bayes. *ICLR 2014*. [arXiv:1312.6114](https://arxiv.org/abs/1312.6114)
- Kingma, D. P., & Welling, M. (2019). An introduction to variational autoencoders. *Foundations and Trends in Machine Learning, 12*(4), 307–392. [arXiv:1906.02691](https://arxiv.org/abs/1906.02691)
- Higgins, I., Matthey, L., Pal, A., Burgess, C., Glorot, X., Botvinick, M., Mohamed, S., & Lerchner, A. (2017). β-VAE: Learning basic visual concepts with a constrained variational framework. *International Conference on Learning Representations (ICLR 2017)*.

**Optimización y regularización**

- Kingma, D. P., & Ba, J. (2015). Adam: A method for stochastic optimization. *ICLR 2015*. [arXiv:1412.6980](https://arxiv.org/abs/1412.6980)
- Loshchilov, I., & Hutter, F. (2019). Decoupled weight decay regularization. *ICLR 2019*. [arXiv:1711.05101](https://arxiv.org/abs/1711.05101)
- Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). Dropout: A simple way to prevent neural networks from overfitting. *Journal of Machine Learning Research, 15*, 1929–1958.

**Datos y fuga de datos**

- Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). Leakage in data mining: Formulation, detection, and avoidance. *ACM Transactions on Knowledge Discovery from Data, 6*(4).
- Xiao, H., Rasul, K., & Vollgraf, R. (2017). Fashion-MNIST: A novel image dataset for benchmarking machine learning algorithms. [arXiv:1708.07747](https://arxiv.org/abs/1708.07747)

**En español**

- Google. *Machine Learning Crash Course* (versión en español): [Conjuntos de datos, generalización y sobreajuste](https://developers.google.com/machine-learning/crash-course/overfitting?hl=es-419): división de datos, curvas de pérdida, complejidad del modelo y regularización L2, con ejercicios interactivos.

**Práctica**

- PyTorch. *Learn the Basics* (tutorial oficial): [pytorch.org/tutorials/beginner/basics](https://pytorch.org/tutorials/beginner/basics/intro.html)
