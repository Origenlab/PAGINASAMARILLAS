# Prompts para Claude en Chrome — Pamari (paginasamarillas.mx)

Tres tareas independientes. Copia el bloque que necesites, uno a la vez.
Generados el 2026-07-16, con `main` en `e36123c`.

---

## Contexto común (pégalo al inicio de cualquiera de los tres)

```
Trabajo en el sitio Pamari — https://paginasamarillas.mx

Datos que necesitas:
- Es un directorio de empresas en México. La empresa se llama PAMARI.
  El dominio sigue siendo paginasamarillas.mx a propósito: la marca cambió,
  el dominio no. NO reportes eso como error.
- Stack: Astro 6 estático, desplegado en GitHub Pages, con Cloudflare como
  proxy/CDN delante. Repo: Origenlab/PAGINASAMARILLAS.
- El sitio tiene 42 páginas: home, /categorias, /blog/, 3 páginas de
  categoría y ~16 fichas de negocio en /negocios/<categoria>/<slug>.
- Regla de diseño OBLIGATORIA del proyecto: PROHIBIDAS las animaciones y
  transiciones en todo el sitio. Única excepción: los botones (.btn), el
  botón hamburguesa y .blog-filters button. Imágenes, cards, links y menús
  cambian de estado de forma instantánea, sin transición.
- Otra regla: sin datos falsos. Nada de ratings inventados, badges falsos
  ni links muertos (href="#").
- Puedes verificar qué build sirve el dominio en:
  https://paginasamarillas.mx/build-id.txt  → debe devolver e36123c...
```

---

## 1. Cloudflare — Rocket Loader

```
[PEGA AQUÍ EL CONTEXTO COMÚN]

TAREA: diagnosticar si Cloudflare Rocket Loader está rompiendo el sitio.

Qué sabemos ya:
- Rocket Loader ESTÁ activo. El HTML en vivo llega con los scripts
  reescritos así: <script type="73a790cbcb72f2bb12e4d5d1-text/javascript">
  Ese type falso es la firma de Rocket Loader: impide que el navegador
  ejecute el script hasta que Rocket Loader decida.
- El buscador de la home es JS inline: un array `searchIndex` y un IIFE que
  usa los ids #searchInput, #searchResults y #searchForm.
- También hay email obfuscation de Cloudflare activa: los mailto salen como
  /cdn-cgi/l/email-protection y un <span class="__cf_email__">.

PASO 1 — Diagnóstico ANTES de tocar nada (esto es lo importante):
  a) Abre https://paginasamarillas.mx/ y escribe "sepri" en el buscador.
     ¿Aparecen resultados? ¿Cuánto tarda? Repite con "extintores".
  b) Abre la consola y reporta CUALQUIER error de JS.
  c) Comprueba si el email del topbar y del footer se ve como un email real
     o como "[email protected]".
  d) Compara: vuelve a cargar con ?nocf=1 o desde una ventana de incógnito y
     mira si el comportamiento cambia.
  e) Mide el tiempo hasta que el buscador responde al primer tecleo.

PASO 2 — Panel de Cloudflare (dashboard.cloudflare.com, zona
paginasamarillas.mx). SOLO MIRA Y REPÓRTAME, no cambies nada todavía:
  - Speed → Optimization: estado de Rocket Loader, Auto Minify, Early Hints,
    Brotli.
  - Caching → Configuration: Caching Level y Browser Cache TTL.
  - Rules / Page Rules: cualquier regla que afecte a /css/ o a *.css
  - SSL/TLS: modo (debe ser Full o Full strict, no Flexible).

IMPORTANTE — NO cambies ninguna configuración por tu cuenta. Repórtame el
diagnóstico y tu recomendación, y espera mi OK explícito antes de tocar
cualquier toggle. Si algo requiere confirmación, pregúntame.

Contexto para tu recomendación: el sitio ya sirve el CSS versionado por hash
(/css/style.css?v=<hash>), así que un Browser Cache TTL alto ya no causa
desincronización de estilos. El HTML va con max-age=600.
```

---

## 2. Google Search Console — reindexar tras el rebrand

```
[PEGA AQUÍ EL CONTEXTO COMÚN]

TAREA: acelerar la reindexación tras el cambio de marca a Pamari.

Qué cambió (todo ya está en vivo):
- La marca pasó de "Páginas Amarillas México" / "PáginasAmarillas.mx" a
  "Pamari". Google todavía indexa la marca vieja.
- Los <title> se reescribieron para poner la keyword al frente y sacar la
  marca. Ejemplos en vivo:
    /                              → Directorio de Empresas en México | Negocios Verificados
    /categorias                    → Categorías de Empresas en México | Directorio por Sector
    /categoria/seguridad-privada   → Empresas de Seguridad Privada en México | Directorio
    /blog/                         → Guías para Contratar Empresas en México | Blog
  Antes las 16 fichas tenían titles de 61 a 92 caracteres (truncados en el
  SERP). Ahora ninguna pasa de 60.

En Search Console (search.google.com/search-console), propiedad
paginasamarillas.mx:
  1. Sitemaps: confirma que https://paginasamarillas.mx/sitemap-index.xml
     está enviado y sin errores. Si aparece un sitemap.xml antiguo listado,
     dímelo: esa URL ahora da 404 a propósito.
  2. Inspección de URL + "Solicitar indexación" para, al menos:
     /  ,  /categorias  ,  /blog/  y las 3 de /categoria/*
  3. Cobertura / Páginas: reporta cualquier error nuevo.
  4. ESPERADO, no lo reportes como problema: estas 4 URLs ahora dan 404 a
     propósito (eran plantillas y archivos de respaldo que nunca debieron
     ser públicos):
       /blog/templates/article-template.html
       /blog/templates/card-template.html
       /negocios/entretenimiento/redeil-backup.html
       /negocios/entretenimiento/inflables-para-fiestas-backup.html
  5. Mejoras / Datos estructurados: verifica que el JSON-LD de la home valide.
     El publisher es Organization con telephone +525510053423 y sameAs a
     Facebook e Instagram. El handle de X se retiró porque daba 404.

Reporta qué enviaste y qué encontraste. No cambies configuración de la
propiedad ni añadas usuarios sin preguntarme.
```

---

## 3. QA visual — 42 páginas, desktop y móvil

```
[PEGA AQUÍ EL CONTEXTO COMÚN]

TAREA: QA visual. Solo mirar y reportar, NO tocar código ni configuración.

Revisa en DOS viewports: desktop (1440x900) y móvil (390x844).

Empieza SIEMPRE con recarga forzada (Cmd+Shift+R). El sitio tuvo un problema
de caché: el CSS viaja con max-age de 4 días y una versión vieja puede pintar
HTML nuevo con estilos viejos. Si ves algo raro, antes de reportarlo verifica
en la consola que el <link> del CSS termine en ?v=<hash> — si no lo lleva,
tienes HTML cacheado y hay que recargar de nuevo.

Páginas a revisar:
  /  ,  /categorias  ,  /blog/  ,  /sitemap
  /categoria/seguridad-privada , /categoria/entretenimiento ,
  /categoria/equipos-contra-incendios
  y al menos 3 fichas de /negocios/<categoria>/<slug>

Checklist:
  1. LOGO: header con imagen /images/logo-pamari.avif (fallback .webp),
     36px de alto, sin deformarse ni saltar al cargar. El footer usa un
     lockup de texto "Pamari" (Pa + mari en amarillo) — es intencional.
  2. TOPBAR: en desktop se ven "Guías", el teléfono 55 1005 3423 y el email.
     En MÓVIL debe verse SOLO el teléfono (es tap-to-call, el CTA de más
     valor); "Guías" y el email se ocultan a propósito.
  3. TELÉFONO: el link debe ser tel:+525510053423 y debe abrir la llamada.
  4. CARDS DE CATEGORÍA: 4 por fila en desktop. En móvil apiladas.
  5. ANIMACIONES: esto es lo más importante. Pasa el ratón por imágenes,
     cards, links del menú y del footer. NO debe haber ninguna transición,
     fade, zoom ni desplazamiento. El cambio de color/borde es instantáneo.
     Los ÚNICOS que sí pueden animarse son los botones y el hamburguesa.
     Reporta cualquier transición fuera de esos.
  6. BUSCADOR de la home: escribe "sepri", "extintores" e "inflables".
     ¿Salen resultados? ¿Los links funcionan?
  7. MENÚ HAMBURGUESA en móvil: abre, cierra, navega.
  8. FOOTER: solo deben verse los iconos de Facebook e Instagram. Si ves un
     icono de X/Twitter, repórtalo: se retiró porque daba 404.
  9. LINKS MUERTOS: cualquier href="#" o link que dé 404.
 10. IMÁGENES: alguna rota, deformada o sin cargar.
 11. CLS: ¿algo salta o se recoloca al cargar?

Reporta cada hallazgo con: página, viewport, qué esperabas, qué viste, y
captura. Ordénalos por gravedad. Si todo está bien, dilo claramente en vez
de inventar problemas menores.
```
