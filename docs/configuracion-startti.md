# Configuración de Startti ADP

*Guía para tener tu workspace, tu primer agente y tu API key listos. Activa tu licencia **antes del sábado 10 de octubre**: ese día la S05 y la S06 van seguidas y no hay tiempo entre una y otra.*

**Startti ADP** es una plataforma para construir agentes de IA de forma visual: sobre un lienzo (*canvas*) conectas nodos de entrada, modelos de lenguaje, herramientas y bases de conocimiento; luego **publicas** el agente y lo llamas desde tus propias aplicaciones por API. En el curso la usamos para pasar del prototipo en código al agente listo para integrarse.

| Recurso | Enlace |
|---|---|
| Sitio y documentación | [adp.startti.ai](https://adp.startti.ai) · [adp.startti.ai/docs](https://adp.startti.ai/docs) |
| Aplicación (donde construyes tus agentes) | [app.startti.ai](https://app.startti.ai) |
| API | `https://api.startti.ai` |

**¿Dónde se usa en el curso?**

| Sesión | Uso |
|---|---|
| S06 (sábado 10 oct.) | Primer agente, publicación y primera llamada por API desde Kaggle |
| S07 (viernes 16 oct.) | Agente de servicio al cliente con base de conocimiento, evaluado desde Kaggle con un set de conversaciones |
| S09 (sábado 17 oct.) | Agente sectorial (salud, finanzas o educación) |
| Proyecto final | Opcional: puedes exponer tu solución como agente de Startti o como app en Gradio |

> **¿Prefieres no crear una cuenta?** Todo el curso se puede hacer sin Startti: ver la sección 11.

> Las interfaces cambian. Si un botón o menú no tiene exactamente el nombre que indica esta guía, busca la opción equivalente o consulta la [documentación oficial](https://adp.startti.ai/docs).

---

## 1. Activa tu licencia y tu workspace

- El profesor gestiona las **licencias del curso sin costo para ti**. Cada estudiante tiene **su propio workspace**.
- Recibirás las instrucciones de activación por los canales del curso (en clase y en e-Aulas). Al terminar podrás iniciar sesión en [app.startti.ai](https://app.startti.ai) y verás tu workspace.
- La licencia es personal: no compartas tu usuario ni tu contraseña.

## 2. Crea tu primer agente

La [guía de inicio rápido](https://adp.startti.ai/docs) de Startti describe el flujo completo. En resumen:

1. **Crea un proyecto** en tu workspace, con un nombre que describa el proceso que vas a resolver (por ejemplo, `S06 - asistente Andes Bank`).
2. **Arma el flujo mínimo** en el lienzo:
   - un nodo de **entrada de chat** (lo que escribe la persona llega aquí);
   - un nodo de **llamada al modelo de lenguaje**, donde eliges el modelo y escribes las **instrucciones del sistema**;
   - un nodo de **salida de chat**, conectado a la respuesta del modelo.
3. **Pruébalo en la vista previa** (el chat que aparece junto al lienzo).

Si la plataforma te pide una clave de proveedor de modelos, sigue las indicaciones que dará el profesor en clase; no uses claves personales de pago.

**Instrucciones del sistema: una plantilla para empezar**

```text
Eres el asistente virtual de Andes Bank, un banco ficticio.
Objetivo: responder preguntas frecuentes sobre tarjetas, cuentas y canales de atención.
Tono: cordial, claro y breve (máximo 4 frases).
Límites:
- Responde solo con la información de la base de conocimiento. Si no la tienes, dilo y ofrece hablar con un asesor humano.
- Nunca pidas contraseñas, números completos de tarjeta ni documentos de identidad.
- No des asesoría financiera personalizada.
```

## 3. Agrega una base de conocimiento

Una base de conocimiento permite que el agente responda con información de tus documentos.

1. **Crea una colección de conocimiento** en tu workspace (se recomienda una por tema: preguntas frecuentes, políticas, manuales).
2. **Sube los documentos** arrastrándolos. Espera a que su estado pase a **indexado** antes de probar. Si una carga falla, la plataforma muestra el motivo.
3. **Conecta la búsqueda en la base de conocimiento** como herramienta del nodo del modelo.
4. **Describe el contenido** de la base en la descripción de la herramienta, no su funcionamiento:
   - ✅ "Preguntas frecuentes de Andes Bank sobre tarjetas, bloqueos, cuentas y horarios de atención"
   - ❌ "Busca documentos en la base vectorial"

En el curso usarás documentos **ficticios** que encontrarás en la carpeta `data/` de cada sesión (por ejemplo, las preguntas frecuentes de Andes Bank en `sessions/07-chatbots-and-agents/data/`).

**Buenas prácticas.** Una base de conocimiento funciona bien para información estable (políticas, preguntas frecuentes, manuales), no para datos que cambian a cada minuto (saldos, estados de pedidos). Sube solo los documentos necesarios: tu plan puede tener límites de almacenamiento.

## 4. Publica el agente

- **Publicar es un paso explícito, distinto de guardar.** Mientras no lo publiques, el agente es un borrador que solo funciona en la vista previa.
- **Para llamarlo por API, el agente debe estar publicado.** Si no lo está, la API responde **409**.
- Puedes despublicarlo después sin perder su configuración.
- Tu plan puede tener límites (por ejemplo, número de agentes publicados); si ves un error **402**, avísale al profesor. Mientras tanto, puedes despublicar los agentes que ya no uses.

## 5. Crea tu API key

La API key es la credencial con la que tus notebooks llaman a tus agentes.

1. Con tu sesión iniciada, crea una clave nueva desde el **backoffice de ADP** (la opción de API keys de tu workspace). Las claves se crean desde la plataforma con tu usuario, no desde un notebook.
2. **El secreto se muestra una sola vez.** Cópialo de inmediato y guárdalo en Kaggle Secrets (sección 6). Si lo pierdes, crea una clave nueva y revoca la anterior.
3. La clave empieza por `adp_`.
4. Cada clave **pertenece a un solo workspace** y puede **restringirse a agentes específicos**. Si la restringes, recuerda agregar los agentes nuevos que crees en S07 y S09; de lo contrario, la API responderá **403**.

**Cuida tu clave como una contraseña.** Nunca la pegues en una celda de código, en un chat, en una captura de pantalla, en tus slides ni en un repositorio. Si se expone, revócala y crea una nueva.

## 6. Guarda la clave en Kaggle Secrets

1. En tu notebook de Kaggle, abre **Add-ons → Secrets**.
2. Agrega un secreto con el nombre **`STARTTI_API_KEY`** y como valor tu clave `adp_…`.
3. Verifica que el secreto esté **adjunto al notebook**. Debes adjuntarlo en cada notebook donde lo uses.
4. Ejecuta la celda del cliente de Startti: debe imprimir `Startti key found ✅`.

En Colab, guárdala con el ícono de llave 🔑 de la barra lateral; en tu computador, como variable de entorno `STARTTI_API_KEY`. Más detalles en [configuracion-kaggle.md](configuracion-kaggle.md).

## 7. Encuentra el ID de tu agente

Para llamar a un agente necesitas su **ID** (`agentId`). El ID aparece en la página del agente en ADP y en su URL; el profesor lo mostrará en clase. Cópialo en la celda correspondiente del notebook:

```python
AGENT_ID = "pega-aquí-el-id-de-tu-agente"
```

El ID no es secreto (sin tu API key no sirve para nada), pero tampoco hace falta publicarlo.

## 8. Llama a tu agente por API

### Desde Kaggle, con `startti_run`

Los notebooks de S06, S07 y S09 incluyen una celda con el cliente del curso ([`tools/snippets/startti_client.py`](../tools/snippets/startti_client.py)). Lee la clave desde los *Secrets* y define la función `startti_run`:

```python
AGENT_ID = "pega-aquí-el-id-de-tu-agente"

# Una pregunta
respuesta = startti_run(AGENT_ID, "Hola, ¿qué puedes hacer por mí?")
print(respuesta)

# Una conversación de varios turnos: usa el mismo session_key en todos los mensajes
print(startti_run(AGENT_ID, "Quiero bloquear mi tarjeta", session_key="prueba-01"))
print(startti_run(AGENT_ID, "Es la tarjeta de crédito", session_key="prueba-01"))
```

- `session_key` es un identificador que **tú eliges** para una conversación. Si repites el mismo valor, el agente continúa esa conversación; si lo omites, cada llamada empieza una conversación nueva.
- Si el agente necesita hacerte una pregunta antes de responder, `startti_run` devuelve un texto que empieza por `[AGENT ASKED]`.
- Si hay un error, `startti_run` lanza una excepción con el código HTTP y una pista (ver la sección 9).

### Desde una terminal, con `curl`

Útil para probar tu agente fuera de Kaggle. Carga la clave sin escribirla en el historial de la terminal:

```bash
read -s STARTTI_API_KEY && export STARTTI_API_KEY   # pega la clave y presiona Enter

curl -s https://api.startti.ai/v1/run \
  -H "Authorization: Bearer $STARTTI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"agentId": "<AGENT_ID>", "prompt": "Hola, ¿qué puedes hacer por mí?", "sessionKey": "prueba-01"}'
```

Respuesta (resumida):

```json
{
  "sessionId": "…",
  "sessionKey": "prueba-01",
  "output": {
    "text": "Hola, soy el asistente virtual de Andes Bank…",
    "suspended": false,
    "suspendQuestions": [],
    "errorText": null
  }
}
```

| Campo | Significado |
|---|---|
| `output.text` | La respuesta del agente |
| `output.suspended` | `true` si el agente se detuvo para hacerte una pregunta; las preguntas vienen en `output.suspendQuestions` |
| `output.errorText` | Mensaje de error del agente, si lo hubo |
| `sessionId`, `sessionKey` | Identificadores de la conversación |

## 9. Errores frecuentes

| Código o mensaje | Qué significa | Qué hacer |
|---|---|---|
| `No STARTTI_API_KEY — Startti cells will be skipped.` | El notebook no encontró tu clave | Revisa el nombre exacto del secreto (`STARTTI_API_KEY`) y que esté adjunto al notebook; vuelve a ejecutar la celda del cliente |
| **400** | La solicitud está mal formada (por ejemplo, `prompt` vacío) | Revisa que envías `agentId` y un `prompt` con texto |
| **401** | Clave inválida o revocada | Verifica que copiaste la clave completa; si la perdiste o la revocaste, crea una nueva |
| **402** | Alcanzaste un límite de tu plan (por ejemplo, número de agentes publicados) | Avísale al profesor; mientras tanto, puedes despublicar los agentes que no uses |
| **403** | La clave no tiene acceso a ese agente (otro workspace o clave restringida a otros agentes) | Usa una clave del mismo workspace del agente o agrega el agente a la lista de la clave |
| **404** | No se encontró el agente | Revisa el `AGENT_ID` (sin espacios ni comillas de más) |
| **409** | El agente no está publicado | Publícalo en ADP y vuelve a intentarlo |
| `Agent error: …` | El agente se ejecutó pero falló internamente | Pruébalo en la vista previa de ADP para ver el detalle y corrige su configuración |
| Tiempo de espera agotado (*timeout*) | El agente tardó más de lo esperado | Reintenta; si persiste, simplifica el prompt o revisa las herramientas del agente |

## 10. Protección de datos

- **No pongas datos personales ni sensibles** en tus agentes, bases de conocimiento, prompts o conversaciones de prueba: nombres, cédulas, teléfonos, correos o direcciones de personas reales, ni datos sensibles como los de salud o los biométricos.
- En Colombia, el tratamiento de datos personales está regulado por la **Ley 1581 de 2012** (régimen general de protección de datos personales). En el curso trabajamos solo con **datos ficticios o públicos**.
- Tampoco subas información confidencial de tu empresa.
- Si tu proyecto final requiere datos reales, anonimízalos antes de usarlos y consúltalo con el profesor.

## 11. Alternativa sin cuenta

Si prefieres no crear una cuenta en Startti, puedes hacer todo el curso con la **alternativa en Python** que incluyen los labs:

- En el lab de S07 construyes un **bot en Python** (clasificador de intenciones, extracción de datos, manejo de estado y respuesta con un modelo de lenguaje abierto) que cumple el mismo papel que el agente de Startti. En S06 y S09, las partes de Startti tienen su equivalente en código (la app en Gradio y los prototipos en Python).
- Las celdas que dependen de Startti **se omiten automáticamente** si no hay una API key, así que el notebook se ejecuta completo.
- El evaluador de conversaciones de S07 recibe cualquier función `agent_fn(prompt, session_key) -> str`: puedes pasarle tu agente de Startti o tu bot en Python.
- Los challenges de S06, S07 y S09 aceptan el camino de Startti o la alternativa en Python; ambos se califican con la misma rúbrica.

## 12. Lista de verificación

**Antes del sábado 10 de octubre (S05 y S06)**

- [ ] Activé mi licencia e inicié sesión en [app.startti.ai](https://app.startti.ai).
- [ ] Veo mi workspace.

**Durante la Sesión 06 (en el lab)**

- [ ] Creé y probé mi primer agente en la vista previa.
- [ ] Lo publiqué.
- [ ] Creé mi API key y la guardé en Kaggle Secrets como `STARTTI_API_KEY`.
- [ ] Llamé a mi agente desde Kaggle con `startti_run`.

**Antes de la Sesión 07 (viernes 16 de octubre)**

- [ ] Mi API key sigue funcionando desde Kaggle (la celda del cliente imprime `Startti key found ✅`).
