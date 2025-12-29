# Instalacion del Workflow n8n - Blog Paginas Amarillas

Guia completa paso a paso para instalar y configurar el workflow de generacion automatica de articulos.

---

## REQUISITOS PREVIOS

### Software
- n8n version 1.30+ (self-hosted o cloud)
- Node.js 18+ (si es self-hosted)

### Cuentas y APIs
- [ ] Cuenta GitHub con acceso al repositorio PAGINASAMARILLAS
- [ ] API Key de OpenAI (GPT-4o recomendado)
- [ ] Bot de Telegram configurado
- [ ] Cuenta Google con acceso a Sheets (opcional para logs)

---

## PASO 1: IMPORTAR EL WORKFLOW

### 1.1 Acceder a n8n

```
# Si es self-hosted
n8n start

# URL por defecto
http://localhost:5678
```

### 1.2 Importar JSON

1. Ir a **Workflows** en el menu lateral
2. Click en **Import from File**
3. Seleccionar: `workflow-blog-articulos-v2.json`
4. Click en **Import**

El workflow aparecera con el nombre:
**"Blog Paginas Amarillas - Generador de Articulos SEO v2.0"**

---

## PASO 2: CONFIGURAR VARIABLES DE ENTORNO

### 2.1 Acceder a Variables

En n8n, ir a:
**Settings** > **Variables** > **Add Variable**

### 2.2 Variables Requeridas

| Variable | Valor | Descripcion |
|----------|-------|-------------|
| `GITHUB_OWNER` | `Origenlab` | Usuario/organizacion de GitHub |
| `GITHUB_REPO` | `PAGINASAMARILLAS` | Nombre del repositorio |
| `TELEGRAM_CHAT_ID` | `123456789` | ID del chat de Telegram |
| `GOOGLE_SHEET_ID` | `1abc...xyz` | ID de Google Sheet para logs |

### 2.3 Crear Variables

Para cada variable:
1. Click **Add Variable**
2. Nombre: `GITHUB_OWNER`
3. Valor: `Origenlab`
4. Click **Save**

---

## PASO 3: CONFIGURAR CREDENCIALES

### 3.1 GitHub API

1. Ir a **Settings** > **Credentials** > **Add Credential**
2. Buscar **GitHub**
3. Seleccionar **GitHub API**

**Crear Personal Access Token en GitHub:**

1. GitHub > Settings > Developer Settings > Personal Access Tokens > Tokens (classic)
2. Click **Generate new token (classic)**
3. Nombre: `n8n-paginas-amarillas`
4. Expiracion: 90 dias o sin expiracion
5. Permisos requeridos:
   - [x] `repo` (Full control of private repositories)
   - [x] `workflow` (Update GitHub Action workflows)
6. Click **Generate token**
7. **COPIAR EL TOKEN** (solo se muestra una vez)

**En n8n:**
- Access Token: `ghp_xxxxxxxxxxxx`
- Click **Save**

### 3.2 OpenAI API

1. Ir a **Settings** > **Credentials** > **Add Credential**
2. Buscar **OpenAI**
3. Seleccionar **OpenAI API**

**Obtener API Key:**
1. Ir a [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Click **Create new secret key**
3. Nombre: `n8n-paginas-amarillas`
4. **COPIAR LA KEY** (solo se muestra una vez)

**En n8n:**
- API Key: `sk-xxxxxxxxxxxx`
- Click **Save**

### 3.3 Telegram Bot

**Crear Bot:**
1. Abrir Telegram y buscar `@BotFather`
2. Enviar `/newbot`
3. Seguir instrucciones:
   - Nombre: `Paginas Amarillas Blog Bot`
   - Username: `paginasamarillas_blog_bot`
4. Copiar el token: `123456789:ABCdefGHIjklMNO...`

**Obtener Chat ID:**
1. Enviar cualquier mensaje al bot
2. Abrir en navegador:
   ```
   https://api.telegram.org/bot<TU_TOKEN>/getUpdates
   ```
3. Buscar `"chat":{"id":123456789`
4. Copiar el numero (puede ser negativo para grupos)

**En n8n:**
1. Ir a **Settings** > **Credentials** > **Add Credential**
2. Buscar **Telegram**
3. Access Token: `123456789:ABCdefGHIjklMNO...`
4. Click **Save**

### 3.4 Google Sheets (Opcional)

1. Ir a **Settings** > **Credentials** > **Add Credential**
2. Buscar **Google Sheets**
3. Seleccionar **OAuth2**
4. Seguir el flujo de autorizacion de Google

**Crear Spreadsheet:**
1. Crear nuevo Google Sheet
2. Renombrar primera hoja a `Log`
3. Agregar encabezados en fila 1:
   ```
   fecha | empresa | articulo | slug | tipo | url | status
   ```
4. Copiar el ID del Sheet de la URL:
   ```
   https://docs.google.com/spreadsheets/d/[ESTE-ES-EL-ID]/edit
   ```

---

## PASO 4: CONECTAR CREDENCIALES A NODOS

### 4.1 Nodos de GitHub

En cada nodo de GitHub, verificar:
1. Click en el nodo
2. En **Credential to connect with**, seleccionar la credencial creada

Nodos a verificar:
- `GitHub - Obtener Configuracion`
- `GitHub - Subir Articulo`
- `GitHub - Obtener blog/index.html`
- `GitHub - Actualizar blog/index.html`

### 4.2 Nodo de OpenAI

1. Click en `OpenAI - Generar Articulo`
2. Verificar que la credencial este seleccionada

### 4.3 Nodos de Telegram

1. Click en `Telegram - Notificar`
2. Seleccionar credencial
3. Verificar `Chat ID` = `{{ $env.TELEGRAM_CHAT_ID }}`

4. Repetir para `Telegram - Error`

### 4.4 Nodo de Google Sheets

1. Click en `Google Sheets - Log`
2. Seleccionar credencial
3. Verificar `Document ID` = `{{ $env.GOOGLE_SHEET_ID }}`

---

## PASO 5: VERIFICAR CONFIGURACION

### 5.1 Test Individual de Nodos

1. Desactivar el workflow temporalmente
2. Click en cada nodo y ejecutar **Test step**

**Orden de prueba:**
1. `GitHub - Obtener Configuracion` - Debe devolver JSON de blog-config.json
2. `Code - Procesar Configuracion` - Debe mostrar empresa y tipo seleccionados
3. `OpenAI - Generar Articulo` - Debe generar contenido (puede tardar 30-60 seg)

### 5.2 Ejecucion Manual Completa

1. Desactivar Schedule Trigger
2. Agregar nodo **Manual Trigger** temporal
3. Conectar al inicio del workflow
4. Click **Execute Workflow**
5. Verificar cada nodo en verde

---

## PASO 6: ACTIVAR EL WORKFLOW

### 6.1 Configurar Schedule

El workflow esta configurado para ejecutarse:
- **Cada 3 dias a las 9:00 AM**
- Timezone: Local del servidor

Para cambiar:
1. Click en `Schedule Trigger - Cada 3 Dias`
2. Modificar intervalo segun necesidad

### 6.2 Activar

1. Toggle **Active** en la esquina superior derecha
2. El workflow comenzara a ejecutarse automaticamente

---

## ARQUITECTURA DEL WORKFLOW

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKFLOW COMPLETO                            │
└─────────────────────────────────────────────────────────────────┘

[Schedule Trigger]
       │
       ▼
[GitHub - Obtener Configuracion]
       │
       ▼
[Code - Procesar Configuracion]
       │ Selecciona: empresa + tipo + imagenes
       ▼
[IF - Validar Seleccion]
       │
       ├─── TRUE ──────────────────────────────────────┐
       │                                                │
       ▼                                                ▼
[OpenAI - Generar Articulo]                    [Error Branch]
       │                                                │
       ▼                                                ▼
[Code - Parsear Contenido]                     [Telegram - Error]
       │
       ▼
[Code - Construir HTML Articulo]
       │
       ▼
[Code - Construir Card HTML]
       │
       ▼
[GitHub - Subir Articulo]
       │
       ▼
[GitHub - Obtener blog/index.html]
       │
       ▼
[Code - Insertar Card]
       │
       ▼
[GitHub - Actualizar blog/index.html]
       │
       ▼
[Google Sheets - Log]
       │
       ▼
[Telegram - Notificar]
       │
       ▼
[Success - Fin]
```

---

## TROUBLESHOOTING

### Error: "Resource not found" en GitHub

**Causa:** Token sin permisos o repositorio incorrecto

**Solucion:**
1. Verificar variable `GITHUB_OWNER` y `GITHUB_REPO`
2. Regenerar token con permisos `repo`

### Error: "Marcador n8n no encontrado"

**Causa:** El archivo blog/index.html no tiene el marcador

**Solucion:**
Agregar en blog/index.html dentro del `<div class="blog-grid">`:
```html
<!-- n8n:INSERT-NEW-CARDS-HERE -->
```

### Error: "Rate limit exceeded" en OpenAI

**Causa:** Demasiadas solicitudes

**Solucion:**
1. Verificar limites de tu plan OpenAI
2. Aumentar intervalo del Schedule Trigger

### Error: "SHA mismatch" al actualizar

**Causa:** El archivo fue modificado mientras se procesaba

**Solucion:**
1. El nodo GitHub nativo maneja esto automaticamente
2. Reintentar la ejecucion

### Articulo no aparece en el sitio

**Causa:** Cache o GitHub Pages no actualizado

**Solucion:**
1. Esperar 2-5 minutos para que GitHub Pages actualice
2. Hacer hard refresh (Ctrl+Shift+R)

---

## MANTENIMIENTO

### Agregar Nueva Empresa

1. Editar `blog/blog-config.json`
2. Agregar en `businesses.seguridad-privada`:
```json
{
  "id": "nueva-empresa",
  "name": "Nueva Empresa SA",
  "slug": "nueva-empresa",
  "businessPage": "/negocios/seguridad-privada/nueva-empresa.html",
  "mainImage": "imagen-principal.webp",
  "services": ["servicio1", "servicio2"],
  "location": "CDMX",
  "keywords": ["keyword1", "keyword2"]
}
```

### Agregar Nuevas Imagenes

1. Subir imagenes a `/img/img-seguridad-privada/`
2. Agregar nombres en `blog-config.json` > `images.seguridad-privada`

### Modificar Prompt de OpenAI

1. Click en nodo `OpenAI - Generar Articulo`
2. Editar el prompt en `Messages`
3. Guardar y probar

---

## LOGS Y MONITOREO

### Google Sheets

Cada ejecucion registra:
- Fecha y hora
- Empresa
- Titulo del articulo
- Slug
- Tipo de articulo
- URL final
- Estado

### Telegram

Notificaciones:
- ✅ Exito: Titulo, empresa, URL del articulo
- ❌ Error: Mensaje de error, nodo fallido

### n8n Execution History

1. Ir a **Executions**
2. Ver historial de ejecuciones
3. Click en una para ver detalles

---

## COSTOS ESTIMADOS

| Servicio | Costo por Ejecucion | Mensual (10 articulos) |
|----------|---------------------|------------------------|
| OpenAI GPT-4o | ~$0.05-0.10 USD | ~$0.50-1.00 USD |
| GitHub | Gratis | Gratis |
| n8n Cloud | Segun plan | Segun plan |
| Telegram | Gratis | Gratis |
| Google Sheets | Gratis | Gratis |

**Total estimado: $0.50 - $5.00 USD/mes**

---

## SOPORTE

### Recursos
- Documentacion n8n: [docs.n8n.io](https://docs.n8n.io)
- API OpenAI: [platform.openai.com/docs](https://platform.openai.com/docs)
- GitHub API: [docs.github.com](https://docs.github.com/en/rest)

### Archivos del Proyecto
- Workflow: `n8n-workflows/workflow-blog-articulos-v2.json`
- Configuracion: `blog/blog-config.json`
- Templates: `blog/templates/`
- Documentacion: `WORKFLOW-AUTOMATIZACION.md`

---

*Guia de Instalacion v2.0 - Diciembre 2024*
