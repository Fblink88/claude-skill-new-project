# Identidad visual — referencia para el bloque 11

Se carga solo cuando la conversación llega al bloque 11. Basado en `DOC/insumo-sistema-visual-ui.md` (28 secciones), triangulado con investigación propia (2026) — ver fuentes al final de cada parte.

## Dos ejes distintos, no mezclar

El insumo original mezclaba esto en una sola lista — separarlo ayuda a preguntar mejor:

- **Eje estético (cómo se ve):** minimalismo, maximalismo/"minimalist maximalism", glassmorphism, liquid glass, claymorphism, neubrutalism/brutalism, flat design, soft UI, spatial UI, retro, futurista.
- **Eje de tono/dominio (qué transmite, según el rubro):** corporativo, SaaS, médico, educativo, financiero, editorial, institucional, juvenil, premium.

Un proyecto combina ambos ejes (ej. "SaaS + minimalista", "médico + soft UI, evitando lo infantil").

## Glosario de estilos estéticos (verificado, 2026)

- **Minimalismo** — quitar todo lo no esencial, mucho espacio en blanco, pocos colores, foco en la función.
- **"Minimalist maximalism"** (tendencia híbrida 2025-2026) — se mantiene limpio y funcional, pero con más personalidad, profundidad y riqueza visual que el minimalismo puro; no es lo mismo que maximalismo clásico (recargado a propósito).
- **Glassmorphism** — elementos translúcidos tipo "vidrio esmerilado", capas con profundidad, el fondo se ve a través de los componentes.
- **Liquid glass** — evolución 2025 del glassmorphism (el rediseño de Apple ese año): además de la transparencia, simula comportamiento óptico real (luz, refracción, bordes que se difuminan), más refinado y realista que el glassmorphism clásico.
- **Claymorphism** — formas suaves, infladas, tipo plastilina 3D; sensación táctil y juguetona.
- **Neubrutalism / brutalism** — a propósito "crudo": grillas rígidas, tipografías marcadas o descuadradas, bordes gruesos, colores saturados sin suavizar. Comunica audacia, no elegancia.
- **Spatial UI** — interfaces pensadas como objetos flotando en un espacio (ligado a computación espacial tipo Vision Pro), poco común fuera de proyectos específicos de esa categoría.
- **Flat design / Material Design / Fluent Design** — estilos "planos" o semi-planos con reglas propias de una marca (Google/Microsoft respectivamente), buena opción cuando se quiere algo probado y coherente sin definir un estilo propio desde cero.

Fuentes (2026): [Zignuts — Neumorphism vs Glassmorphism](https://zignuts.com/blog/neumorphism-vs-glassmorphism), [Pixso — Glassmorphism vs Neumorphism vs Claymorphism](https://pixso.net/articles/glassmorphism-vs-neumorphism-vs-claymorphism/), [Everyday UX — Glassmorphism y Liquid Glass de Apple](https://www.everydayux.net/glassmorphism-apple-liquid-glass-interface-design/), [Superfiles — Spatial UI, Glassmorphism 2.0](https://superfiles.in/ui-ux-design-trends-2026-spatial-glassmorphism.php).

## Paso 1 — preguntas cortas (siempre, para cualquier proyecto con interfaz visual)

1. "¿Tienes en mente algún estilo visual o una app/sitio que te guste como referencia, o no tienes idea todavía?"
2. "¿Qué sensación debe transmitir? ¿Hay algo que definitivamente quieras evitar (ej. que se vea infantil, recargado, muy corporativo)?"
3. "¿Necesitas modo oscuro además del claro, o basta con uno solo?"

## Compuerta — ¿tiene idea o no?

Si en la pregunta 1 la persona no tiene una idea clara (dice "no sé", da una respuesta vaga, o pide ayuda directamente): ofrecer explícitamente profundizar, mencionando la cantidad. Ejemplo: "No hay problema — puedo hacerte 7 preguntas cortas y simples (nada de vocabulario técnico) para ir armando el estilo visual paso a paso. ¿Las hacemos, o prefieres que te proponga algo directo y lo ajustamos después?"

Si dice que sí tiene idea o da una referencia concreta: saltar el paso 2 y que Claude arme la matriz visual directo con eso + los defaults de este documento.

## Paso 2 — preguntas guiadas (solo si la persona pidió ayuda, sin vocabulario de diseño)

1. "¿Tienes un color que te represente o quieras usar como principal (ej. de tu marca/logo), o prefieres que se proponga uno según el tipo de proyecto?"
2. "¿Prefieres pocos colores y mucho espacio en blanco, o algo más colorido y con más elementos visuales?"
3. "¿Buscas algo que se vea más clásico y serio, o más moderno?"
4. "¿Prefieres pantallas con harta información visible de una vez (tipo panel de control), o algo más espaciado y simple?"
5. "¿Te gustan más los bordes rectos y definidos, o las esquinas redondeadas y suaves?"
6. "¿Prefieres una interfaz plana (sin sombras), o con algo de profundidad (sombras suaves, sensación de capas)?"
7. "¿Prefieres que se sienta bien quieta/estática, o con movimiento sutil al interactuar (transiciones, animaciones)?"

Con las respuestas, traducir a un estilo del glosario de arriba (ej. respuestas "pocos colores + espaciado simple + esquinas suaves + con profundidad" → algo cercano a soft UI minimalista) — no pedirle a la persona que elija el nombre del estilo, eso lo hace Claude.

## Paso 3 — Claude propone la matriz visual completa

Con lo del paso 1 (siempre) y el paso 2 (si aplicó), Claude arma la matriz visual (plantilla abajo) completando el resto con defaults razonados según el estilo resuelto + el stack técnico (bloque 7) + la plataforma (bloque 2). El usuario ajusta lo que quiera — todo esto es barato de cambiar después, no se necesita su aprobación campo por campo.

### Plantilla de matriz visual

```
IDENTIDAD — estilo, personalidad, referencias, qué evitar
COLORES — primario, secundario, fondo, superficie, texto, estados (éxito/advertencia/error/info)
TIPOGRAFÍA — familia, jerarquía (títulos/body/labels)
LAYOUT — grid, ancho máximo, márgenes, densidad
ESPACIADO — escala, padding, gap
FORMAS — border radius, bordes, sombras
ICONOS — estilo, biblioteca
COMPONENTES — sistema/librería elegida, justificación
RESPONSIVE — cómo cambia la composición en mobile/tablet/desktop
ANIMACIONES — nivel (ninguna/mínima/moderada/expresiva)
```

## Librerías de iconos (gratis salvo que se indique lo contrario)

- **Lucide** — gratis/open source. Mejor default para proyectos web en 2026, 1500+ iconos, paquetes para React/Vue/Svelte/Angular/Flutter.
- **Phosphor** — gratis/open source. La mayor variedad (9000+ iconos, 6 grosores distintos) — mejor opción si se necesita flexibilidad fina.
- **Heroicons** — gratis/open source. Curada (292 iconos), hecha por el equipo de Tailwind CSS — natural si el proyecto ya usa Tailwind.
- **Tabler Icons** — gratis/open source, 5000+ iconos, licencia MIT.
- **Font Awesome** — tiene versión gratis, pero los iconos y features más completos están en **Font Awesome Pro (de pago)** — la única de esta lista con un tier pagado relevante. Advertir esto si se propone.

Fuentes (2026): [PkgPulse — Lucide vs Heroicons vs Phosphor](https://www.pkgpulse.com/guides/lucide-vs-heroicons-vs-phosphor-react-icon-libraries-2026), [Mantlr — Open Source Icon Libraries](https://mantlr.com/blog/best-open-source-icon-libraries-compared).

## Skills de diseño instalables (ejemplos concretos, ya usados y validados por el usuario)

Si están disponibles en el entorno, se pueden usar en vez de (o junto con) las heurísticas de este documento:

- **`emilkowalski/skill`** — colección de varias skills de diseño/animación: `animation-vocabulary` (vocabulario de animación), `apple-design` (estilo Apple), `emil-design-eng`, `find-animation-opportunities`, `improve-animations`, `pick-ui-library` (elegir librería de componentes), `review-animations`. De Emil Kowalski, conocido en la comunidad de design engineering.
- **`meodai/skill.color-expert`** — asistencia especializada en paletas de color.

## Librerías/sistemas de componentes (gratis salvo que se indique lo contrario)

- **shadcn/ui** — gratis, código que se copia al proyecto (no es una dependencia externa tradicional, se "posee" el código). Default recomendado para proyectos nuevos con React + Tailwind.
- **Radix UI / Base UI** — gratis. Primitivos sin estilo, máximo control y accesibilidad. Nota 2026: Radix fue adquirida por WorkOS y su desarrollo se hizo más lento; **Base UI** (del equipo de MUI) surgió como alternativa activa con el mismo enfoque.
- **Material UI (MUI)** — gratis en su versión core (con componentes premium de pago aparte). Bueno para MVP rápido con diseño ya resuelto (Material Design de Google).
- **Ant Design** — gratis/open source. El más fuerte para aplicaciones enterprise con tablas de datos complejas y formularios extensos.
- **Chakra UI** — gratis/open source. Bueno para iteración rápida y simplicidad.
- **Bootstrap** — gratis/open source. El más veterano, útil si se quiere algo simple sin comprometerse a un framework de JS específico (funciona con HTML/CSS puro también).

**Heurística por defecto:** proyecto nuevo con React + Tailwind (stack común hoy) → shadcn/ui + Lucide. Aplicación con muchas tablas/formularios tipo panel administrativo → Ant Design. MVP rápido sin mucho tiempo para pulir → Chakra UI o MUI. Proyecto sin framework de JS pesado → Bootstrap.

Fuentes (2026): [InspoAI — shadcn vs Radix vs Chakra vs MUI](https://www.inspoai.io/blog/ui-component-library-comparison), [Dualite — Best UI Component Libraries](https://dualite.dev/blogs/best-ui-component-libraries), [adminlte.io — shadcn/ui vs MUI vs Ant Design](https://adminlte.io/blog/shadcn-ui-vs-mui-vs-ant-design/).
