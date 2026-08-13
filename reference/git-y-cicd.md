# Git y CI/CD — referencia para el bloque 10

Se carga solo cuando la conversación llega al bloque 10.

## GitHub vs. GitLab

- **GitHub** — enfoque modular, ecosistema enorme de acciones reutilizables (GitHub Actions), más simple para empezar. Más popular entre desarrolladores individuales y proyectos open source (81% vs. 36% según encuesta de desarrolladores 2025). Free tier más generoso en minutos de CI.
- **GitLab** — plataforma DevOps integrada de una sola pieza: código, CI/CD, seguridad, registro de paquetes, todo junto de fábrica. Más control y costos predecibles si el CI/CD es crítico, más fuerte en empresas grandes y organismos con requisitos de seguridad/compliance.
- Migrar de uno a otro después no es trivial: la sintaxis y arquitectura de CI/CD son distintas entre ambos, no hay traductor automático (a 2026).

**Heurística:** proyecto individual u open source, se busca simplicidad y buen ecosistema de terceros → GitHub. Equipo dentro de una organización con requisitos de seguridad/compliance fuertes, o se quiere todo integrado en una sola plataforma → GitLab.

## Herramientas de CI/CD

- **GitHub Actions** — la opción natural si el código vive en GitHub; camino de menor resistencia.
- **GitLab CI** — la opción natural si el código vive en GitLab; viene integrado, sin configurar herramienta aparte.
- **CircleCI** — herramienta especializada de CI/CD en la nube (no aloja código), útil cuando se necesita algo que las anteriores no dan bien (debug por SSH, paralelización inteligente de tests). Vale el costo extra solo si eso importa de verdad.
- **Jenkins** — self-hosted, máxima flexibilidad y control, pero requiere mantenimiento propio. Solo para equipos con capacidad dedicada a mantenerlo, o entornos sin acceso a internet (air-gapped).

**Heurística por defecto:** una vez elegido dónde vive el repositorio (GitHub o GitLab), usar su CI/CD nativo salvo una razón concreta para algo distinto — no agregar una herramienta de CI/CD aparte sin necesidad, mismo criterio de "no sobrearquitectura" de bloques anteriores.

Fuentes (2026): [Strapi — GitLab vs GitHub](https://strapi.io/blog/gitlab-vs-github-devops-platform-comparison), [DEV Community — GitHub Actions vs GitLab CI/CD](https://dev.to/_d7eb1c1703182e3ce1782/github-actions-vs-gitlab-cicd-complete-cicd-comparison-2026-48ac), [Northflank — Best CI/CD tools](https://northflank.com/blog/best-ci-cd-tools), [TechnologyMatch — Jenkins vs GitLab CI vs CircleCI vs GitHub Actions](https://technologymatch.com/blog/jenkins-vs-gitlab-ci-vs-circleci-vs-github-actions-the-ci-cd-decision-guide-in-2026).
