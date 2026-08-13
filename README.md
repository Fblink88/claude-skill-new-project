# claude-skill-new-project

Skill de Claude Code para arrancar un proyecto de software nuevo — o retomar uno existente — decidiendo arquitectura, stack, seguridad, base de datos, UX y más *antes* de escribir código, en vez de improvisarlo sobre la marcha.

No es un formulario ni un checklist fijo: es una conversación guiada. Pregunta solo lo que bloquea decisiones importantes según el tamaño del proyecto, explica opciones y tradeoffs antes de decidir, y deja todo documentado en `DOC/` a medida que se avanza.

## Cómo funciona

- **`SKILL.md`** orquesta el flujo completo: 13 bloques de decisiones ordenados por dependencia (no se pregunta por base de datos antes de saber qué datos maneja el sistema, por ejemplo), más un tema transversal de documentación viva y guardrails de IA.
- **`reference/*.md`** — contenido de apoyo que se carga solo cuando corresponde (heurísticas de arquitectura, stack, seguridad, identidad visual, etc.), para no sobrecargar la conversación con todo de una vez.
- Al arrancar, se elige el alcance (rápido / completo / sin guía) y el nivel de explicación deseado — no todos quieren el mismo nivel de detalle.

## Los 13 bloques

Ordenados por dependencia: un bloque va antes que otro solo si el segundo no se puede decidir bien sin la respuesta del primero.

**Kickoff (antes de programar):**

1. **Punto de entrada** — proyecto nuevo o existente, alcance, modo de trabajo.
2. **Producto y contexto** — qué se construye, quién lo usa, plataforma, tamaño.
3. **Alcance** — MVP, qué queda fuera, funcionalidades, reglas de negocio.
4. **Modelo del dominio** — entidades y relaciones (sin llegar al diseño físico de base de datos).
5. **Datos sensibles y legal** — país, legislación, datos de menores/salud/pagos. Siempre se pregunta, sin excepción.
6. **Arquitectura y paradigma** — monolito, monolito modular o distribuido; frontend/backend.
7. **Stack técnico** — lenguaje, framework, tipo de base de datos.
8. **Auth, autorización y multi-tenancy** — login, roles, aislamiento entre organizaciones.
9. **Seguridad e infraestructura** — hosting, presupuesto, secretos, checklist de seguridad mínima.
10. **Git, ambientes, CI/CD y convenciones** — repositorio, commits, ambientes, nivel de comentarios en el código.
11. **UX/UI** — identidad visual, estilo, accesibilidad.

**Después, cuando corresponda (no en el kickoff):**

12. **Testing** — se activa al empezar a implementar de verdad.
13. **Producción y operación** — se activa al ir a lanzar: backups, rollback, observabilidad.

Documentación viva (`DOC/plan.md`, `DOC/decisiones.md`, etc.) y guardrails de IA (`CLAUDE.md`) corren en paralelo desde el bloque 1, no son un bloque aparte.

## Instalación

Clonar (o agregar como submódulo) dentro de `.claude/skills/new-project/` en el proyecto donde se quiera usar, o en `~/.claude/skills/new-project/` para tenerla disponible en todos los proyectos.

## Estado

Primera versión completa de los 13 bloques + referencias. Todavía sin probar en un proyecto real.
