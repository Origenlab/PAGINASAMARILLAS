# Configuracion del Workflow n8n - Paginas Amarillas MX

## Archivo del Workflow

**Archivo:** `workflow-blog-seguridad-privada.json` (en la raiz del proyecto)

## Que hace el Workflow

1. **Selecciona aleatoriamente** una empresa y tipo de articulo
2. **Genera contenido** con ChatGPT (articulo SEO profesional)
3. **Crea HTML completo** con estilos, meta tags y Schema.org
4. **Sube automaticamente** el archivo a GitHub
5. **Inserta la card** automaticamente en blog/index.html
6. **Notifica por Telegram** con enlace

---

## Configuracion Paso a Paso

### 1. Importar el Workflow en n8n

1. Abrir n8n
2. Click en **Workflows** > **Import from File**
3. Seleccionar: `workflow-blog-seguridad-privada.json`
4. Click en **Import**

### 2. Configurar Credencial de OpenAI

1. Ir a **Settings** > **Credentials** > **Add Credential**
2. Buscar **OpenAI API**
3. Pegar tu API Key de [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
4. Guardar

En el nodo **"ChatGPT - Generar Articulo"**:
- Seleccionar la credencial de OpenAI

### 3. Configurar Credencial de GitHub

1. Ir a **Settings** > **Credentials** > **Add Credential**
2. Buscar **GitHub**
3. Crear un Personal Access Token en GitHub:
   - GitHub > Settings > Developer Settings > Personal Access Tokens > Tokens (classic)
   - Permisos necesarios: `repo` (full control)
4. Pegar el token en n8n
5. Guardar

**IMPORTANTE:** Usar la MISMA credencial en estos nodos:
- **"GitHub - Subir Articulo"**
- **"GitHub - Actualizar Blog Index"**

### 4. Configurar Telegram (Opcional)

1. Crear bot con @BotFather en Telegram (`/newbot`)
2. Copiar el token del bot
3. Obtener tu Chat ID:
   - Enviar mensaje al bot
   - Ir a: `https://api.telegram.org/bot<TU_TOKEN>/getUpdates`
   - Buscar "chat":{"id": XXXXXX}
4. En n8n: **Settings** > **Credentials** > **Add** > **Telegram**
5. Pegar el token

En el nodo **"Telegram - Notificar Publicacion"**:
- Poner tu Chat ID
- Seleccionar la credencial de Telegram

---

## Datos del Workflow

### Configuracion de GitHub

| Parametro | Valor |
|-----------|-------|
| Owner | `Origenlab` |
| Repository | `PAGINASAMARILLAS` |
| Ruta articulos | `blog/seguridad-privada/` |

### Empresas Configuradas

| Empresa | Slug | Imagen Principal |
|---------|------|------------------|
| ORIGINS Private Security | `origins-private-security` | equipo-seguridad-corporativo.webp |
| SeguridadPrivadaMX | `seguridad-privada-mx` | centro-monitoreo-camaras.webp |
| SEPRI | `sepri` | grupo-guardias-edificio.webp |
| Seguridad Condominios MX | `seguridad-condominios` | guardia-caseta-residencial.webp |

### Tipos de Articulos

1. **resena-completa** - Analisis detallado con servicios
2. **caso-exito** - Historia de implementacion exitosa
3. **guia-servicios** - Desglose de cada servicio
4. **opiniones-clientes** - Testimonios de clientes
5. **tecnologia-innovacion** - Analisis de tecnologia

---

## Programacion Automatica

El workflow esta configurado para ejecutarse:

- **Cada 3 dias** a las **8:00 AM**
- Tambien puede ejecutarse **manualmente**

---

## Como Funciona la Insercion de Cards

1. El workflow obtiene blog/index.html desde raw.githubusercontent.com
2. Inserta la nueva card despues de `<div class="blog-grid">`
3. Usa el nodo nativo de GitHub para actualizar (maneja SHA automaticamente)

Las cards nuevas aparecen al **INICIO** del grid (newest first).

---

## Troubleshooting

### Error: "No se encontro blog-grid"
- Verificar que blog/index.html tenga `<div class="blog-grid">`

### El articulo no aparece en el blog
- Verificar que la credencial de GitHub tenga permisos `repo`
- Revisar los logs del nodo "GitHub - Actualizar Blog Index"

---

*Workflow para Paginas Amarillas Mexico - Diciembre 2024*
