# Arquitectura — referencia para el bloque 6

Se carga solo cuando la conversación llega al bloque 6. Contiene el razonamiento completo detrás de la propuesta de arquitectura — en `SKILL.md` solo va la versión corta.

## Monolito, monolito modular, distribuido — qué significa cada uno

**Monolito (simple).** Todo el código vive en un solo proyecto, se despliega como una sola unidad, generalmente una sola base de datos. Es lo más simple de construir, entender y desplegar.

**Monolito modular.** Sigue siendo un solo proyecto, un solo despliegue — pero organizado internamente en módulos con fronteras claras (ej. módulo Usuarios, módulo Pagos, módulo Reportes) que no se mezclan entre sí. Tiene la disciplina de "cada cosa en su lugar" sin el costo operativo de desplegar y coordinar varios servicios separados. Conviene cuando el dominio tiene varias áreas de negocio bien diferenciadas pero no hay necesidad real de escalar o desplegar esas partes por separado — es el punto dulce para la mayoría de proyectos medianos.

**Microservicios / arquitectura distribuida.** El sistema se parte en varios servicios independientes, cada uno con su propio despliegue —a veces su propia base de datos— que se comunican por red. Distinto de serverless/FaaS (ver más abajo, "Patrones adicionales"): ahí cada función se despliega y escala por separado sin administrar servidores; acá cada servicio sigue siendo una aplicación tradicional que alguien despliega y opera. Conviene de verdad cuando:
- Partes del sistema tienen necesidades de escala muy distintas entre sí (ej. procesamiento pesado de video vs. servir un login), y separar permite escalar solo lo que hace falta.
- Equipos grandes y distintos necesitan desplegar sus partes sin coordinarse con todos los demás.

Costo real que casi nunca se menciona: más infraestructura (cada servicio necesita su propio pipeline), llamadas de red que pueden fallar y hay que manejar, más difícil de debuggear (el problema puede estar en cualquier servicio o en la red entre ellos), y generalmente hace falta gente dedicada a mantener esa infraestructura. No usar microservicios solo porque "es más escalable" o porque está de moda — casi ningún proyecto nuevo lo necesita desde el día uno.

## Compuerta previa: ¿hay servidor?

Antes de proponer nada de lo anterior, hay que saber si el proyecto tiene algún componente que corra en un servidor. Si todo corre localmente en el dispositivo del usuario (ej. una app de escritorio sin conexión, un CLI que no llama a nada remoto), la pregunta de monolito/modular/distribuido **no aplica** — no hay nada que distribuir ni réplicas que balancear.

Esto suele inferirse del tipo de plataforma (bloque 2): CLI o Escritorio sin mención de backend → probablemente sin servidor; Web, PWA o API → casi seguro que sí. Se confirma con el usuario, no se asume en silencio.

**Nota de alcance:** este bloque solo determina *si hay servidor*. *Dónde* vive ese servidor (nube, VPS, servidor propio) se resuelve después, en el bloque 9 (infraestructura), ya con el stack técnico definido.

## Heurística de propuesta (solo si hay servidor)

- Tamaño personal/pequeño (bloque 2) + dominio simple, pocas entidades (bloque 4) → **monolito simple**.
- Dominio con varias áreas de negocio diferenciadas, pero sin necesidad de escalar o desplegar partes por separado → **monolito modular**.
- Escala ya conocida (bloque 2: "ya tiene usuarios reales o escala conocida") **y** necesidad real de escalar partes de forma distinta, o equipos grandes trabajando en paralelo → **distribuido**. Poco frecuente, se justifica con más detalle.

## Por qué un monolito modular sí puede escalar

Un monolito (modular o no) puede escalar horizontalmente: correr varias réplicas detrás de un balanceador de carga — no es exclusivo de microservicios. La condición es que sea "stateless" (no guarde estado en memoria local entre peticiones), para que cualquier réplica pueda atender cualquier petición.

El límite real casi nunca es "el monolito no aguanta" — normalmente la base de datos se vuelve el cuello de botella primero, o aparece una parte específica del sistema con necesidades de escala muy distintas al resto. Ahí recién tiene sentido separar *esa pieza puntual*, no todo el sistema de una vez. La ventaja concreta de que ya sea modular: cuando ese momento llega, separar un módulo con fronteras claras es mucho más fácil que separar un monolito desordenado.

**Nota técnica para cuando se escale horizontalmente (relevante en el bloque 9 — seguridad e infraestructura):** cualquier estado que deba ser consistente entre réplicas (ej. contadores de rate limiting) necesita vivir en un almacén compartido (ej. Redis), no en memoria local de cada instancia — si no, el límite efectivo termina siendo "el límite configurado × cantidad de réplicas", porque cada una cuenta por su cuenta sin saber de las otras. Además, el rate limiting conviene aplicarlo antes de que la petición llegue a la aplicación (proxy, load balancer, API gateway, CDN) — si se rechaza dentro del código de la app, ya se gastó casi todo el costo de atender la petición solo para decir que no.

## Manejo de la "moda" de microservicios

Si el usuario pide microservicios solo porque están de moda o porque se los pidieron sin una razón concreta de escala/equipo, explicar el tradeoff (arriba) y ofrecer monolito modular como alternativa. Si el usuario insiste después de escuchar el argumento, se respeta su decisión — es su proyecto, no se le impone nada.

## Patrones adicionales (por trigger, no por defecto)

Estos cuatro no entran en la heurística principal de arriba — cada uno se activa solo si aparece la señal concreta que lo justifica (ver bloque 6 en `SKILL.md` para el trigger exacto de cada uno). Ofrecerlos sin esa señal agrega opciones que la mayoría de proyectos no necesita evaluar.

### Serverless / FaaS (Función como Servicio)

Cada función se despliega y ejecuta por separado — la plataforma la corre solo cuando llega una petición (AWS Lambda, Vercel Functions, Cloudflare Workers, Supabase Edge Functions) — en vez de mantener un servidor corriendo todo el tiempo. Se paga por invocación/tiempo de ejecución, no por servidor encendido.

**Conviene cuando:** tráfico esporádico o impredecible (picos raros, mucho tiempo sin uso), el equipo no quiere o no puede administrar infraestructura, o el stack elegido ya lo hace el camino natural (ej. Next.js desplegado en Vercel).

**Costo real:**
- **Cold starts** — la primera invocación después de estar inactiva tarda más, puede notarse en la experiencia del usuario.
- **Límite de tiempo de ejecución** por invocación — no sirve para procesos largos sin rediseñarlos (dividirlos, usar colas).
- **Debugging más difícil** que un servidor tradicional — los logs quedan repartidos por invocación en vez de un flujo continuo.
- **Vendor lock-in fuerte** — el código termina acoplado a las particularidades de la plataforma (cómo maneja el contexto de ejecución, límites, formato de eventos); migrar a otro proveedor casi siempre implica reescribir partes.

**Distinto de "distribuido":** un proyecto puede ser 100% serverless siendo chico y sin ningún equipo grande detrás — no es lo mismo que la decisión de microservicios, que se justifica por escala o coordinación de equipos.

### Event-Driven Architecture

Los componentes no se llaman directo entre sí — publican eventos ("pedido creado", "pago confirmado") en una cola o bus (RabbitMQ, Kafka, SQS, o algo tan simple como una tabla outbox en la misma base de datos), y otros componentes reaccionan a esos eventos de forma desacoplada, sin saber quién los generó.

**Conviene cuando:** una acción dispara varias reacciones que no necesitan ocurrir en el mismo instante ni bloquear al usuario esperando que todas terminen (ej. un pago confirmado dispara actualizar inventario + enviar email + generar factura, y el usuario no necesita esperar a que las tres terminen para ver "listo"), o cuando distintas partes del sistema —posiblemente microservicios separados— necesitan enterarse de cambios sin acoplarse directamente entre sí.

**Costo real:**
- Más difícil seguir el flujo completo de una operación — ¿qué reacciona a qué? Hace falta buena observabilidad para no perderse.
- Duplicar o perder un evento es un problema real que hay que diseñar explícitamente (idempotencia, reintentos) — no es automático.
- Suma una pieza de infraestructura más (la cola/bus) que hay que mantener y monitorear, si se usa una externa.

**No hace falta infraestructura dedicada para "sentirse" event-driven a chica escala:** un monolito puede emitir y reaccionar a eventos en memoria o con una tabla outbox en la misma base de datos, sin sumar una cola externa — reservar Kafka/RabbitMQ para cuando el volumen o el desacople entre servicios realmente lo justifique.

### Microkernel (patrón de plug-ins)

Un núcleo mínimo con la lógica esencial, y el resto de la funcionalidad vive en plug-ins que se conectan a través de puntos de extensión bien definidos. Ejemplos reales: editores de código, IDEs, CMS como WordPress, navegadores con extensiones.

**Conviene cuando:** el proyecto necesita que terceros (u otros equipos internos) agreguen funcionalidad sin tocar ni redesplegar el núcleo, o se anticipa que partes del comportamiento van a variar mucho por cliente/instalación.

**Costo real:** diseñar una buena API de extensión desde el principio es difícil y cuesta más que no tenerla — si se define mal, los plug-ins terminan rompiéndose con cada cambio del núcleo. No conviene si no hay una necesidad real y ya visible de extensibilidad por terceros — es fácil sobre-diseñar "por si acaso".

### SOA (arquitectura orientada a servicios)

Predecesor de los microservicios — el sistema se parte en servicios de negocio, pero de grano más grueso que microservicios típicos, coordinados a menudo por un bus de servicios central (ESB) que maneja ruteo, transformación de mensajes y orquestación entre ellos.

**Conviene cuando:** hay que integrarse con sistemas empresariales o legacy ya existentes (ERPs, sistemas de terceros con contratos SOAP/XML) que no se pueden modificar y que ya hablan ese protocolo — es la realidad de muchas integraciones corporativas, no una elección de arquitectura de cero.

**Costo real:** el ESB central es un punto único de falla y cuello de botella si no se dimensiona bien, y la industria se movió a microservicios hace años — para un proyecto nuevo sin necesidad de integración legacy, elegir SOA agrega la complejidad de una era anterior sin el beneficio que la justificaba.
