import { defineCollection, z } from 'astro:content';
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
    services: z
      .array(z.object({ name: z.string(), description: z.string() }))
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
    publishDate: z.coerce.date().optional(),
    updatedDate: z.coerce.date().optional(),
    relatedBusiness: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { negocios, blog };
