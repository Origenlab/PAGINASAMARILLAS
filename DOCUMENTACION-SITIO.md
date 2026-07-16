# Documentación — paginasamarillas.mx

> Análisis técnico del repositorio `Origenlab/PAGINASAMARILLAS`.
> Fecha de análisis: 2026-07-13 · Rama: `main` · Último commit: `62e1993`

---

## 1. Resumen ejecutivo

**paginasamarillas.mx** es un **directorio de negocios de México** (estilo "páginas amarillas"), enfocado en SEO. Conecta usuarios que buscan servicios con empresas listadas por categoría. Es propiedad de **Origenlab** y forma parte de su portafolio de sitios.

Hoy el sitio está **vivo y funcionando**, pero es un **MVP de contenido**: no tiene backend, buscador funcional ni sistema de registro. Su valor está en las **páginas de perfil de empresa** y en un **blog SEO** grande, ambos altamente optimizados con datos estructurados (schema.org).

Estado actual:
- **3 categorías activas:** Seguridad Privada, Entretenimiento, Equipos Contra Incendios.
- **16 empresas** con perfil (4 seguridad, 7 entretenimiento, 5 incendios).
- **~55 artículos de blog** (la gran mayoría de seguridad privada).
- Arquitectura **híbrida**: cascarón Astro + mucho HTML estático pre-generado.

✅ **Actualización 2026-07-13 — deploy arreglado.** Antes producción servía la versión vieja pre-Astro porque el workflow de deploy **fallaba desde el 15-mar** (`astro build` no corría en Node 20). Se subió el CI a **Node 22**; el build ahora pasa y producción **ya sirve la versión Astro** del repo. Drift resuelto. Detalle en §9.

---

## 2. Qué es y para qué sirve

Es un directorio empresarial. La propuesta de valor declarada en el sitio:

- Buscar negocios "verificados" por rubro y ciudad.
- Cada empresa tiene ficha con dirección, teléfono, horarios, servicios, FAQs y reseñas.
- Blog con guías SEO que alimentan tráfico hacia las fichas.

Monetización **planeada** (aún no construida — son enlaces `#`): "Registrar Negocio", "Planes y Precios", "Soluciones de Publicidad", "Estadísticas". El modelo de negocio implícito es cobrar a empresas por listarse/destacarse.

Público y localización: México, español (`es-MX`), foco geográfico CDMX y Estado de México.

---

## 3. Stack técnico

| Capa | Tecnología |
|---|---|
| Framework | **Astro 6** (`astro@^6.0.4`) |
| Integración | `@astrojs/sitemap@^3.7.1` |
| Output | Estático (`build.format: 'file'` → genera `pagina.html`) |
| Estilos | CSS plano, 4 archivos, con variables (design tokens) |
| JavaScript | Vanilla JS, 3 archivos, sin framework |
| Tipografía | Inter (Google Fonts) |
| Node | `engines: >=22.12.0` |
| Hosting | GitHub Pages (vía GitHub Actions) |
| DNS/CDN | Cloudflare (proxy delante del dominio) |
| Dominio | `paginasamarillas.mx` (archivo `CNAME`) |

No hay React/Vue/Svelte, ni base de datos, ni backend. Todo es estático.

---

## 4. Arquitectura — clave para entender el sitio

El punto más importante: **es un híbrido Astro + HTML estático**, no un sitio Astro "puro".

```
Astro compila SOLO 4 páginas (src/pages/*.astro):
   /            → index.astro      (home: hero + búsqueda + 3 categorías)
   /categorias  → categorias.astro (listado de categorías)
   /sitemap     → sitemap.astro    (mapa del sitio en HTML)
   /404         → 404.astro

TODO lo demás vive en public/ y Astro lo copia TAL CUAL al build:
   public/negocios/<categoria>/<empresa>.html   ← fichas de empresa
   public/categoria/<categoria>.html            ← páginas de categoría
   public/blog/**/*.html                         ← blog completo
   public/css/*.css  public/js/*.js  public/img/**
```

Consecuencias prácticas:
- El **90% del contenido son archivos HTML sueltos**, escritos a mano o generados por automatización, no componentes Astro.
- Editar una ficha o un artículo = editar su `.html` directamente en `public/`. Astro no los toca.
- Solo el home, categorías, sitemap y 404 usan el sistema de componentes/Layout de Astro.

### `Layout.astro` (único layout)
Define el cascarón compartido de las páginas Astro: `<head>` con SEO completo (meta, Open Graph, Twitter, geo, favicons, preload de fuentes), header con nav (Inicio / Categorías / Blog + botones "Iniciar Sesión" / "Registrar Negocio"), y footer extenso. Recibe props: `title`, `description`, `canonical`, `ogTitle/ogDescription/ogImage/ogType`, `extraHead`, `extraCss`.

**Nota:** las páginas HTML de `public/` **no** usan este Layout — tienen su propio `<head>` y su propia copia de header/footer embebida. Por eso hay que mantener el diseño en dos lugares.

---

## 5. Contenido e inventario

### Categorías (3)
| Categoría | Página | Empresas | Color |
|---|---|---|---|
| Seguridad Privada | `/categoria/seguridad-privada.html` | 4 | `#dc2626` |
| Entretenimiento | `/categoria/entretenimiento.html` | 7 | `#f59e0b` |
| Equipos Contra Incendios | `/categoria/equipos-contra-incendios.html` | 5 | — |

### Empresas con ficha (`public/negocios/`)
- **Seguridad privada (4):** Origins Private Security, Seguridad Condominios MX, SEPRI, Seguridad Privada MX.
- **Entretenimiento (7):** bolas-disco, eventech, inflables-para-fiestas, podiumex, redeil, renta-de-iluminacion, resoil. *(+2 archivos `-backup` que no deberían ir a producción.)*
- **Equipos contra incendios (5):** bombero-mx, gama-de-mexico, lga-contra-incendios, meseci, proyecto-red.

Cada ficha es una landing SEO muy completa: meta tags + `business:contact_data` + **JSON-LD rico** (`LocalBusiness`, `FAQPage` con 6 preguntas, `Service`/`OfferCatalog`, `AggregateRating`, `OpeningHoursSpecification`, `BreadcrumbList`, `GeoCoordinates`). Usan `css/style.css` + `css/perfil.css` + `js/perfil.js`.

### Blog (`public/blog/`)
- **~52 artículos** en `seguridad-privada/` y **3** en `eventos/`.
- `blog/index.html` es la portada con grid de tarjetas.
- **Automatización n8n:** las tarjetas se insertan entre marcadores HTML (`<!-- n8n:INSERT-NEW-CARDS-HERE -->`, `<!-- n8n:BLOG-GRID-START/END -->`). El historial git muestra commits automáticos "Add article" / "Add card". Config en `public/blog/blog-config.json` (categorías, negocios, rutas, marcadores).
- Plantillas en `public/blog/templates/` (`article-template.html`, `card-template.html`, `placeholders.json`).
- Artículos usan JSON-LD `Article` y `css/blog-article.css`.

### Documentación heredada (`_html_backup/docs/`)
Fichas de negocio en Markdown y catálogo: `CATALOGO-EMPRESAS.md`, `TEMPLATE-PERFIL-NEGOCIO.md`, y `*-INFO.md` por empresa. Es el "source of truth" editorial del proceso manual anterior.

---

## 6. Sistema de diseño

Definido con variables CSS en `public/css/style.css` (`:root`). Paleta v2.0 "colores sólidos" (sin gradientes):

- **Primario (amarillo):** `#F4B942` · dark `#E6A82E` · light `#FFF8E7`
- **Secundario (azul marino):** `#1A2332` · light `#2C3E50`
- Escala de grises `--color-gray-50…900`, acentos azul/púrpura/esmeralda/naranja.
- Tokens de `spacing`, `radius`, `font-size`. Tipografía **Inter**. Mobile-first, responsive.

Archivos CSS: `style.css` (global, 46 KB), `perfil.css` (fichas, 27 KB), `categoria.css` (categorías, 27 KB), `blog-article.css` (blog, 11 KB).
Archivos JS: `app.js` (menú móvil, smooth scroll, header dinámico, validación de búsqueda), `categoria.js` (filtros/orden en categoría), `perfil.js` (interacción en fichas).

---

## 7. SEO

Es el corazón del proyecto. Prácticas presentes:
- Meta description, keywords, `robots` avanzado, canonical por página.
- Open Graph + Twitter Card completos, `og:locale es_MX`.
- Geo tags (`geo.region`, `geo.position`, `ICBM`) apuntando a CDMX.
- **JSON-LD** extenso y variado según tipo de página (ver §5).
- `robots.txt`: permite todo salvo `/admin`, `/docs/`, `*.md`, `webpack*.js`; **bloquea** AhrefsBot, SemrushBot, DotBot; declara el sitemap.
- `.htaccess`: reglas Apache (URLs limpias, headers de seguridad, cache). **Solo aplica en Apache** — no tiene efecto en GitHub Pages ni Cloudflare Pages.
- `manifest.json` / `site.webmanifest` (PWA básica), favicons múltiples.

---

## 8. Build y Deploy

**Flujo (`.github/workflows/deploy.yml`):**
```
push a main  →  GitHub Actions:
   checkout → setup-node (v20) → npm ci → npm run build → sube ./dist
   → deploy a GitHub Pages
```
Dominio `paginasamarillas.mx` vía `CNAME`, con **Cloudflare** como proxy/CDN por delante (se detecta la ofuscación de email `cdn-cgi/l/email-protection` en el HTML en vivo).

**Comandos locales:**
```bash
npm install        # instalar dependencias
npm run dev        # servidor de desarrollo (localhost:4321)
npm run build      # genera ./dist
npm run preview    # previsualiza el build
```

---

## 9. ⚠️ Hallazgos y riesgos (leer antes de trabajar)

1. ~~**Producción ≠ repo (drift crítico).**~~ **✅ RESUELTO (2026-07-13).** El sitio en vivo servía la versión **vieja pre-Astro**. Confirmado por el historial de Actions: los runs del workflow del 15-mar fallaron; los deploys previos (ene) eran "deploy from branch" del HTML viejo. Tras el fix de Node 22, producción ya sirve la versión Astro (nav `/categorias` sin `.html`, sin meta keywords, footer de 3 categorías).

2. ~~**Causa del drift: versión de Node en CI.**~~ **✅ CONFIRMADO Y ARREGLADO.** El log del run fallido mostró: `npm ci` ✓ pero **`npm run build` ✗ (exit 1)** en Node 20. `astro build` sí pasa en Node 22 (probado local + CI). Se cambió `node-version: "20"` → `"22"` en `deploy.yml` (commit `dd35b94`). El siguiente run quedó **verde** y desplegó.

3. ~~**Riesgo de rutas 404.**~~ **✅ VERIFICADO OK.** Aunque el nav enlaza `/categorias` y `/sitemap` sin `.html`, GitHub Pages resuelve la extensión automáticamente: `/categorias`, `/sitemap`, `/blog/` y las fichas devuelven **HTTP 200** en producción. No es un problema.

4. **Sitemaps incompletos.** El `sitemap.xml` manual solo lista **6 URLs** (home + 1 categoría + 4 negocios); le faltan blog y ~10 negocios. Además, el `@astrojs/sitemap` automático **solo cubre rutas renderizadas por Astro**, no los HTML de `public/` — así que **ningún sitemap cubre bien el blog ni las fichas**. Gap de SEO real.

5. **Funcionalidad simulada.** Búsqueda (`/buscar`), login y "Registrar Negocio" no existen: son formularios/enlaces sin backend (`#`, ruta inexistente). El header promete features no implementadas.

6. **Riesgo SEO de contenido duplicado.** Hay muchos artículos casi idénticos (variantes "reseña/guía/opiniones" de las mismas empresas: ~52 en seguridad privada). Puede leerse como *doorway pages*. Conviene consolidar/canonicalizar.

7. **Higiene del repo.** Se versionan `.DS_Store`, archivos `*-backup.html` que se publican, y `img/` en la raíz que parece duplicado de `public/img/` (solo `public/` se sirve). El `_html_backup/` completo (sitio viejo con webpack) también vive en el repo.

---

## 10. Cómo trabajar en el sitio

**Editar contenido existente** (fichas, blog, categorías): editar directamente el `.html` en `public/…`. No pasa por componentes Astro.

**Editar home / categorías / sitemap / 404:** editar `src/pages/*.astro` y `src/layouts/Layout.astro`.

**Agregar una empresa nueva** (proceso del proyecto, según `CATALOGO-EMPRESAS.md`):
1. Crear la ficha `public/negocios/<categoria>/<slug>.html` (partir de una existente).
2. Agregar su tarjeta en `public/categoria/<categoria>.html`.
3. Actualizar `sitemap.xml` y el catálogo.
4. Añadir imágenes en `public/img/img-<categoria>/`.

**Agregar un artículo de blog:** normalmente vía la automatización n8n (marcadores en `blog/index.html` + `blog-config.json`), o manualmente copiando `templates/article-template.html`.

**Recomendación de arranque** (antes de features nuevas):
- Arreglar el pipeline de deploy (Node 22) y confirmar que el Astro sí publica.
- Resolver el drift para que producción = repo.
- Corregir enlaces `/categorias` y `/sitemap`, y los sitemaps.

---

## 11. Mapa rápido de archivos

```
PAGINASAMARILLAS/
├─ astro.config.mjs         # config Astro (site, trailingSlash:never, format:file, sitemap)
├─ package.json             # Astro 6, scripts, engines Node>=22.12
├─ .github/workflows/deploy.yml   # CI → GitHub Pages (⚠ Node 20)
├─ CNAME                    # paginasamarillas.mx
├─ robots.txt · sitemap.xml · manifest.json · .htaccess
├─ generate-images.py       # genera OG/placeholder images con PIL
├─ src/
│  ├─ layouts/Layout.astro  # cascarón + SEO + header/footer (solo páginas Astro)
│  └─ pages/                # index · categorias · sitemap · 404
├─ public/                  # SE SIRVE TAL CUAL
│  ├─ negocios/<cat>/*.html # 16 fichas de empresa (+2 backup)
│  ├─ categoria/*.html      # 3 páginas de categoría
│  ├─ blog/                 # ~55 artículos + index + blog-config.json + templates
│  ├─ css/ · js/ · img/
└─ _html_backup/            # sitio viejo pre-Astro (webpack) + docs/ editoriales
```
