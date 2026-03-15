# Template de Perfil de Negocio - PaginasAmarillas.mx
## Guía Completa para Crear Nuevos Perfiles de Empresas

---

## 📋 Índice

1. [Estructura HTML](#estructura-html)
2. [Secciones del Perfil](#secciones-del-perfil)
3. [Estilos CSS](#estilos-css)
4. [JavaScript Requerido](#javascript-requerido)
5. [Checklist de Implementación](#checklist-de-implementación)
6. [Proceso Paso a Paso](#proceso-paso-a-paso)

---

## 🏗️ Estructura HTML

### Archivos Base

```
negocios/
└── [categoria]/
    └── [slug-empresa].html
```

**Ejemplo:**
```
negocios/seguridad-privada/origins-private-security.html
```

### Template HTML Completo

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- SEO Meta Tags -->
  <title>[Nombre Empresa] - [Categoría] en [Ciudad] | PaginasAmarillas.mx</title>
  <meta name="description" content="[Descripción breve del negocio, 150-160 caracteres]">
  <meta name="keywords" content="[keyword1], [keyword2], [keyword3], [ciudad], México">

  <!-- Open Graph -->
  <meta property="og:title" content="[Nombre Empresa] - [Categoría]">
  <meta property="og:description" content="[Descripción breve]">
  <meta property="og:type" content="business.business">
  <meta property="og:url" content="https://paginasamarillas.mx/negocios/[categoria]/[slug]">
  <meta property="og:image" content="[URL imagen principal]">

  <!-- CSS -->
  <link rel="stylesheet" href="../../css/style.css">
  <link rel="stylesheet" href="../../css/perfil.css">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="../../favicon.png">
</head>

<body>
  <!-- Header (copiar de Origins) -->
  <!-- Breadcrumbs -->
  <!-- Hero Section -->
  <!-- Services Grid (8 cards) -->
  <!-- About Section -->
  <!-- Contact Info + Form -->
  <!-- FAQs Section -->
  <!-- Reviews Section -->
  <!-- Final CTA -->
  <!-- Footer -->

  <!-- Scripts -->
  <script src="../../js/app.js"></script>
  <script src="../../js/perfil.js"></script>
</body>
</html>
```

---

## 📦 Secciones del Perfil

### 1. Header y Navegación

**Ubicación:** Top de la página
**Contenido:**
- Logo PaginasAmarillas.mx
- Menú de navegación
- Botones "Iniciar Sesión" y "Registrar Negocio"

**Código:**
```html
<header class="header" id="header">
  <div class="container">
    <nav class="navbar">
      <div class="logo">
        <a href="../../index.html">
          <span class="logo-text">Páginas<span class="logo-highlight">Amarillas</span>.mx</span>
        </a>
      </div>
      <!-- Mobile Menu Toggle -->
      <button class="menu-toggle" id="menuToggle">
        <span class="hamburger"></span>
      </button>
      <!-- Nav Menu -->
      <div class="nav-menu" id="navMenu">
        <ul class="nav-list">
          <li><a href="../../index.html#categorias">Categorías</a></li>
          <li><a href="../../index.html#como-funciona">Cómo Funciona</a></li>
          <li><a href="../../index.html#para-empresas">Para Empresas</a></li>
        </ul>
        <div class="nav-actions">
          <a href="#login" class="btn btn-ghost">Iniciar Sesión</a>
          <a href="#registrar" class="btn btn-primary">Registrar Negocio</a>
        </div>
      </div>
    </nav>
  </div>
</header>
```

---

### 2. Breadcrumbs

**Ubicación:** Después del header
**Propósito:** SEO y navegación

```html
<section class="breadcrumbs">
  <div class="container">
    <nav aria-label="Breadcrumb">
      <ol class="breadcrumb-list">
        <li><a href="../../index.html">Inicio</a></li>
        <li><a href="../../categorias.html">Categorías</a></li>
        <li><a href="../../categoria/[categoria].html">[Categoría]</a></li>
        <li aria-current="page">[Nombre Empresa]</li>
      </ol>
    </nav>
  </div>
</section>
```

---

### 3. Hero Section (Información Principal)

**Contenido:**
- Nombre del negocio (H1)
- Rating y reseñas
- Badges (Verificado, Certificaciones, Años de experiencia)
- Imagen principal
- Galería de thumbnails
- Botones CTA: Llamar, WhatsApp, Enviar Mensaje

**Estructura:**

```html
<section class="business-hero">
  <div class="container">
    <div class="business-hero-content">

      <!-- Left Column: Info -->
      <div class="business-info">
        <div class="business-header-main">
          <h1 class="business-title">[Nombre Empresa]</h1>

          <div class="business-meta">
            <!-- Rating -->
            <div class="business-rating">
              <div class="stars">★★★★★</div>
              <span class="rating-value">4.8</span>
              <a href="#reviews" class="rating-link">(47 reseñas)</a>
            </div>

            <!-- Badges -->
            <div class="business-badges-inline">
              <span class="badge badge-verified">✓ Verificado</span>
              <span class="badge badge-certified">[Certificación]</span>
              <span class="badge badge-experience">[XX]+ Años</span>
            </div>
          </div>
        </div>

        <!-- Description -->
        <p class="business-description">
          [Descripción corta del negocio, 2-3 líneas]
        </p>

        <!-- Quick Info -->
        <div class="business-quick-info">
          <div class="quick-info-item">
            <svg>[icono ubicación]</svg>
            <span>[Colonia, Alcaldía/Municipio, Ciudad]</span>
          </div>
          <div class="quick-info-item">
            <svg>[icono teléfono]</svg>
            <a href="tel:+52[teléfono]">[Teléfono formateado]</a>
          </div>
          <div class="quick-info-item">
            <svg>[icono reloj]</svg>
            <span>Lun-Vie: [Horario] | Sáb: [Horario]</span>
          </div>
        </div>

        <!-- CTA Buttons (Vertical Stack) -->
        <div class="business-cta-buttons">
          <a href="tel:+52[teléfono]" class="btn btn-primary btn-large">
            <svg>[icono teléfono]</svg>
            Llamar ahora: [Teléfono]
          </a>
          <a href="https://wa.me/521[teléfono]?text=[mensaje]" class="btn btn-outline btn-large" target="_blank">
            <svg>[icono WhatsApp]</svg>
            WhatsApp
          </a>
          <button class="btn btn-outline btn-large" id="btn-contact-form">
            <svg>[icono mensaje]</svg>
            Enviar mensaje
          </button>
        </div>
      </div>

      <!-- Right Column: Images -->
      <div class="business-images">
        <div class="business-main-image">
          <img src="[imagen-principal.jpg]" alt="[Nombre Empresa] - [Categoría]">
        </div>

        <!-- Gallery Thumbnails -->
        <div class="business-gallery">
          <div class="gallery-thumb active">
            <img src="[imagen-1-thumb.jpg]" alt="[Alt text]">
          </div>
          <div class="gallery-thumb">
            <img src="[imagen-2-thumb.jpg]" alt="[Alt text]">
          </div>
          <div class="gallery-thumb">
            <img src="[imagen-3-thumb.jpg]" alt="[Alt text]">
          </div>
          <div class="gallery-thumb">
            <img src="[imagen-4-thumb.jpg]" alt="[Alt text]">
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
```

**IMPORTANTE:**
- Botones CTA en **vertical** (flex-direction: column)
- Texto completo en botones ("Llamar ahora: XX XXXX XXXX", "Enviar mensaje")
- Galería con 4 thumbnails mínimo

---

### 4. Services Grid (8 Servicios)

**Estructura:**
```html
<section class="business-section">
  <div class="container">
    <h2 class="section-title">Servicios y Productos</h2>

    <div class="services-grid">
      <!-- Card 1 -->
      <div class="service-card">
        <div class="service-icon">
          <svg>[icono]</svg>
        </div>
        <h3 class="service-title">[Nombre del Servicio]</h3>
        <p class="service-description">[Descripción breve, 1-2 líneas]</p>
      </div>

      <!-- Repetir 7 veces más (Total: 8 cards) -->
    </div>
  </div>
</section>
```

**Grid Layout:**
- Desktop: 4 columnas
- Tablet: 2 columnas
- Mobile: 1 columna

---

### 5. About Section

```html
<section class="business-section bg-light">
  <div class="container">
    <h2 class="section-title">Sobre [Nombre Empresa]</h2>

    <div class="about-content">
      <div class="about-text">
        <p>[Párrafo 1: Historia o presentación]</p>
        <p>[Párrafo 2: Valores o diferenciadores]</p>
        <p>[Párrafo 3: Compromiso o misión]</p>
      </div>

      <!-- Stats (Opcional) -->
      <div class="about-stats">
        <div class="stat-item">
          <div class="stat-number">[XX]+</div>
          <div class="stat-label">[Métrica]</div>
        </div>
        <!-- Más stats... -->
      </div>
    </div>
  </div>
</section>
```

---

### 6. Contact Information + Form

**IMPORTANTE:** Formulario DENTRO de la sección de información de contacto

```html
<section class="business-section">
  <div class="container">
    <h2 class="section-title">Información de Contacto</h2>

    <div class="business-contact-grid">

      <!-- Contact Details Cards -->
      <div class="contact-details">
        <h3>Dirección</h3>
        <p>[Calle y Número]<br>[Colonia], [CP]<br>[Alcaldía/Municipio], [Ciudad]</p>
      </div>

      <div class="contact-details">
        <h3>Teléfonos</h3>
        <p>
          <a href="tel:+52[teléfono]">[Teléfono formateado]</a><br>
          <a href="tel:+52[celular]">[Celular formateado]</a>
        </p>
      </div>

      <div class="contact-details">
        <h3>Email</h3>
        <p>
          <a href="mailto:[email]">[email]</a>
        </p>
      </div>

      <div class="contact-details">
        <h3>Sitio Web</h3>
        <p>
          <a href="[url]" target="_blank">[dominio.com]</a>
        </p>
      </div>

      <div class="contact-details">
        <h3>Horario</h3>
        <p>
          <strong>Lunes - Viernes:</strong> [HH:MM-HH:MM]<br>
          <strong>Sábados:</strong> [HH:MM-HH:MM]
        </p>
      </div>

      <!-- Contact Form -->
      <div class="contact-form-wrapper">
        <h3 class="form-title">Solicita una Cotización</h3>
        <p class="form-subtitle">Evaluación gratuita | Respuesta en 24 horas</p>

        <form class="contact-form" id="contact-form">
          <div class="form-group">
            <label for="name">Nombre completo *</label>
            <input type="text" id="name" name="name" required>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="email">Email *</label>
              <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
              <label for="phone">Teléfono *</label>
              <input type="tel" id="phone" name="phone" required>
            </div>
          </div>

          <div class="form-group">
            <label for="company">Empresa</label>
            <input type="text" id="company" name="company">
          </div>

          <div class="form-group">
            <label for="service">Servicio de interés *</label>
            <select id="service" name="service" required>
              <option value="">Selecciona un servicio</option>
              <option value="[servicio-1]">[Servicio 1]</option>
              <!-- Agregar opciones según servicios del negocio -->
            </select>
          </div>

          <div class="form-group">
            <label for="message">Mensaje *</label>
            <textarea id="message" name="message" rows="4" required placeholder="Describe brevemente tus necesidades..."></textarea>
          </div>

          <button type="submit" class="btn btn-primary btn-large">
            Enviar solicitud
          </button>

          <p class="form-disclaimer">
            Al enviar este formulario aceptas que [Nombre Empresa] se ponga en contacto contigo. Respetamos tu privacidad.
          </p>
        </form>
      </div>

    </div>
  </div>
</section>
```

---

### 7. FAQs Section (Preguntas Frecuentes)

**Ubicación:** ANTES de la sección de reseñas

```html
<section class="business-section">
  <div class="container">
    <h2 class="section-title">Preguntas Frecuentes</h2>

    <div class="faqs-section">

      <!-- FAQ Item 1 -->
      <div class="faq-item">
        <h3 class="faq-question" data-faq="1" aria-expanded="false">
          [Pregunta 1]
          <svg class="faq-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="6 9 12 15 18 9"/>
          </svg>
        </h3>
        <div class="faq-answer" id="faq-1">
          <p>[Respuesta detallada]</p>
        </div>
      </div>

      <!-- Repetir para 5-8 preguntas frecuentes -->

    </div>
  </div>
</section>
```

**Cantidad recomendada:** 6 preguntas frecuentes

**Funcionalidad:**
- Click en pregunta abre/cierra respuesta
- Solo 1 FAQ abierto a la vez (accordion)
- Icono chevron rota al abrir
- Transiciones suaves

---

### 8. Reviews Section

```html
<section class="business-section" id="reviews">
  <div class="container">
    <h2 class="section-title">Reseñas de Clientes</h2>

    <div class="reviews-summary">
      <div class="reviews-average">
        <div class="average-score">[4.8]</div>
        <div class="stars-large">★★★★★</div>
        <p>Basado en [XX] reseñas</p>
      </div>
    </div>

    <!-- Individual Reviews -->
    <div class="reviews-list">
      <div class="review-card">
        <div class="review-header">
          <div class="review-author">
            <div class="author-avatar">[Inicial]</div>
            <div>
              <h4 class="author-name">[Nombre]</h4>
              <div class="review-meta">
                <div class="stars">★★★★★</div>
                <span class="review-date">[Hace X días/meses]</span>
              </div>
            </div>
          </div>
        </div>
        <p class="review-text">[Texto de la reseña]</p>
      </div>

      <!-- Más reseñas (mínimo 5) -->
    </div>

    <div class="reviews-cta">
      <a href="#contact-form" class="btn btn-outline">Deja tu reseña</a>
    </div>
  </div>
</section>
```

---

### 9. Final CTA Section

```html
<section class="final-cta">
  <div class="container">
    <div class="cta-content-center">
      <h2>¿Listo para [acción principal]?</h2>
      <p>Contacta a [Nombre Empresa] hoy mismo y obtén [beneficio]</p>

      <div class="cta-buttons-center">
        <a href="tel:+52[teléfono]" class="btn btn-primary btn-large">
          Llamar ahora
        </a>
        <a href="#contact-form" class="btn btn-outline btn-large">
          Solicitar cotización
        </a>
      </div>
    </div>
  </div>
</section>
```

---

### 10. Footer

**Copiar exactamente el footer de Origins Private Security**

---

## 🎨 Estilos CSS

### Archivos CSS Requeridos

1. **style.css** (Global)
   - Variables CSS
   - Componentes generales (botones, cards, etc.)
   - Header y Footer
   - Utilities

2. **perfil.css** (Específico de perfil)
   - Breadcrumbs
   - Hero section
   - Services grid
   - Contact form
   - FAQs accordion
   - Reviews

### CSS Variables Clave

```css
/* Colores */
--color-primary: #F4B942;
--color-secondary: #1A2332;
--color-gray-900: #111827;
--color-white: #FFFFFF;

/* Espaciado */
--spacing-xs: 0.5rem;
--spacing-sm: 0.75rem;
--spacing-md: 1rem;
--spacing-lg: 1.5rem;
--spacing-xl: 2rem;
--spacing-2xl: 3rem;
--spacing-3xl: 4rem;

/* Tipografía */
--font-size-xs: 0.75rem;
--font-size-sm: 0.875rem;
--font-size-base: 1rem;
--font-size-lg: 1.125rem;
--font-size-xl: 1.25rem;
--font-size-2xl: 1.5rem;
--font-size-4xl: 2.25rem;

/* Bordes */
--radius-md: 8px;
--radius-lg: 12px;
--radius-full: 9999px;

/* Transiciones */
--transition-base: 0.2s ease;
```

---

## ⚙️ JavaScript Requerido

### Archivos JS

1. **app.js** (Global)
   - Menu toggle mobile
   - Scroll effects
   - Utilities

2. **perfil.js** (Específico de perfil)
   - Gallery functionality
   - Contact form modal trigger
   - Form submission
   - Phone formatting
   - FAQs accordion
   - Analytics tracking

### Funcionalidades Clave

```javascript
// 1. Gallery Image Switching
const galleryThumbs = document.querySelectorAll('.gallery-thumb');
const mainImage = document.querySelector('.business-main-image img');
// Click en thumbnail cambia imagen principal

// 2. Smooth Scroll to Contact Form
const btnContactForm = document.getElementById('btn-contact-form');
// Scroll suave + focus en primer input

// 3. Form Submission
const contactForm = document.getElementById('contact-form');
// Validación + envío + mensaje de éxito/error

// 4. Phone Number Formatting
const phoneInput = document.getElementById('phone');
// Formato: XX XXXX XXXX

// 5. FAQs Accordion
const faqQuestions = document.querySelectorAll('.faq-question');
// Toggle respuestas + cerrar otras
```

---

## ✅ Checklist de Implementación

### Pre-requisitos

- [ ] Categoría existe en `/categoria/[categoria].html`
- [ ] Carpeta creada: `/negocios/[categoria]/`
- [ ] Slug generado correctamente (minúsculas, sin acentos, guiones)

### Contenido Requerido

**Información Básica:**
- [ ] Nombre de la empresa
- [ ] Categoría
- [ ] Descripción (corta y larga)
- [ ] Ubicación (calle, colonia, CP, alcaldía, ciudad)
- [ ] Teléfono(s)
- [ ] Email
- [ ] Sitio web
- [ ] Horarios de atención

**Imágenes:**
- [ ] Logo o imagen principal (600x400px mínimo)
- [ ] 4 imágenes para galería (thumbnails 120x80px)

**Servicios:**
- [ ] 8 servicios/productos con nombre y descripción
- [ ] Iconos SVG para cada servicio

**Contenido Adicional:**
- [ ] 3 párrafos "Sobre la empresa"
- [ ] 6 preguntas frecuentes con respuestas
- [ ] 5-10 reseñas de clientes (nombre, rating, texto, fecha)
- [ ] Badges/Certificaciones (si aplica)

**SEO:**
- [ ] Meta title (60 caracteres)
- [ ] Meta description (150-160 caracteres)
- [ ] Keywords (5-10 relevantes)
- [ ] Alt text para todas las imágenes
- [ ] Open Graph tags

### Archivos a Crear/Modificar

- [ ] Archivo HTML del negocio creado
- [ ] Imágenes subidas a `/img/negocios/[categoria]/[slug]/`
- [ ] Card agregada en `/categoria/[categoria].html`

---

## 🚀 Proceso Paso a Paso

### Paso 1: Preparar Información

1. Reunir toda la información del negocio
2. Preparar y optimizar imágenes
3. Generar slug: `"Café París" → "cafe-paris"`

### Paso 2: Crear Archivo HTML

```bash
# Copiar template de Origins
cp negocios/seguridad-privada/origins-private-security.html \
   negocios/[categoria]/[slug-empresa].html
```

### Paso 3: Personalizar Contenido

**Orden de edición:**

1. **Meta Tags** (líneas 1-20)
   - Title
   - Description
   - Keywords
   - Open Graph

2. **Breadcrumbs** (después del header)
   - Actualizar categoría y nombre

3. **Hero Section**
   - H1: Nombre empresa
   - Rating y badges
   - Descripción
   - Quick info (ubicación, teléfono, horario)
   - Botones CTA con teléfonos correctos
   - Imágenes (principal + galería)

4. **Services Grid**
   - 8 servicios con nombre, icono y descripción

5. **About Section**
   - 3 párrafos sobre la empresa
   - Stats (opcional)

6. **Contact Info + Form**
   - Dirección completa
   - Teléfonos
   - Email
   - Sitio web
   - Horarios
   - Opciones del select de servicios

7. **FAQs**
   - 6 preguntas frecuentes

8. **Reviews**
   - Rating promedio
   - 5-10 reseñas individuales

9. **Final CTA**
   - Personalizar mensaje
   - Actualizar teléfonos en botones

### Paso 4: Actualizar Listado de Categoría

En `/categoria/[categoria].html`, agregar nueva card:

```html
<article class="business-card">
  <div class="business-image">
    <img src="../img/negocios/[categoria]/[slug]/principal.jpg" alt="[Nombre] - [Categoría]">
    <div class="business-badges">
      <span class="badge badge-verified">✓ Verificado</span>
    </div>
  </div>
  <div class="business-content">
    <div class="business-header">
      <h3 class="business-name">
        <a href="../negocios/[categoria]/[slug].html">[Nombre Empresa]</a>
      </h3>
      <div class="business-rating">
        <div class="stars">★★★★★</div>
        <span class="rating-value">[X.X]</span>
        <span class="rating-count">([XX] reseñas)</span>
      </div>
    </div>
    <p class="business-excerpt">[Descripción breve]</p>
    <div class="business-info-items">
      <div class="info-item">
        <svg>[icono ubicación]</svg>
        <span>[Colonia], [Alcaldía]</span>
      </div>
      <div class="info-item">
        <svg>[icono teléfono]</svg>
        <a href="tel:+52[teléfono]">[Teléfono]</a>
      </div>
    </div>
    <div class="business-actions">
      <a href="tel:+52[teléfono]" class="btn btn-outline">Llamar</a>
      <a href="https://wa.me/521[teléfono]" class="btn btn-outline">WhatsApp</a>
      <a href="../negocios/[categoria]/[slug].html" class="btn btn-primary">Ver perfil</a>
    </div>
  </div>
</article>
```

### Paso 5: Testing

- [ ] Verificar todos los links funcionan
- [ ] Probar formulario de contacto
- [ ] Verificar galería de imágenes
- [ ] Probar acordeón de FAQs
- [ ] Verificar botones CTA (tel: y WhatsApp)
- [ ] Responsive en móvil y tablet
- [ ] Validar HTML (W3C Validator)
- [ ] Verificar velocidad de carga

---

## 📝 Notas Importantes

### DO's ✅

- **Usar rutas relativas** para CSS/JS: `../../css/style.css`
- **Teléfonos en formato internacional**: `+52` para México
- **WhatsApp**: Incluir código de país: `https://wa.me/521[teléfono]`
- **Imágenes optimizadas**: WebP preferiblemente, max 200KB
- **Alt text descriptivo** en todas las imágenes
- **Formulario dentro** de la sección de contacto
- **FAQs antes** de reseñas
- **8 servicios exactos** en la grid

### DON'Ts ❌

- **NO** usar rutas absolutas en desarrollo
- **NO** dejar placeholder text en producción
- **NO** incluir información falsa o inventada
- **NO** copiar reseñas de otros sitios
- **NO** usar imágenes sin derechos
- **NO** poner botones CTA en 3 columnas (solo vertical)
- **NO** acortar texto de botones ("Llamar ahora: XX XXXX XXXX", NO "Llamar")
- **NO** poner FAQs dentro de la sección de contacto

---

## 🔄 Actualizaciones y Mantenimiento

### Actualizar Información

Para actualizar información de un negocio existente:

1. Editar directamente el archivo HTML
2. Mantener la estructura intacta
3. Actualizar también la card en listado de categoría si cambia info visible

### Agregar Nuevas Reseñas

```html
<div class="review-card">
  <div class="review-header">
    <div class="review-author">
      <div class="author-avatar">[Inicial]</div>
      <div>
        <h4 class="author-name">[Nombre]</h4>
        <div class="review-meta">
          <div class="stars">★★★★★</div>
          <span class="review-date">[Fecha]</span>
        </div>
      </div>
    </div>
  </div>
  <p class="review-text">[Texto]</p>
</div>
```

Actualizar también:
- Rating promedio en hero
- Número total de reseñas

---

## 📚 Referencias

- **Archivo de referencia completo:** `/negocios/seguridad-privada/origins-private-security.html`
- **CSS:** `/css/perfil.css`
- **JavaScript:** `/js/perfil.js`
- **Estructura de carpetas:** `/docs/ESTRUCTURA-CARPETAS.md`

---

## 🎯 KPIs de Calidad

Un perfil de negocio bien implementado debe tener:

- ✅ **Score SEO:** 90+ (Lighthouse)
- ✅ **Performance:** 85+ (Lighthouse)
- ✅ **Accessibility:** 95+ (Lighthouse)
- ✅ **Mobile-Friendly:** Sí (Google Mobile Test)
- ✅ **Validación HTML:** 0 errores (W3C)
- ✅ **Velocidad de carga:** < 3 segundos

---

**Última actualización:** Noviembre 2025
**Versión del template:** 1.0
**Basado en:** Origins Private Security (perfil de referencia)
**Creado por:** PaginasAmarillas.mx Development Team
