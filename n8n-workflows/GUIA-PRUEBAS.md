# Guia de Pruebas - Workflow Blog Paginas Amarillas

Checklist completo para validar el funcionamiento del workflow antes de activarlo en produccion.

---

## PRE-REQUISITOS DE PRUEBAS

### Verificar Archivos Base

- [ ] `blog/blog-config.json` existe y es JSON valido
- [ ] `blog/index.html` contiene marcador `<!-- n8n:INSERT-NEW-CARDS-HERE -->`
- [ ] Carpeta `blog/seguridad-privada/` existe
- [ ] Imagenes existen en `img/img-seguridad-privada/`

### Verificar Credenciales

- [ ] GitHub API configurada y conectada
- [ ] OpenAI API configurada con saldo disponible
- [ ] Telegram Bot creado y Chat ID obtenido
- [ ] Google Sheets conectado (opcional)

### Verificar Variables

- [ ] `GITHUB_OWNER` configurada
- [ ] `GITHUB_REPO` configurada
- [ ] `TELEGRAM_CHAT_ID` configurada
- [ ] `GOOGLE_SHEET_ID` configurada (si aplica)

---

## PRUEBA 1: OBTENER CONFIGURACION

### Objetivo
Verificar que el workflow puede leer `blog-config.json` de GitHub.

### Pasos
1. Click en nodo `GitHub - Obtener Configuracion`
2. Click **Test step**

### Resultado Esperado
```json
{
  "version": "2.0",
  "categories": [...],
  "businesses": {...},
  "articleTypes": [...],
  "images": {...}
}
```

### Criterios de Exito
- [ ] Respuesta HTTP 200
- [ ] JSON parseado correctamente
- [ ] Contiene `categories` con al menos 1 elemento
- [ ] Contiene `businesses.seguridad-privada` con al menos 1 empresa

### Troubleshooting
| Problema | Solucion |
|----------|----------|
| 404 Not Found | Verificar ruta del archivo |
| 401 Unauthorized | Regenerar token GitHub |
| JSON invalido | Validar blog-config.json en jsonlint.com |

---

## PRUEBA 2: PROCESAR CONFIGURACION

### Objetivo
Verificar la seleccion aleatoria de empresa, tipo y imagenes.

### Pasos
1. Ejecutar primero Prueba 1
2. Click en nodo `Code - Procesar Configuracion`
3. Click **Test step**

### Resultado Esperado
```json
{
  "config": {...},
  "category": {
    "id": "seguridad-privada",
    "name": "Seguridad Privada",
    "slug": "seguridad-privada"
  },
  "business": {
    "id": "origins-private-security",
    "name": "ORIGINS Private Security",
    "services": ["vigilancia", "escoltas", ...]
  },
  "articleType": {
    "id": "resena-completa",
    "name": "Resena Completa"
  },
  "heroImage": "equipo-seguridad-corporativo.webp",
  "galleryImages": ["img1.webp", "img2.webp", ...],
  "dateISO": "2024-12-28",
  "slugUnique": "origins-private-security-resena-completa-..."
}
```

### Criterios de Exito
- [ ] `business` no es null
- [ ] `articleType` no es null
- [ ] `heroImage` existe en la lista de imagenes
- [ ] `galleryImages` tiene al menos 4 elementos
- [ ] `slugUnique` es unico (contiene timestamp)

---

## PRUEBA 3: GENERAR CONTENIDO CON OPENAI

### Objetivo
Verificar la generacion de contenido SEO con GPT-4o.

### Pasos
1. Ejecutar Prueba 1 y 2
2. Click en nodo `OpenAI - Generar Articulo`
3. Click **Test step**
4. **Esperar 30-60 segundos**

### Resultado Esperado
JSON con estructura:
```json
{
  "title": "ORIGINS Private Security: Resena Completa 2024",
  "titleShort": "Resena ORIGINS",
  "slug": "origins-private-security-resena-completa-2024",
  "metaDescription": "Descripcion de 150-160 caracteres...",
  "keywords": "seguridad privada, CDMX, escoltas...",
  "readingTime": 10,
  "wordCount": 2500,
  "heroHook": "Parrafo enganchador de 60-80 palabras...",
  "tocItems": [...],
  "sections": [...],
  "statModule": {...},
  "tipModule": {...},
  "faqs": [...],
  "excerpt": "Extracto de 80-120 caracteres..."
}
```

### Criterios de Exito
- [ ] Respuesta recibida sin errores
- [ ] JSON valido y parseable
- [ ] `title` < 70 caracteres
- [ ] `metaDescription` entre 150-160 caracteres
- [ ] `sections` tiene 5-6 elementos
- [ ] `faqs` tiene 5 preguntas
- [ ] Contenido en espanol mexicano
- [ ] Sin emojis en el contenido

### Troubleshooting
| Problema | Solucion |
|----------|----------|
| Rate limit | Esperar o aumentar plan OpenAI |
| JSON invalido | Revisar prompt, agregar ejemplos |
| Timeout | Aumentar timeout en nodo HTTP |
| Contenido corto | Ajustar wordCount minimo en prompt |

---

## PRUEBA 4: CONSTRUIR HTML

### Objetivo
Verificar la construccion del HTML completo del articulo.

### Pasos
1. Ejecutar Pruebas 1-3
2. Click en nodo `Code - Construir HTML Articulo`
3. Click **Test step**

### Resultado Esperado
HTML completo que incluye:
- DOCTYPE y estructura base
- Meta tags SEO
- Open Graph y Twitter Cards
- Schema.org Article y FAQPage
- Hero section de dos columnas
- Contenido con secciones H2
- Modulos (stat, tip, quote, alert)
- Galeria de imagenes
- FAQ accordion
- CTA final
- Footer

### Criterios de Exito
- [ ] HTML valido (sin errores de sintaxis)
- [ ] Meta description presente
- [ ] Schema.org Article presente
- [ ] Schema.org FAQPage presente
- [ ] 5 FAQs en accordion
- [ ] Galeria con 4 imagenes
- [ ] Todos los placeholders reemplazados (sin `{{}}`)

### Validacion Manual
1. Copiar HTML del output
2. Pegar en [validator.w3.org](https://validator.w3.org/#validate_by_input)
3. Verificar 0 errores criticos

---

## PRUEBA 5: CONSTRUIR CARD

### Objetivo
Verificar la construccion de la card para blog/index.html.

### Pasos
1. Ejecutar Pruebas 1-4
2. Click en nodo `Code - Construir Card HTML`
3. Click **Test step**

### Resultado Esperado
```html
<!-- n8n:AUTO - ORIGINS Private Security - 2024-12 -->
<article class="blog-card">
  <a href="/blog/seguridad-privada/slug.html" class="blog-card-image">
    <img src="/img/img-seguridad-privada/imagen.webp" alt="...">
    <span class="blog-category-badge">Seguridad Privada</span>
  </a>
  <div class="blog-card-content">
    <h3 class="blog-card-title">
      <a href="...">Titulo del Articulo</a>
    </h3>
    <div class="blog-meta">...</div>
    <p class="blog-card-excerpt">Extracto...</p>
    <a href="..." class="btn btn-outline">Leer articulo completo</a>
  </div>
</article>
```

### Criterios de Exito
- [ ] Comentario n8n:AUTO presente
- [ ] Clase `blog-card` correcta
- [ ] URL del articulo correcta
- [ ] Imagen con ruta correcta
- [ ] Badge de categoria presente
- [ ] Excerpt de longitud apropiada

---

## PRUEBA 6: SUBIR ARTICULO A GITHUB

### Objetivo
Verificar que el articulo se sube correctamente al repositorio.

### Pasos
1. Ejecutar Pruebas 1-5
2. Click en nodo `GitHub - Subir Articulo`
3. Click **Test step**

### Resultado Esperado
```json
{
  "content": {
    "name": "slug-del-articulo.html",
    "path": "blog/seguridad-privada/slug-del-articulo.html",
    "sha": "abc123...",
    "html_url": "https://github.com/..."
  },
  "commit": {
    "message": "Add article: Titulo del Articulo"
  }
}
```

### Criterios de Exito
- [ ] Respuesta HTTP 201 (Created)
- [ ] Archivo creado en ruta correcta
- [ ] SHA generado
- [ ] Commit realizado

### Verificacion Manual
1. Ir a GitHub > Repositorio > blog/seguridad-privada/
2. Verificar que el archivo existe
3. Abrir y verificar contenido

---

## PRUEBA 7: INSERTAR CARD EN INDEX

### Objetivo
Verificar la insercion de card en blog/index.html.

### Pasos
1. Ejecutar Pruebas 1-6
2. Click en nodo `GitHub - Obtener blog/index.html`
3. Click **Test step**
4. Click en nodo `Code - Insertar Card`
5. Click **Test step**

### Resultado Esperado
El HTML de blog/index.html ahora contiene:
```html
<!-- n8n:INSERT-NEW-CARDS-HERE -->

<!-- n8n:AUTO - ORIGINS Private Security - 2024-12 -->
<article class="blog-card">
  ...
</article>

<!-- Cards anteriores -->
```

### Criterios de Exito
- [ ] Marcador encontrado
- [ ] Card insertada despues del marcador
- [ ] Cards anteriores preservadas
- [ ] HTML valido

---

## PRUEBA 8: ACTUALIZAR INDEX EN GITHUB

### Objetivo
Verificar que blog/index.html se actualiza correctamente.

### Pasos
1. Ejecutar Pruebas 1-7
2. Click en nodo `GitHub - Actualizar blog/index.html`
3. Click **Test step**

### Resultado Esperado
```json
{
  "content": {
    "name": "index.html",
    "path": "blog/index.html",
    "sha": "nuevo-sha..."
  },
  "commit": {
    "message": "Add card for: Titulo del Articulo"
  }
}
```

### Criterios de Exito
- [ ] Respuesta HTTP 200 (Updated)
- [ ] SHA actualizado
- [ ] Commit realizado

### Verificacion Manual
1. Ir a GitHub > blog/index.html
2. Ver historial de commits
3. Verificar que la card aparece primero en el grid

---

## PRUEBA 9: REGISTRO EN GOOGLE SHEETS

### Objetivo
Verificar el logging de ejecuciones.

### Pasos
1. Ejecutar Pruebas 1-8
2. Click en nodo `Google Sheets - Log`
3. Click **Test step**

### Resultado Esperado
Nueva fila en el Sheet con:
| fecha | empresa | articulo | slug | tipo | url | status |
|-------|---------|----------|------|------|-----|--------|
| 2024-12-28 09:00:00 | ORIGINS | Titulo... | slug | Resena | https://... | success |

### Criterios de Exito
- [ ] Fila agregada correctamente
- [ ] Todos los campos completos
- [ ] URL valida
- [ ] Status = "success"

---

## PRUEBA 10: NOTIFICACION TELEGRAM

### Objetivo
Verificar el envio de notificacion.

### Pasos
1. Ejecutar Pruebas 1-9
2. Click en nodo `Telegram - Notificar`
3. Click **Test step**

### Resultado Esperado
Mensaje en Telegram:
```
✅ Nuevo Articulo Publicado

📝 ORIGINS Private Security: Resena Completa 2024

🏢 Empresa: ORIGINS Private Security
📁 Tipo: Resena Completa
⏱️ Lectura: 10 min

🔗 Ver Articulo

📊 Keywords: seguridad privada, CDMX...
```

### Criterios de Exito
- [ ] Mensaje recibido en Telegram
- [ ] Formato Markdown correcto
- [ ] Link clickeable
- [ ] Informacion completa

---

## PRUEBA COMPLETA E2E

### Objetivo
Ejecutar el workflow completo de principio a fin.

### Pasos
1. Agregar nodo **Manual Trigger** al inicio
2. Conectar a `GitHub - Obtener Configuracion`
3. Click **Execute Workflow**
4. Esperar finalizacion (2-5 minutos)

### Verificacion
1. Todos los nodos en verde
2. Articulo creado en GitHub
3. Card visible en blog/index.html
4. Registro en Google Sheets
5. Notificacion en Telegram

---

## CHECKLIST FINAL ANTES DE PRODUCCION

### Configuracion
- [ ] Variables de entorno configuradas
- [ ] Credenciales conectadas a todos los nodos
- [ ] Schedule Trigger configurado (cada 3 dias)
- [ ] Timezone correcto

### Archivos
- [ ] blog-config.json actualizado con todas las empresas
- [ ] Todas las imagenes subidas
- [ ] Templates en su lugar
- [ ] Marcadores en blog/index.html

### Pruebas
- [ ] 10 pruebas individuales pasadas
- [ ] 1 prueba E2E exitosa
- [ ] Articulo de prueba verificado visualmente
- [ ] Limpieza de articulo de prueba (si es necesario)

### Monitoreo
- [ ] Notificaciones de error configuradas
- [ ] Google Sheets accesible
- [ ] Dashboard de n8n accesible

---

## METRICAS DE EXITO

| Metrica | Objetivo | Como Medir |
|---------|----------|------------|
| Tasa de exito | > 95% | Executions exitosas / Total |
| Tiempo de ejecucion | < 3 min | n8n Execution time |
| Calidad contenido | > 8/10 | Revision manual |
| SEO Score | > 80 | PageSpeed Insights |
| Errores criticos | 0 | Logs de error |

---

*Guia de Pruebas v2.0 - Diciembre 2024*
