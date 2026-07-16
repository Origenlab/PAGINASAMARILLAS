# Template canónico del blog

**Referencia viva: `/blog/equipos-contra-incendios/nom-002-stps-requisitos-centros-de-trabajo`.**

Tercera capa del sistema, junto a `docs/TEMPLATE-CATEGORIA.md` (`/categoria/*`) y
`docs/TEMPLATE-NEGOCIO.md` (`/negocios/*`). Render único por tipo de página:
`blog/[categoria]/[slug].astro`, `blog/categorias/[categoria].astro` y
`blog/index.astro`. **No se crean páginas de blog sueltas.**

---

## 1. El blog NO declara fechas

Decisión tomada el 2026-07-16, y es deliberada — no un olvido.

Las 11 guías migradas del sitio viejo nunca tuvieron fecha de publicación. Se
rastreó por tres vías: git solo muestra la fecha de la migración a Astro
(2026-07-13), el HTML legacy de esas 11 no tiene `datePublished`, `<time>` ni
fecha visible, y los sitemaps con `lastmod` ya no están en el repo. Las 5 que sí
tenían fecha la heredaron del legacy, donde existía. El dato, para las otras 11,
**no existe**: solo podía inventarse, y eso rompe la regla de "sin datos falsos".

En consecuencia:

- **No hay `publishDate` ni `updatedDate`** en el schema.
- El artículo **no renderiza `<time>`**.
- El JSON-LD de `Article` **no lleva `datePublished` ni `dateModified`** (son
  opcionales en `@lib/seo`: si no se pasan, no se emiten).
- Ningún copy promete recencia. El home dice "Guías destacadas", no "recientes".

Si alguna vez se recuperan las fechas reales, se puede revertir. Mientras tanto,
**no inventes una para homologar**.

## 2. `order` manda el listado

Sustituye a `publishDate` como criterio de orden, igual que en `negocios`.

- Entero, **ascendente**. Desempate: `title.localeCompare`.
- Es **global**, no por categoría: el home toma los 3 de menor `order` de todo el
  blog. Los órdenes 1, 2 y 3 están asignados a una guía de cada categoría a
  propósito, para que el home no muestre tres del mismo tema.
- Criterio editorial: primero las guías de intención de compra (costos, qué
  necesitas, normativa), al final las reseñas de empresa.
- Se ordena en 4 lugares: `index.astro`, `blog/index.astro`,
  `blog/categorias/[categoria].astro` y `CategorySidebar.astro`. En
  `BusinessSidebar.astro` va después del criterio de `relatedBusiness`.

## 3. `relatedBusiness` — id completo, nunca el nombre

**Este campo estuvo roto desde que existe.** Guardaba el nombre visible
(`"SEPRI"`, `"REDEIL"`) mientras el código comparaba contra el slug del archivo
(`"sepri"`), así que el `===` fallaba siempre: 0 de 9 guías hacían match y la
priorización de guías relacionadas nunca funcionó. En silencio, porque un sort
que no prioriza nada no se ve roto.

Reglas ahora:

- Es `reference('negocios')` y se escribe con el **id completo**:
  `"seguridad-privada/sepri"`, `"entretenimiento/redeil"`.
- **`reference()` NO valida en build.** Astro solo comprueba que el id exista al
  llamar `getEntry()`. El guard real está en el `getStaticPaths` de
  `blog/[categoria]/[slug].astro` y ahí sí truena con la lista de guías huérfanas.
  Si mueves o borras ese guard, el campo vuelve a poder romperse en silencio.
- Solo lo llevan las guías que hablan de **una empresa concreta** (reseñas,
  guías de servicios). Las guías genéricas —normativa, costos, comparativas— van
  **sin** `relatedBusiness`, y eso es correcto: no es drift.

## 4. Contrato de la ficha `src/content/blog/<categoria>/<slug>.md`

Schema en `src/content.config.ts`.

**Obligatorio:**

- `title` — **≤ 60 chars**, el guard rompe el build. Es el `h1` y el `<title>`.
- `description` — **≤ 160 chars**, el guard rompe el build. Es el lead visible
  (`.article-lead`) y la meta description: tiene que funcionar en los dos lados.
- `categoryName` — nombre visible de la categoría.
- `order` — ver §2.
- `image` — hero del artículo y `og:image`. Ruta de la carpeta de la categoría.
- `keywords[]` — alimentan `<meta name="keywords">`.
- `author` — default `"Pamari"`.

**Opcional:** `relatedBusiness` (ver §3), `draft` (excluye del build).

## 5. Cuerpo del artículo

- Arranca con un párrafo de gancho **antes** del primer `##`. Nada de "En este
  artículo veremos".
- Encabezados `##`, sin `#` (el `h1` lo pone el template).
- **Links internos a fichas del directorio** con ruta absoluta:
  `/negocios/<categoria>/<slug>`. Es el trabajo real del blog: mover tráfico de
  la guía a la ficha. Sin `.html`.
- Prosa. Las listas solo donde son literalmente una lista (requisitos, clases,
  programas).
- **Sin anécdotas inventadas.** Varias guías heredadas del sitio viejo usan
  primera persona con historias falsas ("hace poco ayudé a un emprendedor…").
  No repliques ese patrón: es experiencia fabricada en un directorio que se vende
  como verificado.
- Si la guía se apoya en normativa, **cita la fuente oficial al final** y aclara
  que es informativa y no sustituye asesoría. Ver la guía de referencia.

## 6. Checklist

1. `title` ≤ 60 y `description` ≤ 160 (si no, el build truena).
2. `order` asignado y coherente con el criterio de §2.
3. `relatedBusiness` con id completo, solo si la guía es sobre una empresa.
4. Links internos a `/negocios/...` verificados contra `dist`.
5. Sin fechas, en ningún campo ni en el cuerpo.
6. Datos verificables contra fuente citada; nada inventado.
7. `npm run build` limpio.

## Estado

| Categoría | Guías | Con `order` | `relatedBusiness` válido |
|---|---|---|---|
| seguridad-privada | 13 | 13 | 6/6 |
| eventos | 3 | 3 | 3/3 |
| equipos-contra-incendios | 3 | 3 | n/a (genéricas) |

**Pendiente:** `public/img/img-equipos-contra-incendios/` son placeholders
generados, no fotos. Las 3 guías nuevas los usan como hero. Ver la nota de
imágenes en `docs/TEMPLATE-CATEGORIA.md`.
