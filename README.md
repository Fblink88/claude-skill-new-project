# claude-skill-new-project

Skill de Claude Code para arrancar un proyecto de software nuevo — o retomar uno existente — decidiendo arquitectura, stack, seguridad, base de datos, UX y más *antes* de escribir código, en vez de improvisarlo sobre la marcha.

No es un formulario ni un checklist fijo: es una conversación guiada. Pregunta solo lo que bloquea decisiones importantes según el tamaño del proyecto, explica opciones y tradeoffs antes de decidir, y deja todo documentado en `DOC/` a medida que se avanza. Nace de destilar el método usado en un proyecto real ya construido, no de una plantilla teórica bajada de internet — y en el camino, sin buscarlo, terminó pareciéndose a lo que hoy se conoce como *spec-driven development*.

## Cómo funciona

- **`SKILL.md`** orquesta el flujo completo: 13 bloques de decisiones ordenados por dependencia (no se pregunta por base de datos antes de saber qué datos maneja el sistema, por ejemplo), más un tema transversal de documentación viva y guardrails de IA.
- **`reference/*.md`** — contenido de apoyo que se carga solo cuando corresponde (heurísticas de arquitectura, stack, seguridad, identidad visual, etc.), para no sobrecargar la conversación con todo de una vez.
- Al arrancar, además del alcance (rápido / completo / sin guía), se elige por separado: cuánto se explican las opciones antes de decidir, si los términos técnicos necesitan definirse o no (un senior no necesita que le expliquen qué es un webhook; alguien nuevo sí, aunque quiera ir rápido — son ejes distintos), el idioma, y cómo se pide aprobación durante el proceso (todo, solo lo grande, o autónomo).

## Instalación

Clonar (o agregar como submódulo) dentro de `.claude/skills/new-project/` en el proyecto donde se quiera usar, o en `~/.claude/skills/new-project/` para tenerla disponible en todos los proyectos.

## Los 13 bloques

Ordenados por dependencia: un bloque va antes que otro solo si el segundo no se puede decidir bien sin la respuesta del primero. Acá va qué busca resolver cada uno y qué conceptos técnicos toca, para que quede claro de entrada qué se va a cubrir.

**Kickoff (antes de programar):**

1. **Punto de entrada** — si el proyecto es nuevo o ya existe y se quiere definir cómo seguir. Define el alcance de la guía, el modo de trabajo (explicado arriba) y los guardrails de la IA (qué puede hacer sola vs. qué necesita aprobación explícita, ej. tocar producción o borrar datos).
2. **Producto y contexto** — qué problema resuelve, quién lo usa, en qué país opera (relevante para el bloque 5), tipo de plataforma (web, app móvil, escritorio, PWA, API, CLI) y tamaño/envergadura esperada. Es la base de la que dependen casi todas las decisiones siguientes.
3. **Alcance** — MVP, qué queda deliberadamente fuera, funcionalidades (incluye pagos/suscripciones tipo SaaS, notificaciones automáticas, procesos en segundo plano), reglas de negocio, y para quien necesita trazabilidad real (ej. auditoría legal) la opción de formular requisitos críticos en formato testeable estilo EARS.
4. **Modelo del dominio** — entidades y relaciones (sin llegar al diseño físico de base de datos: eso es implementación), más un glosario de vocabulario del dominio para que un mismo concepto no termine con varios nombres distintos a lo largo del proyecto.
5. **Datos sensibles y legal** — si hay datos de menores, salud, financieros o biométricos; qué legislación de protección de datos podría aplicar según el país (nunca se asume, siempre se pregunta); inventario de datos y registro de actividades de tratamiento cuando la ley lo exige.
6. **Arquitectura y paradigma** — si hace falta servidor o no; monolito, monolito modular o arquitectura distribuida (con la heurística real detrás, no la moda de turno); separación frontend/backend; y un diagrama de arquitectura estilo C4 (niveles de contexto y contenedores).
7. **Stack técnico** — lenguaje y framework, si se prioriza estabilidad o lo más nuevo en las versiones, y tipo de base de datos (relacional, documento, key-value, grafo, vectorial) según cómo se relacionan los datos del bloque 4.
8. **Auth, autorización y multi-tenancy** — si hace falta login y con qué método, qué puede hacer cada rol, y si los datos de distintas organizaciones/clientes deben estar completamente separados entre sí (multi-tenancy) y con qué estrategia de aislamiento.
9. **Seguridad e infraestructura** — dónde se hospeda y con qué presupuesto, manejo de secretos (nunca en el código), rate limiting, y una checklist de seguridad mínima (validación de datos, cifrado, CORS, sesiones con expiración, entre otros).
10. **Git, ambientes, CI/CD y convenciones** — dónde vive el repositorio, formato de commits (y si mencionan uso de IA o no), cantidad de ambientes (local/staging/producción), metodología de trabajo si se quiere una formal (Scrum, Kanban), y convenciones de código (nombres, nivel de comentarios).
11. **UX/UI** — estilo visual (con ayuda guiada para quien no tiene ninguna referencia en mente), paleta de colores, tipografía, accesibilidad, y si el resultado se entrega como prototipo real o como prompt para una herramienta de diseño.

**Cierre del kickoff, antes de implementar:** el plan se convierte en un desglose de tareas concretas (organizadas en sprints si se eligió Scrum), y se arma un registro de riesgos agregando las señales ya levantadas en los bloques anteriores.

**Después, cuando corresponda (no en el kickoff):**

12. **Testing** — se activa al empezar a implementar de verdad: nivel de pruebas automatizadas, plan de pruebas y casos de prueba (con su resultado esperado y, si falla, el error específico registrado), pruebas manuales, definition of done.
13. **Producción y operación** — se activa al ir a lanzar de verdad: checklist de producción, respaldos con su procedimiento de restauración probado (no basta con que existan), plan de rollback, observabilidad mínima.

Documentación viva (`DOC/plan.md`, `DOC/decisiones.md`, `DOC/modelo-datos.md`, `DOC/glosario.md`, `DOC/riesgos.md`, entre otros) y guardrails de IA (`CLAUDE.md`) corren en paralelo desde el bloque 1, no son un bloque aparte.
