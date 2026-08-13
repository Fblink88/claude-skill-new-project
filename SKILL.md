---
name: new-project
description: Guía de descubrimiento conversada para arrancar un proyecto de software nuevo — o retomar uno existente — antes de escribir código. Ayuda a decidir, en orden de dependencia: producto y alcance (problema, usuarios, plataforma, tamaño, MVP, funcionalidades, reglas de negocio), modelo del dominio (entidades y relaciones), datos sensibles y aspectos legales, arquitectura (monolito, monolito modular o distribuido) y paradigma, stack técnico (lenguaje, framework, base de datos), autenticación/autorización/multi-tenancy, seguridad e infraestructura (hosting, secretos, checklist de seguridad mínima), git/ambientes/CI-CD/convenciones de código, identidad visual y UX/UI, y —ya en implementación— testing y checklist de producción (backups, rollback, observabilidad). Pregunta solo lo que bloquea decisiones importantes según el tamaño del proyecto, explica opciones y tradeoffs antes de decidir, y deja todo documentado en DOC/. Úsala cuando el usuario quiera empezar un proyecto de software desde cero, decidir cómo seguir uno ya en marcha, o pedir ayuda para elegir arquitectura/stack/tecnología antes de programar.
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
   - **Modo completo** — Recorremos: producto y contexto, alcance, modelo del dominio, datos sensibles y legal, arquitectura, stack técnico, auth, seguridad e infraestructura, git/CI/CD, UX/UI.
   - **Modo rápido** — Solo lo que bloquea decisiones importantes: qué se construye, país y datos sensibles, arquitectura de alto nivel, stack.
   - **Sin guía de decisiones** — no recorremos bloques.
2. **Verbosidad:**
   - **Modo aprendizaje** — explico opciones y tradeoffs antes de decidir.
   - **Modo directo** — pregunto y avanzamos, sin explicaciones largas.
3. **Idioma:**
   - Español
   - Inglés

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

Si de todas formas hace falta investigar código porque el usuario no tiene claridad, guarda lo investigado en un documento persistente (`DOC/` o `CLAUDE.md`) para no repetir la investigación en sesiones futuras. Si el usuario tiene el plugin oficial `claude-code-setup` disponible, mencionarlo como complemento opcional (analiza el proyecto de solo lectura y sugiere MCP/skills/hooks/subagentes) — no es obligatorio, es una sugerencia.

Pregunta verbosidad e idioma igual que en el caso "nuevo", salvo que ya consten en documentación existente.

## Transversal — Documentación viva, ADR y guardrails de IA

No es un bloque numerado — se activa justo después del bloque 1 (si el modo elegido no fue "nada"), no al final.

**Estructura de `DOC/` a crear:**
- `DOC/plan.md` — el plan vivo del proyecto, se llena bloque por bloque con las decisiones tomadas a medida que se avanza. Funciona como el equivalente al PRD del proyecto — no se genera un documento separado para eso, sería duplicar lo mismo.
- `DOC/avances.md`, `DOC/errores-y-arreglos.md`, `DOC/cambios-del-plan.md` — bitácoras para la fase de implementación (se empiezan a usar ahí, no durante el descubrimiento).
- `DOC/decisiones.md` (ADR) — se llena automáticamente cada vez que se use el formato "propuesta razonada + confirmar" en cualquier bloque (arquitectura, stack, multi-tenancy, hosting): decisión, alternativas descartadas, motivo, consecuencias. No hace falta pedirlo aparte, es un subproducto de ese formato.
- `DOC/insumos/` — carpeta para material externo que el usuario ya tenga (un plan en `.md`, un Excel, un PDF, notas) que deba considerarse durante el proceso.
- `DOC/pruebas-manuales.md` y `DOC/definition-of-done.md` — se crean recién al activarse el bloque 12 (testing), no en el kickoff. Ver ese bloque para el detalle. Mismo nombre que ya se usa para este tipo de material ("insumo"), para no confundirla con `reference/` (que es interno de la skill, no del proyecto del usuario). Preguntar al crear la estructura: "¿Tienes algún documento externo ya armado que deba tener en cuenta? Puedes dejarlo en `DOC/insumos/` o decirme la ruta." Revisar esta carpeta al inicio y cada vez que se retome el proyecto (se suma a lo que ya se revisa en la rama "existente" del bloque 1). Si el formato no se puede leer directo (ej. un Excel sin exportar), avisar y pedir que se exporte a texto/CSV en vez de asumir su contenido.

**Guardrails de IA → `CLAUDE.md`** (en la raíz del repo, Claude Code lo lee automáticamente):
- Preguntar temprano, junto al bloque 1: "¿Hay algo que la IA nunca debería hacer sin tu aprobación explícita en este proyecto? (ej. tocar producción, eliminar datos, hacer pagos reales, enviar correos reales a usuarios)." Default si no responde: producción y eliminación de datos siempre piden aprobación.
- `CLAUDE.md` se genera/actualiza al cerrar el bloque 11, con estos guardrails más lo ya decidido en el bloque 10 (quién hace los commits, mención de IA en commits).

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
3. "¿El sistema va a incluir algo de esto?" — Pagos o cobros · Notificaciones automáticas (email/SMS/push) · Procesos que tardan o corren en segundo plano (reportes pesados, archivos grandes) · Nada de esto. (Estas tres cambian decisiones de arquitectura más adelante, por eso se preguntan siempre.) Si marca notificaciones automáticas o integraciones con servicios externos (Slack, email, CRMs), se puede mencionar n8n-mcp como opción para automatizar esos workflows — sugerencia opcional, no obligatoria.

Si marcó "pagos o cobros": "¿Es un modelo de suscripción con distintos planes (lo que técnicamente se llama SaaS), un pago único, u otra cosa?" Si es suscripción, en modo completo (pregunta 4) profundizar: ¿hay período de prueba gratuito? ¿los usuarios pueden cambiar de plan? ¿qué pasa si un pago falla o se cancela la suscripción?

**Completo — resto de funcionalidades, selección múltiple:**
4. "Además de lo anterior, ¿cuáles de estas otras funcionalidades necesita?" — Crear/editar/eliminar registros · Generar reportes o informes · Exportar datos (PDF/Excel/CSV) · Importar datos externos · Otra.

**Completo — reglas de negocio, prosa:**
5. "¿Hay reglas sobre quién puede hacer qué, y bajo qué condiciones? Por ejemplo: ¿alguien necesita aprobar algo antes de que quede confirmado? ¿hay acciones que no se pueden deshacer una vez hechas?"

**Completo — historias de usuario formales**, solo si el tamaño (bloque 2) no fue "uso personal o uso ocasional":
6. "¿Quieres que transformemos la lista de funcionalidades en historias de usuario formales (funcionalidad → quién la usa → para qué), o te basta con la lista?"

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

## Bloque 5 — Datos sensibles y legal

**Bloqueante, siempre — sin excepción, ni siquiera en modo rápido:**

1. Recupera el país ya dicho en el bloque 2 (no se vuelve a preguntar) y confirma: "Dijiste que esto es para [país]. ¿Sabes si hay alguna ley o regulación específica que debas cumplir (protección de datos, datos de menores, facturación electrónica, etc.)? Si no estás seguro, puedo investigar lo básico para tu país — aunque de todas formas te recomiendo confirmarlo con un profesional antes de producción, esto no reemplaza asesoría legal." Si el usuario pide investigar, usa búsqueda web para lo básico y lo deja anotado como referencia, no como asesoría definitiva.
2. "De las entidades que ya definimos, ¿alguna guarda alguno de estos tipos de datos?" (selección múltiple): Datos de menores de edad · Datos de salud · Datos financieros o de pago · Ubicación en tiempo real · Datos biométricos · Ninguno de estos.
3. Si marcó algo distinto de "ninguno de estos": "¿Hay un motivo para guardar estos datos solo por un tiempo limitado, o se guardan indefinidamente? ¿Alguien podría pedir que se eliminen sus datos?"

**Aviso obligatorio** (se muestra si se marcó algo sensible en la pregunta 2): "Esto no reemplaza asesoría legal — si tu proyecto maneja datos de menores, salud o pagos, te recomiendo confirmarlo con un profesional antes de pasar a producción."

**Completo — prosa:**
4. "¿Vas a necesitar pedir consentimiento explícito para recolectar estos datos (ej. checkbox de aceptación, política de privacidad publicada)?"
5. "¿Hay obligaciones de facturación o impuestos relacionadas (ej. boleta electrónica, IVA)?"

Nota de diseño: acá Claude no actúa como abogado — solo levanta la bandera y pregunta si el usuario ya sabe algo (ofreciendo investigar lo básico si lo pide), en vez de intentar saber todas las leyes de todos los países. Nunca se asume que una legislación aplica o no aplica sin preguntar.

## Bloque 6 — Arquitectura y paradigma

Lee `reference/arquitectura.md` antes de este bloque — tiene el razonamiento completo (qué es monolito/monolito modular/distribuido, heurística, por qué un monolito modular escala, cómo manejar pedidos de microservicios por moda).

**Bloqueantes:**

1. **Compuerta — ¿hay servidor?** Infiere del tipo de plataforma (bloque 2: CLI/Escritorio sin backend → probablemente no; Web/PWA/API → probablemente sí) y confirma con el usuario, no asumas en silencio. Si no hay servidor, se omite la pregunta 2 completa — no aplica.
2. **Monolito / monolito modular / distribuido** (solo si hay servidor). Propone según la heurística de `reference/arquitectura.md`, explica por qué, qué alternativa descartó, y pregunta si el usuario está de acuerdo o quiere otra cosa.
3. **Frontend/backend.** Se omite si la plataforma ya lo hace evidente (CLI, API/backend puro). Para el resto: "¿Frontend y backend separados (dos proyectos, se comunican por API) o integrados (un solo proyecto)? Separado da más flexibilidad después, pero suma complejidad desde el día uno. Para tu tamaño, sugiero integrado — ¿de acuerdo, o prefieres separarlos?"

**Completo — con opción de diferir al bloque 7:**

4. "¿Tienes preferencia de paradigma (orientado a objetos, funcional, mixto), o prefieres que lo sugiera según el lenguaje que elijamos en el siguiente bloque?"
5. "¿Definimos ahora una separación básica de capas (interfaz, lógica de negocio, acceso a datos), o prefieres que se resuelva según el framework que elijamos?"

Nota de alcance: "dónde" vive el servidor (nube, VPS, servidor propio) no se decide acá — eso es bloque 9.

## Bloque 7 — Stack técnico

Lee `reference/stack-y-datos.md` antes de este bloque — tiene la heurística completa de lenguaje/framework y tipo de base de datos, y el principio de estable-vs-nuevo.

**Bloqueantes:**

1. "¿Tienes preferencia o experiencia previa con algún lenguaje o framework? ¿Hay alguna restricción (ej. el equipo ya sabe X, o necesita ser compatible con algo que ya tienes)?" Si no tiene preferencia, propone según plataforma (bloque 2) + arquitectura (bloque 6) + dominio (bloque 4), con el mismo formato de propuesta razonada del bloque 6.
2. "Al elegir versiones de lenguaje, framework y librerías, ¿priorizamos estabilidad (versiones LTS o maduras, mejor compatibilidad) o lo más nuevo (últimas funcionalidades, menos probado)?" Esta preferencia aplica desde ahora en adelante, no solo en este bloque — cada vez que se proponga una versión concreta (acá o durante la implementación), decir explícitamente si es la más estable o la más nueva, y por qué.
3. **Tipo de base de datos** — depende de si hay servidor (bloque 6) y de las relaciones entre entidades (bloque 4). Propuesta razonada con alternativa, igual que arquitectura.

**Completo:**
4. "¿Hay restricciones de versión que ya conozcas (ej. compatibilidad con algo que ya usas)?"
5. Nota, no pregunta: una vez elegido el stack, documentar las versiones exactas usadas.

## Bloque 8 — Auth, autorización y multi-tenancy

Lee `reference/auth-y-multitenancy.md` antes de la pregunta 5 — tiene las cuatro estrategias de aislamiento multi-tenant y la heurística completa.

**Bloqueantes:**

1. **Compuerta — ¿necesita autenticación?** Se infiere de los roles ya mencionados (bloques 2/4) y se confirma con callback. Ej.: "Me dijiste que esto lo van a usar evaluadores, un coordinador y alguien que visualiza — eso suena a que cada quien necesita iniciar sesión con su propia cuenta. ¿Es así, o alguno de estos roles puede compartir acceso sin login individual?"
2. **Si necesita auth — método:** Email y contraseña / Cuenta de Google u otro proveedor / Ambas / No estoy seguro, que se proponga según el proyecto.
3. **Roles y permisos**, retomando el callback: "Definamos qué puede hacer cada rol: [roles ya mencionados]. ¿Qué puede hacer cada uno? ¿hay algo que uno no debería poder ver o modificar?"
4. **Compuerta multi-tenancy**, con callback a "sede" u organización si se mencionó en el bloque 4: "¿Los datos de una sede deben estar completamente separados e invisibles para otra, o es un mismo conjunto de datos visible según el rol de cada quien?" Si la respuesta es que sí deben estar separados y además el bloque 3 marcó "pagos o cobros" con modelo de suscripción, mencionar la conexión: "esto es justo lo que técnicamente se conoce como un SaaS multi-tenant."

**Completo:**
5. Si multi-tenancy = sí: propuesta razonada de aislamiento (ver `reference/auth-y-multitenancy.md`) según cantidad esperada de organizaciones y sensibilidad de los datos (bloque 5).
6. Detalles finos de sesión (expiración, recuperación de contraseña, cierre de sesión, MFA) — solo si hay auth.
7. RBAC/ABAC formal, si los roles de la pregunta 3 resultan complejos.

## Bloque 9 — Seguridad e infraestructura

Lee `reference/seguridad-e-infraestructura.md` antes de este bloque — tiene la heurística de hosting/presupuesto, las alternativas a Docker, el detalle de rate limiting y la nota de vendor lock-in.

**Bloqueantes (solo si hay servidor, compuerta del bloque 6):**

1. **Dónde vive el servidor + presupuesto.** "¿Buscas la opción más económica posible (incluso gratis con límites), o tienes margen para algo más robusto?" + propuesta razonada de nube administrada/VPS/servidor propio según tamaño (bloque 2) y presupuesto. Si la opción es "gratis", advertir explícitamente que hay que revisar los límites reales antes de comprometerse. Nota aparte, solo si tamaño (bloque 2) es "uso personal o uso ocasional" y datos sensibles (bloque 5) es "ninguno de estos": se puede mencionar Omniroute (gateway gratuito a 200+ proveedores de IA) como opción de ahorro para el propio desarrollo con IA — nunca sugerirlo si hay datos sensibles o va a producción real, por el tema de privacidad de enrutar prompts a terceros.
2. **Rate limiting**, solo si va a haber endpoints públicos (formulario abierto, API pública, etc.): explicar los dos errores comunes (ver referencia) y preguntar si se planea desde ya o se deja para más adelante.

**Bloqueante, siempre (haya o no servidor):**
3. **Secretos.** "¿Este proyecto va a manejar contraseñas, tokens o llaves de API? Nunca van en el código ni se suben a git." Si ya se eligió dónde vive el servidor (pregunta 1), decir concretamente dónde van los secretos en esa plataforma (Vercel/Supabase/GitHub Actions tienen cada uno su propio lugar — ver referencia), no solo "en variables de entorno" en abstracto. Aplica incluso a apps locales que llaman APIs externas.

**Completo:**
4. **Contenedores** — no por defecto, solo si el hosting elegido lo pide o el equipo ya lo usa. Si aplica, mencionar que Docker no es la única opción (Podman, containerd, o directamente sin contenedores si el PaaS elegido lo resuelve solo) — ver referencia.
5. Vendor lock-in — "¿qué tan fácil sería migrarte de este proveedor si en el futuro deja de convenirte?"
6. Infrastructure as Code — nota: rara vez hace falta en proyectos chicos/medianos, solo si la infraestructura es compleja o cambia mucho.
7. Threat modeling formal (STRIDE) — nota: casi nunca aplica, solo proyectos con datos muy sensibles (bloque 5) o escala grande. Si aplica, mencionar como opción la herramienta Strix (agente autónomo de pentesting, valida vulnerabilidades con pruebas de concepto reales) — sugerencia opcional, no obligatoria.
8. **Checklist de seguridad mínima** — nota para Claude, no pregunta uno por uno, pero verificar que se cumpla al implementar (ver `reference/seguridad-e-infraestructura.md` para el detalle de cada punto): rate limiting, IP limiting donde corresponda, secretos fuera del código, sanitización de inputs, validación server-side (nunca confiar solo en la del cliente), RLS con deny-by-default (aplica aunque no haya multi-tenancy), cifrado en tránsito (HTTPS siempre) y en reposo para datos sensibles, sesiones con expiración, y CORS configurado explícitamente (nunca `*` en producción para endpoints con datos de usuarios).

## Bloque 10 — Git, ambientes, CI/CD, convenciones de código

Lee `reference/git-y-cicd.md` antes de este bloque — tiene la comparación GitHub vs. GitLab y las herramientas de CI/CD.

**Bloqueantes:**
1. "¿Cuántas personas van a trabajar en este proyecto (contándote a ti)?"
2. "¿Dónde va a vivir el repositorio (GitHub, GitLab, otro) y va a ser público o privado?" — si duda entre GitHub/GitLab, usar la comparación de la referencia.
3. "¿Prefieres hacer tú los commits, o que los haga la IA (mostrándote el mensaje antes de confirmar)?"
4. **Inmediatamente después de (3), sin excepción:** "¿Quieres que los commits mencionen el uso de IA (ej. 'Co-authored-by: Claude'), o prefieres que no se mencione?" Nunca se asume. Si en (3) se eligió que la IA haga los commits, esta pregunta se hace ahí mismo, no se deja para después.
5. **Ambientes** — propuesta razonada según tamaño (bloque 2): "Para tu tamaño, propongo [local + producción / local + staging + producción]. Además, te recomiendo que los tests automatizados usen su propia base de datos, separada de desarrollo y producción — se resetea en cada corrida y evita que una prueba corrompa datos reales. ¿De acuerdo?"

**Completo:**
6. Flujo de branches/gitflow — propuesta razonada según cantidad de personas (pregunta 1).
7. CI/CD — herramienta según dónde vive el repo (ver referencia); "¿configuramos integración continua desde ya, o se deja para más adelante?"
8. Convenciones de nombres — inferido del lenguaje (bloque 7), se confirma.
9. "¿Qué tanto quieres que el código tenga comentarios explicativos?" — Mínimo (default: solo cuando el "por qué" no es obvio, no se explica el "qué") / Moderado (propósito de funciones y bloques principales) / Extenso (para aprender, documentar, o equipos con niveles dispares). Nunca asumir el default en silencio — preguntarlo, porque no todos lo prefieren igual.
10. Identidad de git (autor vs. cuenta que hace push, firma) — nota condicional, solo si hay más de una persona o restricciones de CI/CD.

## Bloque 11 — UX/UI

Lee `reference/identidad-visual.md` antes de este bloque — tiene el glosario de estilos, las preguntas guiadas para quien no tiene idea, la matriz visual, y las librerías de iconos/componentes.

**Bloqueante (solo si la plataforma tiene interfaz visual — se omite para CLI y API/backend puro):**
1. "¿Necesita funcionar bien en distintos tamaños de pantalla (celular, tablet, escritorio), o se va a usar siempre en un solo tipo de dispositivo?"

**Identidad visual — flujo de tres pasos (ver referencia para el detalle completo):**
2. Paso 1, preguntas cortas siempre: estilo/referencia, personalidad a transmitir y a evitar, modo oscuro. Si el usuario da una referencia visual real (un sitio o repo concreto), se puede mencionar SkillUI como opción (extrae el sistema de diseño real de esa referencia — colores, tipografía, espaciado — en vez de describirla de oído) — sugerencia opcional, no obligatoria.
3. Compuerta: si no tiene idea clara de estilo, ofrecer explícitamente las preguntas guiadas mencionando la cantidad (7, sin vocabulario técnico) — nunca asumir un estilo en silencio para alguien que pidió ayuda. Si está disponible, se puede mencionar UI UX Pro Max como opción (base de datos curada de estilos/paletas/tipografías para explorar cuando no hay ninguna referencia en mente) — sugerencia opcional, no obligatoria.
4. Paso 3: proponer la matriz visual completa (colores, tipografía, iconos, librería de componentes según el stack del bloque 7) como default razonado — el usuario ajusta lo que quiera, no se pide aprobación campo por campo porque UI es barato de cambiar.

**Completo — preguntas cortas:**
5. "¿Es importante que aparezca en buscadores (SEO), o es una herramienta interna/privada donde no aplica?" — solo si la plataforma es web pública.
6. "¿Hay algún requisito de accesibilidad que conozcas, o aplicamos un nivel básico por default (contraste adecuado, navegación por teclado)?"

**Completo — notas para aplicar como default al implementar, no preguntar una por una:**
7. Estados de UI completos: carga, vacío, error, éxito — no dejarlo solo en el camino feliz (caso real ya anotado: DominioLector no avisaba que estaba cargando).
8. Formularios: error de validación server-side (bloque 9) mostrado de forma clara, no solo en consola.
9. Microcopy: mensajes específicos y con tono adecuado al proyecto, no "Error" genérico.
10. Consistencia: todos los componentes siguen las mismas reglas de la matriz visual (alineación, espaciado, colores, radius) — evitar que cada pantalla parezca de otra app.

<!-- Bloques 12-13: no son de kickoff, se activan cuando el proyecto se acerca a esa etapa. Con el bloque 11 se completa el flujo de arranque. -->

## Bloque 12 — Testing (no es kickoff — se activa al empezar a implementar)

Lee `reference/testing.md` antes de este bloque — tiene la pirámide de testing, qué hace bueno a un test, y la heurística de ubicación/formato.

**Disparador:** ofrecerlo proactivamente cuando se esté por escribir la primera funcionalidad real (no scaffolding), o si el usuario lo pide antes.

**Bloqueantes:**
1. "¿Qué nivel de testing quieres como mínimo?" — propuesta razonada según tamaño (bloque 2) + criticidad (datos sensibles del bloque 5, pagos del bloque 3), explicando brevemente la pirámide si hace falta.
2. Si hay CI/CD (bloque 10): "¿qué debe pasar obligatoriamente antes de poder mergear/desplegar?"
3. Ubicación/formato de los tests — inferido del stack (bloque 7), se confirma, no se pregunta desde cero.

**Completo:**
4. Checklist de pruebas manuales para funcionalidades críticas (ej. login correcto/incorrecto, sesión expirada, sin conexión, doble clic) — se guarda y crece en `DOC/pruebas-manuales.md`.
5. Definition of Done — propuesta razonada, ajustada al tamaño del proyecto — se guarda en `DOC/definition-of-done.md`.

Nota para Claude, no pregunta: al escribir cualquier test, que sea determinista, independiente, y pruebe comportamiento no implementación (ver referencia).

## Bloque 13 — Producción y operación (no es kickoff — se activa al ir a producción de verdad)

**Disparador:** ofrecerlo cuando el usuario mencione ir a producción, lanzar, o pregunte si el proyecto está listo.

**Bloqueante:**
1. Checklist de producción — repasa rápido lo ya resuelto en bloques anteriores (secretos, HTTPS, seguridad del bloque 9) y pregunta lo que falta: **backups** (frecuencia; advertir que un backup no cuenta hasta que se prueba restaurarlo, no basta con que exista), **plan de rollback** si un deploy falla, **observabilidad mínima** ("¿cómo te enteras si esto se cae?", no solo "¿funciona?").

**Completo:**
2. RPO/RTO formal (cuánto dato se puede perder, cuánto tiempo tolera estar caído).
3. Runbook básico de incidentes, aunque sea una sola persona en el proyecto.
