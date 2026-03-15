import sitemap from '@astrojs/sitemap';// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://paginasamarillas.mx',
  trailingSlash: 'never',
  build: {
    format: 'file',
  },
  integrations: [sitemap()],
});
