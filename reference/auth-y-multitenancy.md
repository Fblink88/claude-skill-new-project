# Auth y multi-tenancy — referencia para el bloque 8

Se carga solo cuando la conversación llega al bloque 8.

## Cuatro estrategias de aislamiento multi-tenant (solo si el bloque 8 detectó que aplica)

**1. Compartido, mismo esquema, con Row-Level Security (RLS).** Todos los tenants viven en las mismas tablas; cada fila lleva un `tenant_id`, y la base de datos garantiza (vía políticas RLS) que cada consulta solo vea las filas de su propio tenant. Más barato de operar, una sola migración sirve para todos, escala a miles de tenants. Riesgo real: la seguridad depende de que las políticas estén bien implementadas en todas las capas — un bug o un filtro faltante puede filtrar datos entre tenants. Recomendado para la mayoría de proyectos B2B chicos/medianos.

**2. Compartido, esquemas separados.** Misma base de datos, pero cada tenant tiene su propio esquema (como una carpeta separada adentro). Más aislamiento que RLS, exportar los datos de un tenant es más simple — pero las migraciones se corren una vez por esquema, y con muchos tenants la gestión se vuelve pesada. Punto intermedio, para decenas/cientos de tenants.

**3. Bases de datos separadas por tenant.** Cada tenant tiene su propia base de datos completa. Máximo aislamiento, casi imposible que se mezclen datos entre tenants, permite ajustar rendimiento/backups por tenant — pero es caro y difícil de escalar a muchos tenants. Se usa en SaaS de nivel empresarial con datos muy sensibles (financiero, salud, gobierno).

**4. Modelo híbrido.** La mayoría de los tenants comparten esquema con RLS (barato); los clientes grandes o con exigencias de compliance fuertes obtienen una base de datos dedicada. Es el modelo más usado en producción a esta fecha — combina costo bajo con aislamiento fuerte solo donde hace falta.

Fuentes consultadas (2026): [Bytebase](https://www.bytebase.com/blog/multi-tenant-database-architecture-patterns-explained/), [Ali Asghar](https://aliasghar.me/blog/multi-tenant-saas-data-isolation), [Redis](https://redis.io/blog/data-isolation-multi-tenant-saas/), [Kodekx](https://kodekx-solutions.medium.com/saas-tenant-isolation-database-schema-and-row-level-security-strategies-7337d2159066).

## Heurística de propuesta

- **No hay multi-tenancy** (single tenant, la compuerta del bloque 8 dio negativo) → nada de esto aplica, es la mayoría de proyectos personales/pequeños.
- **Pocos tenants esperados, sin datos muy sensibles (bloque 5)** → RLS compartido (opción 1). Default recomendado salvo razón concreta para otra cosa.
- **Decenas o cientos de tenants, se quiere algo más de aislamiento que RLS** → esquemas separados (opción 2).
- **Datos muy sensibles (bloque 5: menores/salud/financiero) y/o pocos tenants "enterprise" con exigencias fuertes de compliance** → base de datos separada (opción 3), al menos para esos tenants puntuales.
- **Mezcla: muchos tenants chicos + algunos grandes o sensibles** → modelo híbrido (opción 4): RLS para la mayoría, base dedicada para los que lo requieran.

Como con arquitectura (bloque 6) y stack (bloque 7): proponer con justificación, decir qué alternativa se descartó y por qué, y dejar que el usuario confirme o corrija.
