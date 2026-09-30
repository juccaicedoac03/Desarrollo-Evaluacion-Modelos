# Model card — Plantilla

*Proyecto final · Desarrollo y Evaluación de Modelos Propios*

> **Cómo usar esta plantilla**
>
> - Sigue la estructura de *Model Cards for Model Reporting* (Mitchell et al., 2019), con dos secciones adicionales al final: impacto ambiental y cómo usar el modelo.
> - Guárdenla como `MODEL_CARD.md` en el repositorio, como sección final del notebook o como `README.md` del modelo en Hugging Face Hub. Súbanla también a e-Aulas como `PF_G<NN>_model-card.md`.
> - Escríbanla en español, para dos públicos: una persona técnica que quiere reutilizar el modelo y una persona de negocio que decide si lo adopta.
> - Todos los números deben coincidir con el informe técnico. Si una sección no aplica, expliquen por qué en lugar de dejarla vacía.
> - Copien desde el título `[Nombre del modelo]` hacia abajo y borren las instrucciones en cursiva antes de entregar.

---

# [Nombre del modelo] — v[versión]

**Grupo:** G__ · **Integrantes:** ______________________ · **Fecha:** ____________
**Enlaces:** código · demo · informe técnico

## 1. Detalles del modelo

- **Desarrollado por:** *grupo e integrantes, en el marco del curso (Rosario GSB, Universidad del Rosario).*
- **Fecha y versión:**
- **Tipo de modelo:** *tarea (clasificación, generación, extracción…), arquitectura y modelo base (identificador de Hugging Face).*
- **Método de adaptación:** *fine-tuning completo, LoRA (rango, alfa, módulos) o entrenamiento desde cero.*
- **Información de entrenamiento:** *hiperparámetros principales, épocas, hardware y tiempo (detalle en el informe §3).*
- **Licencia:** *debe ser compatible con las licencias del modelo base y de los datos.*
- **Cómo citarlo:**
- **Contacto:** *para preguntas o para reportar problemas.*

## 2. Uso previsto

- **Usos principales:** *qué tarea resuelve, en qué proceso de negocio y con qué nivel de automatización (sugerencia a una persona o decisión automática).*
- **Usuarios previstos:**
- **Usos fuera de alcance:** *usos para los que NO debe emplearse (p. ej., decisiones sobre personas sin revisión humana, otro idioma o dominio, asesoría médica, legal o financiera).*

## 3. Factores

- **Factores relevantes:** *grupos, condiciones o características que pueden cambiar el desempeño: variante del idioma (español colombiano frente a otros), región, canal (correo, chat, redes), longitud o formalidad del texto, errores ortográficos y, si aplica, grupos demográficos.*
- **Factores evaluados:** *cuáles de ellos se midieron en la sección 7 y por qué se eligieron.*

## 4. Métricas

- **Métricas de desempeño:** *cuáles y por qué reflejan lo que importa al negocio y al riesgo (costo de un falso positivo frente a un falso negativo).*
- **Umbrales de decisión:** *umbral de confianza usado en la demo y cómo se eligió.*
- **Variación:** *cómo se estimó la incertidumbre (varias semillas, intervalos, validación cruzada).*

## 5. Datos de evaluación

- **Datasets:** *nombre, fuente, licencia y tamaño del conjunto de prueba.*
- **Motivación:** *por qué representan el uso real.*
- **Preprocesamiento:**

## 6. Datos de entrenamiento

*Fuente, tamaño, distribución de clases, datos sintéticos (cómo se generaron y revisaron), anonimización y consentimiento (Ley 1581 de 2012). Si no pueden publicar los datos, descríbanlos con el detalle suficiente para entender sus límites (inspírense en* Datasheets for Datasets, *Gebru et al., 2021).*

## 7. Análisis cuantitativo

**Resultados globales** (conjunto de prueba)

| Sistema | Métrica 1 | Métrica 2 |
|---|---|---|
| Línea base | | |
| Este modelo | | |

**Resultados por factor o subgrupo**

| Factor / subgrupo | N | Métrica 1 | Métrica 2 | Brecha frente al global |
|---|---|---|---|---|
| | | | | |
| | | | | |

*Comenten las brechas: ¿son importantes para el negocio? ¿Qué las explica?*

## 8. Consideraciones éticas

- **Datos:** *¿hay datos personales o sensibles? ¿Cómo se protegieron?*
- **Impacto en las personas:** *¿el modelo influye en decisiones que afectan a personas (acceso a servicios, prioridad de atención, reputación)?*
- **Riesgos y daños:** *sesgos, errores costosos, alucinaciones, usos indebidos previsibles.*
- **Mitigaciones:** *qué se hizo (y qué queda pendiente): umbrales, revisión humana, filtros, monitoreo.*
- **Casos de uso problemáticos:**

## 9. Advertencias y recomendaciones

*Limitaciones conocidas, condiciones para usarlo con seguridad, monitoreo recomendado en producción (drift, reentrenamiento), pruebas adicionales que harían antes de desplegarlo.*

## 10. Impacto ambiental *(sección adicional)*

| Dato | Valor |
|---|---|
| Hardware | *p. ej., GPU T4 de Kaggle* |
| Horas de cómputo (entrenamiento + experimentos) | |
| Emisiones estimadas (kg CO₂eq) | |
| Herramienta o método | *CodeCarbon, o la calculadora de Lacoste et al. (2019)* |

## 11. Cómo usar el modelo *(sección adicional)*

```python
# Ejemplo mínimo: ajústenlo a su tarea y a la ubicación real del modelo
from transformers import pipeline

modelo = pipeline("text-classification", model="<usuario>/<nombre-del-modelo>")
print(modelo("Texto de ejemplo"))
```

**Metadatos para Hugging Face Hub** *(opcional, solo si publican el modelo allí; van al inicio del `README.md` del modelo)*

```yaml
---
language: es
license: <licencia compatible con el modelo base y los datos>
base_model: <identificador del modelo base>
datasets:
  - <identificador del dataset>
metrics:
  - <métrica>
pipeline_tag: <tarea, p. ej. text-classification>
---
```

---

## Referencias

- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. En *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT\* '19)* (pp. 220–229). ACM. https://doi.org/10.1145/3287560.3287596
- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12), 86–92. https://arxiv.org/abs/1803.09010
- Lacoste, A., Luccioni, A., Schmidt, V., & Dandres, T. (2019). *Quantifying the carbon emissions of machine learning*. arXiv. https://arxiv.org/abs/1910.09700
- Hugging Face. *Model Cards* (documentación). https://huggingface.co/docs/hub/model-cards
