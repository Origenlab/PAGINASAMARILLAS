import { defineCollection, reference, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * Guards SEO — rompen el build si un title/description se pasa de largo.
 * Google trunca el title ~60 chars y la description ~160. Antes de este guard
 * las 16 fichas estaban entre 61 y 92 chars, o sea truncadas en el SERP.
 * El title es el final: los templates ya NO concatenan la marca.
 */
const seoTitle = z.string().max(60, 'title SEO: máximo 60 caracteres (Google lo trunca)');
const seoDescription = z.string().max(160, 'meta description: máximo 160 caracteres');

const negocios = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/negocios' }),
  schema: z.object({
    name: z.string(),
    categoryName: z.string(),
    title: seoTitle,
    description: seoDescription,
    keywords: z.array(z.string()).default([]),
    slogan: z.string().optional(),
    tagline: z.string().optional(),
    image: z.string(),
    phone: z.string(),
    phoneDisplay: z.string().optional(),
    phones: z.array(z.string()).default([]),
    whatsapp: z.string().optional(),
    email: z.string().optional(),
    website: z.string().optional(),
    address: z.object({
      street: z.string(),
      locality: z.string(),
      region: z.string(),
      postalCode: z.string().optional(),
      country: z.string().default('MX'),
    }),
    geo: z.object({ lat: z.number(), lng: z.number() }).optional(),
    hours: z
      .array(
        z.object({
          days: z.array(z.string()),
          opens: z.string(),
          closes: z.string(),
        }),
      )
      .default([]),
    hoursDisplay: z.array(z.string()).default([]),
    foundingDate: z.string().optional(),
    yearsExperience: z.number().optional(),
    employees: z.number().optional(),
    priceRange: z.string().optional(),
    areaServed: z.array(z.string()).default([]),
    coverage: z.string().optional(),
    sectors: z.array(z.string()).default([]),
    whyUs: z.array(z.string()).default([]),
    /**
     * Servicios del negocio. `name` + `description` son lo mínimo.
     * Si se agrega `image` la card se renderiza en versión enriquecida
     * (imagen + título + texto + link); si no, cae al layout de solo texto.
     * `slug` genera la página /negocios/{cat}/{negocio}/servicios/{slug}
     * (si se omite se deriva del nombre).
     */
    services: z
      .array(
        z.object({
          name: z.string(),
          description: z.string(),
          slug: z.string().optional(),
          /** Anchor text del botón de la card (fallback: name + región) */
          keyword: z.string().optional(),
          image: z.string().optional(),
          imageAlt: z.string().optional(),
          /** Etiqueta corta sobre la imagen, ej. "24/7" o "Certificado CNSP" */
          badge: z.string().optional(),
          /** 2 párrafos SEO para la columna derecha del hero de la página de servicio */
          heroIntro: z.array(z.string()).default([]),
          /** Bullets cortos para la card y la página de detalle */
          highlights: z.array(z.string()).default([]),
          /** Párrafos largos para la página del servicio */
          detail: z.array(z.string()).default([]),
          /** Pasos numerados de "cómo se implementa" */
          proceso: z
            .array(z.object({ title: z.string(), text: z.string() }))
            .default([]),
          /** Tabla comparativa de modalidades/alcances */
          comparativa: z
            .object({
              title: z.string().optional(),
              intro: z.string().optional(),
              headers: z.array(z.string()),
              rows: z.array(z.array(z.string())),
              note: z.string().optional(),
            })
            .optional(),
          /** Casos de uso: a qué tipo de cliente le sirve */
          casos: z
            .array(z.object({ title: z.string(), text: z.string() }))
            .default([]),
          /** Ficha técnica: pares dato/valor */
          specs: z
            .array(z.object({ label: z.string(), value: z.string() }))
            .default([]),
          /**
           * Requerimientos logísticos/técnicos que el cliente debe prever
           * para montar el servicio (energía, espacio, acceso, tiempo).
           * Es el diferenciador de eventos: responde "¿funcionará en mi lugar?".
           */
          requisitos: z
            .array(z.object({ concepto: z.string(), detalle: z.string() }))
            .default([]),
          /**
           * Marco normativo aplicable al servicio (NOM, NFPA, etc.).
           * `exige` = lo que dice la norma; `implica` = qué significa para el
           * comprador. Solo citar normas verificadas: una referencia falsa
           * en un sector regulado es peor que no citar ninguna.
           */
          normativa: z
            .array(
              z.object({
                norma: z.string(),
                titulo: z.string().optional(),
                exige: z.string(),
                implica: z.string().optional(),
              })
            )
            .default([]),
          /** FAQs específicas del servicio */
          faqs: z.array(z.object({ q: z.string(), a: z.string() })).default([]),
        })
      )
      .default([]),
    faqs: z.array(z.object({ q: z.string(), a: z.string() })).default([]),
    /** Párrafo largo para el módulo "Empresa destacada" (fallback: description) */
    summary: z.string().optional(),
    /** H1 SEO del hero de la ficha (HTML permitido, ej. <span class="highlight">) */
    heroTitle: z.string().optional(),
    /** 2 párrafos SEO/marketing para la columna derecha del hero de la ficha */
    heroIntro: z.array(z.string()).default([]),
    /** Mini galería (1 grande + 2 chicas). Fallback: image + imágenes de la categoría */
    gallery: z.array(z.string()).default([]),
    featured: z.boolean().default(false),
    order: z.number().default(0),
  }),
});

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: seoTitle,
    description: seoDescription,
    categoryName: z.string(),
    keywords: z.array(z.string()).default([]),
    image: z.string().optional(),
    author: z.string().default('Pamari'),
    /**
     * Orden de listado (asc), igual que en `negocios`. Sustituye a `publishDate`:
     * las 11 guías migradas del sitio viejo nunca tuvieron fecha de publicación
     * — no está en el HTML legacy, ni en los sitemaps, y en git solo aparece la
     * fecha de la migración a Astro (2026-07-13). Inventarla habría roto la
     * regla de "sin datos falsos", así que el blog no declara fechas y ordena
     * por este campo, que es determinista y curable a mano.
     */
    order: z.number().default(0),
    /**
     * Ficha de negocio de la que habla la guía, por id completo:
     * "seguridad-privada/sepri" (NO el nombre visible, NO el slug suelto).
     *
     * Antes era `z.string()` y guardaba el nombre ("SEPRI") mientras el código
     * comparaba contra el slug ("sepri"): las 9 guías que lo declaraban fallaban
     * el === en silencio y la feature nunca funcionó desde que existe.
     *
     * OJO: `reference()` NO valida en build — Astro solo comprueba que el id
     * exista cuando se llama `getEntry()`, así que un id inventado pasaría igual.
     * El guard real está en el getStaticPaths de blog/[categoria]/[slug].astro,
     * que sí rompe el build. Si mueves esa validación, este campo vuelve a poder
     * romperse en silencio.
     */
    relatedBusiness: reference('negocios').optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { negocios, blog };
