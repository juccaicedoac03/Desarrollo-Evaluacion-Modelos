# Informe técnico — Plantilla

*Proyecto final · Desarrollo y Evaluación de Modelos Propios*

> **Reglas de formato**
>
> - **Máximo 8 páginas**, sin contar portada, referencias ni anexos. Lo que pase de la página 8 no se califica.
> - PDF, tamaño carta, fuente de 11 pt, interlineado sencillo, márgenes de 2.5 cm. Nombre del archivo: `PF_G<NN>_informe.pdf`.
> - En español. Las tablas y figuras cuentan dentro de las 8 páginas: úsenlas cuando digan más que el texto.
> - Todo número del informe debe salir de ejecutar su código. Resultados fabricados = 0.0 en el componente ([rúbrica](../rubrica.md)).
> - Las extensiones sugeridas son orientativas. Borren las instrucciones en cursiva antes de entregar.
> - **Hito H4 (S11):** entreguen el borrador de la sección 5 (bitácora) con el enlace al código.

---

## Portada *(no cuenta)*

- **Título del proyecto**
- **Grupo** G__ · integrantes (nombre y código)
- **Enlaces:** código (repositorio de GitHub o notebook de Kaggle) · demo (Gradio, Hugging Face Spaces o agente de Startti) · video de respaldo (opcional) · model card
- Fecha

---

## Resumen ejecutivo *(½ página)*

*Escrito para una persona de negocio que solo leerá esta sección: el problema, qué construyeron, el resultado principal frente a la línea base (con números), la recomendación (go / no-go / piloto) y el principal riesgo.*

## 1. Problema y contexto *(½–¾ página)*

*Organización (real o ficticia) y proceso actual; usuarios; costo del problema; KPI de éxito; por qué un modelo propio y no solo reglas o prompting de un API. Criterio 1 de la rúbrica.*

## 2. Datos *(1 página)*

*Criterio 2 de la rúbrica.*

- *Fuente, licencia y autorización de uso; si hay datos sintéticos: cómo se generaron (modelo, prompt, cantidad) y cómo se revisaron.*
- *Tamaño, distribución de clases o de longitudes y ejemplos representativos.*
- *Particiones de entrenamiento, validación y prueba: cómo se hicieron y cómo verificaron que no hubiera fuga (duplicados, casi duplicados, mismo cliente o documento en dos particiones).*
- *Preprocesamiento y problemas de calidad encontrados.*
- *Privacidad: qué datos personales había, cómo se anonimizaron y cómo se verificó (Ley 1581 de 2012).*

| Partición | N.º de ejemplos | Distribución de clases o nota |
|---|---|---|
| Entrenamiento | | |
| Validación | | |
| Prueba | | |

## 3. Modelo y entrenamiento *(1 página)*

*Criterio 3 de la rúbrica.*

- *Modelo base y por qué (tarea, idioma, tamaño, licencia, cómputo disponible).*
- *Enfoque: fine-tuning completo, LoRA (rango, alfa, módulos) o entrenamiento desde cero.*
- *Hiperparámetros, curva de pérdida de entrenamiento y validación (figura), hardware y tiempo de entrenamiento.*
- *Reproducibilidad: semilla, versiones de librerías y cómo correr el código.*

| Hiperparámetro | Valor | Por qué |
|---|---|---|
| Tasa de aprendizaje | | |
| Épocas / pasos | | |
| Tamaño de lote (y acumulación) | | |
| Longitud máxima | | |
| (LoRA) r, alfa, módulos | | |

## 4. Evaluación *(1½ páginas)*

*Criterio 4 de la rúbrica.*

- *Métricas (al menos 2) y por qué capturan lo que importa al negocio y al riesgo. Si usan un LLM como juez, expliquen cómo lo validaron frente a juicios humanos.*
- *Línea base: qué es y por qué es una comparación justa.*
- *Resultados en el conjunto de prueba reservado. Si es posible, reporten la variabilidad (varias semillas o un intervalo).*
- *Análisis de errores: revisión manual de una muestra (sugerido: 20 o más), con categorías, conteos, 2 o 3 ejemplos y una hipótesis por categoría.*

| Sistema | Métrica 1 | Métrica 2 | Latencia o costo (opcional) |
|---|---|---|---|
| Línea base | | | |
| Modelo v1 | | | |
| Modelo final | | | |

| Categoría de error | Conteo (de N revisados) | Ejemplo | Hipótesis |
|---|---|---|---|
| | | | |

## 5. Mejora iterativa *(1 página)*

*Criterio 5 de la rúbrica. Cada iteración: hipótesis (que salga del análisis de errores) → cambio → resultado → decisión. Decidan con validación; el conjunto de prueba se usa al final para reportar todas las versiones, sin ajustar nada sobre él.*

**Bitácora de experimentos**

| # | Fecha | Hipótesis (¿de qué error sale?) | Cambio realizado | Métrica 1 (val.) | Métrica 2 (val.) | Decisión | Commit o versión |
|---|---|---|---|---|---|---|---|
| 0 | | Línea base | — | | | — | |
| 1 | | | | | | | |
| 2 | | | | | | | |

*Cierren con un párrafo: ¿qué aprendieron de la iteración y qué probarían después?*

## 6. Demo y diseño del producto *(½ página)*

*Arquitectura de la demo (diagrama simple); dónde entra el modelo propio; decisiones de producto (umbral de confianza, escalamiento a una persona, mensajes de incertidumbre); latencia observada; si usan Startti, cómo se orquesta con el modelo propio.*

## 7. Ética y sostenibilidad *(1 página)*

*Criterio 6 de la rúbrica.*

- *Riesgos específicos del caso: sesgo, privacidad, usos indebidos, impacto en las personas usuarias y afectadas.*
- *Al menos una prueba empírica: desempeño por subgrupo (variante del idioma, canal, longitud del texto, región) o prueba contrafactual; resultados y mitigación.*
- *Emisiones o energía del entrenamiento (CodeCarbon) y cómo se comparan con alternativas (p. ej., un modelo más pequeño o solo la línea base).*
- *Clasificación de riesgo razonada (p. ej., según el EU AI Act) y marcos de referencia vistos en la S10.*
- *Resumen de la model card y enlace a ella.*

## 8. Conclusiones, limitaciones y recomendación *(½ página)*

*¿Se cumplió la métrica de éxito? Recomendación de negocio (go / no-go / piloto con condiciones), limitaciones honestas y siguientes pasos (datos, modelo, monitoreo en producción).*

---

## Referencias *(no cuentan)*

*Estilo APA 7. Incluyan el modelo base, los datasets y las librerías principales. No incluyan referencias que no hayan verificado.*

## Anexo A. Declaración de contribuciones *(no cuenta, obligatorio)*

| Integrante | Principales aportes (datos, código, modelo, evaluación, informe, demo, pitch) | Porcentaje estimado del trabajo total |
|---|---|---|
| | | |
| | | |
| | | |

*El profesor usa esta tabla, junto con el historial del código, como evidencia en la revisión de la coevaluación.*

## Anexo B. Material complementario *(opcional, no cuenta)*

*Figuras o tablas adicionales. El profesor no está obligado a leerlo: lo esencial debe estar en las 8 páginas.*

---

**Antes de entregar**

- [ ] ≤ 8 páginas (sin portada, referencias ni anexos), en PDF.
- [ ] Todos los números coinciden con los que produce el código entregado.
- [ ] Hay línea base, al menos 2 métricas justificadas, análisis de errores y al menos una iteración en la bitácora.
- [ ] La sección 7 tiene al menos una prueba empírica y la medición de emisiones.
- [ ] Portada con enlaces que funcionan (pruébenlos desde una ventana privada si son públicos, o con la cuenta de otro integrante si son privados).
- [ ] Model card y [registro de uso de IA](registro-uso-ia.md) completos.
