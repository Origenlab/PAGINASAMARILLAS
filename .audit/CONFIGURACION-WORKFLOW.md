# Configuracion del Workflow n8n - Paginas Amarillas MX

## Archivo del Workflow

**Archivo:** `.audit/workflow-blog-seguridad-privada.json`

Este workflow genera automaticamente articulos de blog para empresas de seguridad privada y los sube a GitHub.

---

## Que hace el Workflow

1. **Selecciona aleatoriamente** una empresa y tipo de articulo
2. **Genera contenido** con ChatGPT (articulo SEO profesional)
3. **Crea HTML completo** con estilos, meta tags y Schema.org
4. **Sube automaticamente** el archivo a GitHub
5. **Notifica por Telegram** con enlace y card para el blog index

---

## Configuracion Paso a Paso

### 1. Importar el Workflow en n8n

1. Abrir n8n
2. Click en **Workflows** > **Import from File**
3. Seleccionar: `.audit/workflow-blog-seguridad-privada.json`
4. Click en **Import**

### 2. Configurar Credencial de OpenAI (Header Auth)

1. Ir a **Settings** > **Credentials** > **Add Credential**
2. Buscar **Header Auth** (tipo HTTP Header Auth)
3. Configurar:
   - **Name**: `Authorization`
   - **Value**: `Bearer sk-tu-api-key-aqui`
   (Reemplaza `sk-tu-api-key-aqui` con tu API Key de [platform.openai.com/api-keys](https://platform.openai.com/api-keys))
4. Guardar como **"OpenAI Header Auth"**

En el nodo **"ChatGPT - Generar Articulo"** (HTTP Request):
- Click en el nodo
- En **"Authentication"**, seleccionar **"Generic Credential Type"**
- En **"Generic Auth Type"**, seleccionar **"Header Auth"**
- En **"Credential for Header Auth"**, seleccionar **"OpenAI Header Auth"**

### 3. Configurar Credencial de GitHub

1. Ir a **Settings** > **Credentials** > **Add Credential**
2. Buscar **GitHub**
3. Crear un Personal Access Token en GitHub:
   - GitHub > Settings > Developer Settings > Personal Access Tokens > Tokens (classic)
   - Permisos necesarios: `repo` (full control)
4. Pegar el token en n8n
5. Guardar

En el nodo **"7. Subir Articulo a GitHub"**:
- Click en el nodo
- En "Credential", seleccionar la credencial de GitHub
- Verificar que Owner sea: `Origenlab`
- Verificar que Repository sea: `PAGINASAMARILLAS`

### 4. Configurar Telegram (Opcional)

Si quieres recibir notificaciones:

1. Crear bot con @BotFather en Telegram (`/newbot`)
2. Copiar el token del bot
3. Obtener tu Chat ID:
   - Enviar mensaje al bot
   - Ir a: `https://api.telegram.org/bot<TU_TOKEN>/getUpdates`
   - Buscar "chat":{"id": XXXXXX}
4. En n8n: **Settings** > **Credentials** > **Add** > **Telegram**
5. Pegar el token

En el nodo **"9. Notificar por Telegram"**:
- Click en el nodo
- En "Chat ID", poner tu Chat ID
- En "Credential", seleccionar la credencial de Telegram

---

## Datos del Workflow

### Configuracion de GitHub

| Parametro | Valor |
|-----------|-------|
| Owner | `Origenlab` |
| Repository | `PAGINASAMARILLAS` |
| Ruta articulos | `blog/seguridad-privada/` |

### Rutas de Imagenes

| Tipo | Ruta |
|------|------|
| Relativa | `/img/img-seguridad-privada/` |
| Absoluta | `https://paginasamarillas.mx/img/img-seguridad-privada/` |

### Empresas Configuradas

| Empresa | Slug | Imagen Principal |
|---------|------|------------------|
| ORIGINS Private Security | `origins-private-security` | equipo-seguridad-corporativo.webp |
| SeguridadPrivadaMX | `seguridad-privada-mx` | centro-monitoreo-camaras.webp |
| SEPRI | `sepri` | vigilante-caseta-fraccionamiento.webp |
| Seguridad Condominios MX | `seguridad-condominios` | guardia-caseta-residencial.webp |

### Tipos de Articulos

El workflow genera aleatoriamente estos tipos:

1. **resena-completa** - Analisis detallado con servicios y precios
2. **caso-exito** - Historia de implementacion exitosa
3. **comparativa** - Ventajas competitivas
4. **guia-servicios** - Desglose de cada servicio
5. **opiniones** - Testimonios de clientes

---

## Programacion Automatica

El workflow esta configurado para ejecutarse:

- **Cada 3 dias** a las **9:00 AM**
- Tambien puede ejecutarse **manualmente**

Para cambiar la frecuencia:
1. Click en nodo "Publicar cada 3 dias"
2. Modificar "Days Interval" o "Trigger at Hour"

---

## Despues de Cada Publicacion

1. El articulo se sube automaticamente a GitHub
2. Recibes notificacion en Telegram con:
   - Enlace al articulo
   - Card HTML para agregar a `/blog/index.html`
3. Copiar la card y pegarla en el grid de articulos del blog

---

## Archivos Requeridos

Estos archivos deben existir en el repositorio:

| Archivo | Estado |
|---------|--------|
| `/css/style.css` | Requerido |
| `/css/blog-article.css` | Requerido |
| `/js/app.js` | Requerido |
| `/img/img-seguridad-privada/*.webp` | 60 imagenes |

---

## Troubleshooting

### Error: "Could not find credential"
- Revisar que las credenciales esten configuradas en n8n
- Seleccionar la credencial correcta en cada nodo

### Error: "Repository not found"
- Verificar que el token de GitHub tenga permisos `repo`
- Verificar que el repositorio sea `PAGINASAMARILLAS` (mayusculas)

### Error: "Invalid JSON"
- ChatGPT no devolvio formato correcto
- Ejecutar de nuevo el workflow

### Articulo no aparece en el sitio
- El archivo se subio a GitHub pero falta hacer pull en local
- O falta agregar la card a `/blog/index.html`

---

*Workflow para Paginas Amarillas Mexico - Diciembre 2024*
