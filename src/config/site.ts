export const site = {
  name: 'Páginas Amarillas México',
  shortName: 'PáginasAmarillas.mx',
  url: 'https://paginasamarillas.mx',
  locale: 'es-MX',
  lang: 'es-MX',
  description:
    'Encuentra empresas y negocios en México. Directorio completo con direcciones, teléfonos, horarios y reseñas verificadas. Miles de empresas mexicanas en un solo lugar.',
  email: 'contacto@paginasamarillas.mx',
  phone: '55 5555 5555',
  phoneHref: '+525555555555',
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
    imagesFolder: 'img-incendios',
  },
];

export function getCategory(slug: string): Category | undefined {
  return categories.find((c) => c.slug === slug);
}
