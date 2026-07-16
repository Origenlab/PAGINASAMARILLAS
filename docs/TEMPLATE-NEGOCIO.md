# Template canónico de ficha de negocio

**Referencia viva: `/negocios/seguridad-privada/origins-private-security`.**

Toda página de negocio debe rendir **idéntica** a esa. Render único:
`src/pages/negocios/[categoria]/[slug].astro`. **No se crean páginas de negocio
sueltas.** Si una ficha se ve distinta, el problema está en los datos del `.md`,
no en el template.

Complemento de `docs/TEMPLATE-CATEGORIA.md`: ese cubre `/categoria/*`, este
cubre `/negocios/*`. Las dos capas comparten las mismas fichas `.md`.

---

## 1. Estructura obligatoria (orden exacto)

| # | Bloque | Se cae si falta |
|---|--------|-----------------|
| 1 | Breadcrumbs | — |
| 2 | Hero col 1: tag categoría · colonia, `bh-brand` (nombre), `h1`, slogan, CTAs | `heroTitle` → H1 genérico |
| 3 | Hero col 2: 2 párrafos | `heroIntro` → fallback desbalanceado |
| 4 | Servicios Profesionales | `services[]` |
| 5 | Cobertura y Sectores (2 columnas) | `sectors[]` → queda a media tabla |
| 6 | Sidebar de contacto | `phone`, `whatsapp`, `website` |
| 7 | Cuerpo del `.md` | — |
| 8 | FAQs | `faqs[]` |
| 9 | JSON-LD LocalBusiness + BreadcrumbList + FAQPage | — |

## 2. `heroTitle` — reglas duras

Es el H1 de la página: la señal SEO más fuerte de la ficha.

- **NUNCA repetir el nombre de la empresa.** Ya se imprime arriba en `.bh-brand`.
  `PODIUMEX — Entretenimiento en Cuauhtémoc` con "PODIUMEX" ya encima es
  duplicación pura.
- **Keyword comercial, no la categoría genérica.** Lo que la gente teclea:
  `renta de pódiums`, `equipo para bomberos`, `renta de inflables`. NO
  `Entretenimiento`, NO `Equipos Contra Incendios`.
- **`<span class="highlight">` sobre el diferenciador**, no sobre la palabra
  genérica. En origins va sobre `certificada CNSP` — lo que distingue, no lo que
  clasifica.
- **Ciudad real, no colonia.** `en CDMX`, `en Querétaro`, `en México`. Nadie
  busca "en Cuauhtémoc" ni "en Nápoles".
- Una sola línea, sin punto final. HTML permitido (solo `<span class="highlight">`).

**Matiz**: varias empresas se llaman igual que su keyword (BOLAS DISCO, RENTA DE
ILUMINACIÓN, BOMBERO MX, Seguridad Privada MX). Ahí el solape es inevitable y
correcto — el keyword manda. Lo prohibido es usar la marca **como marca**
(`PODIUMEX — Entretenimiento en Cuauhtémoc`), no que el keyword coincida con el
nombre (`Fabricación y venta de bolas disco de 10 cm a más de 1 metro en CDMX`).

Referencia:

```yaml
heroTitle: 'Seguridad privada <span class="highlight">certificada CNSP</span> para empresas, industria y corporativos en CDMX'
```

## 3. `heroIntro` — exactamente 2 párrafos

Columna derecha del hero. Se renderizan solo los 2 primeros; un tercero se ignora.

- **Equilibrados**: ~55-75 palabras cada uno. Un párrafo de 8 líneas junto a uno
  de 1 línea se ve roto — es justo lo que produce el fallback.
- **P1 = quién es y a qué escala**: años, tamaño de operación, modelo de servicio,
  cobertura. Datos concretos de la ficha, nunca inventados.
- **P2 = el diferenciador y cómo arranca la relación**: qué lo separa del resto,
  certificaciones, y el primer paso (cotización, diagnóstico, asesoría).
- Prosa corrida. Sin viñetas, sin negritas, sin listas.
- No repetir literal el `summary` ni el `tagline`: son otros bloques de la misma
  página y Google lee la duplicación.

**Sin `heroIntro`**, el fallback arma P1 con `summary` y P2 con `coverage` — y
`coverage` es una frase genérica repetida entre fichas. Sirve para no romper, no
como estado final.

## 4. Resto del contrato

- `sectors[]` — **obligatorio**, mínimo 6. Sin él, "Cobertura y Sectores" pierde
  su columna izquierda y la sección queda coja.
- `services[]` — mínimo 4, con `name` y `description` reales.
- `faqs[]` — mínimo 5, preguntas que la gente hace de verdad.
- `title` ≤ 60 y `description` ≤ 160: los guards de `content.config.ts` rompen
  el build si te pasas.
- `image`, `gallery`, `summary`, `featured`, `order`: ver `docs/TEMPLATE-CATEGORIA.md` §3.

## 5. Checklist

1. `heroTitle` sin el nombre, con keyword comercial, `highlight` en el diferenciador y ciudad real.
2. `heroIntro` con 2 párrafos equilibrados y datos verídicos.
3. `sectors` ≥ 6, `services` ≥ 4, `faqs` ≥ 5.
4. `npm run build` sin errores.
5. Comparar en vivo contra `/negocios/seguridad-privada/origins-private-security`.
6. Sin animaciones ni transiciones nuevas (ver `CLAUDE.md`).
