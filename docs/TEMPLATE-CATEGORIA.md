# Template canónico de página de categoría

**Referencia viva: `/categoria/seguridad-privada`.**

Toda página de categoría — actual o futura — debe rendir **idéntica** a esa página.
Si hay duda sobre estructura, orden de bloques o campos, se abre
`/categoria/seguridad-privada` y se copia. No se inventan variantes.

Render único: `src/pages/categoria/[slug].astro`. **No se crean páginas de
categoría sueltas.** Si una categoría se ve distinta, el problema NO está en el
template: está en los datos (`src/config/site.ts` o las fichas `.md`).

---

## 1. Estructura obligatoria (orden exacto)

| # | Bloque | Componente | Fuente de datos |
|---|--------|-----------|-----------------|
| 1 | Breadcrumbs | `Breadcrumbs.astro` | `Categorías > {cat.name}` |
| 2 | Hero | `PageHero.astro` | kicker `"Categoría"`, `titleHtml` con `<span class="highlight">` en la 1ª palabra, `subtitle` = `cat.description` |
| 3 | Chips del hero | slot `meta` | `{n} empresas verificadas` + `Cobertura nacional` |
| 4 | Section head 2 columnas | `.section-head--split` | izq: eyebrow + `h2` + conteo · der: `cat.seoIntro[0]` y `[1]` |
| 5 | Grid de cards | `BusinessCard.astro` × N | todas las fichas de la categoría, orden `order` asc |
| 6 | Bloques "Empresa destacada" | `FeaturedBusiness.astro` × N | fichas con `featured: true` |
| 7 | Sidebar | `CategorySidebar.astro` | `current={slug}` |
| 8 | CTA band | inline | `mailto` de registro |
| 9 | JSON-LD | `@lib/seo` | `BreadcrumbList` + `ItemList` |

---

## 2. Contrato en `src/config/site.ts`

Campos **obligatorios** para que la categoría rinda como el template:

- `id`, `name`, `slug`, `color`, `icon`
- `description` — subtítulo del hero + meta description
- `services`, `count` (= nº real de fichas `.md`), `imagesFolder`
- `image` — imagen OG, ruta `/img/{imagesFolder}/...`
- `seoIntro: [string, string]` — **obligatorio**. Sin él, la columna derecha del
  `.section-head--split` se cae y la categoría deja de verse como el template.
- `blogSlug` — solo si el slug del blog difiere del de la categoría.

## 3. Contrato de cada ficha `src/content/negocios/<categoria>/<slug>.md`

Schema completo en `src/content.config.ts`. Para el **render de categoría**:

**Obligatorio siempre** (grid de cards):

- `name`, `title` (≤60), `description` (≤160), `image`, `phone`, `address`, `order`
- `tagline` — texto de la card (fallback: `description`)
- `services[]` — tags de la card (se muestran 3 + contador)
- `yearsExperience` — badge de la card (fallback: `"Verificada"`)

**Obligatorio para el bloque "Empresa destacada"**:

- `featured: true` — **todas las fichas de la categoría lo llevan.** Es lo que
  hace que la categoría se vea como seguridad-privada. Si nadie es `featured`,
  la página se queda en puro grid y rompe el template.
- `summary` — párrafo largo (~600–800 chars) con datos reales de la empresa.
  Fallback: `description` limpiada; sirve, pero se ve pobre.
- `gallery: [3 rutas]` — 1 grande + 2 chicas, **las 3 distintas entre sí y
  distintas de `image`**. Fallback del componente: `image` ×3 (aceptable como
  provisional, nunca como estado final).
- `slogan`, `whyUs[]` (se muestran 3), `areaServed[]`, `employees` — refuerzan
  el bloque; ausentes, el componente los omite sin romper.

## 4. Reglas de imágenes

- Carpeta por categoría: `public/img/{imagesFolder}/`.
- **Mínimo 4 imágenes por ficha** (1 `image` + 3 `gallery`) para cumplir el
  template sin fallback.
- Dentro de una misma ficha: las 4 rutas son distintas.
- No repetir la misma `image` principal entre fichas de una categoría: el grid
  se ve clonado.
- Sin datos falsos: no se referencian archivos inexistentes ni se inventan
  fotos que no correspondan a la categoría.

## 5. Checklist para lanzar / homologar una categoría

1. Entrada en `categories` de `site.ts` con **todos** los campos de §2, `seoIntro` incluido.
2. `count` = nº real de `.md` en `src/content/negocios/<slug>/`.
3. Cada ficha: `featured: true`, `summary`, `gallery` de 3, `order` consecutivo desde 1.
4. Imágenes reales en `public/img/{imagesFolder}/` (≥ 4 × nº de fichas).
5. `npm run build` sin errores (los guards SEO rompen el build si `title` > 60 o `description` > 160).
6. Comparar contra `/categoria/seguridad-privada`: mismos bloques, mismo orden, mismo aspecto.
7. Sin animaciones ni transiciones nuevas (ver `CLAUDE.md`).

---

## Estado de cumplimiento

| Categoría | Fichas | `seoIntro` | `featured` | `summary` | `gallery` (3 reales) |
|---|---|---|---|---|---|
| seguridad-privada | 4 | ✅ | 4/4 | 4/4 | 4/4 |
| entretenimiento | 7 | ✅ | 7/7 | 7/7 | 7/7 |
| equipos-contra-incendios | 5 | ✅ | 5/5 | 5/5 | 0/5 — fallback |

**Pendiente:** `public/img/img-equipos-contra-incendios/` tiene 5 imágenes para
5 fichas; el template pide ≥ 20 (4 × 5). Hasta que existan, esas fichas usan el
fallback (`image` ×3) y la categoría no cumple §4 al 100%.
