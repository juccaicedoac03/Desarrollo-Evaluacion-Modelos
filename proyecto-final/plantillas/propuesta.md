# Propuesta de proyecto — Canvas

*Proyecto final · Desarrollo y Evaluación de Modelos Propios*

> **Cómo usar esta plantilla**
>
> - **Parte A — Canvas de propuesta (Hito H2):** se entrega hasta el **miércoles 14 de octubre a las 23:59**, después de la Sesión 6; la retroalimentación escrita llega en la Sesión 7 (viernes 16 de octubre). Máximo **1 página**: respuestas cortas y concretas.
> - **Parte B — Canvas de caso de uso (Hito H3):** se entrega en la **Sesión 9** (sábado 17 de octubre, 23:59). Actualicen la Parte A (sigue siendo de máximo 1 página; marquen los cambios con **[CAMBIO]**) y completen la Parte B en **máximo 2 páginas adicionales**. El archivo del H3 tiene, entonces, máximo 3 páginas: Parte A (1) + Parte B (2).
> - Súbanla a e-Aulas en PDF o Markdown: `PF_G<NN>_H2_propuesta` y `PF_G<NN>_H3_canvas`.
> - Borren las preguntas guía antes de entregar. Enunciado, hitos e ideas: [README del proyecto](../README.md).

**Grupo:** G__ · **Nombre del proyecto:** ______________________ · **Fecha:** ____________

| Integrante | Código | Perfil (negocio / técnico / mixto) | Rol principal en el proyecto |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

---

## Parte A — Canvas de propuesta (H2 · máximo 1 página)

| Bloque | Preguntas guía | Respuesta |
|---|---|---|
| **1. Problema** | ¿Qué problema concreto resuelven? ¿Cómo se resuelve hoy y cuánto cuesta (tiempo, dinero, errores)? | |
| **2. Usuarios** | ¿Quién usará la solución y en qué momento de su trabajo? ¿Quién se ve afectado por sus errores? | |
| **3. Valor de negocio** | ¿Qué mejora si funciona? ¿Qué KPI de negocio se movería (tiempo de respuesta, costo por caso, satisfacción…)? | |
| **4. Datos** | Fuente, tamaño estimado, etiquetas, idioma y licencia. ¿Hay datos personales? ¿Cómo los anonimizarán? ¿Tienen la autorización necesaria? | |
| **5. Modelo base y enfoque** | ¿Qué modelo de partida usarán y por qué (tarea, idioma, tamaño, licencia)? ¿Fine-tuning completo, LoRA o entrenamiento desde cero? ¿Cuál será la línea base? | |
| **6. Métrica de éxito** | Al menos 2 métricas (una técnica y una de negocio o de riesgo), con el umbral que consideran "suficientemente bueno" y por qué. | |
| **7. Riesgos** | Técnicos (datos insuficientes, cómputo), éticos (sesgo, privacidad, uso indebido) y de negocio. Una mitigación para cada uno. | |
| **8. Demo prevista** | ¿App de Gradio o agente de Startti? ¿Qué verá la persona usuaria? ¿Qué papel cumple el modelo propio en la demo? | |

**9. Plan por hitos**

| Tramo | Qué lograremos | Responsable |
|---|---|---|
| Hasta la S9 (H3, sábado 17 oct.) | Datos listos y particionados, línea base evaluada, primer modelo entrenado | |
| S9 → viernes 23 oct. (H4 y entrega final) | Análisis de errores, iteración de mejora documentada en el §5 del informe, demo, análisis ético, model card e informe | |
| Viernes 23 oct. → S12 (sábado 24 oct.) | Pitch y ensayo de la demo para la socialización | |

**10. Roles:** completen la columna "Rol principal" de la tabla de integrantes. Cada persona lidera un frente, pero todos programan y todos deben poder explicar todo el proyecto.

**Antes de entregar la Parte A, verifiquen que:**

- [ ] el problema tiene un usuario y un KPI concretos;
- [ ] los datos existen o se pueden construir legalmente, sin datos personales sin autorización;
- [ ] el plan incluye **afinar o entrenar** un modelo (no solo prompting) y una línea base;
- [ ] el modelo elegido cabe en Kaggle gratis (≤ ~1B de parámetros, LoRA para LLM);
- [ ] cabe en 1 página.

---

## Parte B — Canvas de caso de uso (H3 · Sesión 9 · máximo 2 páginas adicionales a la Parte A)

### B1. Cambios desde la propuesta

¿Qué cambió en la Parte A y por qué? ¿Cómo respondieron a la retroalimentación del profesor?

### B2. Estado actual y primeros resultados

| Métrica | Línea base | Primer modelo (si ya existe) | Conjunto evaluado (validación o prueba) y tamaño |
|---|---|---|---|
| | | | |
| | | | |

Datos: ¿cuántos ejemplos tienen por partición y por clase? ¿Qué problemas de calidad encontraron?

### B3. Valor × factibilidad

| Dimensión | Puntaje (1–5) | Justificación con evidencia |
|---|---|---|
| Valor para el negocio | | |
| Factibilidad técnica (datos, modelo, cómputo) | | |
| Factibilidad organizacional (adopción, procesos, personas) | | |
| Riesgo (5 = riesgo bajo) | | |

### B4. KPI

| KPI | Valor actual, sin el modelo | Meta con el modelo | Cómo y cada cuánto se mediría |
|---|---|---|---|
| | | | |
| | | | |

### B5. Estimación simple de ROI

```text
Beneficio anual estimado = (horas ahorradas × costo por hora) + (errores evitados × costo por error) + …
Costo anual estimado     = desarrollo + cómputo + operación + supervisión humana + mantenimiento
ROI                      = (beneficio − costo) / costo
```

| Supuesto | Valor | Fuente o justificación |
|---|---|---|
| | | |

Calculen un escenario base y uno pesimista. **No inventen cifras:** si un valor es una estimación, díganlo y expliquen de dónde sale.

### B6. Riesgos y clasificación preliminar

| Riesgo | Probabilidad (baja / media / alta) | Impacto (bajo / medio / alto) | Mitigación | Responsable |
|---|---|---|---|---|
| | | | | |
| | | | | |

Clasificación preliminar del nivel de riesgo del sistema (p. ej., según las categorías de riesgo del EU AI Act, que se profundizan en la S10) y por qué.

### B7. Decisión

**Continuar / ajustar / pivotar**, con 2 o 3 líneas de justificación basadas en B2–B6.
