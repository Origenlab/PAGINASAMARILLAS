# Estudio de categorías — PáginasAmarillas.mx

> Priorización de categorías de empresas en México para el directorio.
> Fecha: 2026-07-15 · Fuentes: INEGI (Censos Económicos 2024 / DENUE), análisis de directorios competidores (Sección Amarilla), demanda de búsqueda local.

## 1. Contexto de mercado

México registra **más de 5.5 millones de unidades económicas** (DENUE 2025). Distribución por sector:

| Sector | % de establecimientos |
|---|---|
| Comercio | 44% |
| Servicios | 42% |
| Manufactura | 11% |
| Otros | 3% |

El 41.7% del total son comercios al por menor (2.56 millones de pequeños negocios). Ese es el universo natural de un directorio: negocios locales pequeños/medianos que necesitan visibilidad y no tienen SEO propio.

## 2. Criterios de priorización

Cada categoría se calificó (1–5) en cuatro ejes:

1. **Volumen de búsqueda local** — cuánta gente busca "X cerca de mí / en CDMX".
2. **Valor del lead** — ticket del servicio; qué tan dispuesto está el negocio a pagar por aparecer.
3. **Urgencia de la búsqueda** — búsquedas con intención inmediata convierten más (plomero, cerrajero, grúa).
4. **Sinergia** — afinidad con las verticales ya activas (seguridad privada, incendios, eventos) y su contenido.

## 3. Ranking de categorías prioritarias

| # | Categoría | Búsqueda | Lead | Urgencia | Sinergia | Total |
|---|---|---|---|---|---|---|
| 1 | Salud y Medicina (médicos, dentistas, clínicas) | 5 | 4 | 4 | 2 | 15 |
| 2 | Automotriz (mecánicos, hojalatería, grúas) | 5 | 4 | 5 | 2 | 16* |
| 3 | Construcción y Remodelación | 4 | 5 | 3 | 3 | 15 |
| 4 | Plomería y Electricidad (oficios urgentes) | 4 | 3 | 5 | 2 | 14 |
| 5 | Restaurantes y Banquetes | 5 | 3 | 3 | 3 | 14 |
| 6 | Abogados y Notarías | 4 | 5 | 3 | 2 | 14 |
| 7 | Belleza y Cuidado Personal | 4 | 3 | 3 | 1 | 11 |
| 8 | Veterinarias y Mascotas | 4 | 3 | 4 | 1 | 12 |
| 9 | Tecnología y Sistemas (CCTV, redes, soporte) | 3 | 4 | 3 | 5 | 15 |
| 10 | Limpieza y Fumigación | 3 | 4 | 3 | 4 | 14 |
| 11 | Mudanzas y Fletes | 3 | 4 | 5 | 2 | 14 |
| 12 | Educación y Capacitación | 3 | 3 | 2 | 2 | 10 |

\* Automotriz puntúa más alto en urgencia+búsqueda; se lista #2 por competencia SEO más dura que salud.

## 4. Recomendación por fases

**Fase 1 (0–3 meses)** — B2B con sinergia directa al contenido actual y lead caro:
Tecnología y Sistemas (CCTV — cruza con seguridad privada), Limpieza y Fumigación (mismo comprador: administradores de edificios/condominios), Construcción y Remodelación.

**Fase 2 (3–6 meses)** — Alta urgencia, lead directo por teléfono:
Plomería y Electricidad, Automotriz, Mudanzas y Fletes.

**Fase 3 (6–12 meses)** — Volumen masivo, requiere más fichas para competir:
Salud y Medicina, Abogados y Notarías, Restaurantes y Banquetes, Veterinarias, Belleza, Educación.

Lógica: las Fases 1–2 se ganan con 5–10 fichas verificadas + 4–6 guías por categoría (mismo playbook que seguridad privada). La Fase 3 exige volumen y se ataca cuando el dominio tenga más autoridad.

## 5. Implementación en el sitio

- Las 12 categorías aparecen en el home y en /categorias como "Próximamente", en el orden del ranking.
- Cada lanzamiento de categoría = mover de `upcomingCategories` a `categories` en `src/config/site.ts` + fichas .md + guías de blog.

## Fuentes

- [INEGI — Censos Económicos 2024, resultados definitivos](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/ce/CE2024_def.pdf)
- [INEGI — DENUE, actualización 2025 (5.56M establecimientos)](https://www.inegi.org.mx/rnm/index.php/catalog/1103)
- [La Jornada — Incremento de establecimientos de comercio](https://www.jornada.com.mx/noticia/2024/11/26/economia/incrementan-en-la-ultima-decada-establecimientos-de-comercio-en-el-pais-7014)
- [Sección Amarilla — categorías y demanda del buscador](https://www.seccionamarilla.com.mx/)
