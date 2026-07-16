// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://paginasamarillas.mx',
  // 'ignore': acepta /blog y /blog/ (GitHub Pages sirve ambos; en dev no rompe /blog/)
  trailingSlash: 'ignore',
  build: {
    // 'preserve': foo.astro -> foo.html, foo/index.astro -> foo/index.html.
    // Los archivos .html se conservan en disco (las URLs viejas con .html siguen
    // respondiendo en GitHub Pages), pero TODOS los links internos, canonicals y
    // el sitemap usan URLs limpias SIN .html — GitHub Pages resuelve /foo -> foo.html.
    format: 'preserve',
  },
  integrations: [
    mdx(),
    sitemap({
      // URLs limpias en el sitemap (sin .html), consistentes con los canonicals.
      serialize(item) {
        item.url = item.url.replace(/\.html$/, '');
        return item;
      },
    }),
  ],
});
