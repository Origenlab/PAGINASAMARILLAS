# Paleta de Colores - PAGINASAMARILLAS.MX
## Colores Sólidos (Sin Gradientes)

---

## 🎨 Colores Primarios

### Amarillo Profesional

```css
--color-primary: #F4B942
```
**Uso:** Botones principales, badges, elementos destacados
**RGB:** 244, 185, 66
**Contraste con negro:** Excelente ✅

```css
--color-primary-dark: #E6A82E
```
**Uso:** Hover states, elementos activos
**RGB:** 230, 168, 46

```css
--color-primary-light: #FFF8E7
```
**Uso:** Fondos sutiles, highlights
**RGB:** 255, 248, 231

---

## 🔵 Colores Secundarios

### Azul Oscuro

```css
--color-secondary: #1A2332
```
**Uso:** Botón de búsqueda, headers, elementos de contraste
**RGB:** 26, 35, 50
**Contraste con blanco:** Excelente ✅

```css
--color-secondary-light: #2C3E50
```
**Uso:** Hover states de secundarios
**RGB:** 44, 62, 80

---

## ⚪ Neutros (Escala de Grises)

```css
--color-white: #FFFFFF      /* Fondos principales */
--color-gray-50: #F9FAFB    /* Fondos alternativos */
--color-gray-100: #F3F4F6   /* Hover states sutiles */
--color-gray-200: #E5E7EB   /* Bordes */
--color-gray-300: #D1D5DB   /* Bordes hover */
--color-gray-400: #9CA3AF   /* Placeholders, iconos */
--color-gray-500: #6B7280   /* Texto secundario */
--color-gray-600: #4B5563   /* Texto normal */
--color-gray-700: #374151   /* Texto importante */
--color-gray-800: #1F2937   /* Texto muy importante */
--color-gray-900: #111827   /* Headings, texto principal */
--color-black: #000000      /* Raramente usado */
```

---

## 📋 Guía de Uso

### ✅ Botones

**Primarios (CTAs principales)**
```css
background: #F4B942 (amarillo)
color: #111827 (texto oscuro)
hover: #E6A82E
```

**Secundarios (Búsqueda)**
```css
background: #1A2332 (azul oscuro)
color: #FFFFFF (texto blanco)
hover: #2C3E50
```

**Ghost (Sutiles)**
```css
background: transparent
color: #374151
hover: background #F3F4F6
```

**Outline (Bordes)**
```css
background: transparent
border: #D1D5DB
color: #374151
```

---

### 🎯 Secciones

**Hero Section**
```css
background: #F9FAFB (gris muy claro)
```

**Categorías**
```css
background: #FFFFFF (blanco)
cards: borde #E5E7EB
cards-hover: borde #F4B942
```

**Cómo Funciona**
```css
background: #F9FAFB (gris muy claro)
números: #F4B942 (amarillo)
```

**CTA Empresas**
```css
background: #F4B942 (amarillo sólido)
texto: #111827 (oscuro para contraste)
```

**Footer**
```css
background: #111827 (gris muy oscuro)
texto: #9CA3AF (gris medio)
headings: #FFFFFF (blanco)
links-hover: #F4B942 (amarillo)
```

---

## 🔍 Contraste y Accesibilidad

### ✅ Combinaciones Aprobadas (WCAG AA)

| Fondo | Texto | Ratio | Estado |
|-------|-------|-------|--------|
| #F4B942 | #111827 | 8.5:1 | ✅ AAA |
| #1A2332 | #FFFFFF | 14.2:1 | ✅ AAA |
| #FFFFFF | #374151 | 9.8:1 | ✅ AAA |
| #F9FAFB | #111827 | 16.1:1 | ✅ AAA |

---

## 🎨 Comparación: Antes vs Ahora

### ANTES (Con Gradientes)
```css
/* Hero */
background: linear-gradient(135deg, #F9FAFB 0%, #FFFFFF 100%);

/* CTA */
background: linear-gradient(135deg, #FFF4CC 0%, #FFD700 100%);

/* Amarillo muy brillante */
--color-primary: #FFD700
```

### AHORA (Colores Sólidos)
```css
/* Hero */
background-color: #F9FAFB;

/* CTA */
background-color: #F4B942;

/* Amarillo profesional */
--color-primary: #F4B942
```

---

## 💡 Ventajas de los Colores Sólidos

✅ **Más Profesional**: Aspecto limpio y corporativo
✅ **Mejor Performance**: Sin calcular gradientes
✅ **Más Fácil de Mantener**: Colores consistentes
✅ **Mejor Accesibilidad**: Contraste predecible
✅ **Más Minimalista**: Diseño más limpio
✅ **Mejor para Print**: Se ve igual impreso
✅ **Responsive Friendly**: Mismo color en todos los tamaños

---

## 🛠️ Cómo Personalizar

Para cambiar la paleta completa, edita en `css/style.css`:

```css
:root {
  /* Cambia estos 3 colores principales */
  --color-primary: #F4B942;        /* Tu color principal */
  --color-primary-dark: #E6A82E;   /* Versión más oscura */
  --color-secondary: #1A2332;       /* Color de contraste */
}
```

El resto se ajustará automáticamente.

---

## 📱 Vista Previa

**Desktop:**
- Header: Blanco (#FFFFFF) con sombra
- Hero: Fondo gris claro (#F9FAFB)
- Búsqueda: Blanco (#FFFFFF) con sombra
- Categorías: Blanco con bordes grises
- CTA: Amarillo sólido (#F4B942)
- Footer: Gris oscuro (#111827)

**Mobile:**
- Menú lateral: Blanco (#FFFFFF)
- Mismo esquema de colores
- Sin cambios en la paleta

---

**Última actualización:** Noviembre 2025
**Versión:** 2.0 - Colores Sólidos
