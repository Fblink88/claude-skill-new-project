# Stack técnico y base de datos — referencia para el bloque 7

Se carga solo cuando la conversación llega al bloque 7.

## Estable vs. más nuevo — principio general

Siempre declarar explícitamente cuál se está recomendando y por qué, cada vez que se proponga una versión concreta de lenguaje, framework o librería (en este bloque o durante la implementación). Por defecto, ante la duda, priorizar estabilidad (LTS o versión madura ampliamente adoptada) — mejor compatibilidad, menos sorpresas, más documentación y soporte de la comunidad. Ir a lo más nuevo solo si el proyecto necesita una funcionalidad concreta que no existe en la versión estable, y explicarlo. Mismo criterio que con microservicios por moda (bloque 6): no elegir lo último "porque es lo último" sin una razón concreta.

## Heurística de elección de lenguaje/framework (si el usuario no tiene preferencia)

- Según plataforma (bloque 2): web → stack web común; móvil → nativo o multiplataforma según si se necesita rendimiento nativo o rapidez de desarrollo; escritorio → framework multiplataforma salvo integración profunda con el sistema operativo; CLI → lenguaje con buen soporte de librerías de terminal y distribución simple.
- Según arquitectura (bloque 6): monolito simple → framework full-stack que resuelva rápido; monolito modular → uno con buen soporte de organización en módulos; distribuido → uno con buen soporte de comunicación entre servicios.
- Según dominio (bloque 4): reglas de negocio complejas se benefician de lenguajes con tipado fuerte.

## Heurística de tipo de base de datos

- Si no hay servidor (bloque 6): almacenamiento local — SQLite (si hace falta consultar/relacionar datos), archivo simple tipo JSON (si es poco dato sin relaciones), almacenamiento nativo del dispositivo (ej. IndexedDB en web offline).
- Si hay servidor:
  - Entidades muy relacionadas entre sí (bloque 4) → relacional (PostgreSQL, MySQL) — integridad referencial, consultas complejas.
  - Datos poco relacionados, estructura variable entre registros → documento (MongoDB y similares).
  - Lecturas/escrituras muy rápidas, datos simples tipo llave-valor (caché, sesiones, contadores) → key-value (Redis).
  - Relaciones complejas tipo red (recomendaciones, conexiones) → grafo.
  - Búsqueda por similitud semántica (IA/embeddings) → vectorial.
- Es común combinar más de un tipo (ej. PostgreSQL para datos principales + Redis para caché/sesiones) — no forzar una sola tecnología para todo.
