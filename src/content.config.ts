import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// --- piezas reutilizables ---

const enlace = z.object({
  texto: z.string(),
  href: z.string().optional(),
});

const imagen = z.object({
  src: z.string(),
  alt: z.string().optional(),
});

const cta = z.object({
  texto: z.string(),
  href: z.string(),
  estilo: z.enum(['primary', 'outline']).default('outline'),
  icono: z.string().optional(),
});

// --- coleccion: negocios ---

const negocios = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/negocios' }),
  schema: z.object({
    // identidad
    nombre: z.string(),
    categoria: z.enum(['seguridad-privada', 'equipos-contra-incendios', 'entretenimiento']),
    categoriaNombre: z.string().optional(),
    slogan: z.string().optional(),
    tagline: z.string().optional(),
    descripcionLarga: z.string().optional(),

    // seo
    titulo: z.string(),
    descripcion: z.string(),
    keywords: z.array(z.string()).default([]),
    og: z
      .object({
        titulo: z.string().optional(),
        descripcion: z.string().optional(),
        imagen: z.string().optional(),
        tipo: z.string().default('business.business'),
      })
      .optional(),

    // datos duros -> alimentan schema.org
    contacto: z
      .object({
        telefono: z.string().optional(),
        email: z.string().optional(),
        sitioWeb: z.string().url().optional(),
        // numero destino del formulario de cotizacion (solo digitos, con lada 52)
        whatsapp: z.string().regex(/^\d{10,15}$/).optional(),
      })
      .default({}),
    direccion: z
      .object({
        calle: z.string().optional(),
        colonia: z.string().optional(),
        estado: z.string().optional(),
        cp: z.string().optional(),
        pais: z.string().default('MX'),
      })
      .optional(),
    geo: z.object({ lat: z.number(), lng: z.number() }).optional(),
    rating: z
      .object({
        valor: z.number().min(0).max(5),
        resenas: z.number().int().nonnegative(),
      })
      .optional(),
    priceRange: z.string().optional(),
    fundacion: z.string().optional(),
    empleados: z.union([z.string(), z.number()]).optional(),
    areaServed: z.array(z.object({ tipo: z.string(), nombre: z.string() })).default([]),
    sameAs: z.array(z.string()).default([]),

    // catalogo schema.org (hasOfferCatalog)
    catalogoNombre: z.string().optional(),
    catalogo: z
      .array(z.object({ nombre: z.string(), descripcion: z.string().optional() }))
      .default([]),

    // hero
    imagen: z.string().optional(),
    imagenAlt: z.string().optional(),
    badges: z.array(z.string()).default([]),
    galeria: z.array(imagen).default([]),
    ratingLink: enlace.optional(),
    quickInfo: z
      .array(z.object({ icono: z.string().optional(), titulo: z.string(), texto: z.string() }))
      .default([]),
    ctas: z.array(cta).default([]),

    // servicios
    serviciosTitulo: z.string().optional(),
    serviciosSubtitulo: z.string().optional(),
    servicios: z
      .array(
        z.object({
          icono: z.string().optional(),
          titulo: z.string(),
          descripcion: z.string().optional(),
          features: z.array(z.string()).default([]),
        })
      )
      .default([]),

    // sobre + stats (el cuerpo en prosa va en el body del .md)
    aboutTitulo: z.string().optional(),
    beneficiosTitulo: z.string().optional(),
    beneficios: z.array(z.string()).default([]),
    stats: z.array(z.object({ numero: z.string(), label: z.string() })).default([]),

    // cobertura
    coberturaTitulo: z.string().optional(),
    coberturaSubtitulo: z.string().optional(),
    cobertura: z
      .array(
        z.object({
          titulo: z.string(),
          items: z.array(z.object({ texto: z.string(), icono: z.string().optional() })).default([]),
        })
      )
      .default([]),

    // catalogo visual (solo 12 de 16 fichas lo tienen)
    directorioTitulo: z.string().optional(),
    directorioSubtitulo: z.string().optional(),
    directorioTabs: z
      .array(
        z.object({
          texto: z.string(),
          filtro: z.string(),
          icono: z.string().optional(),
          activo: z.boolean().default(false),
        })
      )
      .default([]),
    directorioCtaTexto: z.string().optional(),
    directorioCtaBotones: z.array(cta).default([]),
    directorio: z
      .array(
        z.object({
          filtro: z.string().optional(),
          imagen: z.string().optional(),
          imagenAlt: z.string().optional(),
          badge: z.string().optional(),
          badgeTipo: z.string().optional(),
          titulo: z.string(),
          tag: z.string().optional(),
          tagIcono: z.string().optional(),
          descripcion: z.string().optional(),
          features: z.array(z.string()).default([]),
          ubicacion: z.string().optional(),
          ctaTexto: z.string().optional(),
          ctaHref: z.string().optional(),
        })
      )
      .default([]),

    // sucursales
    ubicacionesTitulo: z.string().optional(),
    ubicacionesSubtitulo: z.string().optional(),
    ubicaciones: z
      .array(z.object({ nombre: z.string(), lineas: z.array(z.string()).default([]) }))
      .default([]),

    // contacto
    contactoTitulo: z.string().optional(),
    contactoSubtitulo: z.string().optional(),
    contactoItems: z
      .array(
        z.object({
          icono: z.string().optional(),
          titulo: z.string(),
          lineas: z.array(enlace).default([]),
        })
      )
      .default([]),

    // formulario de cotizacion
    formTitulo: z.string().optional(),
    formSubtitulo: z.string().optional(),
    formAction: z.string().optional(),
    formBoton: z.string().optional(),
    formCampos: z
      .array(
        z.object({
          name: z.string(),
          label: z.string().optional(),
          tipo: z.string().default('text'),
          requerido: z.boolean().default(false),
          placeholder: z.string().optional(),
          // value: '' es legitimo — es la opcion placeholder del select
          opciones: z.array(z.object({ value: z.string().default(''), texto: z.string() })).default([]),
        })
      )
      .default([]),

    // faq + resenas
    faqTitulo: z.string().optional(),
    faq: z.array(z.object({ pregunta: z.string(), respuesta: z.string() })).default([]),
    resenasTitulo: z.string().optional(),
    resenas: z
      .array(
        z.object({
          autor: z.string().optional(),
          avatar: z.string().optional(),
          texto: z.string(),
          rating: z.number().min(1).max(5).optional(),
          fecha: z.string().optional(),
          sitio: enlace.optional(),
        })
      )
      .default([]),

    // cta final
    ctaFinalTitulo: z.string().optional(),
    ctaFinalTexto: z.string().optional(),
    ctaFinalBotones: z.array(cta).default([]),

    // migracion: URL vieja .html -> para generar los 301
    legacyUrl: z.string(),
  }),
});

// --- coleccion: blog ---

const blog = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/blog' }),
  schema: z.object({
    // titulo = el <h1> visible
    titulo: z.string(),
    // headline = lo que va al schema.org. Solo presente cuando el original
    // tenia un headline distinto del h1; si falta, se usa titulo.
    headline: z.string().optional(),
    descripcion: z.string(),
    categoria: z.enum(['seguridad-privada', 'eventos']),
    // el <title> del HTML original, distinto del titulo del articulo
    seoTitle: z.string().optional(),
    keywords: z.array(z.string()).default([]),
    imagen: z.string().optional(),
    // cabecera: 42 de 51 articulos la traen; el resto solo titulo
    heroImagen: z.string().optional(),
    heroImagenAlt: z.string().optional(),
    gancho: z.string().optional(),
    badge: z.string().optional(),
    minutosLectura: z.number().int().positive().optional(),
    autor: z.string().default('Páginas Amarillas México'),
    publisher: z.string().default('Páginas Amarillas México'),
    publicado: z.coerce.date().optional(),
    modificado: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    // indice del original: etiquetas cortas curadas + anclas a los id de <Seccion>
    toc: z.array(z.object({ texto: z.string(), ancla: z.string() })).default([]),
    faq: z.array(z.object({ pregunta: z.string(), respuesta: z.string() })).default([]),
    legacyUrl: z.string(),
  }),
});

export const collections = { negocios, blog };
