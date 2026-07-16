import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const negocios = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/negocios' }),
  schema: z.object({
    name: z.string(),
    categoryName: z.string(),
    title: z.string(),
    description: z.string(),
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
    title: z.string(),
    description: z.string(),
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
