// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://paginasamarillas.mx',
  trailingSlash: 'never',
  build: {
    // 'preserve': foo.astro -> foo.html, foo/index.astro -> foo/index.html.
    // Mantiene las URLs .html de negocios/blog/categoría y sirve /blog/ como index.
    format: 'preserve',
  },
  integrations: [mdx(), sitemap()],
});
