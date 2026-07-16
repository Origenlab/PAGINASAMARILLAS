import { site } from '@config/site';

export type JsonLd = Record<string, unknown>;

/** Serialize JSON-LD for injection via `set:html`. */
export function jsonLdScript(data: JsonLd | JsonLd[]): string {
  return JSON.stringify(data);
}

export function breadcrumb(items: { name: string; url: string }[]): JsonLd {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((it, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: it.name,
      item: it.url,
    })),
  };
}

export function websiteJsonLd(): JsonLd {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: site.name,
    alternateName: site.shortName,
    url: `${site.url}/`,
    description: site.description,
    inLanguage: site.locale,
  };
}

export function organizationJsonLd(): JsonLd {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: site.name,
    url: `${site.url}/`,
    email: site.email,
    sameAs: [site.social.facebook, site.social.twitter, site.social.instagram],
  };
}

export interface NegocioSeo {
  name: string;
  description: string;
  url: string;
  image: string;
  telephone?: string;
  email?: string;
  address: {
    street: string;
    locality: string;
    region: string;
    postalCode?: string;
    country?: string;
  };
  geo?: { lat: number; lng: number };
  hours?: { days: string[]; opens: string; closes: string }[];
  areaServed?: string[];
  priceRange?: string;
  slogan?: string;
  foundingDate?: string;
  employees?: number;
  services?: { name: string; description: string }[];
}

/**
 * LocalBusiness JSON-LD.
 * NOTE: aggregateRating / reviews are intentionally omitted — no fabricated
 * reviews are ever emitted (regla canónica OrigenLab).
 */
export function localBusiness(n: NegocioSeo): JsonLd {
  return {
    '@context': 'https://schema.org',
    '@type': 'LocalBusiness',
    '@id': n.url,
    name: n.name,
    description: n.description,
    url: n.url,
    image: [n.image],
    ...(n.telephone ? { telephone: n.telephone } : {}),
    ...(n.email ? { email: n.email } : {}),
    address: {
      '@type': 'PostalAddress',
      streetAddress: n.address.street,
      addressLocality: n.address.locality,
      addressRegion: n.address.region,
      ...(n.address.postalCode ? { postalCode: n.address.postalCode } : {}),
      addressCountry: n.address.country ?? 'MX',
    },
    ...(n.geo
      ? {
          geo: {
            '@type': 'GeoCoordinates',
            latitude: String(n.geo.lat),
            longitude: String(n.geo.lng),
          },
        }
      : {}),
    ...(n.priceRange ? { priceRange: n.priceRange } : {}),
    ...(n.slogan ? { slogan: n.slogan } : {}),
    ...(n.foundingDate ? { foundingDate: n.foundingDate } : {}),
    ...(typeof n.employees === 'number'
      ? {
          numberOfEmployees: {
            '@type': 'QuantitativeValue',
            value: String(n.employees),
          },
        }
      : {}),
    ...(n.hours && n.hours.length
      ? {
          openingHoursSpecification: n.hours.map((h) => ({
            '@type': 'OpeningHoursSpecification',
            dayOfWeek: h.days,
            opens: h.opens,
            closes: h.closes,
          })),
        }
      : {}),
    ...(n.areaServed && n.areaServed.length
      ? { areaServed: n.areaServed.map((a) => ({ '@type': 'Place', name: a })) }
      : {}),
    ...(n.services && n.services.length
      ? {
          hasOfferCatalog: {
            '@type': 'OfferCatalog',
            name: `Servicios de ${n.name}`,
            itemListElement: n.services.map((s) => ({
              '@type': 'Offer',
              itemOffered: {
                '@type': 'Service',
                name: s.name,
                description: s.description,
              },
            })),
          },
        }
      : {}),
  };
}

export function faqPage(faqs: { q: string; a: string }[]): JsonLd {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((f) => ({
      '@type': 'Question',
      name: f.q,
      acceptedAnswer: { '@type': 'Answer', text: f.a },
    })),
  };
}

export interface ArticleSeo {
  title: string;
  description: string;
  url: string;
  image?: string;
  author?: string;
  datePublished?: string;
  dateModified?: string;
}

export function article(a: ArticleSeo): JsonLd {
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: a.title,
    description: a.description,
    mainEntityOfPage: a.url,
    ...(a.image ? { image: [a.image] } : {}),
    author: { '@type': 'Organization', name: a.author ?? site.name },
    publisher: {
      '@type': 'Organization',
      name: site.name,
      url: `${site.url}/`,
    },
    ...(a.datePublished ? { datePublished: a.datePublished } : {}),
    ...(a.dateModified ? { dateModified: a.dateModified } : {}),
    inLanguage: site.locale,
  };
}
