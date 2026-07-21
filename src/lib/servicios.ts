/**
 * Helpers para los servicios de una ficha de negocio.
 * Un servicio puede declarar su propio `slug`; si no, se deriva del nombre.
 */

/**
 * Espejo del schema de `services[]` en content.config.ts.
 * Si se agrega un campo allá, agregarlo aquí: es lo que consumen
 * ServiceCard.astro y los templates L4/L5.
 */
export interface ServicioData {
  name: string;
  description: string;
  slug?: string;
  keyword?: string;
  image?: string;
  imageAlt?: string;
  badge?: string;
  heroIntro?: string[];
  highlights?: string[];
  detail?: string[];
  proceso?: { title: string; text: string }[];
  comparativa?: {
    title?: string;
    intro?: string;
    headers: string[];
    rows: string[][];
    note?: string;
  };
  casos?: { title: string; text: string }[];
  specs?: { label: string; value: string }[];
  requisitos?: { concepto: string; detalle: string }[];
  normativa?: { norma: string; titulo?: string; exige: string; implica?: string }[];
  faqs?: { q: string; a: string }[];
}

/** "Rastreo GPS / VEA" -> "rastreo-gps-vea" */
export function slugify(input: string): string {
  return input
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

export function servicioSlug(s: ServicioData): string {
  return s.slug?.trim() ? slugify(s.slug) : slugify(s.name);
}

export function servicioHref(categoria: string, negocio: string, s: ServicioData): string {
  return `/negocios/${categoria}/${negocio}/servicios/${servicioSlug(s)}`;
}

/**
 * Title SEO de una página de servicio, garantizado ≤ 60 caracteres.
 *
 * Google trunca alrededor de los 60. La plantilla fija
 * "{servicio} en {colonia}, {región} | {negocio}" se pasaba en 93 de las 99
 * páginas, así que se prueban variantes de mayor a menor y se toma la primera
 * que quepa: primero se sacrifica la marca, luego la región, luego la colonia.
 */
export function tituloServicio(opts: {
  servicio: string;
  negocio: string;
  locality: string;
  region: string;
}): string {
  const { servicio, negocio, locality, region } = opts;
  const candidatos = [
    `${servicio} en ${locality}, ${region} | ${negocio}`,
    `${servicio} en ${locality} | ${negocio}`,
    `${servicio} en ${locality}, ${region}`,
    `${servicio} en ${locality}`,
    `${servicio} | ${negocio}`,
    `${servicio} en ${region}`,
    servicio,
  ];
  const cabe = candidatos.find((c) => c.length <= 60);
  return cabe ?? `${servicio.slice(0, 57).trimEnd()}…`;
}

/**
 * Meta description ≤ 160. Si la descripción del servicio deja espacio,
 * se le añade la señal local (negocio + colonia) para diferenciarla del
 * texto visible y reforzar la relevancia geográfica.
 */
export function descripcionServicio(opts: {
  description: string;
  negocio: string;
  locality: string;
}): string {
  const { description, negocio, locality } = opts;
  const base = description.trim();
  const cola = ` ${negocio}, ${locality}.`;
  if (base.length + cola.length <= 160) return base + cola;
  if (base.length <= 160) return base;
  return `${base.slice(0, 157).trimEnd()}…`;
}
