# Seguridad e infraestructura — referencia para el bloque 9

Se carga solo cuando la conversación llega al bloque 9.

## Presupuesto y "gratis" engañoso

Antes de proponer hosting, preguntar presupuesto/tolerancia a costo. Si la opción elegida es gratuita o de "free tier", advertir explícitamente que hay que revisar los límites reales (zona geográfica disponible, capacidad, tiempo del free tier, qué pasa al superarlo) antes de comprometerse — un servicio "gratis" de nombre puede resultar impracticable en la práctica. No basta con el nombre del plan.

## Dónde vive el servidor — heurística

- **Tamaño personal/pequeño (bloque 2), sin experiencia previa de infraestructura** → PaaS/hosting administrado (ej. Vercel, Netlify, Railway, Render, Fly.io) — deploy simple, menos control pero mucho menos trabajo operativo.
- **Se necesita más control, presupuesto ajustado, algo de experiencia técnica** → VPS (ej. DigitalOcean, Linode, Hetzner) — más barato que un PaaS a escala, pero más trabajo manual de mantenimiento.
- **Escala grande ya conocida (bloque 2) o requisitos específicos de compliance/tráfico** → proveedor cloud grande (AWS/GCP/Azure) con sus servicios administrados.
- **Restricciones legales de dónde deben vivir los datos (bloque 5), o ya existe infraestructura propia** → servidor propio / on-premise.

### PaaS conocidos — diferenciadores (ejemplos, no la lista completa)

No limitarse a uno o dos nombres — hay varias opciones típicas dentro de "hosting administrado", cada una con un perfil distinto:

- **Vercel** — hecho por los creadores de Next.js, mejor experiencia y soporte de features nuevas si el stack (bloque 7) usa mucho renderizado en servidor (SSR). Plan gratuito (Hobby) bueno para empezar; el plan Pro cobra por asiento ($20/desarrollador/mes + uso), sale caro con equipos grandes.
- **Netlify** — más orientado a sitios estáticos/de contenido, con herramientas incluidas por defecto (formularios, identidad de usuarios, observabilidad) que en otros lados se cobran aparte. Precio de equipo plano ($20/mes por todo el equipo en Pro), conveniente si son varias personas.
- **Railway** — pensado para backends completos con servidor persistente y base de datos incluida, no solo frontend estático/serverless; precio pay-as-you-go según uso real.
- **Render** — alternativa directa a Heroku, soporta servicios web, sitios estáticos, cron jobs y bases de datos; tiene free tier pero los servicios gratuitos se "duermen" con inactividad.
- **Fly.io** — corre máquinas virtuales reales cerca de los usuarios (edge), útil si el proyecto necesita procesos persistentes o websockets, más control que plataformas puramente serverless.
- **Heroku** — el PaaS original, sigue existiendo, ya no tiene free tier y quedó más caro que las alternativas más nuevas, pero sigue siendo simple de usar.

**Heurística:** stack con mucho SSR/framework tipo Next.js → Vercel. Sitio mayormente estático, equipo de varias personas, se busca precio plano → Netlify. Backend con servidor y base de datos que necesita estar siempre corriendo → Railway o Render. Necesita procesos persistentes/websockets con baja latencia global → Fly.io. Esta lista no es exhaustiva — hay más opciones según el stack y la región; usarla como punto de partida, no como las únicas alternativas.

Fuentes (2026): [MakerKit — Vercel vs Netlify Pricing](https://makerkit.dev/pricing-calculator/vercel-vs-netlify), [Netlify vs Vercel — Netlify](https://www.netlify.com/guides/netlify-vs-vercel/), [FocusReactive — Vercel vs Netlify](https://focusreactive.com/vercel-vs-netlify-how-to-pick-the-right-platform/).

## Contenedores — Docker y alternativas

Docker no es la única opción, aunque sea la más conocida. Antes de proponer, considerar:

- **Docker** — el más extendido, mejor documentación y soporte de herramientas, favorito para desarrollo local.
- **Podman** — sin demonio en segundo plano (más seguro), rootless, compatible con los mismos comandos que Docker (`podman` reemplaza a `docker` en casi todo). Preferido en pipelines de CI/CD por temas de seguridad.
- **containerd** — el runtime de bajo nivel que usan tanto Docker como Kubernetes por debajo; rara vez se interactúa con él directamente salvo en configuraciones más avanzadas.
- **Sin contenedores, dejar que la plataforma se encargue** — muchos PaaS (Railway, Render, Heroku) detectan el proyecto y lo empaquetan automáticamente (buildpacks/Nixpacks) sin necesidad de escribir un Dockerfile. Válido y más simple si no hay una razón concreta para necesitar control fino del entorno.

Fuentes (2026): [Spacelift — Docker Alternatives](https://spacelift.io/blog/docker-alternatives), [daily.dev — Docker vs Podman](https://daily.dev/blog/docker-vs-podman-container-runtime-which-to-use/), [EITT — Docker vs Podman vs containerd](https://eitt.academy/knowledge-base/docker-vs-podman-vs-containerd-comparison-2026/).

**Regla general (no solo para contenedores):** no usar contenedores por defecto si el proyecto no los necesita — igual que con microservicios (bloque 6), evitar por moda o porque "es lo profesional".

### Secretos en contenedores self-hosted (Docker Swarm / Kubernetes)

Si el proyecto se despliega self-hosted con contenedores (no en un PaaS administrado), no usar variables de entorno para credenciales — usar el mecanismo nativo de secretos del orquestador, que las monta como **archivo**, no como variable:

- **Docker Swarm** — `docker secret`: se cifra en el log interno de Swarm (Raft) en reposo, viaja cifrado entre nodos (TLS), se monta como archivo en memoria (`/run/secrets/<nombre>`), nunca aparece en `docker inspect` ni se hereda por procesos hijos. Además es **inmutable**: no se edita in-place — para rotar una credencial se crea un secret nuevo, se actualiza el servicio para que apunte a él, y recién ahí se borra el anterior. Es intencional: hace la rotación explícita y auditable.
- **Kubernetes** — tiene su propio objeto `Secret`, también montable como archivo. **Ojo con un error común:** a diferencia de Swarm, los Secrets de Kubernetes **no vienen cifrados por defecto** — solo están codificados en base64 (que no es cifrado, es solo un formato reversible). Hay que activar explícitamente el cifrado en reposo (`encryption at rest`) para que sea equivalente en seguridad a Swarm.
- Por qué importa evitar variables de entorno para esto: quedan visibles en `docker inspect`, las heredan procesos hijos sin pedirlo, y terminan en logs de debug/crash reports con frecuencia — el archivo montado en memoria evita las tres cosas.

Fuentes (2026): [Wiz — Docker Secrets Explained](https://www.wiz.io/academy/container-security/docker-secrets), [OneUptime — Docker Secrets Management](https://oneuptime.com/blog/post/2026-01-30-docker-secrets-management/view), [GitGuardian — Secrets in Docker](https://blog.gitguardian.com/how-to-handle-secrets-in-docker/).

## Rate limiting — los dos errores comunes (anotado desde el bloque 6)

1. **Rate limiting tardío:** si el rechazo ocurre dentro del código de la aplicación (después de que la conexión ya se estableció), se gasta casi todo el costo de atender la petición solo para decir que no. Ponerlo antes de que la petición llegue a la app — proxy, load balancer, API gateway o CDN.
2. **Contador no compartido entre réplicas:** si hay varias instancias del servidor corriendo y cada una lleva su propio contador en memoria local, el límite real termina siendo el configurado multiplicado por la cantidad de réplicas. Se necesita un almacén compartido (ej. Redis) para que el límite sea consistente entre todas las instancias.

## Checklist de seguridad mínima

Se aplica como default al implementar en cualquier proyecto con servidor — no hace falta preguntarlo uno por uno, pero sí verificar que se cumpla. Excepción: si el bloque 5 no detectó nada sensible y el proyecto es muy chico, usar criterio para no sobrearquitecturar la seguridad de un proyecto trivial.

- **Rate limiting** — ver sección arriba.
- **IP limiting** — distinto de rate limiting: no es "cuántas veces puede llamar alguien", es "quién tiene permitido llamar siquiera". Útil sobre todo para paneles de administración o integraciones B2B conocidas, no tiene sentido para endpoints públicos de cara al usuario final (ahí no se sabe de antemano qué IPs son legítimas).
- **Secretos: nunca en el código ni en git.** Dónde van, según la plataforma elegida (bloque 9, pregunta 1): Vercel (Project Settings → Environment Variables), Supabase (vault de secretos / variables de entorno de Edge Functions), GitHub Actions (Settings → Secrets and variables → Actions). El archivo `.env` local siempre en `.gitignore`; dejar un `.env.example` sin valores reales como referencia para quien clone el proyecto.
  - **Matiz importante — archivo vs. variable de entorno, no es lo mismo en todos los casos.** En un **PaaS administrado** (Vercel, Railway, Supabase), lo anterior alcanza: el proveedor ya cifra esas "variables de entorno" en su infraestructura y las inyecta de forma segura, el riesgo de exposición local no aplica igual. Pero si el proyecto es **self-hosted con contenedores** (Docker/Swarm/Kubernetes en un VPS o servidor propio, ver sección de Contenedores abajo), cualquier variable de entorno queda expuesta en `docker inspect`, la heredan procesos hijos, y puede terminar en logs — ahí los secretos deben montarse como **archivo**, no como variable de entorno (ver detalle abajo).
- **Sanitización de inputs** — nunca confiar en lo que llega del cliente tal cual; limpiar/escapar antes de usarlo (previene XSS, inyección).
- **Validación server-side** — toda validación que exista en el cliente (formularios, JS) debe repetirse en el servidor. La validación del cliente es para experiencia de usuario, no para seguridad — un cliente se puede manipular o saltarse.
- **RLS (Row-Level Security)** — no es solo para multi-tenancy (bloque 8, ver `reference/auth-y-multitenancy.md`): aplica como buena práctica general en bases de datos que lo soportan (ej. PostgreSQL/Supabase), con política "deny by default" — nadie ve nada salvo que una política lo permita explícitamente, incluso en proyectos de un solo tenant.
- **Cifrado** — datos en tránsito: HTTPS siempre, sin excepción. Datos sensibles en reposo (bloque 5): considerar cifrado adicional a nivel de campo para lo más crítico (ej. datos de salud, financieros), no confiar solo en el cifrado por defecto de la base de datos.
- **Autenticación con expiración de sesión** — las sesiones no duran para siempre; definir un tiempo de expiración razonable y cómo se renuevan (detalle fino en bloque 8, completo).
- **CORS bien configurado** — el servidor debe rechazar peticiones desde orígenes (dominios) que no sean los explícitamente permitidos. Nunca dejar `*` (cualquier origen) en producción para endpoints que devuelven datos de usuarios — si no, cualquier página puede llamar a la API como si fuera la propia.

## Vendor lock-in

Preguntar qué tan fácil sería migrarse del proveedor elegido si en el futuro deja de convenir (precio, límites, disponibilidad) — no para bloquear la decisión, sino para que quede consciente, igual que con el ejemplo real del usuario con EC2 de Oracle (parecía gratis, resultó limitado por zona/disponibilidad, tuvo que migrar a mitad de camino).
