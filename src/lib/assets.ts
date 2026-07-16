import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

/**
 * Cache-busting de los assets de `public/`.
 *
 * Astro copia `public/` verbatim: la URL `/css/style.css` NUNCA cambia entre
 * deploys, pero se sirve con `cache-control: max-age=345600` (4 días). Un
 * visitante recurrente se queda con el CSS viejo hasta 4 días y ve el HTML
 * nuevo pintado con estilos viejos.
 *
 * Solución: colgar `?v=<hash del contenido>` del link. El hash sale del
 * archivo, no del commit, así que la URL sólo cambia cuando el CSS cambia
 * de verdad — un deploy que no toca el CSS conserva el caché del visitante.
 *
 * Se evalúa en build (SSG), así que no cuesta nada en runtime.
 */
const cache = new Map<string, string>();

function contentHash(publicPath: string): string {
  const cached = cache.get(publicPath);
  if (cached) return cached;

  // process.cwd() = raíz del proyecto durante `astro dev` y `astro build`.
  // (No usar import.meta.url: Vite empaqueta este módulo y la ruta no resuelve.)
  const abs = join(process.cwd(), 'public', publicPath);

  let hash: string;
  try {
    hash = createHash('sha256').update(readFileSync(abs)).digest('hex').slice(0, 8);
  } catch {
    // Si el archivo no existe, no rompemos el build: se sirve sin versionar,
    // exactamente como antes. Avisamos para que no pase inadvertido.
    console.warn(`[assets] no se pudo versionar ${publicPath} (${abs}) — se sirve sin ?v=`);
    hash = '';
  }

  cache.set(publicPath, hash);
  return hash;
}

/**
 * Devuelve la ruta con `?v=<hash>` si el archivo existe en `public/`.
 * Las URLs absolutas (CDN, fuentes) se devuelven intactas.
 */
export function versioned(publicPath: string): string {
  if (/^https?:\/\//.test(publicPath)) return publicPath;
  const hash = contentHash(publicPath);
  return hash ? `${publicPath}?v=${hash}` : publicPath;
}
