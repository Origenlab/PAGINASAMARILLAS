// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import mdx from '@astrojs/mdx';

// 4 articulos del blog eran archivos de 0 bytes que servian 200 con la pagina
// en blanco. Cada uno ya tenia un equivalente escrito, asi que en vez de
// rellenarlos (habria dado 4 URLs peleando por la misma busqueda) se redirigen
// al articulo mas completo de su grupo.
const B = '/blog/seguridad-privada';
const vaciosADestino = {
  'resena-origins-private-security': 'origins-private-security-resena',
  'resena-sepri-seguridad-cdmx': 'resena-completa-sepri-cdmx',
  'guia-servicios-sepri-cdmx': 'guia-servicios-seguridad-residencial-sepri',
  'guia-servicios-seguridad-cdmx': 'guia-completa-seguridad-privada-mexico',
};

// Las URLs indexadas llevan .html; la version sin extension tambien resuelve.
const redirects = {};
for (const [viejo, nuevo] of Object.entries(vaciosADestino)) {
  redirects[`${B}/${viejo}.html`] = `${B}/${nuevo}`;
  redirects[`${B}/${viejo}`] = `${B}/${nuevo}`;
}

export default defineConfig({
  site: 'https://paginasamarillas.mx',
  trailingSlash: 'never',
  build: {
    // 'preserve': index.astro -> /blog/index.html, y el resto -> /x/y.html.
    // Con 'file' el indice del blog salia en /blog.html y los 208 enlaces
    // internos a /blog/ se rompian.
    format: 'preserve',
  },
  redirects,
  integrations: [sitemap(), mdx()],
});
