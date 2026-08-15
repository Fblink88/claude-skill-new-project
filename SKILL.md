---
name: new-project
description: Guía de descubrimiento conversada, estilo spec-driven development, para arrancar un proyecto de software nuevo o retomar uno existente antes de escribir código. Ayuda a decidir, en orden de dependencia: producto y alcance (problema, usuarios, plataforma, MVP, reglas de negocio), modelo del dominio, datos sensibles y legal, arquitectura y paradigma, stack técnico, auth y multi-tenancy, seguridad e infraestructura, git/CI-CD/convenciones/metodología, identidad visual y UX/UI, desglose en tareas con gestión de riesgos, y ya en implementación: testing y checklist de producción (backups, rollback, observabilidad). Pregunta solo lo que bloquea decisiones importantes según el tamaño del proyecto, deja elegir el modo de aprobación, explica tradeoffs antes de decidir, y documenta todo en DOC/. Úsala para empezar un proyecto desde cero, decidir cómo seguir uno en marcha, o elegir arquitectura/stack antes de programar.
---

<!-- Contenido en construcción, se completa en conversación con el autor. Ver DOC/plan-creacion-skill.md para el mapa de dependencias completo (13 bloques) y las decisiones de diseño detrás de este bloque 1. -->

## Bloque 1 — Punto de entrada

Antes de cualquier otra cosa, pregunta:

**Fork inicial** (siempre primero):

"¿Es un proyecto nuevo, o uno que ya tiene código y quieres definir cómo seguir?"
- Nuevo
- Existente, quiero ver cómo seguir

### Si es nuevo

Pregunta en un mismo paso:

1. **Alcance:**
   - **Modo completo** — Recorremos: producto y contexto, alcance, modelo del dominio, datos sensibles y legal, arquitectura, stack técnico, auth, seguridad e infraestructura, git/CI/CD, UX/UI. El tamaño del proyecto (bloque 2) sigue filtrando qué preguntas de cada bloque aplican — "completo" es profundidad dentro de lo relevante para ese tamaño, no todas las preguntas sin filtro (ver notas de "se omite si tamaño..." en los bloques correspondientes).
   - **Modo rápido** — Solo lo que bloquea decisiones importantes: qué se construye, país y datos sensibles, arquitectura de alto nivel, stack.
   - **Sin guía de decisiones** — no recorremos bloques.
2. **Verbosidad:**
   - **Modo aprendizaje** — explico opciones y tradeoffs antes de decidir.
   - **Modo directo** — pregunto y avanzamos, sin explicaciones largas.
3. **Idioma:**
   - Español
   - Inglés
4. **Modo de aprobación** (deja explícito lo que si no se pregunta queda como default silencioso): "¿Cómo prefieres que pida aprobación durante el proceso?"
   - **Todo con aprobación** — cada decisión, paso a paso.
   - **Solo decisiones grandes o costosas de revertir** (default si no se pregunta) — arquitectura, producción, borrar datos, pagos. El resto avanza sin pausas.
   - **Autónomo** — avisar solo al final de cada bloque, no interrumpir dentro de él.
5. **Nivel de tecnicismo** — distinto de la verbosidad (2): esto es si los *términos técnicos* necesitan definición, no cuánto se explican las opciones. "¿Necesitas que defina los términos técnicos que use (ej. qué es un webhook, qué es RLS), o los puedo usar directo?"
   - **Explicar siempre** — definir cualquier término técnico la primera vez que aparece.
   - **Solo lo poco común** — lo básico no se explica, solo jerga específica o poco frecuente.
   - **Sin explicar** — asume experiencia previa de programación, usar los términos directo.
   Un senior puede querer poca explicación de tradeoffs (modo directo) pero igual que no se le defina jerga sin pedirlo; alguien nuevo puede querer avanzar rápido pero necesitar que los términos se aclaren. No asumir uno en función del otro.

Si eligió "sin guía de decisiones", antes de preguntar (2) y (3), pregunta aparte:

"¿Igual quieres que arme la estructura de documentación viva del proyecto, o que resolvamos un bloque puntual?"
- Sí, arma la estructura de documentación viva
- Quiero resolver solo un bloque puntual
- No, nada — no uses la skill

Si la respuesta es "no, nada", termina ahí — no se preguntan verbosidad ni idioma. En cualquier otro caso, sigue con (2) y (3).

### Si es existente

No investigues el código todavía. Pregunta primero:
- Qué stack/arquitectura ya tiene.
- Qué decisiones importantes ya están tomadas.
- Qué le preocupa ahora o qué necesita resolver para seguir.
- Si ya existe documentación (`DOC/`, `CLAUDE.md`, README) que debas leer antes.

Con esas respuestas — y esa documentación si existe — ubica en qué bloques del mapa de dependencias el proyecto ya tiene resuelto y cuáles quedan abiertos, y continúa el flujo desde ahí, sin repetir bloques ya resueltos.

**Cómo se hace el mapeo:** recorre los 13 bloques en silencio (no uno por uno en voz alta) y clasifica cada uno en cuatro estados, según lo que ya dijo el usuario y la documentación existente:
- **Resuelto** — se infiere con confianza de lo dicho o de la documentación.
- **Parcial** — hay algo, pero falta un dato bloqueante puntual de ese bloque.
- **Abierto** — sin señal, se trata como un bloque de proyecto nuevo.
- **Cambiar** — el usuario indica que quiere revisar una decisión ya tomada (no solo llenar un vacío, ej. "antes era monolito, ahora queremos separarlo").

Antes de continuar, presenta un resumen corto — nunca asumas en silencio: "Por lo que me contaste, esto ya está resuelto: [lista]. Esto queda parcial o abierto: [lista]. Esto quieres cambiarlo: [lista, si aplica]. ¿Coincide, o hay algo resuelto que no mencioné?" Recién con esa confirmación, sigue el flujo: salta lo resuelto, entra a lo parcial/abierto solo con la pregunta puntual que falta, y para lo marcado "cambiar" registra el delta (decisión anterior → decisión nueva → motivo) en `DOC/cambios-del-plan.md`, con el mismo formato que ya usa ese archivo — no se crea un documento nuevo aparte.

**Excepción — bloque 5 (datos sensibles y legal) nunca se marca "resuelto" solo por inferencia:** por ser bloqueante siempre, incluso en modo rápido, se reconfirma explícito (al menos país/regulación y tipos de datos sensibles) aunque el usuario diga que ya lo tiene resuelto.

Si de todas formas hace falta investigar código porque el usuario no tiene claridad, guarda lo investigado en un documento persistente (`DOC/` o `CLAUDE.md`) para no repetir la investigación en sesiones futuras. Si el usuario tiene el plugin oficial `claude-code-setup` disponible, mencionarlo como complemento opcional (analiza el proyecto de solo lectura y sugiere MCP/skills/hooks/subagentes) — no es obligatorio, es una sugerencia.

Pregunta verbosidad e idioma igual que en el caso "nuevo", salvo que ya consten en documentación existente.

## Transversal — Documentación viva, ADR y guardrails de IA

No es un bloque numerado — se activa justo después del bloque 1 (si el modo elegido no fue "nada"), no al final.

**Estructura de `DOC/` a crear (flat, sin subcarpetas por categoría):**
- `DOC/plan.md` — el plan vivo del proyecto, se llena bloque por bloque con las decisiones tomadas a medida que se avanza. Funciona como el equivalente al PRD del proyecto — no se genera un documento separado para eso, sería duplicar lo mismo. Si el usuario quiere una red de seguridad automática adicional entre sesiones (compresión + búsqueda semántica), se puede mencionar claude-mem como complemento — `DOC/plan.md` sigue siendo el registro oficial curado y legible, claude-mem no lo reemplaza — sugerencia opcional, no obligatoria.
- `DOC/avances.md`, `DOC/errores-y-arreglos.md`, `DOC/cambios-del-plan.md` — bitácoras para la fase de implementación (se empiezan a usar ahí, no durante el descubrimiento). Si hay más de una persona trabajando (bloque 10), dividir estas tres por persona (ej. `DOC/avances-[nombre].md`) en vez de un archivo compartido único — evita que un solo archivo crezca sin control.
  - **`DOC/errores-y-arreglos.md` — regla de deduplicación:** si un error es del mismo tipo que uno ya registrado, no crear una entrada nueva — agregar una ocurrencia numerada (fecha + qué se estaba haciendo) a la entrada existente. Permite ver cuántas veces se repite el mismo error en vez de fragmentar el historial.
  - **`DOC/cambios-del-plan.md` — formato de cada entrada:** fecha, quién lo pidió, archivo(s) afectado(s), qué se pidió exactamente, qué se implementó, y el motivo — no basta con anotar "se cambió X", hay que poder responder por qué después.
  - **Patrones de decisión repetidos:** si el usuario resuelve una misma disyuntiva de la misma forma varias veces (ej. siempre prioriza alcance completo sobre plazo, o siempre prefiere una opción sobre otra ante un mismo tipo de trade-off), documentarlo explícitamente en `DOC/plan.md` o `CLAUDE.md` como criterio ya establecido — no volver a plantear la alternativa descartada como si fuera nueva cada vez.
- `DOC/decisiones.md` (ADR) — se llena automáticamente cada vez que se use el formato "propuesta razonada + confirmar" en cualquier bloque (arquitectura, stack, multi-tenancy, hosting): decisión, alternativas descartadas, motivo, consecuencias. No hace falta pedirlo aparte, es un subproducto de ese formato. Para decisiones de menor impacto que no ameritan ese formato completo, alcanza una entrada liviana de una línea: "Decisión | Razón".
- `DOC/modelo-datos.md` (MER) y `DOC/glosario.md` (vocabulario del dominio, un término = un significado) — del bloque 4, persistidos como documento, no solo en la conversación.
- `DOC/arquitectura.md` — diagrama C4 (Context + Container, en Mermaid) del bloque 6, solo si hay servidor.
- `DOC/pruebas-manuales.md`, `DOC/definition-of-done.md`, `DOC/plan-de-pruebas.md`, `DOC/casos-de-prueba.md` — se crean recién al activarse el bloque 12 (testing), no en el kickoff. Ver ese bloque para el detalle de cada uno.
- `DOC/riesgos.md` — se crea al cierre del kickoff, agregando señales de riesgo ya levantadas en otros bloques (vendor lock-in, datos sensibles, etc.), no con preguntas nuevas.
- `DOC/comandos.md` — cómo instalar dependencias, correr en local, correr tests, hacer build. Lo lee el programador directamente (no solo Claude), por eso es su propio archivo y no una sección dentro de `CLAUDE.md` — `CLAUDE.md` solo lo referencia.
- `DOC/faq.md` — el "por qué" de decisiones clave, en formato pregunta-respuesta corto, para consulta rápida sin abrir `DOC/decisiones.md`. Solo se crea si el usuario acepta la pregunta de abajo.
- `DOC/manual-admin.md` — opcional, solo si el proyecto tiene un panel de administración que alguien no técnico va a operar (distinto de `DOC/comandos.md`, que es para desarrollo).
- `DOC/insumos/` — única carpeta (no archivo) de esta lista: material externo que el usuario ya tenga (un plan en `.md`, un Excel, un PDF, notas) que deba considerarse durante el proceso. Es carpeta y no archivo porque puede haber cualquier cantidad de archivos sueltos de formatos distintos — el resto de `DOC/` se mantiene flat porque la mayoría de estos documentos ni siquiera llegan a crearse en un proyecto chico (se disparan bloque por bloque, no todos existen siempre). Preguntar al crear la estructura: "¿Tienes algún documento externo ya armado que deba tener en cuenta? Puedes dejarlo en `DOC/insumos/` o decirme la ruta." Revisar esta carpeta al inicio y cada vez que se retome el proyecto. Si el formato no se puede leer directo (ej. un Excel sin exportar), avisar y pedir que se exporte a texto/CSV en vez de asumir su contenido.
- **Si el proyecto pivota fuerte** (no un ajuste menor — termina una etapa completa y arranca una totalmente distinta, ej. "ya está la primera versión funcionando, ahora entra un plan aparte de seguridad y monetización"): en vez de seguir amontonando todo en el mismo `plan.md`, abrir un set de documentos nuevo (ej. `DOC/plan-v2/`) y que `CLAUDE.md` actúe de router explícito ("si trabajas en tal tema, lee este set; si es tal otro, lee este otro").

**Pregunta temprana — FAQ con el porqué de las decisiones:** "¿Quieres que mantenga `DOC/faq.md` con el *por qué* de las decisiones clave a medida que se toman, para consulta rápida?" Se pregunta una sola vez, no decisión por decisión. Si acepta, se llena en paralelo cada vez que se cierra una decisión relevante (mismo momento en que se actualiza `DOC/decisiones.md`).

**Guardrails de IA → `CLAUDE.md`** (en la raíz del repo, Claude Code lo lee automáticamente; mantenerlo corto, referenciando los `DOC/*.md` en vez de contener su contenido):
- Preguntar temprano, junto al bloque 1: "¿Hay algo que la IA nunca debería hacer sin tu aprobación explícita en este proyecto? (ej. tocar producción, eliminar datos, hacer pagos reales, enviar correos reales a usuarios)." Default si no responde: producción y eliminación de datos siempre piden aprobación.
- **Guardrails de disciplina de alcance** (categoría distinta a la anterior — no son acciones que requieren aprobación, son límites de comportamiento siempre activos): nunca inventar nombres de rutas/tablas/columnas que no estén documentados en `DOC/modelo-datos.md` o el código; nunca sugerir cambiar el stack ya confirmado (bloque 7) sin justificación explícita; nunca agregar una dependencia nueva sin que resuelva una necesidad concreta del plan.
- `CLAUDE.md` se genera/actualiza al cerrar el bloque 11, con estos guardrails, referencias a `DOC/comandos.md` y `DOC/faq.md` (si existen), y lo ya decidido en el bloque 10 (quién hace los commits, mención de IA en commits).
- **Según la respuesta del bloque 10 (pregunta 1.6):** si todos usan Claude Code, se genera solo `CLAUDE.md`. Si hay quienes usan otra herramienta de IA (Cursor, Antigravity, Copilot, Gemini CLI, etc.), los guardrails se escriben en `AGENTS.md` (el estándar que leen nativamente la mayoría de esas herramientas) y `CLAUDE.md` queda como puntero corto ("ver `AGENTS.md`, Claude Code no lo lee de forma nativa todavía") en vez de duplicar contenido.
- **Cuando se corrige un bug de un patrón ya documentado** (ej. en `DOC/plan.md`, `references/*.md`, o un patrón de código de referencia): reflejar la corrección directamente en la documentación del patrón, no solo registrarla en `DOC/errores-y-arreglos.md` — así queda imposible repetir el mismo error por seguir la referencia desactualizada.

**Pregunta de cierre — hooks como aplicación automática (no solo prompt):** al generar `CLAUDE.md`/`AGENTS.md`, antes de preguntar, explica qué es un hook y por qué importa — ajustado a los ejes del bloque 1 (verbosidad y nivel de tecnicismo), igual que cualquier otro término técnico de la skill:
- **Modo aprendizaje, o nivel de tecnicismo "explicar siempre"/"solo lo poco común"** (un hook no es jerga común): explicar antes de preguntar, por ejemplo — "Un hook es una regla de Claude Code que se ejecuta sola en un momento específico (ej. antes de guardar un archivo, antes de un commit) y puede bloquear la acción si no se cumple. Es distinto de escribirlo en `CLAUDE.md`/`AGENTS.md`: eso es una instrucción que la IA sigue, pero podría olvidar en una conversación larga; el hook se aplica siempre, sin depender de que la IA se acuerde."
- **Modo directo con tecnicismo "sin explicar":** saltar la explicación, ir directo a la pregunta.

Pregunta: "¿Quieres que además configure hooks que apliquen estas reglas en automático (ej. bloquear comandos peligrosos, escanear secretos antes de un commit), o prefieres que quede solo como instrucción para la IA?" Si acepta, configurar (vía la skill `update-config`) los hooks cuyos datos ya están disponibles en este punto, filtrando por tamaño (bloque 2) donde corresponda:
- Bloque 1 (acciones que requieren aprobación) → hook `PreToolUse` que bloquea comandos peligrosos (`DROP TABLE`, `rm -rf`, deploy a producción) — siempre, sin filtro por tamaño.
- Bloque 9 (secretos nunca en el código) → hook que escanea archivos staged buscando patrones de API keys/tokens antes de permitir el commit — siempre.
- Bloque 9 (checklist de seguridad mínima, ej. CORS en producción) → hook de lint antes de un comando de deploy — se omite si tamaño = "uso personal o uso ocasional".
- Bloque 10 (formato de commit) → hook que valida el mensaje antes de dejar pasar el commit — siempre.
El candidato del bloque 12 (correr tests automático tras implementar) no se ofrece acá — ese bloque no es parte del kickoff, se ofrece de nuevo cuando se active (ver Bloque 12).

## Bloque 2 — Producto y contexto

**Bloqueantes — en prosa, cada una con alcance acotado:**

1. "¿Qué problema resuelve este proyecto? Descríbelo en un par de frases — no hace falta que menciones quién lo va a usar ni con qué tecnología, eso lo vemos en las siguientes preguntas." (ej. "quiero llevar el control de gastos de mi taller, hoy lo hago en una libreta y se me pierde información")
2. "¿Quién lo va a usar?" (ej. "solo yo", "clientes de mi tienda", "estudiantes y profesores de un colegio")
3. "¿En qué país vas a operar o usar esto principalmente?"

**Regla de callback:** si la persona ya adelanta detalles que corresponden a otro bloque (ej. al responder "quién lo usa" menciona roles como "evaluadores, coordinador, alguien que visualiza"), esa información se guarda pero no se da por resuelta. Cuando se llega al bloque donde ese detalle importa, retómalo explícitamente y pregunta lo específico que falta — no lo vuelvas a preguntar desde cero ni lo asumas cerrado. Ejemplo, en el bloque de auth/roles: *"Me dijiste que iban a usar esto evaluadores, un coordinador y alguien que visualiza. Definamos: ¿qué puede hacer cada uno? ¿hay algo que un evaluador no debería poder ver o modificar?"*

**Bloqueantes — opciones cerradas:**

*Tipo de plataforma* (qué es lo que se está construyendo, no cómo trabaja el usuario con la IA — eso es otro tema aparte):
- **Web** — se usa desde el navegador, sin instalar nada.
- **App móvil** — se instala en el celular (Android/iOS).
- **Escritorio** — programa que se instala en una computadora.
- **PWA** — un sitio web que se puede "instalar" y funciona parecido a una app, pero sigue siendo tecnología web.
- **API o servicio backend** — sin interfaz visual, lo consumen otros programas.
- **CLI** — herramienta de línea de comandos, se usa escribiendo comandos en una terminal, sin ventanas ni botones (ej. `git`, `docker`, `npm`).
- **Otra** — especifica cuál.

*Tamaño/envergadura:*
- **Uso personal o uso ocasional** — lo usa el usuario o pocas personas, sin necesidad de que esté siempre disponible ni de que crezca.
- **Proyecto pequeño, pocos usuarios** — un grupo acotado y conocido (un equipo, un negocio chico).
- **Producto con intención de crecer** — hoy es chico pero la idea es escalar con el tiempo.
- **Ya tiene usuarios reales o escala conocida** — ya hay gente usándolo o un número concreto esperado, no es estimación.

**Modo completo — en prosa:**
- "¿Cuál es el objetivo principal? ¿Cómo vas a saber si funcionó?" (ej. "que la gente deje de perder tickets")
- "¿Hay números concretos que te importe ir mirando en el tiempo para saber si el proyecto va bien? No es lo mismo que el objetivo anterior — acá son señales que se miden de forma repetida, no una sola vez. Ejemplos: una tienda online podría mirar 'ventas mensuales'; un sistema de gestión interno, 'cantidad de tareas completadas a tiempo'. Muchos proyectos personales no necesitan ninguna, y está bien responder 'ninguna'." — se puede saltar directo si el tamaño elegido fue "uso personal o uso ocasional".

## Bloque 3 — Alcance

**Bloqueantes — prosa:**
1. "¿Cuál es la versión mínima que tiene que existir para que este proyecto ya sirva?" (ej. "que pueda registrar un gasto y verlo en una lista, nada de reportes ni gráficos todavía")
2. "¿Qué queda deliberadamente FUERA por ahora? ¿Qué no vas a construir, aunque se te ocurra que podría ser útil más adelante?"

**Bloqueante — funcionalidades de alto impacto, selección múltiple acotada:**
3. "¿El sistema va a incluir algo de esto?" — Pagos o cobros · Notificaciones automáticas (email/SMS/push) · Procesos que tardan o corren en segundo plano (reportes pesados, archivos grandes) · **IA como funcionalidad para los usuarios** (distinto de usar IA como herramienta de desarrollo — esto es que el producto en sí responda preguntas, genere contenido, clasifique, etc.) · Nada de esto. (Estas cuatro cambian decisiones de arquitectura más adelante, por eso se preguntan siempre.) Si marca notificaciones automáticas o integraciones con servicios externos (Slack, email, CRMs), se puede mencionar n8n-mcp como opción para automatizar esos workflows — sugerencia opcional, no obligatoria.

Si marcó "pagos o cobros": "¿Es un modelo de suscripción con distintos planes (lo que técnicamente se llama SaaS), un pago único, u otra cosa?" Si es suscripción, en modo completo (pregunta 4) profundizar: ¿hay período de prueba gratuito? ¿los usuarios pueden cambiar de plan? ¿qué pasa si un pago falla o se cancela la suscripción?

Si marcó "IA como funcionalidad para los usuarios": "¿Qué hace esa parte con IA? (ej. responder preguntas sobre documentos/datos propios, generar contenido, clasificar, resumir, otra cosa)." Si implica responder preguntas sobre documentos o datos propios del usuario (RAG), se puede mencionar LightRAG (framework de recuperación aumentada con grafos + vectores) como opción — sugerencia opcional, no obligatoria. Esto queda como el gate que retoman las preguntas 7.5 y 7.6 del bloque 9 (model routing, límites de costo por usuario/plan) — no se vuelve a preguntar si ya se usa IA, se retoma con callback.

**Completo — resto de funcionalidades, selección múltiple:**
4. "Además de lo anterior, ¿cuáles de estas otras funcionalidades necesita?" — Crear/editar/eliminar registros · Generar reportes o informes · Exportar datos (PDF/Excel/CSV) · Importar datos externos · Otra.

**Completo — reglas de negocio, prosa:**
5. "¿Hay reglas sobre quién puede hacer qué, y bajo qué condiciones? Por ejemplo: ¿alguien necesita aprobar algo antes de que quede confirmado? ¿hay acciones que no se pueden deshacer una vez hechas?"

**Completo — historias de usuario formales**, solo si el tamaño (bloque 2) no fue "uso personal o uso ocasional":
6. "¿Quieres que transformemos la lista de funcionalidades en historias de usuario formales (funcionalidad → quién la usa → para qué), o te basta con la lista?"

**Completo — requisitos con formato testeable (EARS-lite)**, solo si hay necesidad real de trazabilidad (ej. auditoría legal, datos sensibles del bloque 5, o el usuario lo pide): "¿Quieres que las funcionalidades críticas queden en un formato que se pueda convertir directo en un test, tipo 'Cuando ocurre X, el sistema debe hacer Y'? Ej.: 'Cuando el usuario intenta pagar con una tarjeta rechazada, el sistema debe mostrar el error y no confirmar el pedido.' No hace falta para todo, solo lo crítico." No ofrecer esto por defecto — agrega formalidad que la mayoría de proyectos no necesita.

Aplica la regla de callback del bloque 2 (si ya mencionó roles/reglas antes, se retoma, no se repite).

## Bloque 4 — Modelo del dominio

**Alcance:** este bloque llega hasta el modelo conceptual (entidades y relaciones) — no diseña la base de datos física. Campos exactos, tipos de dato, claves y normalización se resuelven después, al implementar.

**Bloqueantes — prosa:**
1. "¿Cuáles son las 'cosas' principales que tu sistema necesita guardar o manejar?" (ej. en un control de gastos: Gasto, Categoría, Usuario)
2. "¿Cómo se relacionan entre sí?" (ej. "un Gasto pertenece a una Categoría y fue creado por un Usuario"). Nota para Claude: si el usuario menciona algo que suena a atributo pero podría ser su propia entidad (ej. "sede", "departamento"), confirmar cuál es — "¿'sede' es algo que necesitas manejar con su propia información (una entidad), o es solo un dato dentro de Evaluador?"

Si el usuario menciona atributos espontáneamente (ej. "nombre, apellido, dirección"), se guardan como referencia para la implementación — no hace falta pedirlos exhaustivamente ni para todas las entidades.

Aplica la regla de callback (roles/cosas ya mencionadas en bloques 2-3 son candidatas a entidad).

**Completo — prosa:**
3. "Para los datos más importantes: ¿de dónde nacen? ¿quién los modifica? ¿se eliminan alguna vez o se guardan para siempre? ¿alguien necesita ver el historial de cambios?"
4. "¿Alguna de estas 'cosas' pasa por etapas o estados a lo largo del tiempo?" (ej. pendiente → pagado → enviado → entregado) — solo si el contexto ya descrito sugiere un proceso con pasos, a criterio de Claude; si no, se omite sin preguntar.

**Persistencia y regla de mantenimiento:** el resultado de este bloque se guarda en `DOC/modelo-datos.md` (MER), no solo en la conversación. Regla permanente para `CLAUDE.md`: cada vez que una migración cree o modifique una tabla, actualizar `DOC/modelo-datos.md` en el mismo cambio — nunca después ni acumulando varias migraciones sin reflejarlas. Un modelo desincronizado de la base real deja de servir.

**Glosario de dominio (`DOC/glosario.md`).** Distinto del modelo de entidades: acá se registra el *vocabulario* — una palabra, un significado, siempre. Si durante la conversación aparecen dos términos que podrían significar lo mismo (ej. "activo" y "vigente" usados para lo mismo) o un término ambiguo, no asumir cuál es el correcto — preguntar cuál usar y fijarlo en el glosario. Regla permanente para `CLAUDE.md`: antes de introducir un nombre nuevo para algo que ya tiene término en el glosario, usar el término existente, no inventar un sinónimo. Sin este registro, es común que el código y la conversación terminen usando varios nombres distintos para la misma cosa.

## Bloque 5 — Datos sensibles y legal

**Bloqueante, siempre — sin excepción, ni siquiera en modo rápido:**

1. Recupera el país ya dicho en el bloque 2 (no se vuelve a preguntar) y confirma: "Dijiste que esto es para [país]. ¿Sabes si hay alguna ley o regulación específica que debas cumplir (protección de datos, datos de menores, facturación electrónica, etc.)? Si no estás seguro, puedo investigar lo básico para tu país — aunque de todas formas te recomiendo confirmarlo con un profesional antes de producción, esto no reemplaza asesoría legal." Si el usuario pide investigar, usa búsqueda web para lo básico y lo deja anotado como referencia, no como asesoría definitiva.
2. "De las entidades que ya definimos, ¿alguna guarda alguno de estos tipos de datos?" (selección múltiple): Datos de menores de edad · Datos de salud · Datos financieros o de pago · Ubicación en tiempo real · Datos biométricos · Ninguno de estos.
3. Si marcó algo distinto de "ninguno de estos": "¿Hay un motivo para guardar estos datos solo por un tiempo limitado, o se guardan indefinidamente? ¿Alguien podría pedir que se eliminen sus datos?"

**Aviso obligatorio** (se muestra si se marcó algo sensible en la pregunta 2): "Esto no reemplaza asesoría legal — si tu proyecto maneja datos de menores, salud o pagos, te recomiendo confirmarlo con un profesional antes de pasar a producción."

**Completo — prosa:**
4. "¿Vas a necesitar pedir consentimiento explícito para recolectar estos datos (ej. checkbox de aceptación, política de privacidad publicada)?"
5. "¿Hay obligaciones de facturación o impuestos relacionadas (ej. boleta electrónica, IVA)?"
6. Si se marcó algo sensible en la pregunta 2: "¿quieres que llevemos un inventario de datos (`DOC/inventario-datos.md`: qué dato, dónde vive, de qué sensibilidad) y, si tu país lo exige, un registro de actividades de tratamiento? Varias legislaciones de protección de datos personales (incluida la chilena, Ley 21.719) exigen tener este registro, no es solo buena práctica." No asumir que aplica sin preguntar — mismo criterio que el resto de este bloque.

Nota de diseño: acá Claude no actúa como abogado — solo levanta la bandera y pregunta si el usuario ya sabe algo (ofreciendo investigar lo básico si lo pide), en vez de intentar saber todas las leyes de todos los países. Nunca se asume que una legislación aplica o no aplica sin preguntar.

Nota de terminología, proyectos de salud: usar "usuario", no "paciente", al referirse a las personas atendidas — es la terminología vigente, no la clínica tradicional.

## Bloque 6 — Arquitectura y paradigma

Lee `references/arquitectura.md` antes de este bloque — tiene el razonamiento completo (qué es monolito/monolito modular/distribuido, heurística, por qué un monolito modular escala, cómo manejar pedidos de microservicios por moda).

**Bloqueantes:**

1. **Compuerta — ¿hay servidor?** Infiere del tipo de plataforma (bloque 2: CLI/Escritorio sin backend → probablemente no; Web/PWA/API → probablemente sí) y confirma con el usuario, no asumas en silencio. Si no hay servidor, se omite la pregunta 2 completa — no aplica.
2. **Monolito / monolito modular / distribuido** (solo si hay servidor). Propone según la heurística de `references/arquitectura.md`, explica por qué, qué alternativa descartó, y pregunta si el usuario está de acuerdo o quiere otra cosa.
3. **Frontend/backend.** Se omite si la plataforma ya lo hace evidente (CLI, API/backend puro). Para el resto: "¿Frontend y backend separados (dos proyectos, se comunican por API) o integrados (un solo proyecto)? Separado da más flexibilidad después, pero suma complejidad desde el día uno. Para tu tamaño, sugiero integrado — ¿de acuerdo, o prefieres separarlos?"

**Completo — con opción de diferir al bloque 7:**

4. "¿Tienes preferencia de paradigma (orientado a objetos, funcional, mixto), o prefieres que lo sugiera según el lenguaje que elijamos en el siguiente bloque?"
5. "¿Definimos ahora una separación básica de capas (interfaz, lógica de negocio, acceso a datos), o prefieres que se resuelva según el framework que elijamos?"

**Diagrama de arquitectura (C4, niveles Context + Container).** Con la arquitectura ya decidida (preguntas 1-3), producir un diagrama Mermaid de dos niveles y guardarlo en `DOC/arquitectura.md`: **Context** (el sistema como caja negra: quién lo usa, con qué sistemas externos habla) y **Container** (cómo se parte en piezas desplegables — frontend, backend, base de datos — y cómo se comunican). No usar niveles Component/Code de C4, son demasiado detalle para esta etapa. Se omite si no hay servidor (bloque 6, compuerta) — un diagrama de contenedores no aporta nada a una app local de un solo proceso.

Nota de alcance: "dónde" vive el servidor (nube, VPS, servidor propio) no se decide acá — eso es bloque 9.

## Bloque 7 — Stack técnico

Lee `references/stack-y-datos.md` antes de este bloque — tiene la heurística completa de lenguaje/framework y tipo de base de datos, y el principio de estable-vs-nuevo.

**Bloqueantes:**

1. "¿Tienes preferencia o experiencia previa con algún lenguaje o framework? ¿Hay alguna restricción (ej. el equipo ya sabe X, o necesita ser compatible con algo que ya tienes)?" Si no tiene preferencia, propone según plataforma (bloque 2) + arquitectura (bloque 6) + dominio (bloque 4), con el mismo formato de propuesta razonada del bloque 6.
2. "Al elegir versiones de lenguaje, framework y librerías, ¿priorizamos estabilidad (versiones LTS o maduras, mejor compatibilidad) o lo más nuevo (últimas funcionalidades, menos probado)?" Esta preferencia aplica desde ahora en adelante, no solo en este bloque — cada vez que se proponga una versión concreta (acá o durante la implementación), decir explícitamente si es la más estable o la más nueva, y por qué.
3. **Tipo de base de datos** — depende de si hay servidor (bloque 6) y de las relaciones entre entidades (bloque 4). Propuesta razonada con alternativa, igual que arquitectura.

**Completo:**
4. "¿Hay restricciones de versión que ya conozcas (ej. compatibilidad con algo que ya usas)?"
5. Nota, no pregunta: una vez elegido el stack, documentar las versiones exactas usadas. Si el usuario usa Claude Code (bloque 10) y quiere sugerencias del ecosistema, se puede mencionar Context7 MCP (Upstash) como opción — trae documentación actualizada y específica de la versión de cada librería a la sesión, en vez de depender del conocimiento de entrenamiento del modelo (que causa APIs alucinadas o deprecadas), reforzando directamente la preferencia estable-vs-nuevo de la pregunta 2. Sugerencia opcional, no obligatoria.

## Bloque 8 — Auth, autorización y multi-tenancy

Lee `references/auth-y-multitenancy.md` antes de la pregunta 5 — tiene las cuatro estrategias de aislamiento multi-tenant y la heurística completa.

**Bloqueantes:**

1. **Compuerta — ¿necesita autenticación?** Se infiere de los roles ya mencionados (bloques 2/4) y se confirma con callback. Ej.: "Me dijiste que esto lo van a usar evaluadores, un coordinador y alguien que visualiza — eso suena a que cada quien necesita iniciar sesión con su propia cuenta. ¿Es así, o alguno de estos roles puede compartir acceso sin login individual?" Considerar también un punto intermedio antes de descartar auth completo: **identificación liviana sin login formal** (la persona ingresa su nombre una vez, queda guardado en el dispositivo, sin contraseña) — válida solo si la app es de distribución privada/cerrada (no publicada, acceso ya restringido de otra forma), nunca para algo público.
2. **Si necesita auth — método:** Email y contraseña / Cuenta de Google u otro proveedor / Ambas / No estoy seguro, que se proponga según el proyecto.
3. **Roles y permisos**, retomando el callback: "Definamos qué puede hacer cada rol: [roles ya mencionados]. ¿Qué puede hacer cada uno? ¿hay algo que uno no debería poder ver o modificar?"
4. **Compuerta multi-tenancy**, con callback a "sede" u organización si se mencionó en el bloque 4: "¿Los datos de una sede deben estar completamente separados e invisibles para otra, o es un mismo conjunto de datos visible según el rol de cada quien?" Si la respuesta es que sí deben estar separados y además el bloque 3 marcó "pagos o cobros" con modelo de suscripción, mencionar la conexión: "esto es justo lo que técnicamente se conoce como un SaaS multi-tenant."

**Completo:**
5. Si multi-tenancy = sí: propuesta razonada de aislamiento (ver `references/auth-y-multitenancy.md`) según cantidad esperada de organizaciones y sensibilidad de los datos (bloque 5).
6. Detalles finos de sesión (expiración, recuperación de contraseña, cierre de sesión, MFA) — solo si hay auth.
7. RBAC/ABAC formal, si los roles de la pregunta 3 resultan complejos.

## Bloque 9 — Seguridad e infraestructura

Lee `references/seguridad-e-infraestructura.md` antes de este bloque — tiene la heurística de hosting/presupuesto, las alternativas a Docker, el detalle de rate limiting y la nota de vendor lock-in.

**Bloqueantes (solo si hay servidor, compuerta del bloque 6):**

1. **Dónde vive el servidor + presupuesto.** "¿Buscas la opción más económica posible (incluso gratis con límites), o tienes margen para algo más robusto?" + propuesta razonada de nube administrada/VPS/servidor propio según tamaño (bloque 2) y presupuesto. Si la opción es "gratis", advertir explícitamente que hay que revisar los límites reales antes de comprometerse. Nota aparte, solo si tamaño (bloque 2) es "uso personal o uso ocasional" y datos sensibles (bloque 5) es "ninguno de estos": se puede mencionar Omniroute (gateway gratuito a 200+ proveedores de IA) como opción de ahorro para el propio desarrollo con IA — nunca sugerirlo si hay datos sensibles o va a producción real, por el tema de privacidad de enrutar prompts a terceros.
2. **Rate limiting**, solo si va a haber endpoints públicos (formulario abierto, API pública, etc.): explicar los dos errores comunes (ver referencia) y preguntar si se planea desde ya o se deja para más adelante.

**Bloqueante, siempre (haya o no servidor):**
3. **Secretos.** "¿Este proyecto va a manejar contraseñas, tokens o llaves de API? Nunca van en el código ni se suben a git." Si ya se eligió dónde vive el servidor (pregunta 1), decir concretamente dónde van los secretos en esa plataforma (Vercel/Supabase/GitHub Actions tienen cada uno su propio lugar — ver referencia), no solo "en variables de entorno" en abstracto. Aplica incluso a apps locales que llaman APIs externas. Si hay más de un secreto o un plan de backups no trivial, llevar el registro en `DOC/gestion-secretos-y-backups.md` (qué existe, dónde, cuándo se rotó/respaldó por última vez) en vez de dejarlo solo en la conversación. **Si un secreto se commitea por error:** avisar de inmediato, no solo revertir el commit — el secreto ya quedó expuesto en el historial de git aunque se revierta, hay que rotarlo.

**Completo:**
4. **Contenedores** — no por defecto, solo si el hosting elegido lo pide o el equipo ya lo usa. Si aplica, mencionar que Docker no es la única opción (Podman, containerd, o directamente sin contenedores si el PaaS elegido lo resuelve solo) — ver referencia.
5. Vendor lock-in — "¿qué tan fácil sería migrarte de este proveedor si en el futuro deja de convenirte?" Se omite si tamaño (bloque 2) = "uso personal o uso ocasional" — no aporta a un proyecto que probablemente nunca cambie de proveedor.
6. Infrastructure as Code — se omite si tamaño (bloque 2) = "uso personal o uso ocasional" o "proyecto pequeño, pocos usuarios". Rara vez hace falta salvo que la infraestructura ya sea compleja o cambie mucho.
7. Threat modeling formal (STRIDE) — se omite salvo que el bloque 5 haya marcado datos sensibles reales o el tamaño (bloque 2) sea "ya tiene usuarios reales o escala conocida". Si aplica, mencionar como opción la herramienta Strix (agente autónomo de pentesting, valida vulnerabilidades con pruebas de concepto reales) — sugerencia opcional, no obligatoria.
7.5. **Solo si en el bloque 3 se marcó "IA como funcionalidad para los usuarios" y hay varios agentes/subagentes para tareas distintas** (retomar con callback, no volver a preguntar si ya usa IA): "¿quieres definir qué modelo usa cada uno (ej. uno más barato para generación simple, uno más capaz para razonamiento complejo)?" Documentarlo en tabla en `DOC/decisiones.md`, con la regla "no cambiar sin justificación explícita" — evita tanto gastar de más como perder calidad.
7.6. **Solo si en el bloque 3 se marcó "IA como funcionalidad para los usuarios" y debe limitarse por usuario o plan** (créditos, tokens): el descuento se hace **antes** de ejecutar la llamada a la IA, con un límite duro (ej. HTTP 429) si no alcanza — nunca confiar en un chequeo posterior a que ya se gastó.
8. **Checklist de seguridad mínima** — nota para Claude, no pregunta uno por uno, pero verificar que se cumpla al implementar (ver `references/seguridad-e-infraestructura.md` para el detalle de cada punto): rate limiting, IP limiting donde corresponda, secretos fuera del código, sanitización de inputs, validación server-side (nunca confiar solo en la del cliente), RLS con deny-by-default (aplica aunque no haya multi-tenancy), cifrado en tránsito (HTTPS siempre) y en reposo para datos sensibles, sesiones con expiración, y CORS configurado explícitamente (nunca `*` en producción para endpoints con datos de usuarios).

## Bloque 10 — Git, ambientes, CI/CD, convenciones de código

Lee `references/git-y-cicd.md` antes de este bloque — tiene la comparación GitHub vs. GitLab y las herramientas de CI/CD.

**Bloqueantes:**
1. "¿Cuántas personas van a trabajar en este proyecto (contándote a ti)?"
1.6. "¿Qué herramienta de IA vas a usar para trabajar en este proyecto — Claude Code, u otra (Cursor, Antigravity, Copilot, Gemini CLI, etc.)? Si hay más de una persona, ¿todos usan la misma?" No depende de la cantidad de personas (pregunta 1) — aplica igual a un proyecto de una sola persona. Determina qué archivo de guardrails se genera al cerrar el bloque 11 — ver Transversal, sección de guardrails.

**Solo si usa Claude Code (aunque sea parcial):** "¿Quieres que te vaya sugiriendo recursos del ecosistema de Claude Code (skills/plugins) cuando calcen con lo que necesitas?" Si acepta, mencionar cuando surja la ocasión (no en un momento fijo): Task Observer (útil si usa esta misma skill en varios proyectos con el tiempo, meta-skill que observa sesiones y sugiere qué convertir en skill nueva) y las colecciones awesome-claude-code (punto de partida si pregunta por más herramientas).
1.5. "¿Quieres seguir una metodología formal de trabajo (Scrum, Kanban), o nada en particular?" Se omite si tamaño (bloque 2) = "uso personal o uso ocasional" y la pregunta 1 de este bloque confirma una sola persona — se asume "ninguna" y se menciona de pasada por si igual la quiere. Si es Scrum, se desbloquea más adelante (cierre del kickoff): Product Goal, organización en sprints con su Sprint Goal, y Definition of Done por sprint además de la general del bloque 12.
2. "¿Dónde va a vivir el repositorio (GitHub, GitLab, otro) y va a ser público o privado?" — si duda entre GitHub/GitLab, usar la comparación de la referencia.
3. "¿Prefieres hacer tú los commits, o que los haga la IA (mostrándote el mensaje antes de confirmar)?"
4. **Inmediatamente después de (3), sin excepción:** "¿Quieres que los commits mencionen el uso de IA (ej. 'Co-authored-by: Claude'), o prefieres que no se mencione?" Nunca se asume. Si en (3) se eligió que la IA haga los commits, esta pregunta se hace ahí mismo, no se deja para después.
4.5. "¿Qué formato de mensaje de commit prefieres?" — **Conventional Commits** (`tipo(scope): descripción`, ej. `feat(login): agregar auth`; habilita changelog/versionado automático, rinde más si hay un flujo de releases formal) / **Gitmoji** (emoji + descripción corta, visual, rápido de escanear) / **Libre** (una frase clara en imperativo, sin prefijo fijo). Los tres son independientes del flujo de branches (pregunta 6) — cualquiera funciona con cualquier estrategia de ramas.
5. **Ambientes** — propuesta razonada según tamaño (bloque 2): "Para tu tamaño, propongo [local + producción / local + staging + producción]. Además, te recomiendo que los tests automatizados usen su propia base de datos, separada de desarrollo y producción — se resetea en cada corrida y evita que una prueba corrompa datos reales. ¿De acuerdo?"

**Completo:**
6. Flujo de branches/gitflow — propuesta razonada según cantidad de personas (pregunta 1). Si es una sola persona, se omite la pregunta y se propone directo "commits directos a main, sin flujo de ramas" — el usuario puede corregir si igual lo quiere.
7. CI/CD — herramienta según dónde vive el repo (ver referencia); "¿configuramos integración continua desde ya, o se deja para más adelante?" Se omite si tamaño (bloque 2) = "uso personal o uso ocasional" — se asume "no por ahora, se agrega si hace falta".
8. Convenciones de nombres — inferido del lenguaje (bloque 7), se confirma.
9. "¿Qué tanto quieres que el código tenga comentarios explicativos?" — Mínimo (default: solo cuando el "por qué" no es obvio, no se explica el "qué") / Moderado (propósito de funciones y bloques principales) / Extenso (para aprender, documentar, o equipos con niveles dispares). Nunca asumir el default en silencio — preguntarlo, porque no todos lo prefieren igual.
10. Identidad de git (autor vs. cuenta que hace push, firma) — nota condicional, solo si hay más de una persona o restricciones de CI/CD.

## Bloque 11 — UX/UI

Lee `references/identidad-visual.md` antes de este bloque — tiene el glosario de estilos, las preguntas guiadas para quien no tiene idea, la matriz visual, y las librerías de iconos/componentes.

**Bloqueante (solo si la plataforma tiene interfaz visual — se omite para CLI y API/backend puro):**
1. "¿Necesita funcionar bien en distintos tamaños de pantalla (celular, tablet, escritorio), o se va a usar siempre en un solo tipo de dispositivo?"

**Identidad visual — flujo de tres pasos (ver referencia para el detalle completo):**
2. Paso 1, preguntas cortas siempre: estilo/referencia, personalidad a transmitir y a evitar, modo oscuro. Si el usuario da una referencia visual real (un sitio o repo concreto), se puede mencionar SkillUI como opción (extrae el sistema de diseño real de esa referencia — colores, tipografía, espaciado — en vez de describirla de oído) — sugerencia opcional, no obligatoria.
3. Compuerta: si no tiene idea clara de estilo, ofrecer explícitamente las preguntas guiadas mencionando la cantidad (7, sin vocabulario técnico) — nunca asumir un estilo en silencio para alguien que pidió ayuda. Si está disponible, se puede mencionar UI UX Pro Max como opción (base de datos curada de estilos/paletas/tipografías para explorar cuando no hay ninguna referencia en mente) — sugerencia opcional, no obligatoria.
4. Paso 3: proponer la matriz visual completa (colores, tipografía, iconos, librería de componentes según el stack del bloque 7) como default razonado — el usuario ajusta lo que quiera, no se pide aprobación campo por campo porque UI es barato de cambiar.
5. Con la matriz ya definida, preguntar el formato de salida: "¿prefieres que arme un prototipo HTML real, o te dejo un prompt de diseño listo para pegar en una herramienta como Figma (First Draft, genera pantallas y se queda ahí para iterar) o v0 de Vercel (genera código React/Tailwind directo)?" — HTML real cuando ya se sabe el stack y sirve de referencia directa; prompt para herramienta cuando se quiere iterar el diseño antes de comprometerse a código, o lo hace otra persona del equipo.

**Completo — preguntas cortas:**
5. "¿Es importante que aparezca en buscadores (SEO), o es una herramienta interna/privada donde no aplica?" — solo si la plataforma es web pública.
6. "¿Hay algún requisito de accesibilidad que conozcas, o aplicamos un nivel básico por default (contraste adecuado, navegación por teclado)?"

**Completo — notas para aplicar como default al implementar, no preguntar una por una:**
7. Estados de UI completos: carga, vacío, error, éxito — no dejarlo solo en el camino feliz (caso real ya anotado: DominioLector no avisaba que estaba cargando).
8. Formularios: error de validación server-side (bloque 9) mostrado de forma clara, no solo en consola.
9. Microcopy: mensajes específicos y con tono adecuado al proyecto, no "Error" genérico.
10. Consistencia: todos los componentes siguen las mismas reglas de la matriz visual (alineación, espaciado, colores, radius) — evitar que cada pantalla parezca de otra app.

## Cierre del kickoff — Desglose en tareas y gestión de riesgos

Último paso antes de implementar, después del bloque 11. Resuelve el mismo hueco que tienen Spec Kit/Kiro/BMAD entre "plan" e "implementar": un plan rico no es lo mismo que trabajo ejecutable.

1. **Carátula del proyecto**, como encabezado de `DOC/plan.md`: nombre, objetivo (retomado del bloque 2), alcance (retomado del bloque 3), fechas si las hay. Consolida lo ya respondido, no se vuelve a preguntar.
2. **Desglose en tareas.** Convertir el plan (bloques 2-11) en unidades de trabajo concretas y secuenciadas, con sus dependencias. Si en el bloque 3 se armaron historias de usuario formales, cada una se parte en tareas; si no, se arma una lista de tareas directamente desde las funcionalidades.
3. **Si se eligió Scrum (bloque 10):** organizar el desglose en sprints. Cada sprint tiene su **Sprint Goal** (objetivo del sprint) que aporta al **Product Goal** (objetivo de fondo de todo el producto, se define una sola vez). La Definition of Done general (bloque 12, cuando se active) puede tener criterios adicionales por sprint — se agregan ahí, no se duplican.
4. **`DOC/riesgos.md`** — no es una batería de preguntas nueva: se arma agregando las señales de riesgo ya levantadas en otros bloques (vendor lock-in del bloque 9, datos sensibles del bloque 5, dependencias externas, lo que sea que haya salido) en una matriz simple de probabilidad/impacto/mitigación. Si en el camino no se levantó ninguna señal de riesgo real, este documento no se fuerza.

## Bloque 12 — Testing (no es kickoff — se activa al empezar a implementar)

Lee `references/testing.md` antes de este bloque — tiene la pirámide de testing, qué hace bueno a un test, y la heurística de ubicación/formato.

**Disparador:** ofrecerlo proactivamente cuando se esté por escribir la primera funcionalidad real (no scaffolding), o si el usuario lo pide antes.

**Bloqueantes:**
1. "¿Qué nivel de testing quieres como mínimo?" — propuesta razonada según tamaño (bloque 2) + criticidad (datos sensibles del bloque 5, pagos del bloque 3), explicando brevemente la pirámide si hace falta.
2. Si hay CI/CD (bloque 10): "¿qué debe pasar obligatoriamente antes de poder mergear/desplegar?"
3. Ubicación/formato de los tests — inferido del stack (bloque 7), se confirma, no se pregunta desde cero.

Si la plataforma (bloque 2) tiene interfaz web y se van a automatizar pruebas E2E, se puede mencionar Playwright MCP (+ el Playwright CLI complementario, ~4x menos tokens vía snapshots YAML) como opción — le da a Claude Code control de navegador real para generar/correr tests, complementa (no reemplaza) las skills `claude-in-chrome`/`run` ya disponibles en este entorno para debug del día a día. Si el debugging de esta etapa involucra procesar logs grandes, se puede mencionar también Headroom (comprime salidas de herramientas 60-95%). Ambas, sugerencia opcional, no obligatoria.

**Completo:**
4. Checklist de pruebas manuales para funcionalidades críticas (ej. login correcto/incorrecto, sesión expirada, sin conexión, doble clic) — se guarda y crece en `DOC/pruebas-manuales.md`.
5. Definition of Done — propuesta razonada, ajustada al tamaño del proyecto — se guarda en `DOC/definition-of-done.md`.
6. "¿Prefieres escribir los tests antes o junto con el código de la funcionalidad (test-first), o después de que ya funciona (test-after)?" — no hay default correcto, es preferencia de flujo de trabajo.
7. **Plan de pruebas funcionales**, solo para proyectos con más de una persona o requisitos de auditoría (bloque 5): documento estratégico en `DOC/plan-de-pruebas.md` — qué se prueba, con qué tipo de prueba, en qué ambientes, quién es responsable. Distinto de la checklist táctica del punto 4: acá se define el enfoque, no los casos concretos.
8. **Planilla de casos de prueba**, formato tabular, en `DOC/casos-de-prueba.md` o como tabla dentro de `DOC/pruebas-manuales.md`: cada caso lleva ID, pasos, **resultado esperado**, resultado obtenido, estado (pasó/falló). **Si un caso falla, el error específico se escribe en la propia fila** (qué exactamente salió mal, no solo "se corrigió, ver solución") — la solución puede vivir en `DOC/errores-y-arreglos.md`, pero el caso de prueba conserva su propio registro de en qué se equivocó, para que quede trazable qué se probó mal y por qué, no solo que ya se arregló.

Nota para Claude, no pregunta: al escribir cualquier test, que sea determinista, independiente, y pruebe comportamiento no implementación (ver referencia). Después de cada implementación, dar siempre el comando exacto para verificar que funciona (ej. `npm run test:unit -- archivo`) — no dejar que el usuario tenga que adivinarlo.

**Hook diferido del cierre del kickoff:** si el usuario aceptó hooks automáticos en la Transversal (guardrails), ofrecer acá el candidato que faltaba por falta de datos en ese momento: "¿Quieres que configure también un hook que corra el comando de verificación automático después de cada implementación, en vez de tener que pedirlo cada vez?" Si no aceptó hooks en su momento, no se ofrece este tampoco — mismo criterio, no insistir con algo ya rechazado.

## Bloque 13 — Producción y operación (no es kickoff — se activa al ir a producción de verdad)

**Disparador:** ofrecerlo cuando el usuario mencione ir a producción, lanzar, o pregunte si el proyecto está listo.

**Bloqueante:**
1. Checklist de producción — repasa rápido lo ya resuelto en bloques anteriores (secretos, HTTPS, seguridad del bloque 9) y pregunta lo que falta: **backups** (frecuencia; advertir que un backup no cuenta hasta que se prueba restaurarlo, no basta con que exista), **plan de rollback** si un deploy falla, **observabilidad mínima** ("¿cómo te enteras si esto se cae?", no solo "¿funciona?"). El plan de backups se convierte en un **procedimiento de respaldo paso a paso** en `DOC/gestion-secretos-y-backups.md` (cómo se ejecuta el respaldo, cómo se restaura, quién lo hace) — no basta con confirmar que existe un backup, tiene que quedar escrito cómo se usa.

**Completo:**
2. RPO/RTO formal (cuánto dato se puede perder, cuánto tiempo tolera estar caído). Se omite si tamaño (bloque 2) = "uso personal o uso ocasional".
3. Runbook básico de incidentes, aunque sea una sola persona en el proyecto.
