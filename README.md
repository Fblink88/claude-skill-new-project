# claude-skill-new-project

Skill de Claude Code para arrancar un proyecto de software nuevo — o retomar uno existente — decidiendo arquitectura, stack, seguridad, base de datos, UX y más *antes* de escribir código, en vez de improvisarlo sobre la marcha.

No es un formulario ni un checklist fijo: es una conversación guiada. Pregunta solo lo que bloquea decisiones importantes según el tamaño del proyecto, explica opciones y tradeoffs antes de decidir, y deja todo documentado en `DOC/` a medida que se avanza.

## Cómo funciona

- **`SKILL.md`** orquesta el flujo completo: 13 bloques de decisiones ordenados por dependencia (no se pregunta por base de datos antes de saber qué datos maneja el sistema, por ejemplo), más un tema transversal de documentación viva y guardrails de IA.
- **`reference/*.md`** — contenido de apoyo que se carga solo cuando corresponde (heurísticas de arquitectura, stack, seguridad, identidad visual, etc.), para no sobrecargar la conversación con todo de una vez.
- Al arrancar, se elige el alcance (rápido / completo / sin guía) y el nivel de explicación deseado — no todos quieren el mismo nivel de detalle.

## Instalación

Clonar (o agregar como submódulo) dentro de `.claude/skills/new-project/` en el proyecto donde se quiera usar, o en `~/.claude/skills/new-project/` para tenerla disponible en todos los proyectos.

## Estado

Primera versión completa de los 13 bloques + referencias. Todavía sin probar en un proyecto real.
