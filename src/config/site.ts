export const site = {
  name: 'Pamari',
  shortName: 'Pamari',
  url: 'https://paginasamarillas.mx',
  locale: 'es-MX',
  lang: 'es-MX',
  description:
    'Encuentra empresas y negocios en México. Directorio completo con direcciones, teléfonos, horarios y reseñas verificadas. Miles de empresas mexicanas en un solo lugar.',
  email: 'contacto@paginasamarillas.mx',
  phone: '55 1005 3423',
  phoneHref: '+525510053423',
  geo: { lat: 19.432608, lng: -99.133209 },
  ogImage: 'https://paginasamarillas.mx/images/og-image.webp',
  social: {
    facebook: 'https://www.facebook.com/paginasamarillas.mx',
    twitter: 'https://twitter.com/paginasamx',
    instagram: 'https://www.instagram.com/paginasamarillas.mx',
  },
} as const;

export interface Category {
  id: string;
  name: string;
  slug: string;
  color: string;
  icon: string;
  description: string;
  services: string;
  count: number;
  imagesFolder: string;
  image?: string;
  /** 2 párrafos SEO para el section-head--split de la página de categoría */
  seoIntro?: [string, string];
  /** Slug de la categoría correspondiente en el blog (si difiere) */
  blogSlug?: string;
}

export const categories: Category[] = [
  {
    id: 'seguridad-privada',
    name: 'Seguridad Privada',
    slug: 'seguridad-privada',
    color: '#dc2626',
    icon: 'shield',
    description:
      'Empresas certificadas de vigilancia, guardias de seguridad, escoltas ejecutivos y protección empresarial en todo México.',
    services:
      'Guardias armados y sin armar, monitoreo 24/7, seguridad para eventos, condominios, corporativos e industrial.',
    count: 4,
    imagesFolder: 'img-seguridad-privada',
    image: '/img/img-seguridad-privada/equipo-seguridad-corporativo.webp',
    seoIntro: [
      'Contratar seguridad privada en México es una decisión de confianza: le abres la puerta de tu empresa, condominio o evento a un tercero. Por eso cada empresa de esta categoría fue verificada — registro, teléfonos, domicilio y servicios reales — antes de publicarse en el directorio.',
      'Compara guardias intramuros, escoltas, monitoreo 24/7, CCTV y seguridad para eventos en CDMX, Estado de México y el resto del país. Revisa la ficha de cada empresa, sus certificaciones CNSP y contáctala directo por teléfono o WhatsApp, sin intermediarios.',
    ],
  },
  {
    id: 'entretenimiento',
    name: 'Entretenimiento',
    slug: 'entretenimiento',
    color: '#f59e0b',
    icon: 'star',
    description:
      'Las mejores empresas de entretenimiento para fiestas infantiles, eventos corporativos, bodas y celebraciones en México.',
    services:
      'Inflables, brincolines, shows de luces, DJ, sonido, animadores, payasos, magos y decoración para eventos.',
    count: 7,
    imagesFolder: 'img-eventos',
    image: '/img/img-eventos/decoracion-fiesta-luces.webp',
    seoIntro: [
      'Organizar un evento en México — boda, XV años, fiesta infantil o evento corporativo — depende de elegir bien a los proveedores. En esta categoría encontrarás empresas de entretenimiento verificadas: audio profesional, iluminación, inflables, mobiliario y producción de eventos con datos de contacto reales.',
      'Cada ficha incluye servicios, cobertura y experiencia comprobable, para que cotices directo con la empresa sin comisiones ni intermediarios. Complementa tu decisión con las guías del blog: costos reales, checklists de contratación y comparativas de equipos.',
    ],
    blogSlug: 'eventos',
  },
  {
    id: 'equipos-contra-incendios',
    name: 'Equipos Contra Incendios',
    slug: 'equipos-contra-incendios',
    color: '#dc2626',
    icon: 'flame',
    description:
      'Proveedores certificados de extintores, sistemas contra incendios, detectores de humo y equipos de protección en México.',
    services:
      'Extintores CO2, PQS, agua, sistemas automáticos, gabinetes, mangueras, señalización y capacitación NOM-002-STPS.',
    count: 5,
    imagesFolder: 'img-equipos-contra-incendios',
    image: '/img/img-equipos-contra-incendios/sistemas-incendios.webp',
    seoIntro: [
      'La protección contra incendios en México no es opcional: la NOM-002-STPS obliga a todo centro de trabajo a contar con extintores, señalización y brigadas según su nivel de riesgo. Aquí encontrarás proveedores verificados de equipos contra incendios que te ayudan a cumplir la norma.',
      'Compara empresas de extintores CO2, PQS y agua, sistemas fijos, detección de humo, gabinetes y capacitación de brigadas. Todas con teléfono, domicilio y servicios confirmados — cotiza directo y documenta tu cumplimiento ante Protección Civil.',
    ],
  },
];

export function getCategory(slug: string): Category | undefined {
  return categories.find((c) => c.slug === slug);
}

/**
 * Categorías próximas, priorizadas según docs/ESTUDIO-CATEGORIAS.md
 * (INEGI Censos Económicos 2024 / DENUE + demanda de búsqueda local).
 * Orden = orden de lanzamiento.
 */
export interface UpcomingCategory {
  name: string;
  slug: string;
  icon: string;
  description: string;
  services: string;
}

export const upcomingCategories: UpcomingCategory[] = [
  {
    name: 'Salud y Medicina',
    slug: 'salud-y-medicina',
    icon: 'health',
    description: 'Médicos especialistas, dentistas, clínicas, laboratorios y farmacias.',
    services: 'Consultorios, urgencias, laboratorios clínicos, imagenología, farmacias y especialidades médicas.',
  },
  {
    name: 'Automotriz',
    slug: 'automotriz',
    icon: 'car',
    description: 'Mecánicos, hojalatería y pintura, refaccionarias, grúas y agencias.',
    services: 'Afinación, frenos, suspensión, hojalatería y pintura, refacciones, grúas 24/7 y agencias.',
  },
  {
    name: 'Construcción y Remodelación',
    slug: 'construccion',
    icon: 'build',
    description: 'Constructoras, arquitectos, ingenieros, materiales y acabados.',
    services: 'Obra nueva, remodelaciones, acabados, estructuras, materiales y proyectos llave en mano.',
  },
  {
    name: 'Plomería y Electricidad',
    slug: 'plomeria-electricidad',
    icon: 'tool',
    description: 'Plomeros, electricistas, cerrajeros y reparaciones urgentes.',
    services: 'Fugas, instalaciones hidráulicas, cableado, tableros eléctricos, cerrajería y emergencias 24/7.',
  },
  {
    name: 'Restaurantes y Banquetes',
    slug: 'restaurantes',
    icon: 'food',
    description: 'Restaurantes, taquerías, cafeterías, banquetes y catering.',
    services: 'Cocina mexicana e internacional, banquetes para eventos, catering empresarial y cafeterías.',
  },
  {
    name: 'Abogados y Notarías',
    slug: 'abogados-notarias',
    icon: 'law',
    description: 'Despachos jurídicos, notarías públicas y asesoría legal.',
    services: 'Derecho civil, mercantil, laboral, penal, fiscal, notarías y consultoría corporativa.',
  },
  {
    name: 'Tecnología y Sistemas',
    slug: 'tecnologia-sistemas',
    icon: 'tech',
    description: 'CCTV, redes, soporte TI, desarrollo de software y ciberseguridad.',
    services: 'CCTV y videovigilancia, redes, soporte TI, desarrollo de software y ciberseguridad empresarial.',
  },
  {
    name: 'Limpieza y Fumigación',
    slug: 'limpieza-fumigacion',
    icon: 'clean',
    description: 'Limpieza empresarial, control de plagas y sanitización.',
    services: 'Limpieza de oficinas e industrial, fumigación certificada, sanitización y control de plagas.',
  },
  {
    name: 'Mudanzas y Fletes',
    slug: 'mudanzas-fletes',
    icon: 'truck',
    description: 'Mudanzas locales y foráneas, fletes y transporte de carga.',
    services: 'Mudanzas residenciales y de oficina, fletes locales y foráneos, embalaje y maniobras.',
  },
  {
    name: 'Veterinarias y Mascotas',
    slug: 'veterinarias',
    icon: 'pet',
    description: 'Clínicas veterinarias, estéticas caninas y tiendas de mascotas.',
    services: 'Consulta, vacunación, cirugía, estética canina, hospitalización y alimentos especializados.',
  },
  {
    name: 'Belleza y Cuidado Personal',
    slug: 'belleza',
    icon: 'beauty',
    description: 'Salones de belleza, barberías, spas y estéticas.',
    services: 'Corte y color, barbería, uñas, spa, maquillaje y tratamientos faciales y corporales.',
  },
  {
    name: 'Educación y Capacitación',
    slug: 'educacion',
    icon: 'edu',
    description: 'Escuelas, universidades, idiomas y capacitación empresarial.',
    services: 'Colegios, universidades, idiomas, cursos técnicos y capacitación empresarial.',
  },
];
