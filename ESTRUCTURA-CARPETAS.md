# Estructura de Carpetas - PaginasAmarillas.mx
## Organización Profesional y Escalable

---

## 📁 Estructura Actual

```
/PAGINASAMARILLAS/
│
├── index.html                          # Homepage principal
│
├── categoria/                          # Listados por categoría
│   ├── seguridad-privada.html
│   ├── restaurantes.html (futuro)
│   ├── hoteles.html (futuro)
│   └── ...
│
├── negocios/                           # Perfiles de empresas
│   ├── seguridad-privada/              # ✨ Carpeta por categoría
│   │   ├── origins-private-security.html
│   │   ├── [empresa-2].html
│   │   └── [empresa-3].html
│   │
│   ├── restaurantes/ (futuro)
│   │   ├── [restaurante-1].html
│   │   └── [restaurante-2].html
│   │
│   └── hoteles/ (futuro)
│       └── ...
│
├── css/                                # Hojas de estilo
│   ├── style.css                       # Estilos globales
│   ├── categoria.css                   # Estilos para listados
│   └── perfil.css                      # Estilos para perfiles
│
├── js/                                 # JavaScript
│   ├── app.js                          # JS global
│   ├── categoria.js                    # JS para listados
│   └── perfil.js                       # JS para perfiles
│
├── assets/ (futuro)                    # Recursos estáticos
│   ├── images/
│   │   ├── logos/
│   │   ├── banners/
│   │   └── icons/
│   ├── fonts/
│   └── videos/
│
└── docs/                               # Documentación
    ├── ANALISIS-DIRECTORIOS-MEXICO.md
    ├── ORIGINS-SECURITY-ESTUDIO.md
    ├── PERFIL-NEGOCIO-DOCS.md
    ├── ESTRUCTURA-CARPETAS.md          # Este archivo
    └── ...
```

---

## 🎯 Convención de Nomenclatura

### URLs Amigables

**Patrón:** `/negocios/[categoria]/[slug-empresa]`

**Ejemplos:**
```
✅ /negocios/seguridad-privada/origins-private-security
✅ /negocios/restaurantes/el-cardenal
✅ /negocios/hoteles/fiesta-inn-insurgentes
✅ /negocios/construccion/grupo-constructor-abc
```

**❌ Evitar:**
```
❌ /negocios/origins-private-security (sin categoría)
❌ /negocio.php?id=123 (dinámico sin estructura)
❌ /company/origins (inglés)
```

### Slugs de Empresas

**Reglas:**
1. Todo en minúsculas
2. Sin acentos ni ñ
3. Palabras separadas por guiones (-)
4. Sin espacios ni caracteres especiales
5. Máximo 50 caracteres
6. Descriptivo del negocio

**Ejemplos de conversión:**
```
"Origins Private Security"     → origins-private-security
"El Cardenal Restaurante"      → el-cardenal-restaurante
"Fiesta Inn Insurgentes Sur"   → fiesta-inn-insurgentes-sur
"Café de la Parroquia"          → cafe-de-la-parroquia
"Grupo Constructor ABC S.A."    → grupo-constructor-abc
```

---

## 📂 Categorías Actuales y Futuras

### ✅ Implementadas

1. **seguridad-privada/**
   - origins-private-security.html ✅

### 🔜 Próximas (Sugeridas)

2. **restaurantes/**
   - el-cardenal.html
   - pujol.html
   - quintonil.html

3. **hoteles/**
   - fiesta-inn-insurgentes.html
   - city-express-reforma.html
   - hotel-geneve.html

4. **construccion/**
   - grupo-constructor-abc.html
   - ingenieros-civiles-asociados.html

5. **tecnologia/**
   - sistemas-informaticos-mx.html
   - desarrollo-software-pro.html

6. **salud/**
   - laboratorios-clinicos-central.html
   - hospital-angeles.html

7. **automotriz/**
   - taller-mecanico-express.html
   - refaccionaria-automotriz.html

8. **educacion/**
   - universidad-tecnologica.html
   - instituto-ingles.html

9. **legal/**
   - bufete-juridico-asociados.html
   - notaria-publica.html

10. **contabilidad/**
    - despacho-contable-fiscal.html
    - auditores-independientes.html

---

## 🔗 Sistema de Links

### Links Relativos (Recomendado)

**Desde `/negocios/seguridad-privada/origins-private-security.html`:**

```html
<!-- CSS -->
<link rel="stylesheet" href="../../css/style.css">
<link rel="stylesheet" href="../../css/perfil.css">

<!-- Header/Nav -->
<a href="../../index.html">Inicio</a>
<a href="../../categoria/seguridad-privada.html">Seguridad Privada</a>

<!-- Scripts -->
<script src="../../js/app.js"></script>
<script src="../../js/perfil.js"></script>
```

**Desde `/categoria/seguridad-privada.html`:**

```html
<!-- Link a perfil -->
<a href="/negocios/seguridad-privada/origins-private-security">Ver perfil</a>

<!-- o con ruta relativa -->
<a href="../negocios/seguridad-privada/origins-private-security">Ver perfil</a>
```

### Links Absolutos (Producción)

```html
<!-- Recomendado para producción -->
<a href="https://paginasamarillas.mx/negocios/seguridad-privada/origins-private-security">
  Ver perfil
</a>
```

---

## 🚀 Ventajas de esta Estructura

### 1. **Escalabilidad**
- ✅ Fácil agregar nuevas categorías
- ✅ Fácil agregar nuevas empresas
- ✅ Organización clara por sector
- ✅ No hay límite de crecimiento

### 2. **SEO Optimizado**
- ✅ URLs semánticas: `/negocios/seguridad-privada/origins-private-security`
- ✅ Keywords en la URL (seguridad-privada)
- ✅ Estructura jerárquica clara
- ✅ Breadcrumbs automáticos

### 3. **Mantenimiento Sencillo**
- ✅ Fácil localizar archivos por categoría
- ✅ Evita archivos sueltos en carpeta raíz
- ✅ Convención clara para todo el equipo
- ✅ Backups por categoría

### 4. **Performance**
- ✅ Servidor puede cachear por carpeta
- ✅ CDN puede optimizar por ruta
- ✅ Menos archivos en cada directorio
- ✅ Búsqueda de archivos más rápida

### 5. **UX/UI**
- ✅ URLs legibles y recordables
- ✅ Usuario entiende dónde está navegando
- ✅ Fácil compartir links específicos
- ✅ Navegación intuitiva

---

## 📝 Proceso para Agregar Nueva Empresa

### Paso 1: Verificar Categoría

```bash
# Si la categoría NO existe, crear carpeta
mkdir -p negocios/[categoria]

# Ejemplo:
mkdir -p negocios/restaurantes
```

### Paso 2: Crear Slug

```javascript
// Función helper para crear slug
function createSlug(businessName) {
  return businessName
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '') // Quitar acentos
    .replace(/ñ/g, 'n')
    .replace(/[^a-z0-9\s-]/g, '') // Solo letras, números, espacios, guiones
    .trim()
    .replace(/\s+/g, '-') // Espacios a guiones
    .replace(/-+/g, '-') // Múltiples guiones a uno
    .substring(0, 50); // Max 50 caracteres
}

// Ejemplos:
createSlug("Origins Private Security")  // → "origins-private-security"
createSlug("Café de la Parroquia")      // → "cafe-de-la-parroquia"
```

### Paso 3: Copiar Template

```bash
# Copiar desde Origins (template)
cp negocios/seguridad-privada/origins-private-security.html \
   negocios/[categoria]/[slug-empresa].html

# Ejemplo:
cp negocios/seguridad-privada/origins-private-security.html \
   negocios/restaurantes/el-cardenal.html
```

### Paso 4: Personalizar Contenido

**Actualizar:**
1. Meta tags (title, description, keywords)
2. Breadcrumbs
3. Título H1
4. Servicios/Productos (8 cards)
5. Información de contacto
6. Sobre la empresa
7. Reseñas
8. Imágenes

### Paso 5: Actualizar Listado de Categoría

```html
<!-- En categoria/[categoria].html -->
<article class="business-card">
  <!-- Agregar tarjeta con link correcto -->
  <a href="/negocios/[categoria]/[slug-empresa]">
    Ver perfil
  </a>
</article>
```

---

## 🔒 Seguridad y Best Practices

### Archivos Prohibidos en Carpetas Públicas

**❌ NO incluir:**
```
.env
.htpasswd
config.php
database.sql
backup.zip
```

### Permisos de Carpetas (Servidor Linux)

```bash
# Carpetas: lectura + ejecución
chmod 755 negocios/
chmod 755 negocios/seguridad-privada/

# Archivos HTML: lectura
chmod 644 negocios/seguridad-privada/*.html

# Archivos ejecutables (si aplica)
chmod 755 scripts/*.sh
```

### .htaccess Recomendado

```apache
# En /negocios/.htaccess

# Prevenir listado de directorios
Options -Indexes

# URL Rewriting (opcional)
RewriteEngine On

# Agregar .html automáticamente
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.*)$ $1.html [L]

# Ejemplo: /negocios/seguridad-privada/origins-private-security
#    → /negocios/seguridad-privada/origins-private-security.html

# Redireccionar sin www a con www (opcional)
# RewriteCond %{HTTP_HOST} ^paginasamarillas\.mx [NC]
# RewriteRule ^(.*)$ https://www.paginasamarillas.mx/$1 [L,R=301]
```

---

## 📊 Métricas de Organización

### Límites Recomendados

**Por carpeta de categoría:**
- Mínimo: 5 empresas (antes de publicar categoría)
- Óptimo: 20-50 empresas
- Máximo: 200 empresas (considerar subcategorías)

**Si excede 200 empresas:**
```
negocios/
└── seguridad-privada/
    ├── cdmx/
    ├── guadalajara/
    └── monterrey/
```

o

```
negocios/
└── seguridad-privada/
    ├── guardias/
    ├── escoltas/
    └── tecnologia/
```

---

## 🎯 Roadmap de Categorías

### Fase 1 (Mes 1-2) - 5 Categorías
- [x] Seguridad Privada (1 empresa) ✅
- [ ] Restaurantes (10 empresas)
- [ ] Hoteles (10 empresas)
- [ ] Construcción (10 empresas)
- [ ] Tecnología (10 empresas)

### Fase 2 (Mes 3-4) - 10 Categorías
- [ ] Salud (Hospitales, Laboratorios)
- [ ] Automotriz (Talleres, Refaccionarias)
- [ ] Educación (Universidades, Idiomas)
- [ ] Legal (Abogados, Notarios)
- [ ] Contabilidad (Despachos, Auditores)

### Fase 3 (Mes 5-6) - 15+ Categorías
- [ ] Inmobiliaria
- [ ] Turismo
- [ ] Eventos
- [ ] Marketing
- [ ] Logística
- [ ] ...

---

## 📚 Documentos Relacionados

- [README-DESARROLLO.md](README-DESARROLLO.md) - Documentación general
- [PERFIL-NEGOCIO-DOCS.md](PERFIL-NEGOCIO-DOCS.md) - Cómo crear perfiles
- [ORIGINS-SECURITY-ESTUDIO.md](ORIGINS-SECURITY-ESTUDIO.md) - Ejemplo de estudio
- [CATEGORIA-SEGURIDAD-PRIVADA.md](CATEGORIA-SEGURIDAD-PRIVADA.md) - Docs de categoría

---

## 🛠️ Herramientas Útiles

### Generador de Slugs (Python)

```python
import re
import unicodedata

def create_slug(text):
    # Normalizar y quitar acentos
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')

    # Convertir a minúsculas
    text = text.lower()

    # Reemplazar espacios y caracteres especiales
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)

    # Limitar longitud
    return text.strip('-')[:50]

# Uso:
print(create_slug("Origins Private Security"))
# → "origins-private-security"
```

### Validador de Estructura (Bash)

```bash
#!/bin/bash
# validate-structure.sh

echo "Validando estructura de carpetas..."

# Verificar que existen las carpetas principales
for dir in negocios css js categoria; do
  if [ ! -d "$dir" ]; then
    echo "❌ Falta carpeta: $dir"
  else
    echo "✅ $dir"
  fi
done

# Contar empresas por categoría
for cat_dir in negocios/*/; do
  cat_name=$(basename "$cat_dir")
  count=$(ls -1 "$cat_dir"*.html 2>/dev/null | wc -l)
  echo "📁 $cat_name: $count empresas"
done
```

---

**Última actualización:** Noviembre 2025
**Versión:** 1.0
**Estado:** Estructura implementada y operativa
**Primera categoría:** Seguridad Privada ✅
**Primera empresa:** Origins Private Security ✅
