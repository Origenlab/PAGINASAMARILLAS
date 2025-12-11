# Documentación: Sistema de Perfiles de Negocio
## PaginasAmarillas.mx - Arquitectura Completa

---

## 📋 Resumen Ejecutivo

Se ha implementado un **sistema completo de perfiles de negocio** minimalista, profesional y optimizado para SEO. El primer perfil creado es **Origins Private Security**, que sirve como template para futuras empresas.

---

## 🏗️ Arquitectura del Sistema

### Flujo de Usuario

```
Index (Categorías)
    ↓
Categoría Seguridad Privada (Listado)
    ↓
Tarjeta de Empresa (Origins Private Security)
    ↓
Perfil Completo (/negocio/origins-private-security.html)
```

### Estructura de Archivos

```
/PAGINASAMARILLAS/
├── index.html                          # Homepage
├── categoria/
│   └── seguridad-privada.html          # Listado de categoría
├── negocio/
│   └── origins-private-security.html   # ✨ PERFIL COMPLETO
├── css/
│   ├── style.css                       # Estilos base (compartidos)
│   ├── categoria.css                   # Estilos de categoría
│   └── perfil.css                      # ✨ ESTILOS DE PERFIL
├── js/
│   ├── app.js                          # JS base (compartido)
│   ├── categoria.js                    # JS de categoría
│   └── perfil.js                       # ✨ JS DE PERFIL
└── docs/
    ├── ORIGINS-SECURITY-ESTUDIO.md     # Estudio completo de la empresa
    └── PERFIL-NEGOCIO-DOCS.md          # Este documento
```

---

## 📄 Componentes del Perfil

### 1. **Hero Section** (Sección Principal)

**Elementos:**
- Imagen principal con galería de 4 thumbnails
- Badges: ✓ Verificado | SSC CDMX | 15+ Años
- Título H1: "Origins Private Security"
- Rating: 4.8 estrellas (47 reseñas) con link a reviews
- Tagline descriptivo
- 4 Quick Info Cards:
  - Ubicación
  - Horario 24/7
  - Especialización
  - Certificaciones
- 3 CTAs principales:
  - Llamar ahora (teléfono clickeable)
  - WhatsApp (con mensaje pre-configurado)
  - Sitio Web (link a página web de la empresa)

**Características técnicas:**
- Grid responsivo 1.2fr / 1fr (desktop)
- Galería interactiva con JavaScript
- Transición suave de imágenes (200ms fade)

### 2. **Services Section** (Servicios)

**Grid de 8 servicios:**
1. Guardias Intramuros
2. Guardias Armados
3. Escoltas Ejecutivos
4. CCTV y Videovigilancia
5. Control de Acceso
6. Sistemas de Alarmas
7. Rastreo GPS / VEA
8. Capacitación Corporativa

**Cada servicio incluye:**
- Icono SVG temático en fondo amarillo claro
- Título H3
- Descripción de 2-3 líneas
- 3 bullets de características con checkmarks

**Layout:**
- Grid auto-fill minmax(300px, 1fr)
- Hover effect: translateY(-4px) + shadow-lg
- Responsive: 2 columnas (tablet) → 1 columna (mobile)

### 3. **About Section** (Sobre Nosotros)

**Contenido:**
- Historia de la empresa (15+ años)
- Propuesta de valor
- **IMPORTANTE:** El primer párrafo debe incluir un enlace con palabra clave SEO relevante apuntando al sitio web de la empresa
- 6 razones para elegir Origins:
  - 15+ años de experiencia
  - Personal certificado CNSP
  - Evaluación de riesgos gratis
  - Respuesta 24/7 <30 minutos
  - Tecnología integrada
  - Transparencia total

**Stats Cards (4):**
- 15+ Años de Experiencia
- 200+ Clientes Activos
- 500+ Elementos Certificados
- 24/7 Disponibilidad

**Layout:**
- Grid 1.5fr / 1fr (contenido / stats)
- Stats en grid 2x2
- Fondo gris claro

### 4. **Coverage Section** (Cobertura)

**Dos columnas:**

**Sectores Atendidos:**
- Industria (Manufactura, Farmacéutica, Automotriz)
- Corporativos (Edificios AAA, Multinacionales)
- Comercial (Centros comerciales, Retail)
- Residencial Premium (Torres, Condominios)
- Eventos (Corporativos, Conciertos, Exposiciones)
- Instituciones Financieras

**Área de Cobertura:**
- Ciudad de México (todas las alcaldías)
- Estado de México (Zona Metropolitana)
- Municipios específicos: Naucalpan, Tlalnepantla, Ecatepec
- Disponibilidad nacional para eventos

### 5. **Contact Section** (Contacto)

**Grid 1fr / 1fr:**

**Información de Contacto (6 tarjetas):**
1. **Dirección:** Basiliso Romo Anguiano No. 22 Int. 3, Col. Industrial
2. **Teléfonos:** 4 números (todos clickeables)
3. **Email:** 2 direcciones (josecruz@ y comercial@)
4. **WhatsApp:** 55 3025 5580 con link directo
5. **Sitio Web:** seguridad-privada.com.mx y originsecurity.mx
6. **Horario:** Emergencias 24/7 | Oficinas Lun-Vie 9-18h

**Formulario de Contacto:**
- Título: "Solicita una Cotización"
- Subtítulo: "Evaluación de riesgos gratis | Respuesta en 24 horas"
- Campos:
  - Nombre completo *
  - Email * | Teléfono * (row)
  - Empresa
  - Servicio de interés * (select con 9 opciones)
  - Mensaje * (textarea)
- Botón submit: "Enviar solicitud"
- Disclaimer de privacidad
- Validación y formateo automático (teléfono)
- Mensaje de éxito/error animado

### 6. **Reviews Section** (Reseñas)

**Resumen de Calificación:**
- Score grande: 4.8
- Estrellas doradas
- "Basado en 47 reseñas"

**Grid de 3 reseñas destacadas:**
1. Jorge Martínez ★★★★★ - Instalaciones industriales, 3 años
2. Ana Rodríguez ★★★★★ - Escoltas CEO, impecable
3. Carlos Flores ★★★★☆ - CCTV rápido, buen servicio

**Cada reseña incluye:**
- Avatar con iniciales
- Nombre del autor
- Fecha relativa
- Estrellas
- Texto de reseña

**CTA:** "Ver todas las reseñas (47)"

### 7. **Final CTA** (Llamada a la Acción Final)

**Fondo amarillo corporativo:**
- Título H2: "¿Listo para proteger tu empresa?"
- Subtítulo: "Solicita evaluación gratis + cotización en 24h"
- 2 botones grandes:
  - Llamar ahora: 55 3025 5580
  - Cotizar por WhatsApp

---

## 🎨 Diseño y Estilos

### Paleta de Colores

**Primarios:**
- Amarillo: `#F4B942` (principal)
- Amarillo oscuro: `#E6A82E` (hover)
- Amarillo claro: `#FFF8E7` (fondos)

**Secundarios:**
- Azul oscuro: `#1A2332` (textos importantes)
- Azul secundario: `#2C3E50`

**Badges:**
- Verde experiencia: `#10B981` (15+ Años)
- Mensajes éxito: `#D1FAE5` / `#10B981`
- Mensajes error: `#FEE2E2` / `#EF4444`

**Neutros:**
- Grises: del 50 al 900 (scale completa)

### Tipografía

**Font:** Inter (Google Fonts)
- Regular: 400
- Medium: 500
- Semibold: 600
- Bold: 700

**Tamaños:**
- H1: 48px (4xl) → 36px mobile
- H2: 36px (3xl) → 30px mobile
- H3: 24px (2xl)
- Body: 16px (base)
- Small: 14px (sm)
- XSmall: 12px (xs)

### Espaciado

Sistema de spacing consistente:
- XS: 4px
- SM: 8px
- MD: 16px
- LG: 24px
- XL: 32px
- 2XL: 48px
- 3XL: 64px

### Efectos

**Sombras:**
- SM: `0 1px 2px rgba(0,0,0,0.05)`
- MD: `0 4px 6px rgba(0,0,0,0.1)`
- LG: `0 10px 15px rgba(0,0,0,0.1)`
- XL: `0 20px 25px rgba(0,0,0,0.1)`

**Transiciones:**
- Base: 200ms
- Slow: 300ms
- Ease: ease-in-out

**Borders:**
- Radius SM: 4px
- Radius MD: 8px
- Radius LG: 12px

---

## 💻 Funcionalidad JavaScript

### 1. Galería de Imágenes

```javascript
// Click en thumbnail cambia imagen principal
galleryThumbs.forEach(thumb => {
  thumb.addEventListener('click', function() {
    // Remove active de todos
    // Add active al clickeado
    // Fade out → cambio src → fade in (200ms)
  });
});
```

**Features:**
- Transición suave con opacity
- Active state en thumbnail seleccionado
- Cambio de src y alt dinámico

### 2. Scroll a Formulario

```javascript
// Botón "Enviar mensaje" hace scroll al form
btnContactForm.addEventListener('click', function() {
  contactFormWrapper.scrollIntoView({ behavior: 'smooth' });
  setTimeout(() => firstInput.focus(), 500);
});
```

### 3. Validación de Formulario

```javascript
contactForm.addEventListener('submit', function(e) {
  e.preventDefault();
  // Recolectar datos
  // Validar campos
  // Enviar (placeholder para backend)
  // Mostrar mensaje éxito/error
  // Reset form
});
```

**Features:**
- Formateo automático de teléfono: `XX XXXX XXXX`
- Validación email con regex
- Validación teléfono 10 dígitos
- Mensajes animados de éxito/error
- Auto-remove mensajes después de 5s

### 4. Analytics Tracking

```javascript
// Track phone clicks
phoneLinks.forEach(link => {
  link.addEventListener('click', () => {
    console.log('Phone click tracked');
    // gtag('event', 'phone_call_clicked');
  });
});

// Track WhatsApp clicks
// Track Email clicks
```

**Preparado para:**
- Google Analytics 4
- Facebook Pixel
- Conversion tracking

---

## 📱 Responsive Design

### Breakpoints

**Desktop (≥1024px):**
- Hero: Grid 1fr / 1.2fr
- Services: Auto-fill minmax(300px, 1fr)
- About: Grid 1.5fr / 1fr
- Contact: Grid 1fr / 1fr
- Stats: Grid 2x2

**Tablet (768px - 1023px):**
- Hero: Single column
- Services: 2 columnas
- About: Single column → Stats 4x1
- Contact: Single column

**Mobile (<768px):**
- Todo a single column
- Quick Info Cards: 1 columna
- Services: 1 columna
- Stats: 2x2
- Form rows: 1 columna
- Gallery thumbs: 2x2
- Buttons: Stack vertical

---

## 🔍 SEO Optimización

### Meta Tags Implementados

```html
<title>Origins Private Security - Seguridad Privada Certificada CDMX | 15+ Años</title>
<meta name="description" content="Empresa líder en seguridad privada en CDMX con 15+ años. Guardias certificados CNSP, escoltas ejecutivos, CCTV, alarmas. Evaluación de riesgos gratis. ☎ 55 3025 5580">
<meta name="keywords" content="seguridad privada cdmx, guardias certificados, escoltas vip, origins security, seguridad industrial, cctv profesional, col industrial">
```

### Open Graph

```html
<meta property="og:title" content="Origins Private Security - Seguridad Privada CDMX">
<meta property="og:description" content="15+ años protegiendo empresas e industrias. Personal certificado CNSP, evaluación de riesgos gratis.">
<meta property="og:type" content="business.business">
<meta property="og:url" content="https://paginasamarillas.mx/negocio/origins-private-security">
```

### Estructura de Headings

```
H1: Origins Private Security (único, título principal)
H2:
  - Servicios Profesionales
  - Sobre Origins Private Security
  - Cobertura y Sectores
  - Información de Contacto
  - Reseñas de Clientes
  - ¿Listo para proteger tu empresa?

H3:
  - 8 Títulos de servicios
  - ¿Por qué elegirnos?
  - Sectores que Atendemos
  - Área de Cobertura
  - Solicita una Cotización
  - Principales ciudades (si se agrega)
```

### Keywords Density

**Objetivo:** 1-2% density para keywords principales

**Keywords principales en contenido:**
- "seguridad privada" → 12 menciones
- "CDMX" / "Ciudad de México" → 8 menciones
- "certificado CNSP" → 6 menciones
- "guardias" → 10 menciones
- "escoltas ejecutivos" → 4 menciones
- "15 años" / "15+ años" → 5 menciones

### Schema.org Markup (Pendiente)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Origins Private Security",
  "image": "https://paginasamarillas.mx/assets/origins-logo.jpg",
  "@id": "https://paginasamarillas.mx/negocio/origins-private-security",
  "url": "https://seguridad-privada.com.mx",
  "telephone": "+525530255580",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Basiliso Romo Anguiano No. 22 Int. 3",
    "addressLocality": "Ciudad de México",
    "addressRegion": "CDMX",
    "postalCode": "07800",
    "addressCountry": "MX"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 19.4721,
    "longitude": -99.1159
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "09:00",
    "closes": "18:00"
  }],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "47"
  },
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Servicios de Seguridad",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Guardias de Seguridad Certificados",
          "description": "Personal de vigilancia permanente certificado CNSP"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Escoltas Ejecutivos VIP",
          "description": "Protección personalizada para directivos"
        }
      }
    ]
  }
}
```

---

## 🚀 Performance

### Optimizaciones Implementadas

1. **CSS:**
   - Variables CSS para consistencia
   - Clases reutilizables
   - Mobile-first approach
   - Media queries optimizadas

2. **JavaScript:**
   - DOMContentLoaded para evitar FOUC
   - Event delegation donde aplica
   - Lazy loading preparado (IntersectionObserver)
   - Debouncing en inputs

3. **Imágenes:**
   - Placeholders via placeholder.com (reemplazar con reales)
   - Aspect ratio CSS para evitar layout shift
   - Lazy loading preparado con data-src

4. **Fonts:**
   - Preconnect a Google Fonts
   - Font-display: swap

### Métricas Objetivo

**Core Web Vitals:**
- LCP (Largest Contentful Paint): <2.5s
- FID (First Input Delay): <100ms
- CLS (Cumulative Layout Shift): <0.1

**Lighthouse Score Objetivo:**
- Performance: >90
- Accessibility: >95
- Best Practices: >95
- SEO: >95

---

## 📋 Checklist de Implementación

### Para cada nueva empresa:

- [ ] **Investigación:**
  - [ ] Estudio completo (como ORIGINS-SECURITY-ESTUDIO.md)
  - [ ] Recopilación de información (servicios, contacto, historia)
  - [ ] Análisis SEO (keywords, competencia)

- [ ] **Tarjeta en Listado:**
  - [ ] Agregar tarjeta en categoria/[categoria].html
  - [ ] Badges correctos (Verificado, Certificaciones, Años)
  - [ ] Descripción optimizada (150 caracteres)
  - [ ] Tags de servicios relevantes
  - [ ] Links correctos (tel, whatsapp, perfil)

- [ ] **Perfil Completo:**
  - [ ] Copiar template origins-private-security.html
  - [ ] Renombrar a [slug-empresa].html
  - [ ] Actualizar meta tags (title, description, keywords, OG)
  - [ ] Cambiar contenido del Hero (título, tagline, rating)
  - [ ] Actualizar 8 servicios (iconos, títulos, descripciones)
  - [ ] Sección Sobre Nosotros (historia, ventajas, stats)
  - [ ] Cobertura y sectores específicos
  - [ ] Información de contacto (todos los datos)
  - [ ] Formulario con opciones de servicio correctas
  - [ ] 3-5 reseñas reales o placeholder
  - [ ] Imágenes reales (logo, oficina, servicios, equipo)

- [ ] **Testing:**
  - [ ] Responsive en mobile, tablet, desktop
  - [ ] Todos los links funcionan
  - [ ] Formulario valida correctamente
  - [ ] Galería cambia imágenes
  - [ ] Scroll suave a secciones
  - [ ] Analytics tracking funcionando
  - [ ] Validación HTML (W3C)
  - [ ] Lighthouse audit >90

- [ ] **SEO:**
  - [ ] URLs limpias y descriptivas
  - [ ] Sitemap actualizado
  - [ ] Schema.org markup agregado
  - [ ] Canonical URL configurado
  - [ ] Alt text en todas las imágenes
  - [ ] Meta robots: index, follow

---

## 🎯 Roadmap Futuro

### Fase 1 (Corto Plazo - 1 mes)
- [ ] Agregar 10+ empresas más al directorio
- [ ] Implementar backend para formularios
- [ ] Sistema de reseñas funcional
- [ ] Integración con Google Maps
- [ ] Sistema de favoritos/guardados

### Fase 2 (Mediano Plazo - 3 meses)
- [ ] Panel de administración para empresas
- [ ] Edición de perfil por empresa
- [ ] Sistema de mensajería interna
- [ ] Calendario de citas/reservaciones
- [ ] Analytics dashboard para empresas

### Fase 3 (Largo Plazo - 6 meses)
- [ ] App móvil (iOS/Android)
- [ ] Sistema de verificación automática
- [ ] Inteligencia artificial para recomendaciones
- [ ] Programa de afiliados
- [ ] API pública para integraciones

---

## 📊 Métricas de Éxito

### Para el Negocio (Origins Security)

**Leads:**
- Clicks en teléfono: >50/mes
- Mensajes WhatsApp: >30/mes
- Formularios enviados: >20/mes
- Conversión leads→clientes: >15%

**Engagement:**
- Tiempo en página: >3 minutos
- Scroll depth: >75%
- Tasa de rebote: <40%
- Páginas por sesión: >2

**SEO:**
- Posición "seguridad privada cdmx": Top 10
- Posición "guardias certificados cdmx": Top 5
- Tráfico orgánico mensual: >500 visitas
- CTR en SERPs: >5%

### Para la Plataforma

**Crecimiento:**
- Nuevas empresas registradas: >10/mes
- Categorías activas: >15
- Total de perfiles: >100 en 6 meses

**Monetización:**
- Upgrades a plan premium: >20%
- Ingresos mensuales: >$50K MXN
- Retención de clientes: >80%

---

## 🔧 Mantenimiento

### Tareas Semanales
- [ ] Revisar formularios enviados
- [ ] Responder consultas de empresas
- [ ] Actualizar métricas de analytics
- [ ] Revisar errores en logs

### Tareas Mensuales
- [ ] Auditoría SEO completa
- [ ] Actualizar contenido de perfiles
- [ ] Revisar velocidad del sitio
- [ ] Backup de base de datos
- [ ] Análisis de competencia

### Tareas Trimestrales
- [ ] Renovar certificados SSL
- [ ] Actualizar dependencias
- [ ] Pruebas de penetración
- [ ] Encuesta de satisfacción a empresas
- [ ] Review de roadmap

---

## 📚 Recursos

### Documentación Relacionada
- [ORIGINS-SECURITY-ESTUDIO.md](ORIGINS-SECURITY-ESTUDIO.md) - Estudio completo de la empresa
- [CATEGORIA-SEGURIDAD-PRIVADA.md](CATEGORIA-SEGURIDAD-PRIVADA.md) - Docs de categoría
- [ACTUALIZACION-FAQ.md](ACTUALIZACION-FAQ.md) - Módulo FAQ
- [PALETA-COLORES.md](PALETA-COLORES.md) - Guía de colores
- [README-DESARROLLO.md](README-DESARROLLO.md) - Docs generales

### Referencias Externas
- [Schema.org LocalBusiness](https://schema.org/LocalBusiness)
- [Google Search Console](https://search.google.com/search-console)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Web.dev Best Practices](https://web.dev/learn/)

---

**Última actualización:** Noviembre 2025
**Versión:** 1.0
**Estado:** Sistema completo operativo
**Primer perfil:** Origins Private Security ✅
