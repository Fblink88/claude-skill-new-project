# Arquitectura — referencia para el bloque 6

Se carga solo cuando la conversación llega al bloque 6. Contiene el razonamiento completo detrás de la propuesta de arquitectura — en `SKILL.md` solo va la versión corta.

## Monolito, monolito modular, distribuido — qué significa cada uno

**Monolito (simple).** Todo el código vive en un solo proyecto, se despliega como una sola unidad, generalmente una sola base de datos. Es lo más simple de construir, entender y desplegar.

**Monolito modular.** Sigue siendo un solo proyecto, un solo despliegue — pero organizado internamente en módulos con fronteras claras (ej. módulo Usuarios, módulo Pagos, módulo Reportes) que no se mezclan entre sí. Tiene la disciplina de "cada cosa en su lugar" sin el costo operativo de desplegar y coordinar varios servicios separados. Conviene cuando el dominio tiene varias áreas de negocio bien diferenciadas pero no hay necesidad real de escalar o desplegar esas partes por separado — es el punto dulce para la mayoría de proyectos medianos.

**Microservicios / arquitectura distribuida** ("distribuido" se usa acá como paraguas para microservicios y arquitecturas parecidas, como serverless con muchas funciones separadas). El sistema se parte en varios servicios independientes, cada uno con su propio despliegue —a veces su propia base de datos— que se comunican por red. Conviene de verdad cuando:
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
