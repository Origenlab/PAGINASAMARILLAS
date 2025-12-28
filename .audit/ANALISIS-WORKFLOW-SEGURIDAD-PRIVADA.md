# Análisis del Workflow n8n - Generador de Artículos de Blog

## Resumen Ejecutivo

Este documento analiza el workflow de n8n diseñado para generar automáticamente artículos de blog/reseñas de empresas de seguridad privada. El workflow está configurado para **OrigenLab** y requiere adaptación para funcionar con **Páginas Amarillas México**.

---

## Arquitectura del Workflow

### Flujo de Datos

```
[Trigger] → [Selector de Tema] → [Constructor Prompt] → [ChatGPT] → [Validador] → [HTML Builder] → [GitHub] → [Telegram]
    ↓           ↓                      ↓                  ↓           ↓              ↓              ↓           ↓
  Manual/   Empresa +      Prompt           JSON        Validar     HTML         Subir        Notificar
  Cada 3    Enfoque +      Completo        Artículo    + Procesar  Profesional   Archivo      Éxito
  días      Imágenes
```

### Nodos del Workflow

| # | Nodo | Tipo | Función |
|---|------|------|---------|
| 1 | Cada 3 Días | scheduleTrigger | Ejecuta automáticamente cada 3 días a las 8:00 AM |
| 2 | Ejecución Manual | manualTrigger | Permite ejecución manual bajo demanda |
| 3 | Selector de Tema e Imágenes | code | Selecciona empresa, enfoque y imágenes aleatorios |
| 4 | Constructor de Prompt | code | Genera prompt detallado para ChatGPT |
| 5 | ChatGPT - Generar Artículo | openAi | Llama a la API de ChatGPT para generar contenido |
| 6 | Validar y Procesar Respuesta | code | Parsea JSON y reemplaza marcadores de imagen |
| 7 | ¿Artículo Válido? | if | Bifurca flujo según éxito/error |
| 8 | Construir HTML Profesional | code | Genera documento HTML completo |
| 9 | GitHub - Subir Artículo | github | Sube archivo al repositorio |
| 10 | Resumen y Código para blog.html | code | Genera código para agregar al índice del blog |
| 11 | Telegram - Notificar Publicación | telegram | Envía notificación de éxito |
| 12 | Manejar Error | code | Procesa errores de generación |

---

## Configuración Actual (OrigenLab)

### URLs y Rutas

| Parámetro | Valor Actual |
|-----------|--------------|
| Dominio | `origenlab.com.mx` |
| Ruta imágenes relativa | `../img/seguridad-privada/` |
| Ruta imágenes absoluta | `https://origenlab.com.mx/img/seguridad-privada/` |
| URL perfil empresa | `https://origenlab.com.mx/categorias/seguridad-privada/{slug}.html` |
| GitHub Owner | `ORIGENLAB` |
| GitHub Repository | `origenlab` |
| Ruta archivo blog | `blog/{slug}.html` |

### Empresas Configuradas

1. **ORIGINS Private Security**
   - ID: `origins-security`
   - Imagen: `control-acceso-residencial-caseta.webp`

2. **SeguridadPrivadaMX**
   - ID: `seguridad-privada-mx`
   - Imagen: `centro-monitoreo-cctv-camaras.webp`

3. **SEPRICO**
   - ID: `seprico`
   - Imagen: `vigilante-fraccionamiento-residencial.webp`

4. **Seguridad para Eventos**
   - ID: `seguridad-eventos`
   - Imagen: `seguridad-eventos-alfombra-roja.webp`

### Tipos de Artículos (Enfoques)

| Tipo | Descripción |
|------|-------------|
| resena-general | Análisis completo de servicios y opiniones |
| caso-exito | Historia de implementación exitosa |
| comparativa | Ventajas competitivas vs mercado |
| guia-servicios | Desglose de cada servicio |
| testimoniales | Recopilación de opiniones de clientes |
| tecnologia | Análisis de herramientas tecnológicas |
| precio-valor | Guía de precios y ROI |
| entrevista | Filosofía y valores del equipo |

---

## Adaptación Requerida para Páginas Amarillas

### Cambios de Configuración

| Parámetro | Valor Actual | Valor Nuevo |
|-----------|--------------|-------------|
| Dominio | `origenlab.com.mx` | `paginasamarillas.mx` |
| Ruta imágenes | `../img/seguridad-privada/` | `../img/img-seguridad-privada/` |
| Ruta imágenes absoluta | `https://origenlab.com.mx/img/seguridad-privada/` | `https://paginasamarillas.mx/img/img-seguridad-privada/` |
| URL perfil empresa | `origenlab.com.mx/categorias/...` | `paginasamarillas.mx/negocios/seguridad-privada/...` |
| GitHub Owner | `ORIGENLAB` | `Origenlab` |
| GitHub Repository | `origenlab` | `PAGINASAMARILLAS` |
| Ruta archivo | `blog/{slug}.html` | `blog/seguridad-privada/{slug}.html` |
| CSS paths | `../css/minimal-global.css` | `/css/style.css` |

### Empresas a Configurar (del directorio actual)

Basado en los archivos en `/negocios/seguridad-privada/`:

1. **ORIGINS Private Security** (`origins-private-security.html`)
2. **SeguridadPrivadaMX** (`seguridad-privada-mx.html`)
3. **SEPRICO** (`sepri.html`)
4. **Seguridad Condominios** (`seguridad-condominios.html`)

### Banco de Imágenes Disponibles (60 imágenes WebP)

```
Guardias y Personal:
- equipo-seguridad-corporativo.webp
- grupo-guardias-edificio.webp
- guardia-caseta-residencial.webp
- guardia-corporativo-oficina.webp
- guardia-uniforme-edificio.webp
- guardia-atencion-visitante.webp
- vigilante-caseta-fraccionamiento.webp
- rondin-nocturno-condominio.webp

Control de Acceso:
- acceso-biometrico-torniquete.webp
- control-huella-digital.webp
- seguridad-acceso-biometrico.webp
- torniquete-acceso-oficina.webp
- control-acceso-credencial.webp
- verificacion-identificacion.webp

Videovigilancia:
- centro-monitoreo-camaras.webp
- monitoreo-cctv-central.webp
- operador-videovigilancia.webp
- seguridad-caseta-cctv.webp

Escoltas y VIP:
- escolta-ejecutivo-vehiculo.webp
- escolta-vip-estacionamiento.webp
- proteccion-vip-auto.webp

Industrial/Comercial:
- vigilancia-planta-industrial.webp
- guardia-nave-industrial.webp
- seguridad-zona-carga.webp
- seguridad-centro-comercial.webp
```

---

## Estructura de Archivos Requerida

```
/PAGINASAMARILLAS/
├── blog/
│   ├── index.html                          ✅ Existe
│   ├── seguridad-privada/
│   │   ├── [articulos-generados].html      📝 Destino de artículos
│   │   └── ...
│   └── categorias/
│       └── seguridad-privada.html          ✅ Existe
├── negocios/
│   └── seguridad-privada/
│       ├── origins-private-security.html   ✅ Existe
│       ├── seguridad-privada-mx.html       ✅ Existe
│       ├── sepri.html                      ✅ Existe
│       └── seguridad-condominios.html      ✅ Existe
├── img/
│   └── img-seguridad-privada/              ✅ 60 imágenes WebP
├── css/
│   └── style.css                           ✅ Existe
└── .audit/
    ├── workflow-seguridadprivada-v1.json   ✅ Original
    ├── workflow-paginasamarillas-v1.json   📝 Adaptado
    └── ANALISIS-WORKFLOW-SEGURIDAD-PRIVADA.md  📝 Este documento
```

---

## Credenciales Requeridas en n8n

| Servicio | Nombre Credencial | Configuración Necesaria |
|----------|-------------------|-------------------------|
| OpenAI | OpenAi account | API Key de OpenAI |
| GitHub | GitHub account | Token con permisos de escritura al repo |
| Telegram | Telegram account | Bot Token + Chat ID |

---

## Instrucciones de Implementación

### 1. Importar Workflow Adaptado

1. Abrir n8n
2. Ir a Workflows → Import from File
3. Seleccionar `.audit/workflow-paginasamarillas-v1.json`
4. Configurar credenciales

### 2. Configurar Credenciales

**GitHub:**
- Crear Personal Access Token en GitHub Settings
- Permisos: `repo` (full control)
- En n8n: Settings → Credentials → Add → GitHub

**OpenAI:**
- Obtener API Key de platform.openai.com
- En n8n: Settings → Credentials → Add → OpenAI

**Telegram:**
- Crear bot con @BotFather
- Obtener Chat ID (enviar mensaje al bot, luego consultar updates)
- En n8n: Settings → Credentials → Add → Telegram

### 3. Probar Workflow

1. Activar workflow
2. Hacer clic en "Execute Workflow" (ejecución manual)
3. Verificar que se genere artículo en GitHub
4. Confirmar notificación en Telegram

### 4. Post-Publicación

Después de cada artículo generado:
1. Copiar código HTML del resumen
2. Agregar al inicio del grid en `/blog/index.html`
3. Verificar visualización correcta

---

## Notas Técnicas

### Formato del HTML Generado

El workflow genera artículos con:
- SEO meta tags completos
- Open Graph y Twitter Cards
- Schema.org BlogPosting
- Tabla de contenidos navegable
- Imágenes lazy-loaded
- CTA al final del artículo
- Sidebar con newsletter y proveedores

### Longitud de Artículos

- Target: 1,800-2,500 palabras
- Tiempo lectura: 10-12 minutos
- 6 secciones obligatorias
- 3 imágenes de contenido

### Frecuencia de Publicación

- Automático: Cada 3 días a las 8:00 AM
- Manual: Bajo demanda desde n8n

---

## Próximos Pasos

1. ✅ Análisis del workflow original
2. ⏳ Crear workflow adaptado para Páginas Amarillas
3. ⏳ Actualizar datos de empresas
4. ⏳ Configurar credenciales en n8n
5. ⏳ Prueba de generación de artículo
6. ⏳ Integración con blog.html

---

*Documento generado para el proyecto Páginas Amarillas México*
*Fecha: Diciembre 2024*
