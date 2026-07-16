# Pamari — Reglas del proyecto

Directorio de empresas en México. Astro 6 + Markdown (content collections), estático, GitHub Pages. Keyword principal: **"Empresas en México"**.

## REGLA DE DISEÑO OBLIGATORIA: sin animaciones ni transiciones

- **PROHIBIDO** en todo el sitio: `animation`, `@keyframes`, `transition`, `scroll-behavior: smooth`, transforms en hover (translateY, scale), zoom de imágenes en hover.
- **ÚNICA EXCEPCIÓN: los botones.** `.btn` (y variantes), el botón hamburguesa del menú y `.blog-filters button` sí llevan transición.
- Imágenes, cards, links, menús y cualquier otro elemento: los cambios de hover son **instantáneos** (cambio de color/borde sin transición).
- Al crear componentes nuevos, respetar esta regla. Al tocar `public/css/style.css`, verificar con: `grep -n "transition\|animation\|@keyframes" public/css/style.css` — solo deben aparecer las 3 de botones.

## REGLA DE TEMPLATE: `/categoria/seguridad-privada` es el canónico

- **Toda página de categoría se ve igual a `/categoria/seguridad-privada`.** Contrato completo en `docs/TEMPLATE-CATEGORIA.md` — leerlo antes de tocar o lanzar cualquier categoría.
- Render único: `src/pages/categoria/[slug].astro`. **Nunca** crear páginas de categoría sueltas ni variantes de layout por categoría.
- Si una categoría se ve distinta, el bug está en los datos, no en el template: falta `seoIntro` en `site.ts`, o faltan `featured: true` / `summary` / `gallery` (3 imágenes) en las fichas `.md`.
- Toda ficha de negocio lleva `featured: true` + `summary` + `gallery` de 3 imágenes reales distintas. Sin eso la categoría se queda en puro grid y rompe el template.

## REGLA DE TEMPLATE: `/negocios/seguridad-privada/origins-private-security` es el canónico

- **Toda ficha de negocio se ve igual a esa.** Contrato completo en `docs/TEMPLATE-NEGOCIO.md`.
- El `h1` (`heroTitle`) **nunca repite el nombre de la empresa** — ya se imprime arriba en `.bh-brand`. Lleva keyword comercial (`renta de pódiums`, no `Entretenimiento`), `<span class="highlight">` sobre el diferenciador y ciudad real (`CDMX`, no la colonia).
- `heroIntro` = exactamente 2 párrafos equilibrados (~55-75 palabras c/u). El fallback (`summary` + `coverage`) sirve para no romper, no como estado final.
- `sectors` ≥ 6 en toda ficha: sin él, "Cobertura y Sectores" pierde una columna.

## REGLA DE TEMPLATE: el blog

- Contrato completo en `docs/TEMPLATE-BLOG.md`. Referencia: `/blog/equipos-contra-incendios/nom-002-stps-requisitos-centros-de-trabajo`.
- **El blog no declara fechas** y es a propósito: las 11 guías migradas nunca tuvieron `publishDate` (no está en el legacy, ni en sitemaps; git solo tiene la fecha de la migración). No hay `<time>` ni `datePublished` en el JSON-LD. **No inventes una fecha para homologar.** El listado ordena por `order` (asc), igual que `negocios`.
- `relatedBusiness` va con **id completo** (`"seguridad-privada/sepri"`), nunca el nombre visible: así estuvo roto y fallaba el `===` en silencio, 0 de 9. `reference()` NO valida en build — el guard vive en el `getStaticPaths` de `blog/[categoria]/[slug].astro`; si lo quitas, el campo se vuelve a romper en silencio.
- Solo las guías sobre una empresa concreta llevan `relatedBusiness`. Las genéricas van sin él y está bien.
- Sin anécdotas inventadas: varias guías heredadas usan primera persona con historias falsas. No replicar ese patrón.

## Otras reglas de diseño

- Design system: un solo archivo `public/css/style.css` (tokens al inicio). No crear CSS nuevos.
- Identidad: "Amarillo Premium" — ink `#101014` + amarillo `#FFC700`, tipografía Sora (display) + Inter (body).
- Layout full-width: `.container` ocupa 100% del viewport con padding lateral fluido. Sin max-width.
- Títulos de sección: patrón 2 columnas (`.section-head--split`): izquierda eyebrow+título+CTA, derecha 2 párrafos SEO.
- Cards de categoría: 4 por fila en desktop.
- Sin datos falsos: nada de ratings inventados, badges falsos ni links muertos (`#`).

## Estructura

- Contenido: `src/content/negocios/<categoria>/<slug>.md` y `src/content/blog/<categoria>/<slug>.md`.
- Config de categorías: `src/config/site.ts` (`categories` activas, `upcomingCategories` priorizadas según `docs/ESTUDIO-CATEGORIAS.md`).
- URLs **limpias sin `.html`** en todos los links internos, canonicals y sitemap. El build sigue en format `preserve` (genera `.html` en disco y GitHub Pages resuelve `/foo` → `foo.html`), así las URLs viejas con `.html` no se rompen. NUNCA escribir links internos con `.html`. `public/blog/**/*.html` son stubs de redirect SEO — no borrar.
- Lanzar categoría nueva = mover de `upcomingCategories` a `categories` + fichas .md + guías de blog. Seguir el checklist de `docs/TEMPLATE-CATEGORIA.md` §5.
