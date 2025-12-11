# Guía de Diseño y Estilo para Artículos de Blog
## Páginas Amarillas México

---

## 📋 ESTRUCTURA OBLIGATORIA DE ARTÍCULOS

### 1. **Header Section**
```html
<header class="blog-article-header">
    - Category badge con link a categoría
    - H1 título principal
    - Meta información (fecha + tiempo de lectura con icono)
</header>
```

### 2. **Hero Section (Two Column Layout)**
```html
<div class="blog-article-hero">
    <div class="blog-article-hero-image">
        - Imagen principal (.webp o .jpg)
    </div>
    <div class="blog-article-hero-content">
        <p class="lead">
            - Párrafo introductorio conversacional y atractivo
            - Debe enganchar al lector desde el inicio
            - Usar anécdotas o ejemplos concretos
        </p>
    </div>
</div>
```

### 3. **Tabla de Contenidos Inline (OBLIGATORIA)**
```html
<nav class="blog-article-toc-inline">
    <h4>En este artículo</h4>
    <ul>
        <li><a href="#seccion-id">Título de la Sección</a></li>
        <!-- Mínimo 5-6 secciones, máximo 10 -->
    </ul>
</nav>
```

**IMPORTANTE:**
- Debe ir inmediatamente después del hero
- Todos los h2 del artículo DEBEN tener IDs correspondientes
- Títulos en la TOC deben ser concisos pero descriptivos

### 4. **Article Content**
```html
<div class="blog-article-content">
    <h2 id="seccion-1">Título de Sección</h2>
    <p>Contenido conversacional y natural...</p>

    <!-- Subsecciones opcionales -->
    <h3>Subtítulo si es necesario</h3>
    <p>Contenido de subsección...</p>
</div>
```

### 5. **Image Gallery (OPCIONAL)**
Solo usar cuando sea relevante para el contenido:
```html
<div class="blog-image-gallery">
    <h3>Título de la Galería</h3>
    <div class="gallery-grid">
        <!-- 4 imágenes en grid 2x2 -->
        <div class="gallery-item">
            <img src="..." alt="...">
            <p class="gallery-caption">Caption</p>
        </div>
    </div>
</div>
```

### 6. **Tags Section**
```html
<div class="blog-article-tags">
    <h3>Temas relacionados:</h3>
    <div class="tags-container">
        <a href="..." class="tag">Tag Principal</a>
        <!-- 5-6 tags relevantes -->
    </div>
</div>
```

### 7. **Related Articles (3-Column Grid)**
```html
<div class="blog-related-articles">
    <h3>Artículos Relacionados</h3>
    <div class="blog-cards-grid">
        <!-- Exactamente 3 artículos relacionados -->
        <article class="blog-card">
            <div class="blog-card-image">
                <img src="..." alt="...">
            </div>
            <div class="blog-card-content">
                <h3 class="blog-card-title">
                    <a href="...">Título</a>
                </h3>
                <p class="blog-card-excerpt">Extracto breve</p>
                <div class="blog-meta">
                    <span class="blog-reading-time">
                        <!-- Icono SVG + tiempo -->
                    </span>
                </div>
            </div>
        </article>
    </div>
</div>
```

---

## 🎨 REGLAS DE ESTILO CSS

### Colores
- **Primary:** `#F4B942` (Amarillo profesional)
- **Secondary:** `#1A2332` (Azul oscuro)
- **Accent Blue:** `#3B82F6`
- **Text:** `#1F2937` (gray-800)
- **Links:** `#0066cc` (blue on hover)

### Tipografía
- **Font Family:** `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- **H1:** `2.25rem` (36px), font-weight: 700
- **H2:** `1.875rem` (30px), font-weight: 600
- **H3:** `1.5rem` (24px), font-weight: 600
- **H4:** `1.25rem` (20px), font-weight: 600
- **Body:** `1rem` (16px), line-height: 1.75
- **Lead paragraph:** `1.125rem` (18px)

### Espaciado
- **Hero margin:** `3rem 0`
- **Section spacing:** `2rem` entre h2
- **Paragraph spacing:** `1.5rem` entre párrafos
- **TOC margin:** `3rem 0`

### Componentes Específicos

#### Inline TOC
```css
.blog-article-toc-inline {
    background: #f5f5f7;
    border-radius: 12px;
    padding: 2rem;
    margin: 3rem 0;
}
```
- Grid 2 columnas en desktop, 1 en mobile
- Flechas → que NO tienen animación
- Links sin transiciones (cambios instantáneos)

#### Hero Section
- Layout grid 2 columnas en desktop
- Imagen 50%, contenido 50%
- Gap de 2rem entre columnas
- Mobile: stack vertical

#### Gallery Grid
- Grid 2x2 (4 imágenes)
- Gap: 1.5rem
- Border-radius: 12px
- Caption: font-size 0.875rem, color: #6B7280

---

## ✍️ GUÍAS DE CONTENIDO

### Tono y Estilo
1. **Conversacional pero profesional**
   - Evitar fórmulas repetitivas
   - Usar "tú" en lugar de "usted"
   - Incluir anécdotas cuando sea apropiado

2. **Estructura de párrafos**
   - Párrafos cortos (3-4 líneas máximo)
   - Una idea por párrafo
   - Uso natural de conectores

3. **Enlaces internos**
   - Mencionar negocios relevantes de forma natural
   - 3-4 enlaces a negocios por artículo
   - Formato: `<a href="../../negocios/categoria/negocio-slug.html">Nombre del Negocio</a>`

4. **Títulos de secciones (H2)**
   - Descriptivos y atractivos
   - Evitar fórmulas genéricas
   - IDs en formato kebab-case
   - Ejemplos buenos:
     - ✅ "Por Qué la Biometría Cambió el Juego"
     - ✅ "Lo Que Nadie Te Dice Sobre Costos"
     - ❌ "Introducción"
     - ❌ "Conclusión"

### Longitud Recomendada
- **Mínimo:** 1,500 palabras
- **Óptimo:** 2,000-3,000 palabras
- **Secciones H2:** 5-8 secciones principales
- **Tiempo de lectura:** 6-12 minutos

---

## 🚫 ANIMACIONES Y TRANSICIONES

**REGLA CRÍTICA:** NO usar transiciones CSS excepto en menú y footer

### ❌ NO PERMITIDO:
```css
/* NO agregar estas propiedades */
transition: all 0.3s ease;
transform: translateY(-4px);
transition: color 0.2s ease;
```

### ✅ PERMITIDO:
- Cambios instantáneos de color en hover
- Cambios de background-color sin transición
- Box-shadow sin transición
- Transiciones SOLO en:
  - `.nav-menu` y elementos del menú
  - `.footer` y elementos del footer

---

## 📁 ESTRUCTURA DE ARCHIVOS

### Imágenes
```
/img/
  /img-seguridad-privada/
    - imagen-hero.webp (o .jpg)
    - imagen-galeria-1.webp
    - imagen-galeria-2.webp
    - etc.
  /img-plomeria/
  /img-electricidad/
  /[categoria]/
```

**Formatos aceptados:** `.webp` (preferido) o `.jpg`

### Artículos HTML
```
/blog/
  /seguridad-privada/
    - articulo-slug.html
  /plomeria/
    - articulo-slug.html
  /[categoria]/
    - articulo-slug.html
```

---

## ✅ CHECKLIST DE VALIDACIÓN

Antes de considerar un artículo completo, verificar:

- [ ] Header con breadcrumbs correctos
- [ ] Hero section con imagen + lead paragraph
- [ ] Tabla de contenidos inline presente
- [ ] Todos los H2 tienen IDs únicos
- [ ] TOC lista todos los H2 del artículo
- [ ] Mínimo 5-6 secciones H2
- [ ] Enlaces a negocios relevantes (3-4 mínimo)
- [ ] Sección de tags con categoría principal
- [ ] 3 artículos relacionados en grid
- [ ] Sidebar con TOC, categorías, y artículos populares
- [ ] Sin transiciones CSS (excepto menú/footer)
- [ ] Todas las imágenes tienen alt text descriptivo
- [ ] Contenido conversacional y natural (no fórmulas)
- [ ] Tiempo de lectura calculado correctamente
- [ ] Meta description presente

---

## 🎯 EJEMPLOS DE REFERENCIA

Artículos que siguen correctamente este diseño:

1. `/blog/seguridad-privada/guia-completa-seguridad-privada-mexico.html`
2. `/blog/seguridad-privada/sistemas-cctv-empresas.html`
3. `/blog/seguridad-privada/certificaciones-cnsp.html`
4. `/blog/seguridad-privada/control-acceso-biometrico.html`
5. `/blog/seguridad-privada/seguridad-condominios.html`
6. `/blog/seguridad-privada/costos-seguridad-privada-cdmx.html`
7. `/blog/seguridad-privada/ia-seguridad-tecnologias-emergentes.html`

---

## 📝 NOTAS IMPORTANTES

1. **Consistencia es clave:** Todos los artículos deben seguir exactamente esta estructura
2. **No improvisar diseños:** Usar siempre las clases CSS existentes
3. **Probar en responsive:** Verificar que se vea bien en mobile/tablet/desktop
4. **SEO:** Siempre incluir meta description y títulos descriptivos
5. **Accesibilidad:** Todos los elementos interactivos deben ser accesibles por teclado

---

**Última actualización:** Noviembre 2025
**Versión:** 1.0
