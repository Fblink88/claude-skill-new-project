# Testing — referencia para el bloque 12

Se carga solo cuando la conversación llega al bloque 12 (al empezar a implementar, no en el kickoff).

## La pirámide de testing

Tres niveles, cada uno prueba algo distinto:

- **Unitarias** — prueban una sola pieza (una función, una clase) aislada del resto; lo que esa pieza necesita (BD, otra función, API externa) se simula ("mock"). Rápidas, deberían ser la mayoría.
- **Integración** — prueban que varias piezas funcionen bien juntas (ej. que el código realmente guarde algo en una base de datos de verdad, no simulada). Más lentas, menos cantidad.
- **End-to-end (E2E)** — prueban el sistema completo como lo usaría una persona real. Las más lentas y caras de mantener, se reservan para los flujos más críticos, la menor cantidad.

Forma de pensarlo: muchas unitarias (base ancha) → menos de integración (medio) → pocas E2E (punta), de ahí "pirámide". Invertirla (muchas E2E, pocas unitarias) es un error común — se vuelve lento y frágil.

## Qué hace bueno a un test automatizado (más importante que la cantidad)

- **Determinista** — mismo resultado siempre; si a veces pasa y a veces falla sin cambios, es un test "flaky", no confiable.
- **Independiente** — no depende de que otro test haya corrido antes ni del orden de ejecución.
- **Prueba comportamiento, no implementación** — verifica el resultado correcto, no detalles internos de cómo se logró; así, refactorizar sin cambiar el comportamiento no debería romper el test.

Aplicar esto como default al escribir cualquier test, no solo mencionarlo.

## Ubicación y formato

Casi siempre lo define el lenguaje/framework elegido (bloque 7), no es una elección libre — inferir del stack, mismo criterio que las convenciones de nombres del bloque 10:

- Algunos ecosistemas colocan el test junto al archivo que prueba (ej. `Componente.test.ts` junto a `Componente.ts`).
- Otros usan una carpeta `tests/` separada que espeja la estructura del código (común en Python con `pytest`, en muchos proyectos Ruby/Rails con `spec/`).
- Cuando el framework tiene convención propia fuerte, seguirla — no imponer una estructura genérica encima.

## Nivel de testing según tamaño y criticidad

- Personal/uso ocasional (bloque 2), sin datos sensibles ni pagos → pruebas manuales básicas puede alcanzar, automatizar solo si molesta repetir algo a mano.
- Proyecto con más de un usuario o intención de crecer → al menos unitarias de la lógica de negocio central.
- Datos sensibles (bloque 5) o pagos (bloque 3) → unitarias + integración de lo crítico, y considerar E2E del flujo de pago/datos sensibles específicamente.

## Documentos vivos de este bloque

- `DOC/pruebas-manuales.md` — checklist que crece con cada funcionalidad nueva, se reutiliza antes de cada release.
- `DOC/definition-of-done.md` — criterios estables, se consulta en cada funcionalidad/PR.
