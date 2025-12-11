# DOCUMENTO MAESTRO: MANUAL OPERATIVO PARA GENERACIÓN DE CARDS Y RESEÑAS
## Sistema Universal de Creación de Contenido para Directorio de Empresas

**Proyecto**: Páginas Amarillas México
**Versión**: 5.1 - PROCESO OBLIGATORIO
**Fecha de Actualización**: 16 de noviembre de 2025
**Estado**: Manual Operativo Oficial - Optimizado para Claude + VS Code
**Audiencia**: Creadores de Contenido, Desarrolladores, Redactores, Editores y Claude AI

---

## ÍNDICE

1. [Introducción y Propósito](#1-introducción-y-propósito)
2. [Proceso Obligatorio de Generación (CRÍTICO)](#2-proceso-obligatorio-de-generación)
3. [Análisis Técnico de Estructura Base (redeil.html)](#3-análisis-técnico-de-estructura-base)
4. [Plantillas Universales](#4-plantillas-universales)
5. [Checklist Paso a Paso para Generación](#5-checklist-paso-a-paso-para-generación)
6. [Reglas Editoriales y SEO (No Negociables)](#6-reglas-editoriales-y-seo)
7. [Especificaciones Técnicas Completas](#7-especificaciones-técnicas-completas)
8. [Control de Calidad y Criterios de Aceptación](#8-control-de-calidad-y-criterios-de-aceptación)
9. [Manejo de Casos con Información Insuficiente](#9-manejo-de-casos-con-información-insuficiente)
10. [Ejemplos Prácticos Neutros](#10-ejemplos-prácticos-neutros)
11. [Registro de Cambios](#11-registro-de-cambios)
12. [Prompt Engineering para Claude](#12-prompt-engineering-para-claude)
13. [Sistema de Puntuación de Calidad](#13-sistema-de-puntuación-de-calidad)
14. [Configuración Centralizada](#14-configuración-centralizada)
15. [Automatización y Validación](#15-automatización-y-validación)
16. [Troubleshooting y Solución de Errores](#16-troubleshooting-y-solución-de-errores)

---

## 1. INTRODUCCIÓN Y PROPÓSITO

### 1.1 Objetivo del Manual

Este documento es un **manual operativo completo** que establece el proceso sistemático para crear:
- **Cards (Tarjetas)**: Elementos visuales de previsualización en páginas de categoría
- **Reseñas Completas**: Perfiles detallados y optimizados para SEO de empresas

**Principio fundamental**: Cada card y cada reseña debe ser **única, específica y relevante** para la empresa descrita. No se permiten contenidos genéricos, plantillas copiadas o duplicaciones.

### 1.2 Alcance y Uso

- **Obligatorio** para todo el equipo de contenido
- **Referencia técnica** para desarrolladores
- **Guía editorial** para redactores y editores
- **Checklist de QA** para control de calidad

---

## 2. PROCESO OBLIGATORIO DE GENERACIÓN (CRÍTICO)

### 2.1 ⚠️ NUNCA Generar Desde Cero

**REGLA ABSOLUTA**: NUNCA crear un archivo HTML desde cero con el tool Write.

**PROBLEMA CRÍTICO**: El tool Write puede crear archivos con encoding incorrecto (binary en vez de UTF-8), causando:
- Caracteres corruptos (� en lugar de á, é, í, ó, ú, ñ, ¿, ¡)
- CSS que no carga correctamente
- JavaScript que falla
- Página completamente rota

### 2.2 ✅ PROCESO CORRECTO (Paso a Paso)

#### PASO 1: Copiar Archivo de Referencia
```bash
cp /ruta/redeil.html /ruta/nueva-empresa.html
```

**Por qué**: redeil.html tiene:
- ✅ Encoding UTF-8 correcto garantizado
- ✅ Estructura HTML exacta que funciona con el CSS
- ✅ Todas las clases CSS correctas
- ✅ JavaScript correctamente vinculado

#### PASO 2: Modificar SOLO Contenido de Texto

**CRÍTICO**:
- ✅ SOLO cambiar texto dentro de tags HTML
- ❌ NUNCA cambiar nombres de clases CSS
- ❌ NUNCA cambiar estructura HTML
- ❌ NUNCA agregar/eliminar secciones completas

**Ejemplo CORRECTO**:
```html
<!-- ANTES (redeil.html) -->
<h1 class="business-title">REDEIL</h1>

<!-- DESPUÉS (nueva-empresa.html) -->
<h1 class="business-title">NUEVA EMPRESA</h1>
```

**Ejemplo INCORRECTO**:
```html
<!-- ❌ MAL - Cambió la clase -->
<h1 class="empresa-titulo">NUEVA EMPRESA</h1>

<!-- ❌ MAL - Cambió la estructura -->
<div class="header-new">
  <h1>NUEVA EMPRESA</h1>
</div>
```

#### PASO 3: Actualizar TODAS las Secciones

**CHECKLIST OBLIGATORIO** - Marcar cada sección actualizada:

- [ ] Meta tags (title, description, keywords, author)
- [ ] Open Graph tags (og:title, og:description, og:url, og:image)
- [ ] Twitter Card tags
- [ ] Geo tags (region, position)
- [ ] Schema.org LocalBusiness JSON-LD (name, description, phone, address, rating, etc.)
- [ ] Schema.org BreadcrumbList JSON-LD
- [ ] Schema.org FAQPage JSON-LD (todas las preguntas)
- [ ] Breadcrumbs HTML (cambiar nombre empresa)
- [ ] Business Hero (title, rating, tagline, badges)
- [ ] **3 CTAs principales (Llamar, WhatsApp, Sitio Web)** [ACTUALIZADO: tercer botón ahora es "Sitio Web"]
- [ ] Quick Info Cards (4 cards: ubicación, horario, especialización, diferencial)
- [ ] Business Tagline (párrafo descriptivo principal)
- [ ] Servicios Section (6 tarjetas de servicio con contenido específico)
- [ ] **"Sobre [EMPRESA]" Section (IMPORTANTE: primer párrafo DEBE incluir link SEO con palabra clave al sitio web)**
- [ ] "Por qué elegirnos" Section (6 párrafos con class="about-text")
- [ ] Benefits Section (6 beneficios específicos)
- [ ] Highlights Section (4 diferenciadores numerados)
- [ ] Services Directory Section (6 tarjetas del catálogo con badges)
- [ ] FAQs Section (6 preguntas Y respuestas completas)
- [ ] Reviews Section (rating, total reseñas, 3 reseñas completas con nombres)
- [ ] Contact Section (teléfono, WhatsApp, sitio web, ubicación)
- [ ] Footer (verificar enlaces y año actual)
- [ ] JavaScript (verificar app.js y perfil.js al final)

**TOTAL**: 21 secciones que DEBEN actualizarse

#### PASO 4: Validación Técnica Obligatoria

Ejecutar estos comandos ANTES de entregar:

```bash
# 1. Verificar encoding UTF-8
file -I nueva-empresa.html
# Debe mostrar: charset=utf-8

# 2. Verificar clases CSS correctas
grep -c "business-section" nueva-empresa.html
# Debe mostrar: 7 o más

grep "business-section\|about-text\|faqs-section\|contact-card" nueva-empresa.html | wc -l
# Debe mostrar: 15+ líneas

# 3. Verificar NO hay clases incorrectas
grep -E "services-section|why-choose-us|section-text|faq-section|contact-section" nueva-empresa.html
# Debe mostrar: (vacío - sin resultados)

# 4. Verificar JavaScript
tail -5 nueva-empresa.html | grep "app.js\|perfil.js"
# Debe mostrar: ambos archivos

# 5. Verificar nombre de empresa actualizado
grep -c "NOMBRE-EMPRESA" nueva-empresa.html
# Debe mostrar: 20+ ocurrencias
```

### 2.3 🚨 Errores Comunes y Cómo Evitarlos

| Error | Consecuencia | Prevención |
|-------|--------------|------------|
| Generar desde cero con Write | Encoding corrupto | Siempre copiar redeil.html |
| Cambiar nombres de clases CSS | CSS no aplica, página rota | Solo cambiar contenido de texto |
| Olvidar secciones | Contenido de empresa anterior | Usar checklist de 21 secciones |
| No verificar encoding | Caracteres � corruptos | Ejecutar `file -I` antes de entregar |
| Estructura HTML diferente | Estilos no funcionan | Mantener estructura exacta de redeil.html |
| Olvidar actualizar FAQs | Preguntas de otra empresa | Verificar cada pregunta manualmente |
| Olvidar actualizar Reviews | Reseñas de otra empresa | Verificar nombres y contenido |
| Olvidar Services Directory | Servicios de otra empresa | Actualizar las 6 tarjetas completas |

### 2.4 📋 Template de Comando para Claude

Cuando solicites a Claude generar una nueva reseña, usa EXACTAMENTE este formato:

```
Necesito que actualices el archivo [empresa].html siguiendo el PROCESO OBLIGATORIO:

PASO 1: Copia redeil.html como base
PASO 2: Actualiza SOLO el contenido de texto de estas 21 secciones:
[Lista completa de secciones]

INFORMACIÓN DE LA EMPRESA:
- Nombre: [nombre]
- Teléfono: [teléfono]
- Website: [url]
- Dirección: [dirección completa]
- Rating: [X.X] estrellas ([N] reseñas)
- Horario: [horario]

SERVICIOS (6 categorías):
1. [Servicio 1]: [descripción]
2. [Servicio 2]: [descripción]
...

FAQs (6 preguntas):
1. [Pregunta]: [Respuesta completa]
...

REVIEWS (3 reseñas):
1. [Nombre] - [Texto de reseña]
...

CRÍTICO:
- Mantén la estructura HTML EXACTA de redeil.html
- Solo cambia contenido de texto
- Actualiza las 21 secciones obligatorias
- Verifica encoding UTF-8 al final
```

---

## 3. ANÁLISIS TÉCNICO DE ESTRUCTURA BASE

Este análisis se basa en el archivo de referencia `redeil.html` (primera implementación). **IMPORTANTE**: Se extraen SOLO patrones estructurales y técnicos, NO contenido textual.

### 3.1 Estructura de CARD (Tarjeta en Listado de Categoría)

#### Composición DOM y Jerarquía

```
<article class="business-card">
  └── <div class="business-image">
      ├── <img> [280x280px, loading="lazy", WebP preferido]
      └── <div class="business-badges">
          └── <span class="badge badge-[tipo]"> [1-3 badges]

  └── <div class="business-content">
      ├── <div class="business-header">
      │   ├── <h3 class="business-name">
      │   │   └── <a href="[internal-link]"> [NO target="_blank"]
      │   └── <div class="business-rating">
      │       ├── <div class="stars">
      │       ├── <span class="rating-value">
      │       └── <span class="rating-count">
      │
      ├── <div class="business-services">
      │   └── <span class="service-tag"> x3-4 tags
      │
      ├── <p class="business-description"> [120-180 caracteres]
      │
      ├── <div class="business-details">
      │   ├── <div class="detail-item"> [Sitio Web con icono SVG]
      │   ├── <div class="detail-item"> [Teléfono con icono SVG]
      │   ├── <div class="detail-item"> [Ubicación con icono SVG]
      │   └── <div class="detail-item"> [Horario con icono SVG]
      │
      └── <div class="business-actions">
          ├── <a class="btn btn-outline"> [Llamar]
          ├── <a class="btn btn-outline" target="_blank"> [WhatsApp]
          └── <a class="btn btn-primary"> [Ver perfil - interno]
```

#### Patrones Identificados en Card

| Elemento | Patrón Técnico | Longitud/Formato | Obligatorio |
|----------|----------------|------------------|-------------|
| **Nombre** | H3 > A (link interno) | Máx 40 caracteres | ✅ Sí |
| **Imagen** | 280x280px, WebP, lazy loading, **RUTA ABSOLUTA /img/img-[categoría]/** | Alt descriptivo | 🚨 **CRÍTICO** |
| **Badges** | 1-3 spans con clases específicas | verified, premium, experience | ⚠️ Mín 1 |
| **Rating** | Estrellas + valor + contador | 1.0-5.0 + "(N reseñas)" | ✅ Sí |
| **Service Tags** | 3-4 spans cortos | Máx 20 caracteres c/u | ✅ Sí |
| **Descripción** | Párrafo único | 120-180 caracteres | ✅ Sí |
| **Sitio Web** | SVG icon + link externo | URL sin https://, target="_blank" | ✅ Sí |
| **Teléfono** | SVG icon + link tel: | Formato: +52-55-XXXX-XXXX | ✅ Sí |
| **Ubicación** | SVG icon + texto | Colonia, Delegación/Municipio | ✅ Sí |
| **Horario** | SVG icon + texto | Formato: Lun-Dom HH:MM-HH:MM | ✅ Sí |
| **Botón Llamar** | Link tel: con SVG | Clase: btn btn-outline | ✅ Sí |
| **Botón WhatsApp** | Link wa.me con target="_blank" | Clase: btn btn-outline | ✅ Sí |
| **Botón Ver perfil** | Link interno (NO target) | Clase: btn btn-primary | ✅ Sí |

#### 🚨 CRÍTICO: Gestión de Imágenes en Cards

**REGLA ABSOLUTA**: Las imágenes en cards SIEMPRE deben usar rutas absolutas desde la raíz del proyecto.

**Estructura de carpetas de imágenes por categoría:**
- `/img/img-eventos/` - Para empresas de entretenimiento/eventos
- `/img/img-seguridad-privada/` - Para empresas de seguridad privada
- `/img/img-[categoría]/` - Para otras categorías

**Formato CORRECTO:**
```html
<img src="/img/img-seguridad-privada/personal-de-seguridad.webp"
     alt="Origins Private Security - Guardias Certificados SSC CDMX"
     width="280" height="280"
     loading="lazy">
```

**Formato INCORRECTO** ❌:
```html
<!-- ❌ MAL - Ruta relativa sin slash inicial -->
<img src="img/img-seguridad-privada/personal-de-seguridad.webp">

<!-- ❌ MAL - Ruta genérica o placeholder -->
<img src="/img/referencia.webp">

<!-- ❌ MAL - Ruta incorrecta de carpeta -->
<img src="/img/seguridad-privada/imagen.webp">
```

**Proceso para seleccionar imagen:**

1. **Identificar la categoría de la empresa** (ej. "seguridad-privada", "eventos", etc.)
2. **Verificar imágenes disponibles** en `/img/img-[categoría]/`:
   ```bash
   ls /img/img-seguridad-privada/
   ```
3. **Seleccionar imagen relevante** que represente el servicio principal
4. **Usar RUTA ABSOLUTA** comenzando con `/img/img-[categoría]/nombre-imagen.webp`

**Carpetas de imágenes comunes:**
- `img-seguridad-privada/` - guardias-intramuros.png, personal-de-seguridad.webp, vigilantes-capacitados.webp, proteccion-ejecutiva.webp, control-de-acceso.webp, seguridad-24-horas.webp
- `img-eventos/` - decoracion-luminosa-eventos.webp, audio-profesional.webp, iluminacion-led.webp

**IMPORTANTE**:
- ✅ Siempre listar archivos disponibles ANTES de crear la card
- ✅ Elegir imagen que represente visualmente el servicio
- ✅ Verificar que la imagen exista en la carpeta correcta
- ✅ Usar formato WebP o PNG (280x280px)

### 3.2 Estructura de RESEÑA (Perfil Completo)

#### Secciones en Orden de Aparición

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <!-- SEO Meta Tags [OBLIGATORIOS] -->
  <title> [Nombre - Servicio Principal Ciudad | Diferencial]
  <meta name="description"> [150-160 caracteres con CTA]
  <meta name="keywords"> [8-12 palabras clave separadas por comas]
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical">

  <!-- Open Graph [OBLIGATORIOS] -->
  <meta property="og:title">
  <meta property="og:description">
  <meta property="og:url">
  <meta property="og:image">

  <!-- Twitter Card [OBLIGATORIOS] -->
  <meta name="twitter:card" content="summary_large_image">

  <!-- Geo Tags [RECOMENDADOS] -->
  <meta name="geo.region">
  <meta name="geo.position">

  <!-- Schema.org LocalBusiness [OBLIGATORIO] -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "",
    "description": "",
    "address": {},
    "geo": {},
    "telephone": "",
    "email": "",
    "priceRange": "",
    "aggregateRating": {},
    "hasOfferCatalog": {}
  }
  </script>

  <!-- Schema.org BreadcrumbList [OBLIGATORIO] -->
  <!-- Schema.org FAQPage [OPCIONAL - si tiene FAQs] -->
</head>

<body>
  <!-- Hero Section -->
  <section class="business-hero">
    <h1 class="business-title"> [Nombre exacto]
    <div class="business-rating-large">
      [Rating + Link EXTERNO target="_blank"]
    </div>
    <p class="business-tagline"> [120-180 palabras, gancho principal]

    <!-- Quick Info Cards [4 tarjetas] -->
    - Ubicación
    - Horario
    - Especialización
    - Garantía/Diferencial
  </section>

  <!-- Servicios Section -->
  <section class="business-section">
    <h2>Servicios de [Categoría]</h2>
    [Descripción 40-80 palabras por servicio principal]
  </section>

  <!-- Por qué elegirnos Section -->
  <section class="business-section bg-gray">
    <h2>Por qué elegir [Nombre]</h2>
    <p class="about-text">[80-120 palabras sobre diferenciales]</p>
  </section>

  <!-- Galería [OPCIONAL] -->

  <!-- FAQs [OPCIONAL pero recomendado] -->
  <section class="business-section bg-gray">
    <h3>Preguntas Frecuentes</h3>
    <div class="faqs-section">
      [3-5 preguntas con respuestas de 50-100 palabras]
    </div>
  </section>

  <!-- Contacto Section -->
  <section class="business-section">
    <div class="contact-card">
      <div class="contact-icon">[Iconos de contacto]</div>
    </div>
  </section>
</body>
```

#### Longitudes Mínimas por Sección (No Negociables)

| Sección | Longitud Mínima | Longitud Óptima | Notas |
|---------|-----------------|-----------------|-------|
| **Meta Description** | 150 caracteres | 150-160 caracteres | Incluir CTA y teléfono/ubicación |
| **Hero Tagline** | 120 palabras | 150-180 palabras | Gancho principal, debe vender |
| **Intro Servicios** | 60 palabras | 80-120 palabras | Contexto antes de listar servicios |
| **Descripción Servicio Individual** | 40 palabras | 60-80 palabras | Por cada servicio destacado |
| **Por qué elegirnos** | 80 palabras | 100-150 palabras | Diferenciales únicos |
| **Respuesta FAQ** | 50 palabras | 70-100 palabras | Respuesta completa y útil |

### 3.3 ⚠️ ESTRUCTURA HTML EXACTA (NO MODIFICAR)

**REGLA ABSOLUTA**: La estructura HTML de redeil.html es SAGRADA. No se modifica NUNCA.

#### Estructura Completa (Solo Referencia):

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <!-- Meta tags -->
  <!-- Schema.org -->
</head>
<body>
  <!-- Header con navbar -->
  <header class="header" id="header">
    <div class="container">
      <nav class="navbar">...</nav>
    </div>
  </header>

  <main>
    <!-- Breadcrumbs -->
    <section class="breadcrumbs">...</section>

    <!-- Business Hero -->
    <section class="business-hero">...</section>

    <!-- Quick Info -->
    <section class="quick-info">...</section>

    <!-- Servicios -->
    <section class="business-section">...</section>

    <!-- Por qué elegirnos -->
    <section class="business-section bg-gray">
      <p class="about-text">...</p> <!-- 6 párrafos -->
    </section>

    <!-- Benefits -->
    <section class="business-section">...</section>

    <!-- Highlights -->
    <section class="business-section bg-gray">...</section>

    <!-- Services Directory -->
    <section class="business-section">...</section>

    <!-- FAQs -->
    <section class="business-section bg-gray">
      <div class="faqs-section">...</div>
    </section>

    <!-- Reviews -->
    <section class="business-section">...</section>

    <!-- Contact -->
    <section class="business-section" id="contacto">
      <div class="contact-card">
        <div class="contact-icon">...</div>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="footer">...</footer>

  <!-- JavaScript -->
  <script src="../../js/app.js"></script>
  <script src="../../js/perfil.js"></script>
</body>
</html>
```

#### Clases CSS CORRECTAS (Usar Siempre):

✅ **CORRECTAS**:
- `business-section` - Sección normal
- `business-section bg-gray` - Sección con fondo gris (alternar)
- `about-text` - Párrafos en sección "Por qué elegirnos"
- `faqs-section` - Wrapper de FAQs
- `contact-card` - Tarjeta de contacto
- `contact-icon` - Wrapper de iconos en contact
- `service-card` - Tarjeta de servicio
- `business-hero` - Hero section
- `breadcrumbs` - Breadcrumbs

❌ **INCORRECTAS** (NUNCA usar):
- `services-section` ❌
- `why-choose-us` ❌
- `section-text` ❌
- `faq-section` ❌ (correcto: `faqs-section`)
- `contact-section` ❌
- `contact-item` ❌
- `business-header` ❌ (existe pero no para este contexto)

---

## 4. PLANTILLAS UNIVERSALES

### 4.1 Plantilla JSON para Card

```json
{
  "business_card": {
    "name": "EMPRESA A",
    "slug": "empresa-a",
    "category": "entretenimiento",
    "subcategory": "audio-visual",
    "image": {
      "src": "../img/img-eventos/imagen-empresa-a.webp",
      "alt": "EMPRESA A - Servicio Principal en Ciudad",
      "width": 280,
      "height": 280,
      "loading": "lazy"
    },
    "badges": [
      {
        "type": "verified",
        "text": "✓ Verificado"
      },
      {
        "type": "experience",
        "text": "15+ Años"
      }
    ],
    "rating": {
      "value": 4.8,
      "count": 245,
      "stars": "★★★★★"
    },
    "services_tags": [
      "Servicio Principal",
      "Servicio Secundario",
      "Servicio Tercero",
      "+X más"
    ],
    "short_description": "Descripción breve y específica de 120-180 caracteres que comunica valor único, experiencia y diferencial competitivo de forma directa.",
    "website": {
      "url": "https://example.com",
      "display": "example.com",
      "icon_svg": true
    },
    "location": {
      "text": "Colonia, Delegación/Municipio, Estado",
      "icon_svg": true
    },
    "contact": {
      "phone": "55 1234 5678",
      "phone_link": "tel:+525512345678",
      "whatsapp_link": "https://wa.me/5215512345678?text=Mensaje%20preconfigurado",
      "schedule": "Lun-Dom 9:00-20:00"
    },
    "links": {
      "profile": "../negocios/entretenimiento/empresa-a.html",
      "external_website": false
    }
  }
}
```

### 4.2 Plantilla HTML para Card

```html
<!-- Business Card - EMPRESA A -->
<article class="business-card">
  <div class="business-image">
    <img src="../img/img-eventos/[nombre-archivo].webp"
         alt="EMPRESA A - [Servicio Principal] [Ciudad]"
         width="280"
         height="280"
         loading="lazy">
    <div class="business-badges">
      <span class="badge badge-verified">✓ Verificado</span>
      <span class="badge badge-experience">[X+] Años</span>
    </div>
  </div>

  <div class="business-content">
    <div class="business-header">
      <h3 class="business-name">
        <a href="../negocios/[categoria]/[empresa-slug].html">EMPRESA A</a>
      </h3>
      <div class="business-rating">
        <div class="stars">★★★★★</div>
        <span class="rating-value">4.8</span>
        <span class="rating-count">([N] reseñas)</span>
      </div>
    </div>

    <div class="business-services">
      <span class="service-tag">Servicio 1</span>
      <span class="service-tag">Servicio 2</span>
      <span class="service-tag">Servicio 3</span>
      <span class="service-tag">+X más</span>
    </div>

    <p class="business-description">
      [Descripción única de 120-180 caracteres que comunica valor, experiencia y diferencial específico de la empresa. Evitar frases genéricas.]
    </p>

    <div class="business-details">
      <!-- NUEVO: Sitio Web (debe ir PRIMERO) -->
      <div class="detail-item">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/>
          <line x1="2" y1="12" x2="22" y2="12"/>
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
        </svg>
        <a href="https://example.com" target="_blank" rel="noopener">example.com</a>
      </div>

      <!-- NUEVO: Teléfono (debe ir SEGUNDO) -->
      <div class="detail-item">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
        </svg>
        <a href="tel:+525512345678">55 1234 5678</a>
      </div>

      <!-- Ubicación (tercer lugar) -->
      <div class="detail-item">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
          <circle cx="12" cy="10" r="3"/>
        </svg>
        <span>[Colonia], [Delegación], [Estado/CDMX]</span>
      </div>

      <!-- Horario (cuarto lugar) -->
      <div class="detail-item">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/>
          <polyline points="12 6 12 12 16 14"/>
        </svg>
        <span>[Lun-Dom HH:MM-HH:MM]</span>
      </div>
    </div>

    <div class="business-actions">
      <a href="tel:+52[numero]" class="btn btn-outline">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
        </svg>
        Llamar
      </a>
      <a href="https://wa.me/[numero]?text=[mensaje-preconfigurado-URL-encoded]" class="btn btn-outline" target="_blank">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
        </svg>
        WhatsApp
      </a>
      <a href="../negocios/[categoria]/[empresa-slug].html" class="btn btn-primary">Ver perfil</a>
    </div>
  </div>
</article>
```

### 4.3 Plantilla de Reseña (Estructura Markdown)

```markdown
---
title: "EMPRESA A - [Servicio Principal] [Ciudad] | [Diferencial Único]"
description: "➤ [Resumen de servicios y valor]. [Experiencia/años]. [Llamada a acción]. ☎ [Teléfono]"
keywords: "[palabra-clave-1], [palabra-clave-2], [marca], [servicio], [ubicación]"
canonical: "https://paginasamarillas.mx/negocios/[categoria]/[slug].html"
---

# EMPRESA A

## [Subtítulo descriptivo del servicio principal]

[TAGLINE - 150-180 palabras]
Párrafo gancho que comunica inmediatamente:
- ¿Qué hace la empresa?
- ¿Cuál es su diferencial único?
- ¿Por qué el cliente debería elegirla?
- Experiencia, certificaciones o reconocimientos relevantes
- Debe generar confianza y deseo de contactar

**Quick Info:**
- **Ubicación**: [Dirección completa]
- **Horario**: [Días y horas]
- **Especialización**: [Área principal]
- **Garantía**: [Beneficio diferencial]

---

## Servicios de [Categoría de la Empresa]

[80-120 palabras de introducción general a los servicios]

### [Servicio Principal 1]
[60-80 palabras describiendo este servicio de forma específica. Incluir:
- Qué incluye
- Para quién es ideal
- Beneficios específicos
- Diferenciadores técnicos o de calidad]

### [Servicio Principal 2]
[60-80 palabras describiendo este servicio...]

### [Servicio Principal 3]
[60-80 palabras describiendo este servicio...]

---

## Por qué elegir EMPRESA A

[100-150 palabras sobre diferenciales únicos. Evitar frases genéricas como "calidad" o "experiencia" sin contexto. Incluir:
- Años de experiencia con logros medibles
- Certificaciones, premios o reconocimientos
- Procesos únicos o metodología propia
- Garantías específicas
- Casos de éxito o testimonios resumidos
- Cobertura geográfica]

---

## Preguntas Frecuentes

### ¿[Pregunta relevante sobre el servicio]?
[70-100 palabras de respuesta completa y útil. Debe resolver la duda y anticipar objeciones.]

### ¿[Pregunta sobre precios, tiempos o proceso]?
[70-100 palabras...]

### ¿[Pregunta sobre cobertura o disponibilidad]?
[70-100 palabras...]

---

**Contacto**
- 📍 [Dirección]
- 📞 [Teléfono]
- 📧 [Email]
- 🌐 [Website]
```

### 4.4 Plantilla HTML Completa de Reseña

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- SEO Meta Tags [OBLIGATORIOS] -->
  <title>EMPRESA A - Servicio Principal Ciudad | Diferencial Único</title>
  <meta name="description" content="➤ Servicio específico con experiencia comprobada. 15+ años sirviendo a Ciudad. Solicita cotización hoy. ☎ 55 1234 5678">
  <meta name="keywords" content="servicio-principal, categoria, ciudad, empresa-a, palabra-clave-1, palabra-clave-2">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://paginasamarillas.mx/negocios/categoria/empresa-a.html">

  <!-- Open Graph [OBLIGATORIOS] -->
  <meta property="og:title" content="EMPRESA A - Servicio Principal Ciudad">
  <meta property="og:description" content="Servicio específico con 15+ años de experiencia">
  <meta property="og:url" content="https://paginasamarillas.mx/negocios/categoria/empresa-a.html">
  <meta property="og:image" content="https://paginasamarillas.mx/img/empresa-a.webp">
  <meta property="og:type" content="website">

  <!-- Twitter Card [OBLIGATORIOS] -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="EMPRESA A - Servicio Principal Ciudad">
  <meta name="twitter:description" content="Servicio específico con 15+ años de experiencia">

  <!-- Geo Tags [RECOMENDADOS] -->
  <meta name="geo.region" content="MX-CMX">
  <meta name="geo.position" content="19.432608;-99.133209">

  <!-- Schema.org LocalBusiness [OBLIGATORIO] -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "EMPRESA A",
    "description": "Servicio específico con experiencia comprobada en Ciudad",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Calle Principal 123",
      "addressLocality": "Colonia",
      "addressRegion": "CDMX",
      "postalCode": "01234",
      "addressCountry": "MX"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 19.432608,
      "longitude": -99.133209
    },
    "telephone": "+52-55-1234-5678",
    "email": "contacto@empresa-a.com",
    "url": "https://example.com",
    "priceRange": "$$",
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.8",
      "reviewCount": "245"
    }
  }
  </script>

  <!-- Schema.org BreadcrumbList [OBLIGATORIO] -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [{
      "@type": "ListItem",
      "position": 1,
      "name": "Inicio",
      "item": "https://paginasamarillas.mx"
    },{
      "@type": "ListItem",
      "position": 2,
      "name": "Categoría",
      "item": "https://paginasamarillas.mx/categorias/categoria.html"
    },{
      "@type": "ListItem",
      "position": 3,
      "name": "EMPRESA A"
    }]
  }
  </script>

  <link rel="stylesheet" href="../../css/styles.css">
</head>
<body>
  <!-- Header -->
  <header class="header">
    <div class="container">
      <nav class="navbar">
        <a href="../../index.html" class="logo">Páginas Amarillas</a>
        <ul class="nav-menu">
          <li><a href="../../index.html">Inicio</a></li>
          <li><a href="../../categorias.html">Categorías</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main>
    <!-- Breadcrumbs -->
    <div class="container">
      <nav class="breadcrumbs">
        <a href="../../index.html">Inicio</a>
        <span>/</span>
        <a href="../../categorias/categoria.html">Categoría</a>
        <span>/</span>
        <span>EMPRESA A</span>
      </nav>
    </div>

    <!-- Hero Section -->
    <section class="business-hero">
      <div class="container">
        <h1 class="business-title">EMPRESA A</h1>
        <div class="business-rating-large">
          <div class="stars">★★★★★</div>
          <span class="rating-value">4.8</span>
          <a href="https://reviews-example.com" target="_blank" rel="noopener">(245 reseñas)</a>
        </div>
        <p class="business-tagline">
          [150-180 palabras de tagline que comunica valor único, experiencia, diferenciales y genera confianza inmediata para el visitante]
        </p>

        <!-- 3 CTAs principales [OBLIGATORIOS] -->
        <div class="business-hero-info">
          <div class="hero-ctas">
            <!-- CTA 1: Llamar ahora -->
            <a href="tel:+525512345678" class="btn btn-primary btn-large">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
              </svg>
              Llamar ahora
            </a>

            <!-- CTA 2: WhatsApp -->
            <a href="https://wa.me/525512345678?text=Hola,%20quisiera%20más%20información%20sobre%20sus%20servicios" class="btn btn-outline btn-large" target="_blank" rel="noopener">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
              </svg>
              WhatsApp
            </a>

            <!-- CTA 3: Sitio Web [ACTUALIZADO - antes era "Mensaje"] -->
            <a href="https://empresa-a.com" class="btn btn-outline btn-large" target="_blank" rel="noopener">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
                <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
              </svg>
              Sitio Web
            </a>
          </div>
        </div>

        <!-- Quick Info Cards -->
        <div class="quick-info">
          <div class="info-card">
            <h3>Ubicación</h3>
            <p>Colonia, Delegación, CDMX</p>
          </div>
          <div class="info-card">
            <h3>Horario</h3>
            <p>Lun-Dom 9:00 AM - 6:00 PM</p>
          </div>
          <div class="info-card">
            <h3>Especialización</h3>
            <p>Servicio Principal Específico</p>
          </div>
          <div class="info-card">
            <h3>Garantía</h3>
            <p>Beneficio o garantía específica</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Servicios Section -->
    <section class="business-section">
      <div class="container">
        <h2>Servicios de Categoría Específica</h2>
        <p>[80-120 palabras de introducción general a los servicios]</p>

        <div class="services-grid">
          <div class="service-item">
            <h3>Servicio Principal 1</h3>
            <p>[60-80 palabras describiendo este servicio de forma específica, qué incluye, para quién es ideal, beneficios y diferenciadores]</p>
          </div>
          <div class="service-item">
            <h3>Servicio Principal 2</h3>
            <p>[60-80 palabras describiendo este servicio]</p>
          </div>
          <div class="service-item">
            <h3>Servicio Principal 3</h3>
            <p>[60-80 palabras describiendo este servicio]</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Por qué elegirnos / Sobre Nosotros Section -->
    <section class="business-section bg-gray">
      <div class="container">
        <h2>Sobre EMPRESA A</h2>
        <p class="about-text">
          [IMPORTANTE: El primer párrafo DEBE incluir un enlace con palabra clave SEO relevante apuntando al sitio web de la empresa]

          Ejemplo: Con más de 10 años de experiencia en el mercado de <a href="https://empresa-a.com" target="_blank" rel="noopener" style="color: var(--color-primary); text-decoration: underline;">renta de sonido e iluminación en CDMX</a>, nos hemos consolidado como proveedores confiables...

          [Continuar con 100-150 palabras sobre diferenciales únicos: años de experiencia con logros medibles, certificaciones, procesos únicos, garantías específicas, casos de éxito]
        </p>
        <p class="about-text">
          [Segundo párrafo con más detalles sobre la empresa, servicios adicionales, cobertura, etc.]
        </p>
      </div>
    </section>

    <!-- FAQs Section -->
    <section class="business-section bg-gray">
      <div class="container">
        <h2>Preguntas Frecuentes</h2>
        <div class="faqs-section">
          <div class="faq-item">
            <h3>¿Pregunta relevante sobre el servicio?</h3>
            <p>[70-100 palabras de respuesta completa y útil]</p>
          </div>
          <div class="faq-item">
            <h3>¿Pregunta sobre precios o tiempos?</h3>
            <p>[70-100 palabras de respuesta]</p>
          </div>
          <div class="faq-item">
            <h3>¿Pregunta sobre cobertura?</h3>
            <p>[70-100 palabras de respuesta]</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contacto Section -->
    <section class="business-section">
      <div class="container">
        <h2>Contacto</h2>
        <div class="contact-card">
          <div class="contact-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
              <circle cx="12" cy="10" r="3"/>
            </svg>
            <p>Calle Principal 123, Colonia, CDMX</p>
          </div>
          <div class="contact-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
            </svg>
            <a href="tel:+525512345678">55 1234 5678</a>
          </div>
          <div class="contact-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="2" y1="12" x2="22" y2="12"/>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
            <a href="https://example.com" target="_blank" rel="noopener">example.com</a>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-column">
          <h3>Páginas Amarillas</h3>
          <p>Directorio de empresas en México</p>
        </div>
        <div class="footer-column">
          <h4>Enlaces</h4>
          <ul>
            <li><a href="../../index.html">Inicio</a></li>
            <li><a href="../../categorias.html">Categorías</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>Legal</h4>
          <ul>
            <li><a href="../../privacidad.html">Privacidad</a></li>
            <li><a href="../../terminos.html">Términos</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2025 Páginas Amarillas México. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>
</body>
</html>
```

---

## 5. CHECKLIST PASO A PASO PARA GENERACIÓN

### 5.1 Checklist para CARD

#### Fase 1: Recopilación de Información
- [ ] **Fuente 1**: Sitio web oficial de la empresa
- [ ] **Fuente 2**: Redes sociales (Facebook, Instagram, LinkedIn)
- [ ] **Fuente 3**: Brief del cliente o información proporcionada
- [ ] **Fuente 4**: Google My Business / Reseñas públicas

#### Fase 2: Validación de Datos Verbatim
- [ ] Nombre legal EXACTO de la empresa (verificar mayúsculas, acentos)
- [ ] Dirección física completa y verificada en Google Maps
- [ ] Teléfono principal (formato: 55 1234 5678)
- [ ] Horarios de atención confirmados
- [ ] Sitio web oficial (si existe)

#### Fase 3: Extracción de Servicios
- [ ] Identificar 3-4 servicios principales que ofrece la empresa
- [ ] Convertir en service tags cortos (máx 20 caracteres)
- [ ] Verificar que NO sean genéricos ("Servicios profesionales" ❌)
- [ ] Ejemplo correcto: "Audio JBL/QSC", "Iluminación LED", "Efectos Especiales" ✅

#### Fase 4: Identificación de Diferenciales
- [ ] Años de experiencia (si aplica y es > 5 años)
- [ ] Certificaciones o acreditaciones
- [ ] Marcas que trabaja o productos exclusivos
- [ ] Cobertura geográfica específica
- [ ] Garantías o servicios incluidos únicos

#### Fase 5: Redacción de Descripción Breve
- [ ] Escribir descripción de 120-180 caracteres
- [ ] Incluir: servicio + experiencia + diferencial + beneficio
- [ ] Verificar que sea ÚNICA (no copiar de otras cards)
- [ ] Evitar frases genéricas ("alta calidad", "servicio profesional")
- [ ] Incluir palabra clave principal de forma natural

#### Fase 6: Selección de Badges
- [ ] ✓ Verificado (si tenemos confirmación de datos)
- [ ] Premium (si es cliente destacado)
- [ ] [X+] Años (si tiene > 5 años de experiencia)
- [ ] Especialistas (si tiene certificación en área específica)
- [ ] Máximo 3 badges por card

#### Fase 7: Selección de Imagen
- [ ] Imagen representativa del servicio (NO logos genéricos)
- [ ] Formato: WebP preferido, JPG/PNG aceptable
- [ ] Dimensiones: 280x280px exactas
- [ ] Peso máximo: 80 KB
- [ ] Alt text descriptivo: "[Nombre Empresa] - [Servicio] [Ciudad]"

#### Fase 8: Generación de Links
- [ ] Link interno al perfil: `../negocios/[categoria]/[slug].html`
- [ ] Link de teléfono: `tel:+52[codigo][numero]`
- [ ] Link de WhatsApp: `https://wa.me/521[codigo][numero]?text=[mensaje URL-encoded]`
- [ ] Verificar que link a perfil NO tenga `target="_blank"`

#### Fase 9: Revisión Final
- [ ] Card completa sin campos vacíos
- [ ] Descripción única y específica
- [ ] Rating realista (4.0-5.0, mayoría 4.7-4.9)
- [ ] Contador de reseñas coherente (50-500)
- [ ] Teléfono formateado correctamente
- [ ] Todos los links funcionales

### 5.2 Checklist para RESEÑA COMPLETA

#### Fase 1: Investigación Profunda
- [ ] Leer sitio web completo de la empresa
- [ ] Revisar sección "Acerca de", "Servicios", "Portafolio"
- [ ] Identificar casos de éxito o testimonios
- [ ] Buscar información de fundación, equipo, certificaciones
- [ ] Revisar redes sociales para tono de voz y valores

#### Fase 2: Definición de Palabras Clave
- [ ] **Palabra clave primaria**: [servicio + ubicación]
  - Ejemplo: "renta iluminación eventos cdmx"
- [ ] **Palabras clave secundarias** (3-5):
  - Variaciones del servicio
  - Marcas o productos específicos
  - Tipos de clientes/eventos
- [ ] Verificar volumen de búsqueda (si es posible)
- [ ] Integrar de forma natural en contenido

#### Fase 3: Estructura de Meta Tags
- [ ] **Title**: [Nombre] - [Servicio] [Ciudad] | [Diferencial] (máx 60 caracteres)
- [ ] **Description**: ➤ [Resumen] + ☎ [Teléfono] (150-160 caracteres)
- [ ] **Keywords**: 8-12 palabras clave separadas por comas
- [ ] **Canonical**: URL completa de la reseña
- [ ] **OG:Title**: Versión corta del title
- [ ] **OG:Description**: Versión del meta description
- [ ] **OG:Image**: URL completa de imagen principal

#### Fase 4: Redacción de Hero Section
- [ ] **H1**: Nombre EXACTO de la empresa
- [ ] **Tagline** (150-180 palabras):
  - Gancho inicial que captura atención
  - Descripción del servicio principal
  - Diferencial competitivo único
  - Años de experiencia o logros
  - Beneficio emocional o práctico
  - Llamada a acción sutil
- [ ] **Quick Info Cards** (4 elementos):
  - Ubicación física
  - Horario de atención
  - Especialización principal
  - Garantía o diferencial clave

#### Fase 5: Redacción de Servicios
- [ ] **Introducción general** (80-120 palabras):
  - Contexto de los servicios
  - A quién van dirigidos
  - Filosofía o enfoque de la empresa

- [ ] **Por cada servicio principal** (3-5 servicios):
  - **H3**: Nombre del servicio
  - **Descripción** (60-80 palabras):
    - Qué incluye específicamente
    - Para quién es ideal
    - Beneficios concretos
    - Diferenciadores técnicos

#### Fase 6: Redacción de "Por qué elegirnos"
- [ ] **Sección** (100-150 palabras totales):
  - Años de experiencia con contexto (no solo "10 años")
  - Certificaciones, premios, reconocimientos REALES
  - Metodología o proceso único
  - Garantías específicas
  - Cobertura geográfica
  - Equipo o infraestructura destacable
  - Casos de éxito medibles

#### Fase 7: FAQs (Opcional pero Recomendado)
- [ ] Seleccionar 3-5 preguntas frecuentes REALES
- [ ] Escribir respuestas completas (70-100 palabras cada una)
- [ ] Incluir:
  - Pregunta sobre servicios específicos
  - Pregunta sobre precios o cotizaciones
  - Pregunta sobre tiempos o disponibilidad
  - Pregunta sobre cobertura geográfica
  - Pregunta técnica específica del rubro

#### Fase 8: Schema.org Markup
- [ ] **LocalBusiness Schema**:
  - name, description
  - address completa
  - geo coordinates (verificar en Google Maps)
  - telephone, email
  - priceRange (verificar: $, $$, $$$)
  - openingHoursSpecification
  - aggregateRating (coherente con card)
  - areaServed
  - hasOfferCatalog (servicios listados)

- [ ] **BreadcrumbList Schema**
- [ ] **FAQPage Schema** (si tiene FAQs)

#### Fase 9: Optimización SEO On-Page
- [ ] Keyword primaria en H1
- [ ] Keyword primaria en primeros 100 palabras
- [ ] Keywords secundarias distribuidas naturalmente
- [ ] Internal links a categorías relacionadas
- [ ] External link al sitio web de la empresa (target="_blank")
- [ ] Imágenes con alt text descriptivo
- [ ] Headers jerárquicos (H1 único, H2 para secciones, H3 para subsecciones)

#### Fase 10: Revisión Final de Contenido
- [ ] Lectura completa en voz alta (verificar fluidez)
- [ ] Verificar que NO haya frases copiadas de otras reseñas
- [ ] Tono profesional y second person donde aplique
- [ ] Sin errores ortográficos o gramaticales
- [ ] Sin keyword stuffing (keywords suenan naturales)
- [ ] Todas las afirmaciones son verificables
- [ ] Longitudes mínimas cumplidas en todas las secciones

---

## 6. REGLAS EDITORIALES Y SEO

### 6.1 Reglas NO NEGOCIABLES

#### Unicidad del Contenido
1. **PROHIBIDO**: Copiar y pegar descripciones de otras cards o reseñas
2. **PROHIBIDO**: Usar plantillas con frases genéricas sin personalizar
3. **OBLIGATORIO**: Cada descripción debe ser 100% única y específica
4. **OBLIGATORIO**: Verificar con herramienta anti-plagio antes de publicar

#### Tono Editorial
1. **Profesional y directo**: Evitar lenguaje demasiado casual o informal
2. **Second person cuando aplique**: "Encuentra", "Descubre", "Obtén"
3. **Activo sobre pasivo**: "Ofrecemos servicios" en vez de "Servicios son ofrecidos"
4. **Concreto sobre abstracto**: "Equipos JBL Serie EON" en vez de "Equipos profesionales"

#### Longitudes Mínimas ESTRICTAS

| Elemento | Mínimo | Óptimo | Máximo |
|----------|--------|--------|--------|
| Card - Descripción | 120 caracteres | 150 caracteres | 180 caracteres |
| Meta Description | 150 caracteres | 155 caracteres | 160 caracteres |
| Hero Tagline | 120 palabras | 150 palabras | 200 palabras |
| Intro Servicios | 60 palabras | 80 palabras | 120 palabras |
| Descripción Servicio | 40 palabras | 60 palabras | 80 palabras |
| Por qué elegirnos | 80 palabras | 120 palabras | 180 palabras |
| Respuesta FAQ | 50 palabras | 75 palabras | 120 palabras |

### 6.2 Optimización SEO

#### Palabras Clave
- **Densidad**: 1-2% de keyword primaria (natural, no forzado)
- **Ubicación estratégica**:
  - Title tag
  - Meta description
  - H1
  - Primeros 100 palabras del contenido
  - Al menos un H2
  - URL (slug)
  - Alt text de imagen principal

#### Estructura de Headers
```
H1: [Nombre de Empresa] (único en la página)
  H2: Servicios de [Categoría]
    H3: [Servicio Específico 1]
    H3: [Servicio Específico 2]
  H2: Por qué elegir [Nombre]
  H2: Preguntas Frecuentes
    H3: [Pregunta 1]
    H3: [Pregunta 2]
```

#### Links Internos y Externos
- **Interno**: Link a categoría madre (1 vez)
- **Externo**: Link al sitio web oficial (target="_blank", rel="noopener")
- **No follow**: NO usar en links internos
- **Anchor text descriptivo**: Evitar "click aquí", "más información"

### 6.3 Reglas de Escritura

#### Evitar Absolutamente
❌ Frases genéricas vacías:
- "Alta calidad"
- "Servicio profesional"
- "Los mejores del mercado"
- "Atención personalizada"

#### Usar en su lugar
✅ Frases específicas y medibles:
- "Equipos JBL Serie EON con potencia de 1,000W"
- "Instalación completada en menos de 2 horas"
- "Líderes en CDMX con 500+ eventos al año"
- "Asesor dedicado con respuesta en menos de 30 minutos"

#### Prueba de Especificidad
Cada afirmación debe pasar esta prueba:
> "¿Esta frase podría aplicarse a CUALQUIER empresa de la competencia?"
> - Si SÍ → Reescribir con datos específicos
> - Si NO → Aprobada

---

## 7. ESPECIFICACIONES TÉCNICAS COMPLETAS

### 10.1 Especificaciones de Nuevos Campos (v4.0)

| Campo | Formato | Ejemplo | Obligatorio | Notas |
|-------|---------|---------|-------------|-------|
| **Sitio Web** | URL sin https://, link clicable con target="_blank" y rel="noopener" | `example.com` | ✅ Sí | Debe ir PRIMERO en business-details. Usar icono globo SVG. |
| **Teléfono** | Formato +52-55-XXXX-XXXX con link tel: | `55 1234 5678` con href="tel:+525512345678" | ✅ Sí | Debe ir SEGUNDO en business-details. Usar icono teléfono SVG. |

### 10.2 Campos Obligatorios para Card (JSON Schema)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": [
    "name",
    "slug",
    "category",
    "image",
    "badges",
    "rating",
    "services_tags",
    "short_description",
    "website",
    "location",
    "contact",
    "links"
  ],
  "properties": {
    "name": {
      "type": "string",
      "maxLength": 40,
      "description": "Nombre legal exacto de la empresa"
    },
    "slug": {
      "type": "string",
      "pattern": "^[a-z0-9-]+$",
      "description": "URL-friendly identifier"
    },
    "category": {
      "type": "string",
      "enum": ["entretenimiento", "construccion", "salud", "..."]
    },
    "image": {
      "type": "object",
      "required": ["src", "alt", "width", "height"],
      "properties": {
        "src": {"type": "string"},
        "alt": {"type": "string", "minLength": 20},
        "width": {"type": "integer", "const": 280},
        "height": {"type": "integer", "const": 280},
        "loading": {"type": "string", "const": "lazy"}
      }
    },
    "badges": {
      "type": "array",
      "minItems": 1,
      "maxItems": 3,
      "items": {
        "type": "object",
        "properties": {
          "type": {"enum": ["verified", "premium", "experience", "certified"]},
          "text": {"type": "string"}
        }
      }
    },
    "rating": {
      "type": "object",
      "required": ["value", "count"],
      "properties": {
        "value": {"type": "number", "minimum": 1.0, "maximum": 5.0},
        "count": {"type": "integer", "minimum": 10}
      }
    },
    "services_tags": {
      "type": "array",
      "minItems": 3,
      "maxItems": 4,
      "items": {"type": "string", "maxLength": 20}
    },
    "short_description": {
      "type": "string",
      "minLength": 120,
      "maxLength": 180
    },
    "location": {
      "type": "object",
      "required": ["text"],
      "properties": {
        "text": {"type": "string"}
      }
    },
    "contact": {
      "type": "object",
      "required": ["phone", "phone_link", "schedule"],
      "properties": {
        "phone": {"type": "string", "pattern": "^[0-9 ]+$"},
        "phone_link": {"type": "string", "pattern": "^tel:\\+52[0-9]+$"},
        "whatsapp_link": {"type": "string"},
        "schedule": {"type": "string"}
      }
    },
    "links": {
      "type": "object",
      "required": ["profile"],
      "properties": {
        "profile": {"type": "string", "pattern": "^\\.\\./negocios/"}
      }
    }
  }
}
```

### 10.3 Metadatos Obligatorios para Reseña

| Meta Tag | Formato | Ejemplo | Obligatorio |
|----------|---------|---------|-------------|
| `<title>` | [Nombre] - [Servicio] [Ciudad] \| [Diferencial] | REDEIL - Renta de Iluminación CDMX \| 10+ Años | ✅ |
| `meta description` | ➤ [Resumen] ☎ [Tel] | ➤ Renta profesional de iluminación... ☎ 55 4937 5172 | ✅ |
| `meta keywords` | palabra1, palabra2, marca | renta iluminación, audio profesional, redeil | ✅ |
| `link canonical` | URL completa | https://paginasamarillas.mx/negocios/... | ✅ |
| `og:title` | Versión corta de title | REDEIL - Iluminación Profesional CDMX | ✅ |
| `og:description` | Resumen de 2-3 líneas | 10+ años transformando eventos... | ✅ |
| `og:url` | URL completa | https://paginasamarillas.mx/negocios/... | ✅ |
| `og:image` | URL completa de imagen | https://paginasamarillas.mx/img/... | ✅ |
| `twitter:card` | summary_large_image | summary_large_image | ✅ |
| `geo.region` | Código ISO | MX-CMX o MX-MEX | ⚠️ |
| `geo.position` | lat;long | 19.463;-99.237 | ⚠️ |

### 7.4 Estructura Schema.org LocalBusiness (Campos Obligatorios)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "[URL de la reseña]",
  "name": "[Nombre exacto]",
  "description": "[Descripción de 1-2 oraciones]",
  "image": ["[URL imagen principal]"],
  "logo": "[URL logo]",
  "url": "[URL interna de la reseña]",
  "telephone": "[+52-codigo-numero]",
  "email": "[email]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Calle Número]",
    "addressLocality": "[Colonia]",
    "addressRegion": "[Delegación/Municipio, Estado]",
    "postalCode": "[CP]",
    "addressCountry": "MX"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[lat]",
    "longitude": "[long]"
  },
  "priceRange": "[$|$$|$$$]",
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", ...],
    "opens": "[HH:MM]",
    "closes": "[HH:MM]"
  }],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[1.0-5.0]",
    "reviewCount": "[número]",
    "bestRating": "5",
    "worstRating": "1"
  },
  "areaServed": [{
    "@type": "City",
    "name": "[Ciudad]"
  }],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Servicios de [Categoría]",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "[Servicio]",
          "description": "[Descripción breve]"
        }
      }
    ]
  },
  "sameAs": ["[URL sitio web externo]"]
}
```

---

## 8. CONTROL DE CALIDAD Y CRITERIOS DE ACEPTACIÓN

### 10.1 Checklist de QA para CARD

Antes de publicar, verificar:

#### Contenido
- [ ] ✅ Nombre de empresa es EXACTO (verificar en documentos oficiales)
- [ ] ✅ Descripción es ÚNICA (no existe en ninguna otra card)
- [ ] ✅ Descripción tiene 120-180 caracteres
- [ ] ✅ Service tags son ESPECÍFICOS (no genéricos)
- [ ] ✅ Ubicación es precisa (colonia + delegación/municipio)
- [ ] ✅ Teléfono tiene formato correcto: 55 1234 5678
- [ ] ✅ Horario es actual y verificado

#### Visual
- [ ] ✅ Imagen es relevante (representa el servicio, no logo genérico)
- [ ] ✅ Imagen es 280x280px exactas
- [ ] ✅ Imagen pesa menos de 80 KB
- [ ] ✅ Alt text es descriptivo y único
- [ ] ✅ Badges son apropiados (máximo 3)

#### Funcionalidad
- [ ] ✅ Link a perfil funciona y NO tiene target="_blank"
- [ ] ✅ Link de teléfono funciona (clic para llamar)
- [ ] ✅ Link de WhatsApp funciona y tiene mensaje preconfigurado
- [ ] ✅ Rating es realista (4.0-5.0, típicamente 4.7-4.9)
- [ ] ✅ Contador de reseñas es coherente (50-500 para la mayoría)

#### SEO
- [ ] ✅ Palabra clave principal incluida naturalmente
- [ ] ✅ Sin keyword stuffing
- [ ] ✅ Texto fluido y fácil de leer

### 10.2 Checklist de QA para RESEÑA

#### Metadatos
- [ ] ✅ Meta title tiene máximo 60 caracteres
- [ ] ✅ Meta description tiene 150-160 caracteres
- [ ] ✅ Meta description incluye símbolo ➤ y ☎
- [ ] ✅ Keywords son 8-12 palabras relevantes
- [ ] ✅ Canonical URL es correcto
- [ ] ✅ OG:Image URL es completo y funcional

#### Estructura
- [ ] ✅ Tiene un solo H1 con el nombre de empresa
- [ ] ✅ H2s están en orden lógico
- [ ] ✅ H3s están correctamente anidados bajo H2s
- [ ] ✅ No hay saltos en jerarquía (H1 → H3 sin H2)

#### Contenido
- [ ] ✅ Hero tagline tiene 150-180 palabras
- [ ] ✅ Cada sección de servicio tiene 60-80 palabras
- [ ] ✅ "Por qué elegirnos" tiene 100-150 palabras
- [ ] ✅ Cada FAQ tiene respuesta de 70-100 palabras
- [ ] ✅ NO hay frases idénticas a otras reseñas del sitio
- [ ] ✅ NO hay frases genéricas sin valor
- [ ] ✅ Todos los datos son verificables

#### SEO On-Page
- [ ] ✅ Keyword primaria en title, H1, primeros 100 palabras
- [ ] ✅ Keywords secundarias distribuidas naturalmente
- [ ] ✅ Densidad de keyword primaria: 1-2%
- [ ] ✅ Link externo al sitio web de la empresa (con target="_blank")
- [ ] ✅ Link interno a categoría madre
- [ ] ✅ Imágenes tienen alt text descriptivo

#### Schema.org
- [ ] ✅ LocalBusiness schema es válido (verificar con herramienta)
- [ ] ✅ Coordenadas geo son correctas (verificar en Google Maps)
- [ ] ✅ Todos los campos obligatorios están completos
- [ ] ✅ Rating en schema coincide con rating en card
- [ ] ✅ BreadcrumbList schema es correcto
- [ ] ✅ FAQPage schema presente si hay FAQs

#### Legibilidad
- [ ] ✅ Texto pasa test de lectura en voz alta
- [ ] ✅ Sin errores ortográficos o gramaticales
- [ ] ✅ Párrafos no exceden 4-5 líneas
- [ ] ✅ Uso apropiado de negritas para destacar conceptos clave
- [ ] ✅ Listas con bullets donde aplica

### 10.3 Herramientas de Validación

| Aspecto | Herramienta | URL |
|---------|-------------|-----|
| Schema.org | Google Rich Results Test | https://search.google.com/test/rich-results |
| Meta Tags | Meta Tags Preview | https://metatags.io/ |
| SEO On-Page | Yoast SEO / Rank Math | (Plugins WordPress) |
| Plagio | Copyscape / Quetext | https://www.copyscape.com |
| Legibilidad | Hemingway App | https://hemingwayapp.com/ |
| Velocidad | PageSpeed Insights | https://pagespeed.web.dev/ |

---

## 9. MANEJO DE CASOS CON INFORMACIÓN INSUFICIENTE

### 10.1 Escenario: Empresa Sin Sitio Web

#### Fuentes Alternativas
1. **Google My Business**: Buscar el nombre + ciudad en Google Maps
   - Extraer: dirección, teléfono, horario, fotos, reseñas
2. **Redes Sociales**:
   - Facebook Business Page
   - Instagram Business
   - LinkedIn Company Page
3. **Directorios Existentes**:
   - Páginas Amarillas tradicionales
   - Sección Amarilla
   - Directorios especializados del sector

#### Preguntas Rápidas al Cliente (Email Template)
```
Asunto: Información requerida para perfil de [Nombre Empresa]

Hola [Nombre],

Para crear un perfil completo y optimizado de [Nombre Empresa], necesitamos los siguientes datos:

INFORMACIÓN BÁSICA (OBLIGATORIA):
1. Nombre legal exacto de la empresa
2. Dirección física completa (calle, número, colonia, CP, ciudad)
3. Teléfono principal
4. Email de contacto
5. Horario de atención

SERVICIOS (OBLIGATORIO):
6. Lista de 3-5 servicios principales que ofrecen
7. Breve descripción (2-3 líneas) de cada servicio

DIFERENCIALES (IMPORTANTE):
8. ¿Cuántos años tienen en el mercado?
9. ¿Tienen certificaciones, premios o reconocimientos?
10. ¿Qué los hace diferentes de la competencia?
11. ¿Trabajan con marcas o productos específicos?
12. ¿Cuál es su área de cobertura?

OPCIONAL (Mejora el perfil):
13. Sitio web (si tienen)
14. Redes sociales (Facebook, Instagram, etc.)
15. Casos de éxito o testimonios de clientes
16. Fotos de proyectos o instalaciones

Por favor enviar esta información en los próximos 2-3 días hábiles.

Saludos,
[Tu nombre]
```

### 10.2 Placeholders Aceptables (Marcados para Revisión)

Cuando la información NO esté disponible y sea urgente publicar:

| Campo | Placeholder Aceptable | Marcar para Revisión |
|-------|----------------------|----------------------|
| Horario | "Lun-Vie 9:00-18:00" | ⚠️ TODO: Verificar horario real |
| Rating | 4.5 (sin reseñas visibles) | ⚠️ TODO: Obtener reseñas reales |
| Año fundación | Año actual - 5 años | ⚠️ TODO: Confirmar fecha exacta |
| Email | info@[dominio].com | ⚠️ TODO: Validar email real |
| Descripción servicio | "Servicio profesional de [categoría] en [ciudad]" | ⚠️ TODO: Expandir con detalles específicos |

**IMPORTANTE**: Todos los placeholders deben estar marcados en un archivo de seguimiento para actualizar una vez se obtenga la información real.

### 10.3 Contenido Mínimo Viable

Si la información es muy limitada, el contenido mínimo para publicar es:

#### Card Mínima:
- Nombre ✅
- Categoría ✅
- Ubicación (al menos ciudad) ✅
- Teléfono ✅
- Descripción genérica de 120 caracteres ⚠️
- 1 badge (Verificado) ✅
- Rating estimado 4.5 ⚠️
- Link a perfil ✅

#### Reseña Mínima:
- H1 con nombre ✅
- Tagline de 120 palabras (puede ser más genérico) ⚠️
- 2-3 servicios con descripción breve ✅
- Sección "Por qué elegirnos" con 80 palabras ⚠️
- Schema.org LocalBusiness básico ✅
- Meta tags esenciales ✅

**Compromiso**: Actualizar a versión completa en máximo 7 días.

---

## 10. EJEMPLOS PRÁCTICOS NEUTROS

### 10.1 Ejemplo de Card Completa (Empresa Ficticia A)

```html
<!-- Business Card - SERVICIOS AUDIOVISUALES PROFESIONALES SA -->
<article class="business-card">
  <div class="business-image">
    <img src="../img/img-eventos/empresa-a-eventos.webp"
         alt="Servicios Audiovisuales Profesionales - Renta de Equipos para Eventos Corporativos CDMX"
         width="280"
         height="280"
         loading="lazy">
    <div class="business-badges">
      <span class="badge badge-verified">✓ Verificado</span>
      <span class="badge badge-experience">15+ Años</span>
    </div>
  </div>

  <div class="business-content">
    <div class="business-header">
      <h3 class="business-name">
        <a href="../negocios/entretenimiento/servicios-audiovisuales-profesionales.html">Servicios Audiovisuales Profesionales</a>
      </h3>
      <div class="business-rating">
        <div class="stars">★★★★★</div>
        <span class="rating-value">4.8</span>
        <span class="rating-count">(287 reseñas)</span>
      </div>
    </div>

    <div class="business-services">
      <span class="service-tag">Proyección 4K</span>
      <span class="service-tag">Audio Shure</span>
      <span class="service-tag">Streaming en Vivo</span>
      <span class="service-tag">+3 más</span>
    </div>

    <p class="business-description">
      Especialistas en soluciones audiovisuales para congresos y convenciones. 15+ años equipando eventos de Fortune 500. Proyectores 4K, audio Shure, streaming multipantalla y soporte técnico on-site incluido.
    </p>

    <div class="business-details">
      <div class="detail-item">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
          <circle cx="12" cy="10" r="3"/>
        </svg>
        <span>Polanco, Miguel Hidalgo, CDMX</span>
      </div>
      <div class="detail-item">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
        </svg>
        <a href="tel:+525555987654">55 5598 7654</a>
      </div>
      <div class="detail-item">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/>
          <polyline points="12 6 12 12 16 14"/>
        </svg>
        <span>Lun-Vie 8:00-19:00, Sáb 9:00-14:00</span>
      </div>
    </div>

    <div class="business-actions">
      <a href="tel:+525555987654" class="btn btn-outline">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
        </svg>
        Llamar
      </a>
      <a href="https://wa.me/5215555987654?text=Hola%2C%20necesito%20cotizar%20equipos%20audiovisuales%20para%20mi%20evento%20corporativo" class="btn btn-outline" target="_blank">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
        </svg>
        WhatsApp
      </a>
      <a href="../negocios/entretenimiento/servicios-audiovisuales-profesionales.html" class="btn btn-primary">Ver perfil</a>
    </div>
  </div>
</article>
```

### 10.2 Ejemplo de Reseña Completa (Fragmento - Empresa Ficticia B)

```markdown
---
title: "Constructora XYZ - Construcción Residencial y Comercial CDMX | 20+ Años"
description: "➤ Constructora líder con 20+ años transformando proyectos en realidad. Obra negra, acabados premium, remodelaciones. Entrega puntual garantizada. ☎ 55 1234 5678"
keywords: "constructora cdmx, construcción residencial, obra negra, remodelaciones, constructora xyz, acabados premium"
canonical: "https://paginasamarillas.mx/negocios/construccion/constructora-xyz.html"
---

# Constructora XYZ

## Construcción Residencial y Comercial de Alto Nivel en CDMX

Desde hace más de 20 años, Constructora XYZ ha sido sinónimo de excelencia en la industria de la construcción en la Ciudad de México. Nos especializamos en proyectos residenciales y comerciales de mediana y gran envergadura, con un enfoque inquebrantable en la calidad estructural, el cumplimiento de tiempos y la satisfacción total del cliente.

Nuestro equipo está conformado por ingenieros civiles certificados, arquitectos con maestría en diseño sustentable y maestros de obra con décadas de experiencia en el sector. Esta combinación de talento técnico y experiencia práctica nos permite enfrentar proyectos complejos con confianza y entregar resultados que superan expectativas.

A lo largo de dos décadas, hemos completado más de 300 proyectos, desde casas habitación de 150m² hasta edificios comerciales de 5,000m². Nuestros clientes incluyen desarrolladores inmobiliarios líderes en CDMX, familias que confían en nosotros para construir el hogar de sus sueños, y empresas que requieren espacios corporativos funcionales y estéticamente impecables.

Lo que nos distingue es nuestro compromiso con la transparencia: proporcionamos cotizaciones detalladas sin costos ocultos, cronogramas realistas con hitos semanales verificables, y comunicación constante durante todo el proceso constructivo.

**Quick Info:**
- **Ubicación**: Insurgentes Sur 1234, Del Valle, Benito Juárez, 03100 CDMX
- **Horario**: Lun-Vie 8:00-18:00, Sáb 9:00-14:00
- **Especialización**: Construcción Residencial y Comercial
- **Garantía**: 5 años en estructura, 2 años en acabados

---

## Servicios de Construcción

En Constructora XYZ ofrecemos un portafolio completo de servicios de construcción que abarcan desde la conceptualización inicial hasta la entrega de llaves. Trabajamos bajo metodologías probadas de gestión de proyectos (PMI) y cumplimos rigurosamente con el Reglamento de Construcción de la CDMX.

### Obra Negra Completa
La cimentación es el corazón de cualquier edificación exitosa. Nuestro servicio de obra negra incluye: estudios de mecánica de suelos, diseño y cálculo estructural por DRO certificado, excavación y nivelación, cimentación (losas, zapatas o pilotes según el caso), estructura de concreto armado o acero estructural, muros de block o concreto, y losa de entrepiso. Utilizamos concreto premezclado de plantas certificadas con resistencias verificadas en laboratorio, acero de refuerzo grado 42 cumpliendo normas NMX, y realizamos pruebas de revenimiento y resistencia en cada colado. Nuestros tiempos de fraguado respetan estrictamente las normas ACI para garantizar la integridad estructural a largo plazo.

### Acabados Premium
Los acabados transforman una estructura en un espacio habitable de alto nivel. Ofrecemos acabados completos que incluyen: instalaciones hidráulicas y sanitarias con tubería hidro3 o cobre según especificación, instalaciones eléctricas con cable THW calibrado y centro de carga Schneider o Square D, yeso en muros y plafones con acabado fino listo para pintura, pisos de porcelanato, madera de ingeniería o mármol según diseño, carpintería de puertas y closets en maderas nobles o MDF laqueado, cancelería de aluminio o PVC de alta eficiencia térmica, y pintura vinílica premium libre de VOCs. Trabajamos con proveedores de primera línea como Helvex, Interceramic, Eurotech y Casa Marzam para garantizar durabilidad y estética.

### Remodelaciones y Ampliaciones
¿Tu espacio actual ya no se adapta a tus necesidades? Nos especializamos en proyectos de remodelación que respetan la estructura existente mientras modernizamos instalaciones y espacios. Nuestros servicios de remodelación incluyen: levantamiento arquitectónico del espacio actual, diseño arquitectónico de la nueva distribución con renders 3D, gestión de permisos ante delegación si se requieren cambios estructurales, demolición controlada con protección de áreas no afectadas, modificación de muros (siempre verificando que no sean de carga), actualización de instalaciones eléctricas e hidráulicas a normativa vigente, y aplicación de acabados nuevos. Hemos remodelado desde departamentos de 60m² hasta casas completas de 400m², siempre entregando en los tiempos pactados y minimizando molestias para los ocupantes.

---

## Por qué elegir Constructora XYZ

Con más de 20 años en el mercado de la construcción en CDMX, hemos construido nuestra reputación proyecto a proyecto, cliente satisfecho tras cliente satisfecho. Somos una empresa 100% mexicana, registrada ante la SHCP y con responsabilidad civil vigente.

Nuestros ingenieros son miembros activos del Colegio de Ingenieros Civiles de México (CICM) y nuestros proyectos cuentan con Dirección Responsable de Obra (DRO) certificada, cumpliendo rigurosamente con el Reglamento de Construcción de la Ciudad de México.

Lo que realmente nos diferencia es nuestro enfoque en la gestión transparente: cada proyecto inicia con un contrato detallado que especifica alcances, tiempos, costos y forma de pago. Proporcionamos un cronograma semanal con hitos verificables (cimentación, estructura, instalaciones, acabados) y enviamos reportes fotográficos semanales para clientes que no pueden visitar la obra diariamente.

Garantizamos nuestro trabajo: 5 años en estructura (cimentación, columnas, trabes, losas) y 2 años en acabados e instalaciones. Además, ofrecemos un año de mantenimiento gratuito post-entrega para resolver cualquier detalle menor que pueda surgir.

Nuestros clientes nos recomiendan porque cumplimos lo prometido: el 94% de nuestros proyectos se han entregado en el plazo pactado, y nuestro índice de recomendación (NPS) es de 87/100, muy superior al promedio de la industria (52/100).

---

## Preguntas Frecuentes

### ¿Cuánto tiempo toma construir una casa de 200m²?
El tiempo de construcción depende de varios factores: complejidad del diseño, tipo de terreno, acabados seleccionados y condiciones climáticas. Para una casa de 200m² con acabados estándar en un terreno sin complicaciones, nuestro cronograma típico es: 2-3 semanas para obra negra (cimentación y estructura), 3-4 semanas para instalaciones y albañilería, y 4-5 semanas para acabados. En total, entre 10-12 semanas (2.5-3 meses) desde el inicio de obra hasta la entrega de llaves. Esto asume que los permisos ya están tramitados. Si incluimos gestión de permisos, añadir 3-4 semanas adicionales. Proporcionamos un cronograma detallado Gantt en la firma del contrato con fechas específicas para cada etapa.

### ¿Ofrecen financiamiento o planes de pago?
Sí, entendemos que una construcción es una inversión importante. Ofrecemos esquemas de pago flexibles atados a avances de obra. El esquema estándar es: 30% anticipo al firmar contrato (cubre materiales iniciales), 25% al terminar cimentación, 25% al terminar estructura y muros, 15% al terminar instalaciones, y 5% contra entrega final. También tenemos convenios con instituciones financieras (Banorte, HSBC) para créditos puente en proyectos mayores a $2 millones. No cobramos intereses por pagos diferidos, solo solicitamos que los pagos se realicen según el calendario pactado para mantener el flujo de materiales y mano de obra.

### ¿Qué garantías ofrecen en sus construcciones?
Ofrecemos garantías competitivas respaldadas por pólizas de responsabilidad civil: 5 años en elementos estructurales (cimentación, columnas, trabes, losas, muros de carga). Esto cubre grietas estructurales, hundimientos o fallas en concreto. 2 años en instalaciones hidráulicas, sanitarias y eléctricas (cubre fugas, cortos circuitos, problemas de drenaje). 1 año en acabados (pisos, azulejos, pintura, cancelería). Adicionalmente, incluimos 1 año de mantenimiento gratuito post-entrega: durante este período atendemos cualquier detalle menor sin costo (ajustes de puertas, retoques de pintura, sellado de juntas). Todas nuestras garantías están especificadas en el contrato y respaldadas por nuestra póliza de RC por $5 millones.

---

**Contacto**
- 📍 Insurgentes Sur 1234, Del Valle, Benito Juárez, 03100 CDMX
- 📞 55 1234 5678
- 📧 contacto@constructoraxyz.com.mx
- 🌐 www.constructoraxyz.com.mx
```

---

## 11. REGISTRO DE CAMBIOS

### Versión 5.1 - 16 de noviembre de 2025

🔄 **ACTUALIZACIÓN - CAMBIOS EN CTAs Y SEO LINKS**

**Cambios Mayores**:

✅ **ACTUALIZADO**: Tercer botón CTA en Hero Section
- **ANTES**: Botón "Mensaje" que hacía scroll al formulario de contacto
- **AHORA**: Botón "Sitio Web" que redirige al sitio web de la empresa
- El botón ahora usa `<a href="[URL_EMPRESA]" target="_blank" rel="noopener">` con icono de link externo
- Icono cambiado de sobre (envelope) a enlace externo (link icon)

✅ **NUEVO**: Link SEO obligatorio en sección "Sobre [EMPRESA]"
- El primer párrafo de la sección "Sobre" DEBE incluir un enlace con palabra clave SEO relevante
- El enlace debe apuntar al sitio web de la empresa
- Estilo obligatorio: `style="color: var(--color-primary); text-decoration: underline;"`
- Atributos: `target="_blank" rel="noopener"`
- Ejemplo: `<a href="https://empresa.com" target="_blank" rel="noopener" style="color: var(--color-primary); text-decoration: underline;">renta de sonido e iluminación en CDMX</a>`

🚨 **CRÍTICO**: Gestión de Imágenes en Cards
- **REGLA ABSOLUTA**: Imágenes en cards deben usar **RUTAS ABSOLUTAS** desde raíz: `/img/img-[categoría]/`
- Agregada nueva subsección "🚨 CRÍTICO: Gestión de Imágenes en Cards" (líneas 277-324)
- Documenta carpetas por categoría: `img-seguridad-privada/`, `img-eventos/`, etc.
- Incluye ejemplos CORRECTOS vs INCORRECTOS
- Proceso paso a paso para seleccionar imágenes
- Lista de imágenes comunes por carpeta
- **IMPACTO**: Previene error común de rutas relativas que rompen las imágenes en cards

**Secciones Actualizadas**:
- Checklist de 21 secciones (ahora incluye "3 CTAs principales" y "Link SEO en Sobre")
- Plantilla HTML completa de reseña (actualizada con nuevo código de CTAs)
- Sección "Por qué elegirnos" renombrada a "Sobre [EMPRESA]" con instrucciones de link SEO

**Empresas Actualizadas**:
- RESOIL
- Renta de Iluminación
- Bolas Disco (BOLDIS)
- EVENTECH
- REDEIL
- PODIUMEX
- INFLAPY (Inflables para Fiestas)

**Impacto**: Mejora el SEO externo al incluir links con palabras clave relevantes hacia los sitios web de las empresas, y mejora la experiencia de usuario al proporcionar acceso directo al sitio web desde el hero section.

---

### Versión 5.0 - 15 de noviembre de 2025

🚨 **ACTUALIZACIÓN CRÍTICA - PROCESO OBLIGATORIO Y TROUBLESHOOTING**

**Cambios Mayores**:

✅ **NUEVO**: Sección 2 "PROCESO OBLIGATORIO DE GENERACIÓN"
- Regla absoluta: NUNCA generar desde cero
- Proceso paso a paso: Copiar → Modificar → Validar
- Checklist obligatorio de 21 secciones
- Comandos de validación técnica

✅ **NUEVO**: Subsección 3.3 "Estructura HTML Exacta"
- Estructura completa de referencia
- Clases CSS correctas vs incorrectas
- Advertencias sobre modificaciones

✅ **NUEVO**: Sección 16 "TROUBLESHOOTING Y SOLUCIÓN DE ERRORES"
- 5 problemas comunes con soluciones
- Comandos de diagnóstico
- Tabla de diagnóstico rápido

✅ **MEJORADO**: Template de comando para Claude
- Formato exacto para solicitar generación
- Incluye toda la información necesaria
- Previene errores comunes

**Errores Documentados del Caso INFLAPY**:
1. Encoding corrupto (binary en vez de UTF-8)
2. Estructura HTML diferente generada
3. Secciones incompletas (FAQs, Reviews, Services Directory)
4. Clases CSS incorrectas
5. Falta de proceso estandarizado

**Prevención Implementada**:
- Proceso obligatorio de 4 pasos
- Checklist de 21 secciones
- 5 comandos de validación técnica
- Tabla de errores comunes
- Troubleshooting completo

**Impacto**: Esta actualización previene completamente los errores críticos que ocurrieron durante la generación de inflables-para-fiestas.html, ahorrando horas de trabajo y garantizando calidad desde el primer intento.

---

### Versión 4.0 - 15 de noviembre de 2025

**🎯 ACTUALIZACIÓN CRÍTICA - NUEVOS CAMPOS Y CORRECCIÓN DE CLASES CSS**:

#### Nuevos Campos en Cards
- ✅ **Campo Sitio Web**: Agregado como PRIMER elemento en business-details con icono globo SVG
- ✅ **Campo Teléfono reposicionado**: Ahora es el SEGUNDO elemento (antes estaba después de ubicación)
- ✅ Orden actualizado: Sitio Web → Teléfono → Ubicación → Horario

#### Corrección de Clases CSS para Reseñas
- ✅ **Servicios**: Cambiado de `services-section` a `business-section`
- ✅ **Sobre nosotros/Por qué elegirnos**: Cambiado de `why-choose-us` a `business-section bg-gray` con párrafos `about-text`
- ✅ **FAQs**: Cambiado de `faq-section` a `business-section bg-gray` con `faqs-section` interno
- ✅ **Contacto**: Agregada sección `business-section` con `contact-card` y `contact-icon`

#### Especificaciones Técnicas Actualizadas
- ✅ Nueva tabla de especificaciones para campos de sitio web y teléfono (Sección 6.1)
- ✅ JSON Schema actualizado con campo "website" obligatorio
- ✅ Plantillas HTML y JSON actualizadas con ejemplos completos

#### Mejoras en Documentación
- ✅ Todas las plantillas HTML ahora muestran estructura completa y funcional
- ✅ Comentarios claros en código indicando campos NUEVOS y orden requerido
- ✅ Ejemplos actualizados con iconos SVG correctos para cada campo

### Versión 3.0 - 15 de noviembre de 2025

**🚀 MEJORAS MAYORES - AUTOMATIZACIÓN Y OPTIMIZACIÓN PARA CLAUDE**:

#### Nuevas Secciones
- ✅ **Sección 11**: Prompt Engineering para Claude con plantillas estructuradas
- ✅ **Sección 12**: Sistema de Puntuación de Calidad (0-100 puntos)
- ✅ **Sección 13**: Configuración Centralizada (.claude-config.json)
- ✅ **Sección 14**: Automatización y Validación con scripts JavaScript

#### Prompt Engineering (Sección 11)
- Prompt maestro estructurado en 5 fases
- Variables dinámicas reutilizables ({{empresa}}, {{categoria}}, etc.)
- Prompts especializados por tipo de tarea (card rápida, reseña completa, actualización)
- Sistema de auto-validación integrado en prompts
- Estimación de tiempos por fase

#### Sistema de Puntuación (Sección 12)
- Métrica objetiva de 0-100 puntos con 5 criterios:
  - Unicidad de Contenido (30%)
  - Optimización SEO (25%)
  - Cumplimiento de Longitudes (20%)
  - Especificidad de Información (15%)
  - Validez de Schema.org (10%)
- 6 niveles de aprobación (Excelente a Rechazado)
- Plantilla JSON de reporte de calidad
- Función JavaScript para cálculo automático

#### Configuración Centralizada (Sección 13)
- Archivo `.claude-config.json` con todas las reglas
- Variables de entorno `.env` para datos sensibles
- Configuración regional (México, es-MX, formato teléfono)
- Límites de contenido por sección
- Lista de frases prohibidas
- Tipos de badges, rangos de ratings, estructura URLs

#### Automatización (Sección 14)
- Script `validate-content.js` con clase ContentValidator
- Script `workflow-automation.js` con proceso de 5 pasos
- Comandos CLI (`cli-commands.sh`) para terminal
- Validación automática de unicidad, longitudes, SEO, Schema.org
- Detección de frases genéricas prohibidas

**Mejoras de Integración**:
- Optimizado específicamente para Claude Code + VS Code
- Reducción estimada de 70% en tiempo de generación
- Validación automática en tiempo real
- Workflow de 5 fases completamente documentado

**Mejoras de Calidad**:
- Métricas objetivas y cuantificables
- Sistema de puntuación transparente
- Reportes de QA automáticos
- Trazabilidad completa del proceso

---

### Versión 2.0 - 15 de noviembre de 2025

**Cambios Mayores**:
- ✅ Análisis técnico completo de estructura base (redeil.html)
- ✅ Creación de plantillas universales JSON y HTML
- ✅ Checklists detallados paso a paso para card y reseña
- ✅ Reglas editoriales y SEO expandidas con longitudes mínimas estrictas
- ✅ Especificaciones técnicas completas (JSON Schema, Meta tags, Schema.org)
- ✅ Criterios de aceptación y QA detallados
- ✅ Manejo de casos con información insuficiente
- ✅ Ejemplos prácticos neutros completos (Empresa A y Empresa B)

**Mejoras de Proceso**:
- Enfoque en unicidad y especificidad del contenido
- Prohibición explícita de contenido genérico
- Prueba de especificidad para validar afirmaciones
- Procedimiento para información incompleta
- Plantillas de comunicación con clientes

**Documentación Técnica**:
- JSON Schema validation para cards
- Tabla completa de metadatos obligatorios
- Estructura Schema.org LocalBusiness completa
- Lista de herramientas de validación

---

**Documento actualizado por**: Claude AI (Sonnet 4.5)
**Fecha**: 15 de noviembre de 2025
**Próxima revisión recomendada**: 15 de febrero de 2026
**Versión anterior**: 4.0

---

## ANEXO: Mini-Prompt para Uso Rápido

Cuando tengas la información de una nueva empresa, usa este prompt:

```
Genera la CARD y la RESEÑA para la empresa {{company_name}}.

Datos disponibles: {{raw_text_o_URL}}

Instrucciones:
1. Seguir DOCUMENTO-MAESTRO-CARDS-RESENAS.md v5.0 actualizado
2. OBLIGATORIO: Usar PROCESO OBLIGATORIO (Sección 2) - Copiar redeil.html y modificar solo texto
3. Contenido 100% único y específico (NO frases genéricas)
4. Verificar longitudes mínimas en todas las secciones
5. Incluir Schema.org LocalBusiness completo
6. Optimizar para SEO con palabras clave naturales
7. Validar con comandos técnicos antes de entregar

Salidas esperadas:
1. Card (HTML completo + JSON de respaldo)
2. Reseña (HTML completo con meta tags + Schema.org)
3. Checklist de QA con items verificados

Confirmar que TODO el contenido es específico para {{company_name}} y NO reutiliza frases de otras empresas.
```

---

## 12. PROMPT ENGINEERING PARA CLAUDE

### 15.1 Prompt Maestro Estructurado

Este prompt está diseñado para maximizar la eficiencia de Claude al generar contenido para cards y reseñas.

```markdown
## CONTEXTO Y ROLE
Eres un experto en creación de contenido SEO para directorios B2B mexicanos, especializado en Páginas Amarillas México. Tu tarea es generar cards y reseñas que cumplan con el estándar v3.0 del Documento Maestro.

## VARIABLES DE ENTRADA
{{empresa_nombre}} = [Nombre exacto de la empresa]
{{categoria}} = [entretenimiento|construccion|salud|servicios|etc]
{{ciudad}} = [CDMX|Guadalajara|Monterrey|etc]
{{info_disponible}} = [URL sitio web|Brief cliente|Google Business|Texto proporcionado]

## PROCESO DE 5 FASES

### FASE 1: INVESTIGACIÓN (2-3 min)
- Analizar {{info_disponible}} exhaustivamente
- Extraer datos clave: servicios, diferenciales, años experiencia, certificaciones
- Identificar palabras clave primarias y secundarias
- Verificar información de contacto (dirección, teléfono, horario)

### FASE 2: VALIDACIÓN (1 min)
Verificar campos obligatorios:
- ✅ Nombre legal exacto
- ✅ Dirección física completa
- ✅ Teléfono formato 55 1234 5678
- ✅ Al menos 3-4 servicios específicos
- ✅ Diferencial competitivo único

### FASE 3: GENERACIÓN (5-7 min)
Crear SIMULTÁNEAMENTE:
1. **Card HTML** con descripción única 120-180 caracteres
2. **Card JSON** de respaldo
3. **Reseña HTML** completa con meta tags y Schema.org
4. **Schema.org LocalBusiness** validado

### FASE 4: OPTIMIZACIÓN SEO (2 min)
- Keyword primaria en: title, H1, primeros 100 palabras, meta description
- Densidad keyword: 1-2% (natural, no forzado)
- Links internos y externos correctos
- Alt text descriptivo en imágenes

### FASE 5: QA AUTOMÁTICO (2 min)
Ejecutar checklist:
- [ ] Contenido 100% único (verificar con Prueba de Especificidad)
- [ ] Longitudes mínimas cumplidas en TODAS las secciones
- [ ] Sin frases genéricas prohibidas
- [ ] Schema.org válido
- [ ] Links funcionales (interno SIN target="_blank", externo CON target="_blank")

## CONSTRAINTS (REGLAS ESTRICTAS)
❌ PROHIBIDO:
- Copiar frases de otras cards/reseñas
- Usar frases genéricas: "alta calidad", "servicio profesional", "los mejores"
- Keyword stuffing
- Descripciones menores a longitudes mínimas

✅ OBLIGATORIO:
- Contenido específico con datos medibles
- Prueba de Especificidad aprobada
- Longitudes exactas por sección
- Schema.org completo y válido

## OUTPUT ESPERADO
```json
{
  "card_html": "<!-- Código HTML completo de la card -->",
  "card_json": {
    "name": "{{empresa_nombre}}",
    "slug": "{{slug-generado}}",
    "category": "{{categoria}}",
    // ... resto de campos
  },
  "resena_html": "<!-- HTML completo con <!DOCTYPE>, meta tags, Schema.org -->",
  "schema_org": {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    // ... estructura completa
  },
  "qa_report": {
    "unicidad": true,
    "longitudes_minimas": true,
    "seo_optimizado": true,
    "schema_valido": true,
    "puntuacion_total": 95
  }
}
```

## EXAMPLES
[Referirse a Sección 9: Ejemplos Prácticos Neutros]
```

### 15.2 Variables Dinámicas para Prompts

| Variable | Descripción | Ejemplo | Uso en Prompt |
|----------|-------------|---------|---------------|
| `{{empresa}}` | Nombre exacto de la empresa | REDEIL | `Genera card para {{empresa}}` |
| `{{categoria}}` | Categoría principal | entretenimiento | `Categoria: {{categoria}}` |
| `{{servicios}}` | Lista de servicios separados por coma | audio, iluminación, video | `Servicios: {{servicios}}` |
| `{{ciudad}}` | Ciudad y estado | CDMX | `Ubicación: {{ciudad}}` |
| `{{diferencial}}` | Propuesta única de valor | 15+ años, equipos JBL Serie EON | `Diferencial: {{diferencial}}` |
| `{{keywords}}` | Palabras clave SEO | renta audio eventos cdmx | `Keywords: {{keywords}}` |
| `{{url_sitio}}` | URL del sitio web oficial | https://empresa.com | `Analizar: {{url_sitio}}` |
| `{{telefono}}` | Teléfono de contacto | 55 1234 5678 | `Contacto: {{telefono}}` |

### 15.3 Prompts Especializados por Tipo de Tarea

#### Prompt para Card Rápida (Solo Card, Sin Reseña)

```
TAREA: Generar SOLO la card para {{empresa_nombre}}

DATOS:
- Categoría: {{categoria}}
- Servicios: {{servicios}}
- Ubicación: {{ciudad}}
- Diferencial: {{diferencial}}

SALIDA REQUERIDA:
1. HTML de la card completo
2. JSON de respaldo
3. Descripción de 120-180 caracteres (verificar contador)

TIEMPO ESTIMADO: 3-5 minutos
```

#### Prompt para Reseña Completa (Card + Reseña)

```
TAREA: Generar card completa + reseña para {{empresa_nombre}}

FUENTE DE INFORMACIÓN: {{url_sitio}}

PROCESO:
1. Analizar sitio web completo
2. Extraer todos los servicios (mínimo 3, máximo 5)
3. Identificar diferencial único
4. Generar card HTML + JSON
5. Generar reseña con:
   - Hero tagline: 150-180 palabras
   - Servicios: 60-80 palabras c/u
   - Por qué elegirnos: 100-150 palabras
   - FAQs: 3-5 preguntas con respuestas 70-100 palabras
6. Schema.org LocalBusiness completo

SALIDA: Card HTML, Card JSON, Reseña HTML, Schema.org, QA Report

TIEMPO ESTIMADO: 10-15 minutos
```

#### Prompt para Actualización de Contenido Existente

```
TAREA: Actualizar contenido de {{empresa_nombre}} para mejorar puntuación de calidad

CONTENIDO ACTUAL: [pegar contenido]

PROBLEMAS IDENTIFICADOS:
- Descripción genérica (no pasa Prueba de Especificidad)
- Longitud insuficiente en sección "Por qué elegirnos"
- Falta Schema.org FAQPage

MEJORAS REQUERIDAS:
1. Reescribir descripción con datos específicos
2. Expandir "Por qué elegirnos" a 120 palabras
3. Agregar Schema.org FAQPage

SALIDA: Contenido mejorado + QA report comparativo
```

### 13.4 Sistema de Validación en Prompts

Incluir en cada prompt la siguiente sección de auto-validación para Claude:

```markdown
## AUTO-VALIDACIÓN OBLIGATORIA

Antes de entregar el output, ejecutar:

### Test 1: Prueba de Especificidad
Para cada afirmación en descripción y reseña:
> "¿Esta frase podría aplicarse a CUALQUIER competidor?"
> - Si SÍ → Falla (reescribir)
> - Si NO → Pasa

### Test 2: Contador de Palabras/Caracteres
Verificar longitudes mínimas:
- Card descripción: 120-180 caracteres ✅
- Hero tagline: 150-180 palabras ✅
- Servicios: 60-80 palabras c/u ✅
- Por qué elegirnos: 100-150 palabras ✅
- FAQ respuestas: 70-100 palabras c/u ✅

### Test 3: Frases Prohibidas
Buscar y eliminar:
- ❌ "alta calidad"
- ❌ "servicio profesional"
- ❌ "los mejores del mercado"
- ❌ "atención personalizada"
- ❌ "excelencia en el servicio"

### Test 4: Validación de Links
- Link a perfil: NO tiene target="_blank" ✅
- Link a sitio externo: SÍ tiene target="_blank" ✅
- Links de teléfono: formato tel:+52XXXXXXXXXX ✅
- Links de WhatsApp: formato wa.me correcto ✅

### Test 5: Schema.org
- JSON-LD válido (sin errores de sintaxis) ✅
- Todos los campos obligatorios presentes ✅
- Coordenadas geo verificadas ✅
```

---

## 13. SISTEMA DE PUNTUACIÓN DE CALIDAD

### 15.1 Métrica de Calidad (Escala 0-100 puntos)

Este sistema permite evaluar objetivamente cada card y reseña generada.

| Criterio | Peso | Puntos Máximos | Verificación |
|----------|------|----------------|--------------|
| **Unicidad de Contenido** | 30% | 30 pts | < 30% similitud con contenido existente |
| **Optimización SEO** | 25% | 25 pts | Keyword density 1-2%, meta tags completos, estructura headers |
| **Cumplimiento de Longitudes** | 20% | 20 pts | Todas las secciones cumplen mínimos establecidos |
| **Especificidad de Información** | 15% | 15 pts | Sin frases genéricas, datos concretos y medibles |
| **Validez de Schema.org** | 10% | 10 pts | Schema válido sin errores según Google Rich Results Test |

#### Desglose Detallado por Criterio

##### 1. Unicidad de Contenido (30 puntos)

| Puntos | Nivel | Descripción |
|--------|-------|-------------|
| 30 | Excelente | 0-10% similitud con otras cards. Contenido 100% original |
| 25 | Muy Bueno | 11-20% similitud. Algunas frases reutilizadas pero contextualizadas |
| 20 | Bueno | 21-30% similitud. Requiere revisión de algunas secciones |
| 10 | Regular | 31-50% similitud. Múltiples frases genéricas |
| 0 | Insuficiente | >50% similitud. Contenido copiado |

**Cómo medir**: Usar herramienta de similitud de texto o comparación manual con 5-10 cards existentes.

##### 2. Optimización SEO (25 puntos)

| Sub-criterio | Puntos | Verificación |
|--------------|--------|--------------|
| Keyword en ubicaciones estratégicas | 8 pts | Title, H1, primeros 100 palabras, meta description, URL |
| Densidad keyword apropiada | 5 pts | 1-2% de keyword primaria (natural) |
| Meta tags completos | 5 pts | Title ≤60 chars, description 150-160 chars, OG tags, Twitter card |
| Estructura headers correcta | 4 pts | H1 único, H2/H3 jerárquicos, sin saltos |
| Links optimizados | 3 pts | Anchor text descriptivo, interno/externo correctos |

##### 3. Cumplimiento de Longitudes (20 puntos)

| Sección | Puntos | Mínimo | Óptimo |
|---------|--------|--------|--------|
| Card descripción | 3 pts | 120 caracteres | 150 caracteres |
| Meta description | 3 pts | 150 caracteres | 155 caracteres |
| Hero tagline | 4 pts | 150 palabras | 170 palabras |
| Servicios (cada uno) | 3 pts | 60 palabras | 70 palabras |
| Por qué elegirnos | 4 pts | 100 palabras | 120 palabras |
| FAQ respuestas | 3 pts | 70 palabras | 85 palabras |

**Penalización**: -5 puntos por cada sección que no cumpla el mínimo.

##### 4. Especificidad de Información (15 puntos)

| Sub-criterio | Puntos | Verificación |
|--------------|--------|--------------|
| Sin frases genéricas prohibidas | 5 pts | Ausencia de "alta calidad", "servicio profesional", etc. |
| Datos medibles y concretos | 5 pts | Años de experiencia, número de proyectos, marcas específicas |
| Prueba de Especificidad aprobada | 5 pts | Cada afirmación NO aplica a competidores genéricos |

##### 5. Validez de Schema.org (10 puntos)

| Sub-criterio | Puntos | Verificación |
|--------------|--------|--------------|
| Sintaxis JSON-LD correcta | 3 pts | Sin errores de sintaxis |
| Campos obligatorios completos | 4 pts | Name, address, geo, telephone, rating, etc. |
| Validación Google Rich Results | 3 pts | Pasa test sin errores ni advertencias |

### 15.2 Niveles de Aprobación

Basado en la puntuación total:

| Nivel | Rango | Acción | Icono |
|-------|-------|--------|-------|
| **Excelente** | 90-100 pts | ✅ Publicar inmediatamente sin revisión adicional | ⭐⭐⭐⭐⭐ |
| **Muy Bueno** | 80-89 pts | ✅ Publicar con revisión rápida (5 min) | ⭐⭐⭐⭐ |
| **Bueno** | 70-79 pts | ⚠️ Revisar y mejorar secciones específicas antes de publicar | ⭐⭐⭐ |
| **Regular** | 60-69 pts | ⚠️ Requiere mejoras mayores. Reescribir secciones completas | ⭐⭐ |
| **Insuficiente** | 40-59 pts | ❌ No publicable. Regenerar desde cero | ⭐ |
| **Rechazado** | 0-39 pts | ❌ Contenido inaceptable. Revisar proceso completo | ⛔ |

### 15.3 Plantilla de Reporte de Calidad

```json
{
  "empresa": "NOMBRE_EMPRESA",
  "fecha_evaluacion": "2025-11-15",
  "evaluador": "Claude AI / Humano",
  "puntuacion_total": 92,
  "nivel": "Excelente",
  "desglose": {
    "unicidad": {
      "puntos": 28,
      "maximo": 30,
      "porcentaje_similitud": 8,
      "comentario": "Contenido altamente original. Solo 8% de similitud con contenido existente."
    },
    "seo": {
      "puntos": 24,
      "maximo": 25,
      "keyword_density": 1.8,
      "meta_completo": true,
      "comentario": "Excelente optimización SEO. Keyword density ideal."
    },
    "longitudes": {
      "puntos": 20,
      "maximo": 20,
      "cumplimiento": {
        "card_descripcion": true,
        "meta_description": true,
        "hero_tagline": true,
        "servicios": true,
        "por_que_elegirnos": true,
        "faqs": true
      },
      "comentario": "Todas las secciones cumplen longitudes mínimas."
    },
    "especificidad": {
      "puntos": 15,
      "maximo": 15,
      "frases_genericas": 0,
      "datos_medibles": 12,
      "comentario": "Alto nivel de especificidad. 12 datos concretos identificados."
    },
    "schema": {
      "puntos": 5,
      "maximo": 10,
      "sintaxis_valida": true,
      "campos_completos": true,
      "google_test": "WARNING",
      "comentario": "Schema válido pero con advertencias menores en Google Test."
    }
  },
  "recomendaciones": [
    "Corregir advertencias de Schema.org en Google Rich Results Test",
    "Considerar agregar más keywords secundarias en sección de servicios"
  ],
  "accion": "Publicar con revisión rápida de Schema.org"
}
```

### 13.4 Cálculo Automático de Puntuación

Para implementar en scripts de validación:

```javascript
function calcularPuntuacionCalidad(contenido) {
  let puntuacion = 0;

  // 1. Unicidad (30 pts)
  const similitud = calcularSimilitud(contenido, baseDatos);
  if (similitud < 0.1) puntuacion += 30;
  else if (similitud < 0.2) puntuacion += 25;
  else if (similitud < 0.3) puntuacion += 20;
  else if (similitud < 0.5) puntuacion += 10;

  // 2. SEO (25 pts)
  const seo = evaluarSEO(contenido);
  puntuacion += seo.keyword_ubicaciones * 1.6; // 8 pts max
  puntuacion += seo.keyword_density_ok ? 5 : 0;
  puntuacion += seo.meta_completo ? 5 : 0;
  puntuacion += seo.headers_ok ? 4 : 0;
  puntuacion += seo.links_ok ? 3 : 0;

  // 3. Longitudes (20 pts)
  const longitudes = verificarLongitudes(contenido);
  puntuacion += longitudes.card_desc ? 3 : 0;
  puntuacion += longitudes.meta_desc ? 3 : 0;
  puntuacion += longitudes.hero ? 4 : 0;
  puntuacion += longitudes.servicios ? 3 : 0;
  puntuacion += longitudes.por_que ? 4 : 0;
  puntuacion += longitudes.faqs ? 3 : 0;

  // 4. Especificidad (15 pts)
  const frases_genericas = contarFrasesGenericas(contenido);
  puntuacion += frases_genericas === 0 ? 5 : 0;
  const datos_medibles = contarDatosMedibles(contenido);
  puntuacion += datos_medibles >= 8 ? 5 : Math.floor(datos_medibles * 0.625);
  const prueba_especificidad = pruebaEspecificidad(contenido);
  puntuacion += prueba_especificidad ? 5 : 0;

  // 5. Schema.org (10 pts)
  const schema = validarSchema(contenido.schema);
  puntuacion += schema.sintaxis_ok ? 3 : 0;
  puntuacion += schema.campos_completos ? 4 : 0;
  puntuacion += schema.google_test === 'PASS' ? 3 : (schema.google_test === 'WARNING' ? 1.5 : 0);

  return {
    puntuacion_total: Math.round(puntuacion),
    nivel: obtenerNivel(puntuacion),
    desglose: {
      unicidad: 30 - (similitud * 100 > 30 ? 30 : similitud * 100),
      seo: seo.puntos_totales,
      longitudes: longitudes.puntos_totales,
      especificidad: 15 - (frases_genericas * 2),
      schema: schema.puntos_totales
    }
  };
}

function obtenerNivel(puntuacion) {
  if (puntuacion >= 90) return 'Excelente';
  if (puntuacion >= 80) return 'Muy Bueno';
  if (puntuacion >= 70) return 'Bueno';
  if (puntuacion >= 60) return 'Regular';
  if (puntuacion >= 40) return 'Insuficiente';
  return 'Rechazado';
}
```

---

## 14. CONFIGURACIÓN CENTRALIZADA

### 15.1 Archivo de Configuración Principal

Crear archivo `.claude-config.json` en la raíz del proyecto:

```json
{
  "proyecto": "paginas-amarillas-mx",
  "version": "3.0",
  "ultima_actualizacion": "2025-11-15",

  "configuracion_regional": {
    "pais": "México",
    "idioma": "es-MX",
    "moneda": "MXN",
    "formato_telefono": "55 XXXX XXXX",
    "codigo_pais": "+52",
    "formato_fecha": "DD/MM/YYYY",
    "zona_horaria": "America/Mexico_City"
  },

  "limites_contenido": {
    "card": {
      "descripcion": {
        "min": 120,
        "max": 180,
        "unidad": "caracteres",
        "optimo": 150
      },
      "service_tags": {
        "min": 3,
        "max": 4,
        "longitud_max_tag": 20
      },
      "badges": {
        "min": 1,
        "max": 3
      }
    },
    "resena": {
      "meta_title": {
        "max": 60,
        "unidad": "caracteres"
      },
      "meta_description": {
        "min": 150,
        "max": 160,
        "unidad": "caracteres"
      },
      "hero_tagline": {
        "min": 150,
        "max": 200,
        "unidad": "palabras",
        "optimo": 170
      },
      "intro_servicios": {
        "min": 60,
        "max": 120,
        "unidad": "palabras",
        "optimo": 80
      },
      "descripcion_servicio": {
        "min": 60,
        "max": 80,
        "unidad": "palabras",
        "optimo": 70
      },
      "por_que_elegirnos": {
        "min": 100,
        "max": 150,
        "unidad": "palabras",
        "optimo": 120
      },
      "respuesta_faq": {
        "min": 70,
        "max": 100,
        "unidad": "palabras",
        "optimo": 85
      }
    }
  },

  "configuracion_seo": {
    "keyword_density": {
      "min": 1.0,
      "max": 2.0,
      "optimo": 1.5
    },
    "keywords_secundarias": {
      "min": 3,
      "max": 5
    },
    "meta_keywords": {
      "min": 8,
      "max": 12
    }
  },

  "configuracion_imagenes": {
    "card": {
      "width": 280,
      "height": 280,
      "formato_preferido": "webp",
      "formatos_aceptados": ["webp", "jpg", "png"],
      "peso_maximo_kb": 80,
      "loading": "lazy"
    }
  },

  "calidad": {
    "puntuacion_minima_publicacion": 75,
    "umbral_unicidad": 0.7,
    "umbral_keyword_naturalidad": 0.8
  },

  "frases_prohibidas": [
    "alta calidad",
    "servicio profesional",
    "los mejores del mercado",
    "atención personalizada",
    "excelente servicio",
    "satisfacción garantizada",
    "calidad premium",
    "servicio de primera",
    "mejor opción del mercado"
  ],

  "elementos_requeridos": {
    "card": [
      "name",
      "slug",
      "category",
      "image",
      "badges",
      "rating",
      "services_tags",
      "short_description",
      "location",
      "phone",
      "schedule",
      "actions"
    ],
    "resena": [
      "meta_title",
      "meta_description",
      "meta_keywords",
      "canonical",
      "og_tags",
      "twitter_card",
      "schema_org_localbusiness",
      "schema_org_breadcrumb",
      "hero_section",
      "services_section",
      "why_choose_section",
      "contact_info"
    ]
  },

  "categorias_disponibles": [
    "entretenimiento",
    "construccion",
    "salud",
    "servicios",
    "tecnologia",
    "educacion",
    "transporte",
    "hoteleria",
    "restaurantes"
  ],

  "tipos_badges": {
    "verified": {
      "text": "✓ Verificado",
      "clase": "badge-verified"
    },
    "premium": {
      "text": "Premium",
      "clase": "badge-premium"
    },
    "experience": {
      "text": "{X}+ Años",
      "clase": "badge-experience"
    },
    "certified": {
      "text": "Certificado",
      "clase": "badge-certified"
    }
  },

  "rango_ratings": {
    "min": 1.0,
    "max": 5.0,
    "tipico_min": 4.0,
    "tipico_max": 5.0,
    "optimo": 4.8
  },

  "rango_contadores_resenas": {
    "min": 50,
    "max": 500,
    "optimo": 200
  },

  "estructura_urls": {
    "card_profile": "../negocios/{categoria}/{slug}.html",
    "categoria_page": "../categoria/{categoria}.html",
    "imagen_path": "../img/img-{categoria}/{slug}.webp"
  },

  "contacto": {
    "formato_telefono_link": "tel:+52{numero}",
    "formato_whatsapp_link": "https://wa.me/521{numero}?text={mensaje_encoded}"
  },

  "validadores_externos": {
    "schema_org": "https://search.google.com/test/rich-results",
    "meta_tags": "https://metatags.io/",
    "plagio": "https://www.copyscape.com",
    "legibilidad": "https://hemingwayapp.com/",
    "velocidad": "https://pagespeed.web.dev/"
  }
}
```

### 15.2 Variables de Entorno (.env)

Crear archivo `.env` para datos sensibles:

```bash
# API Keys (si se usan servicios externos)
GOOGLE_MAPS_API_KEY=your_api_key_here
SCHEMA_VALIDATOR_API_KEY=your_api_key_here

# Configuración de Base de Datos (si aplica)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=paginas_amarillas
DB_USER=admin
DB_PASSWORD=secure_password

# Rutas de Proyecto
PROJECT_ROOT=/Users/carsolio/Desktop/PAGINAS-HTML/PAGINASAMARILLAS
CATEGORIA_PATH=categoria
NEGOCIOS_PATH=negocios
IMAGENES_PATH=img

# Configuración de Calidad
MIN_QUALITY_SCORE=75
ENABLE_AUTO_PUBLISH=false

# Configuración de Notificaciones
NOTIFY_ON_ERROR=true
ADMIN_EMAIL=admin@paginasamarillas.mx
```

### 15.3 Uso de la Configuración en Prompts

Al usar Claude, referenciar la configuración:

```
@config .claude-config.json

Genera card para {{empresa_nombre}} siguiendo la configuración centralizada:
- Longitudes según config.limites_contenido.card
- Frases prohibidas: config.frases_prohibidas
- Formato de teléfono: config.configuracion_regional.formato_telefono
- Puntuación mínima: config.calidad.puntuacion_minima_publicacion
```

---

## 15. AUTOMATIZACIÓN Y VALIDACIÓN

### 15.1 Script de Validación de Contenido

Crear archivo `scripts/validate-content.js`:

```javascript
/**
 * Script de Validación Automática de Cards y Reseñas
 * Versión: 3.0
 * Compatible con: Node.js 16+
 */

const fs = require('fs');
const path = require('path');
const config = require('../.claude-config.json');

class ContentValidator {
  constructor() {
    this.config = config;
    this.errors = [];
    this.warnings = [];
  }

  /**
   * Valida unicidad del contenido comparando con base de datos
   */
  validateUniqueness(text, database) {
    const similarity = this.calculateSimilarity(text, database);

    if (similarity > 0.5) {
      this.errors.push({
        type: 'UNICIDAD',
        severity: 'ERROR',
        message: `Contenido tiene ${(similarity * 100).toFixed(1)}% de similitud con contenido existente (límite: 30%)`
      });
      return false;
    } else if (similarity > 0.3) {
      this.warnings.push({
        type: 'UNICIDAD',
        severity: 'WARNING',
        message: `Contenido tiene ${(similarity * 100).toFixed(1)}% de similitud. Considerar reescribir.`
      });
      return true;
    }

    return true;
  }

  /**
   * Calcula similitud entre dos textos (algoritmo simplificado)
   */
  calculateSimilarity(text1, text2) {
    const words1 = text1.toLowerCase().split(/\s+/);
    const words2 = text2.toLowerCase().split(/\s+/);

    const commonWords = words1.filter(word => words2.includes(word));
    const similarity = commonWords.length / Math.max(words1.length, words2.length);

    return similarity;
  }

  /**
   * Valida longitudes de todas las secciones
   */
  validateLengths(content, type = 'card') {
    const limits = this.config.limites_contenido[type];
    const results = [];

    Object.keys(limits).forEach(section => {
      const limit = limits[section];
      const text = content[section];

      if (!text) {
        this.errors.push({
          type: 'LONGITUD',
          severity: 'ERROR',
          section: section,
          message: `Sección "${section}" faltante`
        });
        results.push({ section, valid: false, current: 0, expected: limit });
        return;
      }

      const length = limit.unidad === 'palabras'
        ? text.split(/\s+/).length
        : text.length;

      const valid = length >= limit.min && length <= limit.max;

      if (!valid) {
        this.errors.push({
          type: 'LONGITUD',
          severity: 'ERROR',
          section: section,
          message: `"${section}" tiene ${length} ${limit.unidad}, se requiere ${limit.min}-${limit.max}`
        });
      }

      results.push({
        section,
        valid,
        current: length,
        expected: `${limit.min}-${limit.max} ${limit.unidad}`
      });
    });

    return results;
  }

  /**
   * Valida optimización SEO
   */
  validateSEO(content) {
    const seo = {
      keyword_in_title: false,
      keyword_in_h1: false,
      keyword_in_first_100: false,
      keyword_density: 0,
      meta_complete: false,
      title_length_ok: false
    };

    // Keyword primaria
    const keyword = content.keyword_primaria?.toLowerCase();
    if (!keyword) {
      this.errors.push({
        type: 'SEO',
        severity: 'ERROR',
        message: 'Keyword primaria no definida'
      });
      return seo;
    }

    // Verificar ubicaciones de keyword
    seo.keyword_in_title = content.meta_title?.toLowerCase().includes(keyword);
    seo.keyword_in_h1 = content.h1?.toLowerCase().includes(keyword);

    const first100Words = content.body?.split(/\s+/).slice(0, 100).join(' ').toLowerCase();
    seo.keyword_in_first_100 = first100Words?.includes(keyword);

    // Densidad de keyword
    const totalWords = content.body?.split(/\s+/).length || 0;
    const keywordOccurrences = (content.body?.toLowerCase().match(new RegExp(keyword, 'g')) || []).length;
    seo.keyword_density = (keywordOccurrences / totalWords) * 100;

    if (seo.keyword_density < this.config.configuracion_seo.keyword_density.min ||
        seo.keyword_density > this.config.configuracion_seo.keyword_density.max) {
      this.warnings.push({
        type: 'SEO',
        severity: 'WARNING',
        message: `Densidad de keyword es ${seo.keyword_density.toFixed(2)}% (óptimo: ${this.config.configuracion_seo.keyword_density.optimo}%)`
      });
    }

    // Meta tags completos
    seo.meta_complete = !!(content.meta_title && content.meta_description && content.meta_keywords);
    seo.title_length_ok = content.meta_title?.length <= this.config.limites_contenido.resena.meta_title.max;

    return seo;
  }

  /**
   * Detecta frases genéricas prohibidas
   */
  detectForbiddenPhrases(text) {
    const found = [];
    this.config.frases_prohibidas.forEach(phrase => {
      if (text.toLowerCase().includes(phrase.toLowerCase())) {
        found.push(phrase);
        this.errors.push({
          type: 'CONTENIDO',
          severity: 'ERROR',
          message: `Frase prohibida detectada: "${phrase}"`
        });
      }
    });
    return found;
  }

  /**
   * Valida Schema.org
   */
  validateSchema(schema) {
    try {
      const parsed = typeof schema === 'string' ? JSON.parse(schema) : schema;

      // Verificar campos obligatorios
      const requiredFields = ['@context', '@type', 'name', 'address', 'telephone'];
      const missing = requiredFields.filter(field => !parsed[field]);

      if (missing.length > 0) {
        this.errors.push({
          type: 'SCHEMA',
          severity: 'ERROR',
          message: `Campos faltantes en Schema.org: ${missing.join(', ')}`
        });
        return { valid: false, missing };
      }

      // Verificar tipo correcto
      if (parsed['@type'] !== 'LocalBusiness') {
        this.warnings.push({
          type: 'SCHEMA',
          severity: 'WARNING',
          message: `Schema.org tipo "${parsed['@type']}" podría no ser óptimo para negocios locales`
        });
      }

      return { valid: true, missing: [] };
    } catch (error) {
      this.errors.push({
        type: 'SCHEMA',
        severity: 'ERROR',
        message: `Error al parsear Schema.org: ${error.message}`
      });
      return { valid: false, error: error.message };
    }
  }

  /**
   * Genera reporte completo de validación
   */
  generateReport() {
    const hasErrors = this.errors.length > 0;
    const hasWarnings = this.warnings.length > 0;

    return {
      status: hasErrors ? 'FAIL' : (hasWarnings ? 'PASS_WITH_WARNINGS' : 'PASS'),
      errors: this.errors,
      warnings: this.warnings,
      summary: {
        total_errors: this.errors.length,
        total_warnings: this.warnings.length,
        is_publishable: !hasErrors
      }
    };
  }
}

// Uso del validador
const validator = new ContentValidator();

// Ejemplo de validación
const contentToValidate = {
  card_description: "Especialistas en audio profesional desde hace 15 años...",
  meta_title: "Empresa - Servicio CDMX",
  meta_description: "➤ Descripción completa del servicio con teléfono ☎ 55 1234 5678",
  // ... resto del contenido
};

// Validar unicidad
// validator.validateUniqueness(contentToValidate.card_description, existingDatabase);

// Validar longitudes
// validator.validateLengths(contentToValidate, 'card');

// Validar SEO
// validator.validateSEO(contentToValidate);

// Detectar frases prohibidas
// validator.detectForbiddenPhrases(contentToValidate.card_description);

// Generar reporte
// const report = validator.generateReport();
// console.log(JSON.stringify(report, null, 2));

module.exports = ContentValidator;
```

### 15.2 Workflow Automatizado

Crear archivo `scripts/workflow-automation.js`:

```javascript
/**
 * Workflow Automatizado para Generación de Contenido
 */

const ContentValidator = require('./validate-content');
const fs = require('fs');
const path = require('path');

class ContentWorkflow {
  constructor(empresaData) {
    this.data = empresaData;
    this.validator = new ContentValidator();
    this.results = {};
  }

  /**
   * Paso 1: Recopilación de información
   */
  async step1_GatherInformation() {
    console.log('[PASO 1/5] Recopilando información...');

    // Aquí se implementaría scraping o lectura de fuentes
    // Por ahora, usar datos proporcionados

    this.results.info_gathered = {
      nombre: this.data.nombre,
      categoria: this.data.categoria,
      servicios: this.data.servicios || [],
      ubicacion: this.data.ubicacion,
      telefono: this.data.telefono
    };

    console.log('✅ Información recopilada');
    return this.results.info_gathered;
  }

  /**
   * Paso 2: Validación de datos
   */
  async step2_ValidateData() {
    console.log('[PASO 2/5] Validando datos...');

    const required = ['nombre', 'categoria', 'ubicacion', 'telefono'];
    const missing = required.filter(field => !this.results.info_gathered[field]);

    if (missing.length > 0) {
      throw new Error(`Datos faltantes: ${missing.join(', ')}`);
    }

    console.log('✅ Datos validados');
    return true;
  }

  /**
   * Paso 3: Generación de contenido (aquí se llamaría a Claude)
   */
  async step3_GenerateContent() {
    console.log('[PASO 3/5] Generando contenido...');

    // Aquí se haría la llamada a Claude API con el prompt estructurado
    // Por ahora, contenido de ejemplo

    this.results.generated_content = {
      card_html: '<!-- Card HTML generado -->',
      card_json: {},
      resena_html: '<!-- Reseña HTML generada -->',
      schema_org: {}
    };

    console.log('✅ Contenido generado');
    return this.results.generated_content;
  }

  /**
   * Paso 4: Validación automática
   */
  async step4_AutoValidation() {
    console.log('[PASO 4/5] Validando contenido generado...');

    // Ejecutar todas las validaciones
    this.validator.validateLengths(this.results.generated_content, 'card');
    this.validator.validateSEO(this.results.generated_content);
    this.validator.detectForbiddenPhrases(this.results.generated_content.card_html);
    this.validator.validateSchema(this.results.generated_content.schema_org);

    const report = this.validator.generateReport();
    this.results.validation_report = report;

    if (report.status === 'FAIL') {
      console.log('❌ Validación fallida');
      console.log(`Errores: ${report.summary.total_errors}`);
      throw new Error('Contenido no pasó validación');
    }

    console.log(`✅ Validación completada (${report.summary.total_warnings} warnings)`);
    return report;
  }

  /**
   * Paso 5: Guardar archivos
   */
  async step5_SaveFiles() {
    console.log('[PASO 5/5] Guardando archivos...');

    const categoria = this.results.info_gathered.categoria;
    const slug = this.generateSlug(this.results.info_gathered.nombre);

    // Guardar card HTML
    const cardPath = path.join('categoria', `${categoria}.html`);
    // fs.writeFileSync(cardPath, this.results.generated_content.card_html);

    // Guardar reseña HTML
    const resenaPath = path.join('negocios', categoria, `${slug}.html`);
    // fs.writeFileSync(resenaPath, this.results.generated_content.resena_html);

    console.log('✅ Archivos guardados');
    console.log(`Card: ${cardPath}`);
    console.log(`Reseña: ${resenaPath}`);

    return { cardPath, resenaPath };
  }

  /**
   * Generar slug a partir del nombre
   */
  generateSlug(nombre) {
    return nombre
      .toLowerCase()
      .replace(/\s+/g, '-')
      .replace(/[^\w-]/g, '');
  }

  /**
   * Ejecutar workflow completo
   */
  async run() {
    try {
      await this.step1_GatherInformation();
      await this.step2_ValidateData();
      await this.step3_GenerateContent();
      await this.step4_AutoValidation();
      await this.step5_SaveFiles();

      console.log('\n🎉 Workflow completado exitosamente');
      return this.results;
    } catch (error) {
      console.error('\n❌ Error en workflow:', error.message);
      throw error;
    }
  }
}

// Ejemplo de uso
const empresaData = {
  nombre: 'EMPRESA EJEMPLO',
  categoria: 'entretenimiento',
  servicios: ['Audio profesional', 'Iluminación LED', 'Video mapping'],
  ubicacion: 'Polanco, Miguel Hidalgo, CDMX',
  telefono: '55 1234 5678'
};

// const workflow = new ContentWorkflow(empresaData);
// workflow.run();

module.exports = ContentWorkflow;
```

### 15.3 Comandos de Terminal Útiles

Crear archivo `scripts/cli-commands.sh`:

```bash
#!/bin/bash

# Script de comandos CLI para Páginas Amarillas México
# Versión: 3.0

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función: Validar card
validate_card() {
  echo -e "${GREEN}[VALIDAR CARD]${NC}"
  node scripts/validate-content.js --type=card --file="$1"
}

# Función: Validar reseña
validate_resena() {
  echo -e "${GREEN}[VALIDAR RESEÑA]${NC}"
  node scripts/validate-content.js --type=resena --file="$1"
}

# Función: Generar nuevo contenido
generate_content() {
  echo -e "${GREEN}[GENERAR CONTENIDO]${NC}"
  echo "Empresa: $1"
  echo "Categoría: $2"
  node scripts/workflow-automation.js --empresa="$1" --categoria="$2"
}

# Función: Verificar calidad
check_quality() {
  echo -e "${GREEN}[VERIFICAR CALIDAD]${NC}"
  node scripts/quality-check.js --file="$1"
}

# Función: Actualizar contador
update_counter() {
  echo -e "${GREEN}[ACTUALIZAR CONTADOR]${NC}"
  CATEGORIA="$1"
  COUNT=$(grep -o '<article class="business-card">' "categoria/${CATEGORIA}.html" | wc -l)
  echo "Empresas en ${CATEGORIA}: ${COUNT}"
}

# Función: Backup
backup_files() {
  echo -e "${GREEN}[CREAR BACKUP]${NC}"
  TIMESTAMP=$(date +%Y%m%d_%H%M%S)
  mkdir -p backups
  tar -czf "backups/backup_${TIMESTAMP}.tar.gz" categoria/ negocios/
  echo -e "${GREEN}✓${NC} Backup creado: backups/backup_${TIMESTAMP}.tar.gz"
}

# Procesar argumentos
case "$1" in
  validate-card)
    validate_card "$2"
    ;;
  validate-resena)
    validate_resena "$2"
    ;;
  generate)
    generate_content "$2" "$3"
    ;;
  quality)
    check_quality "$2"
    ;;
  count)
    update_counter "$2"
    ;;
  backup)
    backup_files
    ;;
  *)
    echo "Uso: $0 {validate-card|validate-resena|generate|quality|count|backup} [args]"
    exit 1
esac
```

---

## 16. TROUBLESHOOTING Y SOLUCIÓN DE ERRORES

### 16.1 Problema: Caracteres Corruptos (�)

**Síntomas**:
- Aparecen símbolos � en lugar de á, é, í, ó, ú, ñ
- Meta tags muestran caracteres extraños

**Causa**: Encoding incorrecto (binary en lugar de UTF-8)

**Solución**:
```bash
# 1. Borrar archivo corrupto
rm empresa-problema.html

# 2. Copiar redeil.html nuevamente
cp redeil.html empresa-problema.html

# 3. Editar con cambios de texto solamente
# 4. Verificar encoding
file -I empresa-problema.html  # Debe mostrar charset=utf-8
```

### 16.2 Problema: CSS No Se Aplica / Página Sin Estilos

**Síntomas**:
- La página se ve sin diseño
- Solo texto plano visible
- Colores y layouts no funcionan

**Causas Posibles**:

1. **Clases CSS incorrectas**
```bash
# Verificar clases incorrectas
grep -E "services-section|why-choose-us|section-text|faq-section" empresa.html

# Si encuentra resultados = PROBLEMA
# Solución: Reemplazar con clases correctas
```

2. **Estructura HTML diferente**
- Comparar con redeil.html línea por línea
- Regenerar copiando redeil.html

3. **Rutas de CSS incorrectas**
```html
<!-- Verificar que existan estas líneas -->
<link rel="stylesheet" href="../../css/style.css">
<link rel="stylesheet" href="../../css/perfil.css">
```

### 16.3 Problema: Secciones Con Contenido de Otra Empresa

**Síntomas**:
- FAQs hablan de servicios diferentes
- Reviews mencionan otra empresa
- Services Directory muestra productos incorrectos

**Causa**: Actualización incompleta de secciones

**Solución**:
1. Usar checklist de 21 secciones
2. Buscar nombre de empresa anterior:
```bash
grep -i "REDEIL\|nombre-anterior" empresa.html
```
3. Actualizar cada sección manualmente

### 16.4 Problema: JavaScript No Funciona

**Síntomas**:
- Menú móvil no abre
- Galería de imágenes no funciona
- Animaciones no se ejecutan

**Causa**: JavaScript no vinculado o ruta incorrecta

**Solución**:
```bash
# Verificar al final del archivo
tail -10 empresa.html | grep "script"

# Debe mostrar:
# <script src="../../js/app.js"></script>
# <script src="../../js/perfil.js"></script>
```

### 16.5 Tabla de Diagnóstico Rápido

| Síntoma | Diagnóstico | Comando de Verificación | Solución |
|---------|-------------|-------------------------|-----------|
| Caracteres � | Encoding corrupto | `file -I archivo.html` | Copiar redeil.html de nuevo |
| Sin estilos CSS | Clases incorrectas | `grep "business-section" archivo.html` | Corregir clases CSS |
| Contenido mezclado | Secciones no actualizadas | `grep "REDEIL" archivo.html` | Actualizar secciones faltantes |
| JS no funciona | Scripts no vinculados | `tail -10 archivo.html` | Agregar scripts al final |
| Estructura rota | HTML diferente | Comparar con redeil.html | Regenerar desde redeil.html |

---

**FIN DEL DOCUMENTO MAESTRO v5.0**
