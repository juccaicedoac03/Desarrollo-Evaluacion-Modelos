# Configuración de Kaggle

*Guía para dejar tu entorno listo **antes de la Sesión 01**.*

Todos los labs y challenges del curso son notebooks de Jupyter que se ejecutan en **Kaggle Notebooks**: un entorno en la nube con GPU gratuita y la mayoría de las librerías del curso ya instaladas (PyTorch, transformers, scikit-learn…). No necesitas instalar nada en tu computador; basta un navegador y una conexión estable.

> Las interfaces de Kaggle y Colab cambian con frecuencia. Si un menú no aparece exactamente con el nombre que indica esta guía, busca una opción equivalente o pregunta en el foro del curso.

---

## 1. Crea tu cuenta

1. Entra a [kaggle.com](https://www.kaggle.com/) y regístrate (*Register*). Puedes usar tu correo institucional o uno personal.
2. Elige un nombre de usuario. No tiene que coincidir con tu código estudiantil.
3. Confirma tu correo electrónico si Kaggle te lo pide.

## 2. Verifica tu número de celular (obligatorio)

Sin verificación telefónica, **Kaggle no te deja activar la GPU ni el acceso a Internet** en los notebooks. Los labs necesitan Internet para descargar modelos y datos de Hugging Face, así que este paso es indispensable.

1. Abre la configuración de tu cuenta (tu foto de perfil → *Settings*).
2. Busca la opción de verificación por teléfono (*Phone verification*).
3. Ingresa tu número celular y el código que recibes por SMS.

Si intentas activar Internet sin haber verificado tu número, Kaggle te pedirá hacerlo en ese momento.

## 3. Abre un notebook del curso

Los notebooks se abren desde enlaces a Kaggle:

- en el [portal del curso](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/), cada sesión tiene los botones **Lab en Kaggle** y **Challenge en Kaggle**;
- en las guías de sesión (`sessions/NN-<tema>/README.md`) y en la tabla de sesiones del README del repositorio, el enlace se llama simplemente **Kaggle** (junto a **Colab**);
- las presentaciones también incluyen un botón de Kaggle en las diapositivas del lab y del challenge.

Todos siguen este patrón:

```text
https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/<NN-tema>/lab.ipynb
```

Qué pasa al hacer clic (el comportamiento exacto depende de la versión de Kaggle; el profesor lo confirmará en la S01):

- Con tu sesión iniciada, Kaggle **importa el notebook desde GitHub y crea una copia en tu cuenta**. Tus cambios no afectan el original.
- **Normalmente, cada clic crea una copia nueva.** Para seguir trabajando en la que ya empezaste, búscala en tu cuenta: según la versión de Kaggle, aparece en tu perfil, en la sección de notebooks (*Code*), o en *Your Work*.
- Tu copia es privada. Mantenla así: los challenges contienen tu configuración personal y tus resultados.

## 4. Configura la sesión: acelerador (GPU) e Internet

Antes de ejecutar la primera celda, revisa en el menú **Settings** del editor (o en el panel lateral de opciones de la sesión):

| Opción | Valor | Cuándo |
|---|---|---|
| **Accelerator** | **GPU T4 x2** (o **GPU P100**) | Cuando el encabezado del notebook lo indica (lista *Kaggle checklist*). Si no lo indica, la CPU es suficiente y ahorras cuota |
| **Internet** | **On** | Siempre: los notebooks descargan modelos y datos |

- Cambiar el acelerador **reinicia la sesión**: vuelve a ejecutar el notebook desde la primera celda.
- Para confirmar que la GPU está activa, mira la salida de la primera celda: debe decir `Device: cuda` (labs) o `Dispositivo: cuda` (challenges). Si dice `cpu`, el acelerador no está activo.
- Cuando termines de trabajar, **detén la sesión** para no consumir cuota de GPU.

## 5. Cuota semanal de GPU

Kaggle asigna una cuota semanal de GPU gratuita, **aproximadamente 30 horas por semana**. Kaggle puede cambiar esta cifra y muestra tu consumo en la interfaz. Para el curso es más que suficiente si:

- activas la GPU solo en los notebooks que la necesitan;
- detienes la sesión al terminar, en lugar de dejarla abierta;
- no ejecutas varias veces el notebook completo sin necesidad.

Si agotas la cuota, puedes seguir en CPU (más lento) o usar Colab (sección 9) hasta que se renueve.

## 6. Secrets: tu API key de Startti

*Solo para las sesiones 06, 07 y 09 y, si lo eliges, para el proyecto final.*

Las claves de API **nunca se escriben en el código**. En Kaggle se guardan como *Secrets*:

1. En el editor del notebook, abre **Add-ons → Secrets**.
2. Agrega un secreto nuevo con:
   - **Nombre (label):** `STARTTI_API_KEY` (exactamente así, en mayúsculas).
   - **Valor:** tu clave de Startti (empieza por `adp_`).
3. Asegúrate de que el secreto quede **adjunto a este notebook** (marcado). Los secretos se guardan en tu cuenta, pero normalmente debes adjuntarlos en cada notebook donde los uses, incluidas las copias nuevas (el profesor lo confirmará en la S01).
4. Vuelve a ejecutar la celda del cliente de Startti. Debe imprimir `Startti key found ✅`.

Cómo obtener la clave: [configuracion-startti.md](configuracion-startti.md). Si decides no usar Startti, no necesitas este paso: los notebooks siguen funcionando con la alternativa en Python.

## 7. Guarda tu trabajo y entrega el challenge

Normalmente, Kaggle guarda el borrador de tu notebook mientras trabajas (según la versión de Kaggle; el profesor lo confirmará en la S01). No dependas de eso: **descarga tu entrega apenas termines**.

1. Ejecuta todo el notebook **en orden** (por ejemplo, con *Run All*).
2. Verifica que se vean **"Tu configuración personal"** y la **huella de resultados** (🔏) al final. Se califican el código y las salidas.
3. Descarga el archivo: **File → Download notebook**.
4. Renómbralo como **`S<NN>_<codigo>.ipynb`**. Por ejemplo, para la Sesión 05 y el código 123456: `S05_123456.ipynb`.
5. Súbelo a **e-Aulas** antes de las **23:59** del día de la sesión.

No necesitas *Save Version* para entregar; la entrega es el archivo `.ipynb` que subes a e-Aulas.

## 8. Problemas frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| La primera celda imprime `cpu` y el lab pide GPU | El acelerador no está activado | *Settings → Accelerator → GPU T4 x2* y vuelve a ejecutar desde el inicio |
| No puedes activar la GPU o Internet | Tu número no está verificado | Verifica tu celular (sección 2) |
| `ConnectionError`, `OSError` o errores al descargar un modelo o dataset | Internet está apagado o Hugging Face no respondió | Activa Internet y vuelve a ejecutar la celda; si persiste, espera unos minutos y reintenta |
| `ModuleNotFoundError` | Falta un paquete y no se pudo instalar | Activa Internet y ejecuta de nuevo la celda de configuración |
| `AssertionError: ⚠️ Escribe tu STUDENT_ID…` | No escribiste tu código estudiantil | Escríbelo en la primera línea de la primera celda y ejecútala de nuevo |
| `NameError: name '...' is not defined` | Se reinició la sesión o ejecutaste celdas en desorden | Ejecuta todo el notebook desde la primera celda |
| `CUDA out of memory` | La GPU se quedó sin memoria (por ejemplo, tras ejecutar varias veces una celda de entrenamiento) | Reinicia la sesión y ejecuta todo una sola vez, en orden |
| `No STARTTI_API_KEY — Startti cells will be skipped.` | El secreto no existe, tiene otro nombre o no está adjunto | Revisa *Add-ons → Secrets*: nombre exacto `STARTTI_API_KEY` y adjunto al notebook; vuelve a ejecutar la celda del cliente |
| La sesión se detuvo sola | Inactividad prolongada o límite de tiempo de la sesión | Vuelve a iniciar la sesión y ejecuta todo desde el inicio |
| Kaggle dice que agotaste tu cuota de GPU | Consumiste la cuota semanal | Sigue en CPU o usa Colab (sección 9) hasta que se renueve |
| El notebook que abriste no tiene los últimos cambios | Estás trabajando en una copia antigua | Ábrelo de nuevo desde el botón *Lab en Kaggle* o *Challenge en Kaggle* del portal (o el enlace *Kaggle* de la guía de la sesión), que importa la versión vigente del repositorio |

## 9. Plan B: Google Colab

Si Kaggle no está disponible o agotaste tu cuota, puedes usar **Google Colab** con una cuenta de Google. Los notebooks del curso detectan automáticamente si corren en Colab.

1. **Abrir:** usa el enlace *Colab* de la guía de la sesión (o de la tabla de sesiones del README del repositorio), o este patrón:

   ```text
   https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/<NN-tema>/challenge.ipynb
   ```

2. **Guardar tu copia:** *File → Save a copy in Drive* (*Archivo → Guardar una copia en Drive*). Si no lo haces, puedes perder tus cambios al cerrar.
3. **Activar la GPU:** *Runtime → Change runtime type → T4 GPU* (*Entorno de ejecución → Cambiar tipo de entorno de ejecución → GPU T4*).
4. **Secrets:** abre el panel de secretos con el **ícono de llave** 🔑 de la barra lateral izquierda, agrega `STARTTI_API_KEY` con tu clave y permite el acceso del notebook. El cliente de Startti de los notebooks lee este secreto automáticamente.
5. **Descargar para entregar:** *File → Download → Download .ipynb* (*Archivo → Descargar → Descargar .ipynb*) y renómbralo como `S<NN>_<codigo>.ipynb`.

Ten en cuenta que en la versión gratuita de Colab la GPU no siempre está disponible y la sesión se desconecta tras un tiempo de inactividad.

## 10. Lista de verificación antes de la Sesión 01

- [ ] Tengo cuenta en Kaggle y sé iniciar sesión.
- [ ] Verifiqué mi número celular.
- [ ] Abrí el lab de la Sesión 01 con el botón *Lab en Kaggle* del portal (o el enlace *Kaggle* de la guía de la sesión) y se creó una copia en mi cuenta.
- [ ] Activé Internet (y la GPU) y la primera celda se ejecutó sin errores.
- [ ] Sé descargar un notebook (*File → Download notebook*).
