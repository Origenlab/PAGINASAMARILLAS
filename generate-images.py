#!/usr/bin/env python3
"""
Script para generar imágenes faltantes de Páginas Amarillas México
Especificaciones según ANALISIS-PRODUCCION.md
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Colores oficiales
COLOR_YELLOW = '#F4B942'
COLOR_NAVY = '#1A2332'
COLOR_GRAY = '#4A5568'
COLOR_CREAM_LIGHT = '#FFF8E7'
COLOR_WHITE = '#FFFFFF'

# Crear directorio images si no existe
os.makedirs('images', exist_ok=True)

print("🎨 Generando imágenes para Páginas Amarillas México...")
print("=" * 60)

# ============================================
# 1. OG IMAGE (1200x630px) - Social Sharing
# ============================================
print("\n1️⃣  Creando og-image.webp (1200x630px)...")

# Crear imagen con gradiente vertical
og_img = Image.new('RGB', (1200, 630), COLOR_CREAM_LIGHT)
draw = ImageDraw.Draw(og_img)

# Gradiente vertical (cream light → yellow)
for y in range(630):
    # Interpolación de color
    factor = y / 630
    r1, g1, b1 = int('FF', 16), int('F8', 16), int('E7', 16)  # Cream light
    r2, g2, b2 = int('F4', 16), int('B9', 16), int('42', 16)  # Yellow

    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)

    draw.rectangle([(0, y), (1200, y+1)], fill=(r, g, b))

# Intentar cargar fuente (o usar default)
try:
    # Intentar fuentes del sistema macOS
    font_title = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 80)
    font_subtitle = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 40)
    font_logo = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 50)
except:
    print("   ⚠️  Usando fuente default (no se encontró Arial)")
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_logo = ImageFont.load_default()

# Dibujar logo en la parte superior
logo_text = "Páginas Amarillas.mx"
# Calcular posición centrada
bbox = draw.textbbox((0, 0), logo_text, font=font_logo)
logo_width = bbox[2] - bbox[0]
logo_x = (1200 - logo_width) // 2
draw.text((logo_x, 60), logo_text, fill=COLOR_NAVY, font=font_logo)

# Headline principal
headline = "Directorio de Empresas"
bbox = draw.textbbox((0, 0), headline, font=font_title)
headline_width = bbox[2] - bbox[0]
headline_x = (1200 - headline_width) // 2
draw.text((headline_x, 220), headline, fill=COLOR_NAVY, font=font_title)

# Subheadline "en México"
subheadline1 = "en México"
bbox = draw.textbbox((0, 0), subheadline1, font=font_title)
sub1_width = bbox[2] - bbox[0]
sub1_x = (1200 - sub1_width) // 2
draw.text((sub1_x, 310), subheadline1, fill=COLOR_NAVY, font=font_title)

# Texto destacado
highlight = "+40,000 negocios verificados"
bbox = draw.textbbox((0, 0), highlight, font=font_subtitle)
highlight_width = bbox[2] - bbox[0]
highlight_x = (1200 - highlight_width) // 2
draw.text((highlight_x, 450), highlight, fill=COLOR_GRAY, font=font_subtitle)

# URL al final
url_text = "paginasamarillas.mx"
font_url = ImageFont.load_default()
bbox = draw.textbbox((0, 0), url_text, font=font_url)
url_width = bbox[2] - bbox[0]
url_x = 1200 - url_width - 40
draw.text((url_x, 590), url_text, fill=COLOR_GRAY, font=font_url)

# Guardar como WebP con calidad 85%
og_img.save('images/og-image.webp', 'WEBP', quality=85, method=6)
file_size = os.path.getsize('images/og-image.webp') / 1024
print(f"   ✅ og-image.webp creado: {file_size:.1f} KB")

# ============================================
# 2. LOGO (250x60px) - Schema.org
# ============================================
print("\n2️⃣  Creando logo.webp (250x60px)...")

# Crear imagen con fondo transparente
logo_img = Image.new('RGBA', (250, 60), (255, 255, 255, 0))
draw = ImageDraw.Draw(logo_img)

# Intentar fuente para logo
try:
    font_logo_main = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 24)
except:
    font_logo_main = ImageFont.load_default()

# Texto "Páginas" (gris oscuro)
text1 = "Páginas "
bbox = draw.textbbox((0, 0), text1, font=font_logo_main)
w1 = bbox[2] - bbox[0]
draw.text((10, 18), text1, fill=COLOR_NAVY, font=font_logo_main)

# Texto "Amarillas" (amarillo)
text2 = "Amarillas"
bbox = draw.textbbox((0, 0), text2, font=font_logo_main)
w2 = bbox[2] - bbox[0]
draw.text((10 + w1, 18), text2, fill=COLOR_YELLOW, font=font_logo_main)

# Texto ".mx" (gris oscuro)
text3 = ".mx"
draw.text((10 + w1 + w2, 18), text3, fill=COLOR_NAVY, font=font_logo_main)

# Guardar como WebP lossless
logo_img.save('images/logo.webp', 'WEBP', lossless=True, method=6)
file_size = os.path.getsize('images/logo.webp') / 1024
print(f"   ✅ logo.webp creado: {file_size:.1f} KB")

# ============================================
# 3. APPLE TOUCH ICON (180x180px) - iOS
# ============================================
print("\n3️⃣  Creando apple-touch-icon.png (180x180px)...")

# Crear imagen con fondo amarillo sólido
icon_img = Image.new('RGB', (180, 180), COLOR_YELLOW)
draw = ImageDraw.Draw(icon_img)

# Dibujar "PA" grande en el centro (iniciales)
try:
    font_icon = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 80)
except:
    font_icon = ImageFont.load_default()

icon_text = "PA"
bbox = draw.textbbox((0, 0), icon_text, font=font_icon)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_x = (180 - text_width) // 2
text_y = (180 - text_height) // 2 - 10

# Sombra para mejor legibilidad
draw.text((text_x + 2, text_y + 2), icon_text, fill=(0, 0, 0, 50), font=font_icon)
# Texto principal en blanco
draw.text((text_x, text_y), icon_text, fill=COLOR_WHITE, font=font_icon)

# Texto pequeño ".mx" debajo
try:
    font_small = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 20)
except:
    font_small = ImageFont.load_default()

mx_text = ".mx"
bbox = draw.textbbox((0, 0), mx_text, font=font_small)
mx_width = bbox[2] - bbox[0]
mx_x = (180 - mx_width) // 2
draw.text((mx_x, text_y + 70), mx_text, fill=COLOR_NAVY, font=font_small)

# Guardar como PNG optimizado
icon_img.save('apple-touch-icon.png', 'PNG', optimize=True)
file_size = os.path.getsize('apple-touch-icon.png') / 1024
print(f"   ✅ apple-touch-icon.png creado: {file_size:.1f} KB")

print("\n" + "=" * 60)
print("✅ Todas las imágenes generadas exitosamente!")
print("\nArchivos creados:")
print("  📁 images/og-image.webp      (1200x630px para redes sociales)")
print("  📁 images/logo.webp          (250x60px para Schema.org)")
print("  📁 apple-touch-icon.png      (180x180px para iOS)")
print("\n📊 Próximo paso: Validar imágenes y subir a producción")
