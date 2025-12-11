{
`command`: `cat >> /home/claude/GUIA-MAESTRA-ARTICULOS-BLOG-V2.md << 'EOF'

> 500ms (percibidas como lentas)

- ❌ Usar `all` en transition (ineficiente, afecta performance)
- ❌ Animar propiedades que causan reflow (`width`, `height`, `top`, `left`)

**PREFERIR:**

- ✅ `transform: translateX/Y/Z()` en lugar de `left/top`
- ✅ `opacity` en lugar de `visibility`
- ✅ `scale()` en lugar de `width/height`
- ✅ Propiedades específicas en transition: `transition: transform 0.3s ease, opacity 0.3s ease`

---

## 5. ESTRATEGIA SEO ON-PAGE AVANZADA

### 5.1 Research de Keywords Pre-Producción

#### 5.1.1 Metodología de Investigación

**Proceso de 5 pasos:**

**PASO 1: Identificación de Keyword Principal**

Criterios de selección:

- ✅ Volumen de búsqueda: Mínimo 500 búsquedas/mes (ideal: 1,000-10,000)
- ✅ Dificultad: Baja-Media (KD < 50 en Ahrefs/SEMrush)
- ✅ Intención de búsqueda: Alineada con contenido del artículo
- ✅ Relevancia comercial: Conecta con servicios del directorio

**Herramientas:**

- Google Keyword Planner
- Ahrefs Keywords Explorer
- SEMrush Keyword Magic Tool
- Ubersuggest

**PASO 2: Análisis de Intención de Búsqueda**

Tipos de intención:

| Intención         | Indicadores                 | Ejemplo                          | Tipo de Contenido        |
| ----------------- | --------------------------- | -------------------------------- | ------------------------ |
| **Informacional** | qué, cómo, por qué, guía    | \"qué es seguridad privada\"     | Guía educativa           |
| **Navegacional**  | nombre de marca, específico | \"Origins Private Security\"     | Página de empresa        |
| **Transaccional** | contratar, precio, mejor    | \"contratar seguridad privada\"  | Comparativa + directorio |
| **Comercial**     | comparar, vs, alternativas  | \"seguridad privada vs pública\" | Artículo comparativo     |

**PASO 3: Mapeo de Keywords Secundarias (3-5)**

Criterios:

- ✅ Relacionadas semánticamente con principal
- ✅ Long-tail (3-5 palabras)
- ✅ Complementan la narrativa del artículo
- ✅ Menor competencia que principal

**Ejemplo para \"seguridad privada México\":**

- Secundaria 1: \"empresas de seguridad privada certificadas\"
- Secundaria 2: \"guardias de seguridad profesionales\"
- Secundaria 3: \"servicios de vigilancia CDMX\"
- Secundaria 4: \"certificación CNSP México\"

**PASO 4: Extracción de LSI Keywords (8-12)**

LSI (Latent Semantic Indexing) = términos relacionados contextualmente

**Métodos de extracción:**

1. Google \"búsquedas relacionadas\" (pie de página de SERPs)
2. Google \"la gente también pregunta\" (People Also Ask)
3. LSIGraph.com
4. Análisis de top 10 competidores

**Ejemplo para \"seguridad privada\":**

- vigilancia, protección, monitoreo
- guardias, vigilantes, custodios
- CNSP, certificación, regulación
- empresas, proveedores, servicios
- residencial, corporativo, industrial

**PASO 5: Análisis Competitivo SERP**

Analizar top 10 resultados para keyword principal:

```
Datos a extraer por competidor:
- Longitud del artículo (palabras)
- Número de H2/H3
- Estructura de contenido
- Keywords en title/description
- Calidad de imágenes
- Schema implementado
- Autoridad de dominio (DA/DR)
- Backlinks a la página
```

**Output del análisis:**

- Longitud objetivo (promedio top 10 + 10-20%)
- Estructura de encabezados común
- Gaps de contenido (temas no cubiertos)
- Oportunidades de diferenciación

#### 5.1.2 Documento de Keyword Strategy

**Template obligatorio:**

```markdown
# Keyword Strategy: [Título del Artículo]

## Keyword Principal

- **Término**: [keyword principal]
- **Volumen**: [búsquedas/mes]
- **Dificultad**: [KD score]
- **Intención**: [Informacional/Transaccional/etc.]

## Keywords Secundarias (3-5)

1. [Secundaria 1] - [volumen] - [KD]
2. [Secundaria 2] - [volumen] - [KD]
3. [Secundaria 3] - [volumen] - [KD]

## LSI Keywords (8-12)

- [LSI 1]
- [LSI 2]
- [LSI 3]
  ...

## Análisis Competitivo

**Top 3 competidores:**

1. [URL] - [palabras] - DA [X] - [fortalezas/debilidades]
2. [URL] - [palabras] - DA [X] - [fortalezas/debilidades]
3. [URL] - [palabras] - DA [X] - [fortalezas/debilidades]

**Longitud objetivo**: [X] palabras
**Gaps identificados**: [Temas no cubiertos por competencia]
**Diferenciadores**: [Ángulo único de nuestro artículo]
```

### 5.2 Optimización de Title Tag Profesional

#### 5.2.1 Fórmulas Comprobadas

**Fórmula 1: Descriptor + Keyword + Geo + Marca**

```
[Tipo Contenido] de [Keyword] en [Geo] | [Marca]

Ejemplos:
✅ Guía Completa de Seguridad Privada en México | Páginas Amarillas
✅ Tutorial de Control de Acceso en CDMX | Páginas Amarillas
```

**Fórmula 2: Número + Keyword + Beneficio + Marca**

```
[#] [Keyword] para [Beneficio] | [Marca]

Ejemplos:
✅ 10 Empresas de Seguridad para Proteger tu Negocio | Páginas Amarillas
✅ 7 Tipos de Vigilancia para Condominios en México | Páginas Amarillas
```

**Fórmula 3: Cómo + Acción + Keyword + (Año)**

```
Cómo [Acción] [Keyword] [Geo/Modificador] [Año] | [Marca]

Ejemplos:
✅ Cómo Elegir Seguridad Privada Certificada 2025 | Páginas Amarillas
✅ Cómo Contratar Guardias Profesionales en CDMX | Páginas Amarillas
```

**Fórmula 4: Keyword + Comparativa/VS**

```
[Keyword A] vs [Keyword B]: [Pregunta] | [Marca]

Ejemplos:
✅ Seguridad Privada vs Pública: ¿Cuál Necesitas? | Páginas Amarillas
```

#### 5.2.2 Optimización Técnica

**Análisis de longitud:**

```
Caracteres:        50        55        60        65        70
               |---------|---------|---------|---------|---------|
Óptimo:        [================================]
Riesgo corte:                                  [===============...]
Demasiado corto: [=====]
```

**Reglas de oro:**

- ✅ **50-65 caracteres** total (incluyendo marca)
- ✅ Keyword principal en **primeras 5 palabras**
- ✅ Marca al final tras separador `|` o `-`
- ✅ Capitalización Title Case (excepto artículos/preposiciones)
- ❌ NO usar ALL CAPS
- ❌ NO usar puntuación excesiva (!!!, ???)
- ❌ NO keyword stuffing

**Testing de CTR:**

Variables a testear (si aplica):

- Uso de números vs no números
- Año actual (2025) vs sin año
- Emojis (⚡✅🔥) vs sin emojis
- Pregunta vs afirmación
- Urgencia (\"Ahora\", \"2025\") vs neutro

#### 5.2.3 Ejemplos Categorizados

**Para guías informacionales:**

```
✅ Guía Completa de [Topic] en México 2025 | Páginas Amarillas
✅ Todo sobre [Topic]: Guía Definitiva | Páginas Amarillas
✅ [Topic] en México: Qué Necesitas Saber | Páginas Amarillas
```

**Para artículos transaccionales:**

```
✅ Mejores Empresas de [Servicio] en CDMX | Páginas Amarillas
✅ Dónde Contratar [Servicio] Certificado | Páginas Amarillas
✅ [Servicio] Profesional: Precios y Opciones | Páginas Amarillas
```

**Para contenido comparativo:**

```
✅ [A] vs [B]: Comparativa Completa 2025 | Páginas Amarillas
✅ Diferencias entre [A] y [B] en México | Páginas Amarillas
```

**Para tutoriales:**

```
✅ Cómo [Acción]: Guía Paso a Paso | Páginas Amarillas
✅ [Acción] en México: Tutorial Completo | Páginas Amarillas
```

### 5.3 Meta Description Persuasiva

#### 5.3.1 Anatomía de una Meta Description Efectiva

**Estructura de 3 componentes (140-160 caracteres):**

```
[Hook/Beneficio] + [Contenido/Qué incluye] + [CTA implícito]

Ejemplo desglosado:
\"Descubre cómo elegir seguridad privada certificada. [HOOK]
Regulaciones, precios, empresas confiables y más. [CONTENIDO]
Guía completa 2025 para México.\" [CTA IMPLÍCITO]
= 158 caracteres ✅
```

**Fórmulas probadas:**

**Fórmula 1: Descubre + Lista + Guía**

```
Descubre [tema]: [beneficio 1], [beneficio 2], [beneficio 3]. Guía completa [año] para [geo].

Ejemplo:
\"Descubre seguridad privada en México: servicios, precios, certificaciones y cómo elegir la mejor empresa. Guía completa 2025 para tu negocio.\"
(159 caracteres)
```

**Fórmula 2: Aprende + Proceso + Resultado**

```
Aprende [qué hacer] en [tiempo/pasos]. [Resultado esperado]. [Autoridad/credibilidad].

Ejemplo:
\"Aprende a contratar seguridad privada en 5 pasos. Protege tu empresa con guardias certificados CNSP. Guía de expertos en México.\"
(140 caracteres)
```

**Fórmula 3: Pregunta + Respuesta + Llamado**

```
¿[Pregunta relevante]? [Respuesta breve]. [Qué encontrarás] en esta guía de [marca].

Ejemplo:
\"¿Buscas seguridad privada confiable? Compara empresas certificadas, precios y servicios. Todo lo que necesitas en Páginas Amarillas MX.\"
(148 caracteres)
```

**Fórmula 4: Estadística + Solución + Acción**

```
[Dato impactante]. [Solución que ofreces]. [Qué hacer ahora].

Ejemplo:
\"70% de empresas sufren robos sin seguridad profesional. Encuentra proveedores certificados CNSP en México. Compara y contrata hoy.\"
(142 caracteres)
```

#### 5.3.2 Principios Psicológicos

**1. Principio de Especificidad**
❌ \"Artículo sobre seguridad\"
✅ \"Guía de 10 pasos para contratar seguridad privada certificada\"

**2. Principio de Beneficio Claro**
❌ \"Información sobre extintores\"
✅ \"Protege tu negocio: cómo elegir extintores que cumplen NOM\"

**3. Principio de Urgencia/Relevancia**
❌ \"Guía de seguridad\"
✅ \"Guía completa 2025: seguridad privada en México\"

**4. Principio de Inclusión**
❌ \"Todo sobre seguridad privada\"
✅ \"Seguridad privada: tipos, precios, certificaciones, contratación\"

**5. Principio de Prueba Social Implícita**
❌ \"Encuentra empresas de seguridad\"
✅ \"Compara las mejores empresas certificadas de México\"

#### 5.3.3 Testing y Optimización

**Variables a testear:**

| Variable | Opción A               | Opción B                       | Métrica |
| -------- | ---------------------- | ------------------------------ | ------- |
| Tono     | Profesional formal     | Conversacional                 | CTR     |
| Longitud | 145 chars              | 158 chars                      | CTR     |
| Números  | \"múltiples opciones\" | \"10+ opciones\"               | CTR     |
| CTA      | Implícito              | Explícito (\"Descubre ahora\") | CTR     |
| Año      | Con \"2025\"           | Sin año                        | CTR     |

**Herramientas de preview:**

- SERP Simulator de Portent
- Yoast SEO (WordPress)
- Preview de Google Search Console

### 5.4 Optimización de URL (Slug)

#### 5.4.1 Construcción de Slug SEO-Friendly

**Proceso de creación:**

```
Título original:
\"Guía Completa de Seguridad Privada en México: Todo lo que Necesitas Saber\"

PASO 1: Extraer keywords principales
seguridad privada + México + guía

PASO 2: Eliminar stop words
de, en, todo, lo, que

PASO 3: Construir slug
guia-seguridad-privada-mexico

PASO 4: Validar longitud
27 caracteres ✅ (< 60)

Slug final:
blog/seguridad-privada/guia-seguridad-privada-mexico.html
```

**Stop words a eliminar:**

- Artículos: el, la, los, las, un, una, unos, unas
- Preposiciones: de, del, en, con, por, para, sin, sobre
- Conjunciones: y, o, pero, aunque
- Pronombres: que, qué, como, cómo
- Otros: todo, más, muy, mucho

**MANTENER si son parte de la keyword:**

- \"cómo hacer\" → `como-hacer` (keyword long-tail)
- \"paso a paso\" → `paso-a-paso` (frase común de búsqueda)

#### 5.4.2 Reglas Técnicas de Slug

**OBLIGATORIO:**

```
✅ Solo minúsculas: guia-completa
❌ Mayúsculas: Guia-Completa

✅ Guiones para separar: seguridad-privada
❌ Underscores: seguridad_privada
❌ Espacios: seguridad privada

✅ Sin acentos: mexico (no méxico)
❌ Con acentos: méxico

✅ Sin eñes: espanol (no español)
❌ Con eñes: español

✅ Sin caracteres especiales: que-es
❌ Con signos: que-es?

✅ Máximo 60 caracteres antes de .html
❌ URLs largas: guia-completa-de-seguridad-privada-en-mexico-con-empresas-certificadas.html
```

**Estructura de ruta completa:**

```
https://paginasamarillas.mx/blog/[categoria]/[slug].html

Componentes:
- Dominio: paginasamarillas.mx
- Sección: /blog/
- Categoría: /seguridad-privada/
- Slug: guia-seguridad-privada-mexico.html
```

#### 5.4.3 Ejemplos por Tipo de Contenido

**Guías:**

```
Título: \"Guía Completa de X en México\"
Slug: guia-completa-x-mexico.html
```

**Tutoriales:**

```
Título: \"Cómo Hacer X Paso a Paso\"
Slug: como-hacer-x-paso-a-paso.html
```

**Comparativas:**

```
Título: \"X vs Y: ¿Cuál es Mejor?\"
Slug: x-vs-y-comparativa.html
```

**Listas:**

```
Título: \"10 Mejores Empresas de X en CDMX\"
Slug: 10-mejores-empresas-x-cdmx.html
```

**Definiciones:**

```
Título: \"¿Qué es X y Para Qué Sirve?\"
Slug: que-es-x.html
```

### 5.5 Optimización de Encabezados (H1-H3)

#### 5.5.1 H1: Título Principal

**Reglas absolutas:**

1. ✅ **Único en la página** (solo 1 H1)
2. ✅ **Keyword principal incluida** (preferiblemente al inicio)
3. ✅ **40-70 caracteres** (legibilidad óptima)
4. ✅ **Descriptivo y claro** (promesa de valor evidente)
5. ✅ **Puede diferir del title tag** (optimización dual)

**Comparación Title vs H1:**

```
Title Tag (SEO-focused):
\"Guía de Seguridad Privada en México 2025 | Páginas Amarillas\"
(65 caracteres, incluye marca y año)

H1 (User-focused):
\"Guía Completa de Seguridad Privada en México\"
(49 caracteres, más limpio visualmente)
```

**Fórmulas para H1:**

```
Fórmula 1: [Tipo] de [Keyword] en [Geo]
Ejemplo: \"Guía Completa de Seguridad Privada en México\"

Fórmula 2: [Keyword]: [Subtítulo Descriptivo]
Ejemplo: \"Seguridad Privada: Todo lo que Necesitas Saber\"

Fórmula 3: Cómo [Acción] [Keyword] [Modificador]
Ejemplo: \"Cómo Elegir Seguridad Privada Certificada\"

Fórmula 4: [#] [Keyword] para [Beneficio]
Ejemplo: \"10 Empresas de Seguridad para Proteger tu Negocio\"
```

#### 5.5.2 H2: Secciones Principales

**Estrategia de H2:**

**Cantidad óptima:** 5-7 H2 para artículos de 2,000-3,500 palabras

**Distribución de keywords:**

```
H2 #1: Incluir keyword principal o variación
Ejemplo: \"Entendiendo la Seguridad Privada en México\"

H2 #2: Keyword secundaria o LSI
Ejemplo: \"Marco Legal y Certificación CNSP\"

H2 #3: Variación de keyword principal
Ejemplo: \"Tipos de Servicios de Seguridad Privada\"

H2 #4: Long-tail keyword (intención transaccional)
Ejemplo: \"Cómo Elegir una Empresa de Seguridad\"

H2 #5-7: Temas relacionados sin forzar keywords
Ejemplo: \"Beneficios de Invertir en Seguridad Profesional\"
```

**Balance entre SEO y Engagement:**

❌ **Títulos planos (solo SEO):**

- \"Marco Legal de Seguridad Privada\"
- \"Tipos de Servicios\"
- \"Cómo Elegir Empresa\"

✅ **Títulos conversacionales (SEO + engagement):**

- \"El Marco Legal: Más Importante de lo que Imaginas\"
- \"Los Diferentes Rostros de la Seguridad Privada\"
- \"Cómo Elegir una Empresa Sin Morir en el Intento\"

**Técnicas de copywriting para H2:**

1. **Pregunta retórica:**
   \"¿Por Qué la Seguridad Privada es Esencial?\"

2. **Beneficio implícito:**
   \"Cómo la Certificación CNSP Protege tu Inversión\"

3. **Contraste/sorpresa:**
   \"Lo que las Empresas No Te Dicen sobre Seguridad\"

4. **Especificidad:**
   \"5 Señales de que Necesitas Seguridad Profesional\"

5. **Urgencia/relevancia:**
   \"Nuevas Regulaciones 2025 que Debes Conocer\"

#### 5.5.3 H3: Sub-secciones

**Uso estratégico de H3:**

H3 debe usarse para:

1. ✅ Dividir secciones H2 muy largas (>500 palabras)
2. ✅ Introducir listas o enumeraciones
3. ✅ Destacar sub-temas específicos
4. ✅ Crear estructura en galerías/FAQs

**Ejemplo de jerarquía correcta:**

```html
<h2>Los Diferentes Rostros de la Seguridad Privada</h2>
<p>[Intro a los tipos de servicios...]</p>

<h3>Seguridad Residencial</h3>
<p>[Explicación de servicios para hogares...]</p>

<h3>Seguridad Corporativa</h3>
<p>[Explicación de servicios para empresas...]</p>

<h3>Seguridad en Eventos</h3>
<p>[Explicación de servicios temporales...]</p>
```

**PROHIBIDO (jerarquía rota):**

```html
❌
<h1>Título</h1>
<h3>Subtítulo</h3>
<!-- Saltó H2 -->

❌
<h2>Sección</h2>
<h4>Sub-sección</h4>
<!-- Saltó H3 -->
```

**Densidad de keywords en H3:**

- ✅ H3 pueden incluir keywords, pero **no forzar**
- ✅ Priorizar claridad y estructura sobre keyword stuffing
- ✅ Si keyword cabe naturalmente, incluirla

### 5.6 Densidad de Keywords y Distribución

#### 5.6.1 Fórmula de Densidad Óptima

**Cálculo:**

```
Densidad = (Número de veces que aparece keyword / Total palabras) × 100

Ejemplo:
Keyword: \"seguridad privada\"
Apariciones: 35 veces
Total palabras artículo: 2,850
Densidad = (35 / 2,850) × 100 = 1.23% ✅
```

**Rangos recomendados:**

| Tipo de Keyword | Densidad Óptima | Apariciones en 2,500 palabras |
| --------------- | --------------- | ----------------------------- |
| Principal       | 1.0% - 1.5%     | 25-37 veces                   |
| Secundaria      | 0.5% - 1.0%     | 12-25 veces                   |
| LSI (cada una)  | 0.3% - 0.7%     | 7-17 veces                    |

**⚠️ ADVERTENCIA:**

- Densidad > 2.5% = Riesgo de keyword stuffing
- Densidad < 0.5% = Insuficiente señal SEO

#### 5.6.2 Distribución Estratégica (On-Page SEO)

**Ubicaciones críticas (ponderar más):**

```
[PESO SEO: ALTO]
1. Title tag (meta title) ✅ OBLIGATORIO
2. Meta description ✅ OBLIGATORIO
3. H1 ✅ OBLIGATORIO
4. Primeras 100 palabras del artículo ✅ OBLIGATORIO
5. URL/slug ✅ OBLIGATORIO

[PESO SEO: MEDIO]
6. Al menos 1 H2 ✅ RECOMENDADO
7. Alt text de imagen hero ✅ RECOMENDADO
8. Último párrafo (conclusión) ✅ RECOMENDADO

[PESO SEO: BAJO]
9. Otros H2/H3 (natural, no forzar) ⚪ OPCIONAL
10. Anchors de enlaces internos ⚪ OPCIONAL
11. Alt text de otras imágenes ⚪ OPCIONAL
```

**Checklist de distribución:**

```
☐ Keyword principal en title tag
☐ Keyword principal en meta description
☐ Keyword principal en H1
☐ Keyword principal en primeras 100 palabras
☐ Keyword principal en URL
☐ Keyword principal o variación en mínimo 1 H2
☐ Keyword principal en imagen hero alt text
☐ Keyword principal en último párrafo/conclusión
☐ Keywords secundarias distribuidas naturalmente (2-3 veces cada una)
☐ LSI keywords integradas en contexto (5-10 veces total)
```

#### 5.6.3 Variaciones y Sinónimos (Evitar Repetición)

**Ejemplo: Keyword principal \"seguridad privada\"**

Usar variaciones naturales:

- seguridad privada ← forma exacta
- servicios de seguridad ← variación
- protección profesional ← sinónimo
- vigilancia privada ← sinónimo
- empresas de seguridad ← variación contextual
- proveedores de seguridad ← sinónimo
- guardias profesionales ← especificación

**Técnica de rotación en texto:**

```
Párrafo 1: \"La seguridad privada en México...\"
Párrafo 3: \"Los servicios de seguridad incluyen...\"
Párrafo 5: \"Contratar vigilancia privada requiere...\"
Párrafo 8: \"Las empresas de seguridad certificadas...\"
```

**PROHIBIDO (keyword stuffing):**

```
❌ \"La seguridad privada es importante. Contratar seguridad
    privada en México requiere verificar que la seguridad
    privada esté certificada. Nuestra seguridad privada...\"
```

✅ **CORRECTO (variación natural):**

```
✅ \"La seguridad privada es importante. Contratar servicios
    profesionales en México requiere verificar certificaciones.
    Los proveedores confiables cuentan con...\"
```

### 5.7 Schema.org Structured Data Avanzado

#### 5.7.1 Article Schema Completo

**Implementación profesional:**

```json
<script type=\"application/ld+json\">
{
    \"@context\": \"https://schema.org\",
    \"@type\": \"Article\",

    \"headline\": \"[Título H1 - máx 110 caracteres]\",
    \"alternativeHeadline\": \"[Subtítulo opcional]\",
    \"description\": \"[Meta description completa]\",

    \"image\": {
        \"@type\": \"ImageObject\",
        \"url\": \"https://paginasamarillas.mx/img/img-[cat]/[hero].webp\",
        \"width\": 1200,
        \"height\": 800,
        \"caption\": \"[Descripción de la imagen]\"
    },

    \"datePublished\": \"2025-11-16T10:00:00-06:00\",
    \"dateModified\": \"2025-11-16T14:30:00-06:00\",

    \"author\": {
        \"@type\": \"Organization\",
        \"name\": \"Páginas Amarillas México\",
        \"url\": \"https://paginasamarillas.mx\",
        \"logo\": {
            \"@type\": \"ImageObject\",
            \"url\": \"https://paginasamarillas.mx/img/logo.svg\",
            \"width\": 250,
            \"height\": 60
        }
    },

    \"publisher\": {
        \"@type\": \"Organization\",
        \"name\": \"Páginas Amarillas México\",
        \"url\": \"https://paginasamarillas.mx\",
        \"logo\": {
            \"@type\": \"ImageObject\",
            \"url\": \"https://paginasamarillas.mx/img/logo.svg\",
            \"width\": 250,
            \"height\": 60
        }
    },

    \"mainEntityOfPage\": {
        \"@type\": \"WebPage\",
        \"@id\": \"https://paginasamarillas.mx/blog/[cat]/[slug].html\"
    },

    \"keywords\": \"[keyword1, keyword2, keyword3, keyword4, keyword5]\",
    \"articleSection\": \"[Categoría del Blog]\",
    \"articleBody\": \"[Extracto del contenido - primeros 200 caracteres]\",

    \"wordCount\": 2850,
    \"timeRequired\": \"PT8M\",
    \"inLanguage\": \"es-MX\",
    \"isAccessibleForFree\": true,

    \"about\": {
        \"@type\": \"Thing\",
        \"name\": \"[Tema principal del artículo]\"
    }
}
</script>
```

**Análisis de propiedades:**

| Propiedad          | Obligatoria    | Descripción                           | Ejemplo                       |
| ------------------ | -------------- | ------------------------------------- | ----------------------------- |
| `headline`         | ✅ Sí          | Título principal (H1)                 | \"Guía de Seguridad Privada\" |
| `description`      | ✅ Sí          | Meta description                      | \"Guía completa sobre...\"    |
| `image`            | ✅ Sí          | Imagen destacada                      | URL completa WebP             |
| `datePublished`    | ✅ Sí          | Fecha de publicación ISO 8601         | \"2025-11-16T10:00:00-06:00\" |
| `dateModified`     | ⚪ Recomendada | Última actualización                  | \"2025-11-16T14:30:00-06:00\" |
| `author`           | ✅ Sí          | Organización autora                   | Páginas Amarillas México      |
| `publisher`        | ✅ Sí          | Publicador (mismo que author)         | Páginas Amarillas México      |
| `mainEntityOfPage` | ⚪ Recomendada | URL canónica del artículo             | URL completa                  |
| `wordCount`        | ⚪ Opcional    | Número de palabras                    | 2850                          |
| `timeRequired`     | ⚪ Opcional    | Tiempo de lectura (ISO 8601 duration) | \"PT8M\" (8 minutos)          |

**Formato de fecha ISO 8601:**

```
YYYY-MM-DDTHH:MM:SS±HH:MM

Ejemplo:
2025-11-16T10:00:00-06:00
│    │  │  │  │  │  └─ Timezone (México GMT-6)
│    │  │  │  │  └──── Segundos
│    │  │  │  └─────── Minutos
│    │  │  └────────── Horas (24h)
│    │  └───────────── Día
│    └──────────────── Mes
└───────────────────── Año
```

**Duración ISO 8601 (timeRequired):**

```
PT#M = # minutos
PT#H#M = # horas # minutos

Ejemplos:
PT5M = 5 minutos
PT8M = 8 minutos
PT1H30M = 1 hora 30 minutos
```

#### 5.7.2 FAQPage Schema (OBLIGATORIO)

**Implementación:**

```json
<script type=\"application/ld+json\">
{
    \"@context\": \"https://schema.org\",
    \"@type\": \"FAQPage\",
    \"mainEntity\": [
        {
            \"@type\": \"Question\",
            \"name\": \"¿Qué es la seguridad privada en México?\",
            \"acceptedAnswer\": {
                \"@type\": \"Answer\",
                \"text\": \"<p>La seguridad privada en México es un servicio profesional regulado por el Consejo Nacional de Seguridad Privada (CNSP) que protege personas, propiedades e información mediante vigilancia, monitoreo y protocolos especializados.</p>\"
            }
        },
        {
            \"@type\": \"Question\",
            \"name\": \"¿Cuánto cuesta contratar seguridad privada en México?\",
            \"acceptedAnswer\": {
                \"@type\": \"Answer\",
                \"text\": \"<p>Los costos varían según el tipo de servicio: vigilancia básica desde $8,000-$12,000 MXN mensuales por guardia, protección ejecutiva desde $25,000 MXN, y monitoreo electrónico desde $3,000 MXN mensuales. Los precios dependen de la zona, horarios y nivel de especialización requerido.</p>\"
            }
        },
        {
            \"@type\": \"Question\",
            \"name\": \"¿Cómo verificar que una empresa de seguridad esté certificada por CNSP?\",
            \"acceptedAnswer\": {
                \"@type\": \"Answer\",
                \"text\": \"<p>Puedes verificar la certificación CNSP de una empresa en el Registro Nacional de Empresas de Seguridad Privada (RENESP) accediendo al portal oficial de la Secretaría de Seguridad Pública. Solicita el número de registro y verifica que esté vigente. Empresas certificadas deben mostrar su registro públicamente.</p>\"
            }
        }
        // ... más preguntas (mínimo 5 total)
    ]
}
</script>
```

**Reglas de implementación:**

1. ✅ **Mínimo 5 preguntas** por artículo
2. ✅ **Text en `acceptedAnswer`** puede incluir HTML básico (`<p>`, `<strong>`, `<em>`, `<ul>`, `<li>`)
3. ✅ **Preguntas en segunda persona** (\"¿Cómo puedes...?\", \"¿Qué necesitas...?\")
4. ✅ **Respuestas completas** (2-4 oraciones, 100-200 palabras)
5. ✅ **Sincronización**: FAQ Schema debe coincidir exactamente con FAQs en HTML

**Beneficios SEO:**

- 📈 Aparición en Rich Results de Google
- 📈 Mayor espacio en SERPs (featured snippets)
- 📈 Mejor CTR (click-through rate)
- 📈 Autoridad percibida

#### 5.7.2.1 Implementación de FAQ Accordion (OBLIGATORIO)

**⚠️ IMPORTANTE**: Las FAQs deben implementarse con funcionalidad accordion/collapse para mejorar la experiencia de usuario. Los usuarios verán solo las preguntas inicialmente, y al hacer clic se desplegará la respuesta.

**Estructura HTML con Accordion:**

```html
<section class="faq-section">
    <h2>Preguntas Frecuentes</h2>

    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">
            <span>¿Qué es la seguridad privada en México?</span>
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
        </button>
        <div class="faq-answer">
            <p>La seguridad privada en México es un servicio profesional regulado por el Consejo Nacional de Seguridad Privada (CNSP) que protege personas, propiedades e información mediante vigilancia, monitoreo y protocolos especializados.</p>
        </div>
    </div>

    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">
            <span>¿Cuánto cuesta contratar seguridad privada en México?</span>
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
        </button>
        <div class="faq-answer">
            <p>Los costos varían según el tipo de servicio: vigilancia básica desde $8,000-$12,000 MXN mensuales por guardia, protección ejecutiva desde $25,000 MXN, y monitoreo electrónico desde $3,000 MXN mensuales.</p>
        </div>
    </div>

    <!-- Repetir para las 5+ preguntas -->
</section>
```

**Características clave de la estructura:**

- ✅ **`<button>` semántico** en lugar de `<h3>` o `<div>` para accesibilidad
- ✅ **`aria-expanded="false"`** para lectores de pantalla
- ✅ **Icono SVG chevron** que rota al expandir
- ✅ **`<span>` wrapper** para el texto de la pregunta
- ✅ **`.faq-answer`** contiene el contenido colapsable

**JavaScript para Accordion:**

```javascript
<script>
document.addEventListener('DOMContentLoaded', function() {
  const faqQuestions = document.querySelectorAll('.faq-question');

  faqQuestions.forEach(function(question) {
    question.addEventListener('click', function() {
      const faqItem = this.parentElement;
      const answer = faqItem.querySelector('.faq-answer');
      const isExpanded = this.getAttribute('aria-expanded') === 'true';

      // Cerrar todas las demás FAQs (comportamiento single-open)
      faqQuestions.forEach(function(q) {
        if (q !== question) {
          q.setAttribute('aria-expanded', 'false');
          q.parentElement.querySelector('.faq-answer').style.maxHeight = null;
        }
      });

      // Toggle la FAQ actual
      if (isExpanded) {
        this.setAttribute('aria-expanded', 'false');
        answer.style.maxHeight = null;
      } else {
        this.setAttribute('aria-expanded', 'true');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });
});
</script>
```

**Comportamiento del accordion:**

- ✅ **Single-open**: Solo una FAQ abierta a la vez (cierra las demás al abrir una nueva)
- ✅ **Toggle suave**: Animación con `max-height` calculado dinámicamente
- ✅ **Accesibilidad**: Actualiza `aria-expanded` en cada interacción
- ✅ **Progressive enhancement**: Si JavaScript falla, el contenido sigue siendo accesible

**CSS para Accordion:**

```css
<style>
.faq-section {
  margin: 3rem 0;
}

.faq-item {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  margin-bottom: 1rem;
  overflow: hidden;
  transition: box-shadow 0.3s ease;
}

.faq-item:hover {
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.faq-question {
  width: 100%;
  background: #fff;
  border: none;
  padding: 1.25rem 1.5rem;
  text-align: left;
  font-size: 1.1rem;
  font-weight: 600;
  color: #1f2937;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background-color 0.3s ease;
}

.faq-question:hover {
  background: #f9fafb;
}

.faq-question:focus {
  outline: 2px solid #f59e0b;
  outline-offset: -2px;
}

.faq-question span {
  flex: 1;
  padding-right: 1rem;
}

.faq-icon {
  flex-shrink: 0;
  transition: transform 0.3s ease;
  color: #6b7280;
}

.faq-question[aria-expanded="true"] {
  background: #fafafa;
}

.faq-question[aria-expanded="true"] .faq-icon {
  transform: rotate(180deg);
  color: #f59e0b;
}

.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
  background: #fafafa;
}

.faq-answer p {
  padding: 1.5rem;
  margin: 0;
  color: #4b5563;
  line-height: 1.7;
}
</style>
```

**Detalles de estilo:**

- ✅ **Bordes redondeados** (8px) para look moderno
- ✅ **Hover states** en botón y contenedor
- ✅ **Focus visible** (outline dorado) para navegación por teclado
- ✅ **Rotación de icono** 180° al expandir
- ✅ **Color dorado** (#f59e0b) en estado activo (coincide con marca)
- ✅ **Transiciones suaves** en todos los estados (0.3s)
- ✅ **Box shadow sutil** en hover para profundidad

**Accesibilidad obligatoria:**

```
☐ Usar <button> (no <div> con onclick)
☐ Atributo aria-expanded actualizado dinámicamente
☐ Navegación por teclado funcional (Tab, Enter, Space)
☐ Focus visible con outline claro
☐ Color de contraste adecuado (WCAG AA mínimo)
☐ Texto legible sin JavaScript activado
```

**Testing de implementación:**

```
☐ Probar en Chrome, Firefox, Safari
☐ Probar en móvil (iOS y Android)
☐ Verificar animación suave sin lag
☐ Confirmar que solo una FAQ abre a la vez
☐ Validar navegación con teclado
☐ Probar con lector de pantalla (NVDA/VoiceOver)
☐ Verificar comportamiento si JavaScript está deshabilitado
```

**⚠️ NOTA IMPORTANTE**: Este accordion debe implementarse en TODOS los artículos nuevos. No es opcional. La experiencia de usuario mejorada y el engagement son críticos para el rendimiento SEO.

#### 5.7.3 BreadcrumbList Schema

**Implementación:**

```json
<script type=\"application/ld+json\">
{
    \"@context\": \"https://schema.org\",
    \"@type\": \"BreadcrumbList\",
    \"itemListElement\": [
        {
            \"@type\": \"ListItem\",
            \"position\": 1,
            \"name\": \"Inicio\",
            \"item\": \"https://paginasamarillas.mx/\"
        },
        {
            \"@type\": \"ListItem\",
            \"position\": 2,
            \"name\": \"Blog\",
            \"item\": \"https://paginasamarillas.mx/blog/\"
        },
        {
            \"@type\": \"ListItem\",
            \"position\": 3,
            \"name\": \"Seguridad Privada\",
            \"item\": \"https://paginasamarillas.mx/categoria/seguridad-privada.html\"
        },
        {
            \"@type\": \"ListItem\",
            \"position\": 4,
            \"name\": \"Guía Completa de Seguridad Privada\",
            \"item\": \"https://paginasamarillas.mx/blog/seguridad-privada/guia-completa.html\"
        }
    ]
}
</script>
```

**⚠️ NOTA**: Este Schema debe coincidir exactamente con los breadcrumbs visibles en HTML (sección 3.1.3).

### 5.8 Open Graph Completo

**Implementación exhaustiva:**

```html
<!-- Open Graph Básico -->
<meta property=\"og:type\" content=\"article\"> <meta property=\"og:title\"
content=\"[Título del artículo - puede diferir de meta title]\"> <meta
property=\"og:description\" content=\"[Descripción persuasiva - puede diferir de
meta description]\"> <meta property=\"og:url\"
content=\"https://paginasamarillas.mx/blog/[cat]/[slug].html\"> <meta
property=\"og:site_name\" content=\"Páginas Amarillas México\"> <meta
property=\"og:locale\" content=\"es_MX\">

<!-- Open Graph Imagen -->
<meta property=\"og:image\"
content=\"https://paginasamarillas.mx/img/img-[cat]/[og-image].jpg\"> <meta
property=\"og:image:secure_url\"
content=\"https://paginasamarillas.mx/img/img-[cat]/[og-image].jpg\"> <meta
property=\"og:image:type\" content=\"image/jpeg\"> <meta
property=\"og:image:width\" content=\"1200\"> <meta property=\"og:image:height\"
content=\"630\"> <meta property=\"og:image:alt\" content=\"[Descripción de la
imagen OG]\">

<!-- Open Graph Article (específico para artículos) -->
<meta property=\"article:published_time\" content=\"2025-11-16T10:00:00-06:00\">
<meta property=\"article:modified_time\" content=\"2025-11-16T14:30:00-06:00\">
<meta property=\"article:author\" content=\"https://paginasamarillas.mx/about\">
<meta property=\"article:section\" content=\"Seguridad Privada\"> <meta
property=\"article:tag\" content=\"seguridad privada\"> <meta
property=\"article:tag\" content=\"CNSP\"> <meta property=\"article:tag\"
content=\"guardias de seguridad\">

<!-- Twitter Card -->
<meta name=\"twitter:card\" content=\"summary_large_image\"> <meta
name=\"twitter:site\" content=\"@PaginasAmarillas\"> <meta
name=\"twitter:creator\" content=\"@PaginasAmarillas\"> <meta
name=\"twitter:title\" content=\"[Título del artículo]\"> <meta
name=\"twitter:description\" content=\"[Descripción]\"> <meta
name=\"twitter:image\"
content=\"https://paginasamarillas.mx/img/img-[cat]/[twitter-image].jpg\"> <meta
name=\"twitter:image:alt\" content=\"[Descripción imagen]\">
```

**Especificaciones de imagen OG:**

| Requisito   | Valor           | Justificación                  |
| ----------- | --------------- | ------------------------------ |
| Dimensiones | 1200×630 px     | Estándar Facebook/LinkedIn     |
| Ratio       | 1.91:1          | Óptimo para preview            |
| Formato     | JPG o PNG       | Compatibilidad universal       |
| Peso máximo | 300 KB          | Performance                    |
| Contenido   | Título + visual | Legibilidad en preview pequeño |

**Testing obligatorio:**

Validar en:

- Facebook Sharing Debugger: https://developers.facebook.com/tools/debug/
- Twitter Card Validator: https://cards-dev.twitter.com/validator
- LinkedIn Post Inspector: https://www.linkedin.com/post-inspector/

### 5.9 Enlaces Internos Estratégicos

#### 5.9.1 Estrategia de Linking Interno

**Objetivos:**

1. **SEO**: Distribuir PageRank interno (link juice)
2. **UX**: Facilitar navegación y descubrimiento de contenido
3. **Conversión**: Dirigir tráfico hacia páginas comerciales (directorio)
4. **Engagement**: Aumentar tiempo en sitio, reducir bounce rate

**Arquitectura de enlaces:**

```
Artículo de Blog
    │
    ├─ Enlaces a Empresas del Directorio (3-5)
    │   ├─ Anchor text: Nombre de empresa
    │   └─ Contexto: Mencionadas como ejemplo de caso de éxito
    │
    ├─ Enlaces a Categorías (1-2)
    │   ├─ Anchor text: \"empresas de [categoría]\", \"[categoría] certificadas\"
    │   └─ Contexto: Recomendación de explorar directorio
    │
    ├─ Enlaces a Otros Artículos del Blog (2-3)
    │   ├─ Anchor text: Título del artículo o variación
    │   └─ Contexto: \"También te puede interesar\", \"Profundiza en este tema\"
    │
    └─ Enlace a Página Principal (1)
        ├─ Breadcrumb
        └─ Logo header
```

**Densidad recomendada:**

```
Artículo de 2,500 palabras = 8-12 enlaces internos totales

Distribución:
- Empresas directorio: 40% (3-5 enlaces)
- Categorías: 15% (1-2 enlaces)
- Otros artículos: 30% (2-3 enlaces)
- Navegación global: 15% (breadcrumb, menú)
```

#### 5.9.2 Anchor Text Optimization

**Tipos de anchor text:**

| Tipo                   | Ejemplo                                  | Uso                          | SEO Value  |
| ---------------------- | ---------------------------------------- | ---------------------------- | ---------- |
| **Exact match**        | \"seguridad privada México\"             | Moderado (1-2 por artículo)  | Alto       |
| **Partial match**      | \"empresas de seguridad certificadas\"   | Frecuente                    | Medio-Alto |
| **Branded**            | \"Origins Private Security\"             | Para empresas del directorio | Medio      |
| **Generic**            | \"haz clic aquí\"                        | ❌ Evitar                    | Bajo       |
| **Natural/Contextual** | \"proveedores confiables de vigilancia\" | Preferido                    | Medio-Alto |
| **Título de artículo** | \"Cómo Elegir Extintores Certificados\"  | Para artículos relacionados  | Medio      |

**Distribución recomendada:**

```
En artículo de 2,500 palabras con 10 enlaces:

1x Exact match (keyword principal)
3x Partial match (variaciones de keyword)
3x Branded (nombres de empresas)
3x Natural/Contextual (descriptivos)
0x Generic (nunca usar)
```

**Ejemplos contextuales:**

❌ **MALO (generic anchor text):**

```
\"Si quieres saber más sobre certificaciones, haz clic aquí.\"
```

✅ **BUENO (natural, descriptivo):**

```
\"La certificación CNSP es obligatoria para operar legalmente
en México. Empresas como Origins Private Security cuentan con
todas las acreditaciones necesarias para garantizar
un servicio profesional.\"
```

#### 5.9.3 Atributos de Enlaces

**Enlaces internos (mismo dominio):**

```html
<!-- Estándar (mayoría) -->
<a href=\"/blog/categoria/articulo.html\">Anchor text</a>

<!-- Con title (accesibilidad) -->
<a href=\"/categoria/empresas.html\"
   title=\"Ver empresas certificadas de seguridad privada\">
   empresas certificadas
</a>
```

**NO usar en internos:**

- ❌ `target=\"_blank\"` (confunde navegación)
- ❌ `rel=\"nofollow\"` (bloquea PageRank)

**Enlaces externos:**

```html
<a href=\"https://sitioexterno.com\"
   target=\"_blank\"
   rel=\"noopener noreferrer\">
   Anchor text
</a>
```

**Atributos obligatorios externos:**

- ✅ `target=\"_blank\"` (abre en nueva pestaña)
- ✅ `rel=\"noopener\"` (seguridad, evita window.opener)
- ✅ `rel=\"noreferrer\"` (privacidad, no envía referrer)
- ⚪ `rel=\"nofollow\"` (opcional, si no quieres pasar PageRank)

#### 5.9.4 Colocación Estratégica

**Ubicaciones de alto valor:**

1. **Primeros párrafos** (above the fold)

   - Mayor tasa de click
   - Señal de relevancia temprana

2. **Dentro de listas/enumeraciones**

   - Escaneabilidad alta
   - Contexto claro

3. **Módulos de interés** (highlights)

   - Visualmente destacados
   - Atención enfocada

4. **Conclusión/último párrafo**
   - Natural call-to-action
   - Usuarios comprometidos

**Ubicaciones de bajo valor:**

- ❌ Pie de página (percibido como spam)
- ❌ Sidebar excesivo (banner blindness)
- ❌ Inicio de todos los párrafos (patrón artificial)

---

## 6. METODOLOGÍA DE PRODUCCIÓN DE CONTENIDO

### 6.1 Brief Editorial y Análisis Inicial

#### 6.1.1 Template de Brief

**Documento de entrada (proporcionado por cliente/editor):**

```markdown
# BRIEF EDITORIAL - [Título Tentativo]

## Información Básica

- **Categoría**: [Seguridad Privada / Entretenimiento / etc.]
- **Keyword Principal**: [keyword objetivo]
- **Fecha de entrega**: [YYYY-MM-DD]
- **Prioridad**: [Alta / Media / Baja]

## Audiencia Objetivo

- **Perfil**: [B2B empresas / B2C hogares / Mixto]
- **Nivel de conocimiento**: [Principiante / Intermedio / Experto]
- **Pain point principal**: [Problema que resuelve el artículo]

## Objetivos del Artículo

1. [Objetivo 1: ej. Educar sobre regulaciones CNSP]
2. [Objetivo 2: ej. Generar tráfico para categoría del directorio]
3. [Objetivo 3: ej. Posicionar keyword principal en top 10]

## Enfoque/Ángulo

[Descripción del enfoque único del artículo, qué lo diferencia
de la competencia]

## Referencias

- URL competidor 1: [link]
- URL competidor 2: [link]
- Fuentes oficiales: [links a fuentes autorizadas]

## Contenido a Incluir (Obligatorio)

- [Tema/sección específica 1]
- [Tema/sección específica 2]
- [Estadísticas/datos duros]

## Enlaces Internos Sugeridos

- [URL empresa 1 del directorio]
- [URL categoría relevante]
- [URL artículo relacionado existente]

## Material de Apoyo

- [Imágenes proporcionadas: sí/no]
- [Infografías: sí/no]
- [Entrevistas a realizar: sí/no]
```

#### 6.1.2 Análisis del Brief (Checklist)

**Redactor debe validar:**

```
☐ Brief leído completamente (2 lecturas)
☐ Keyword principal identificada y validada (herramientas SEO)
☐ Audiencia objetivo comprendida
☐ Pain point claro
☐ Objetivos realistas y medibles
☐ Enfoque diferenciador definido
☐ Competidores analizados (top 10 SERPs)
☐ Fuentes de información identificadas y accesibles
☐ Material de apoyo disponible o plan para crearlo
☐ Deadline factible
```

**Red flags que requieren aclaración:**

- ⚠️ Keyword con volumen < 100 búsquedas/mes
- ⚠️ Keyword con dificultad > 70 (muy competitiva)
- ⚠️ Audiencia no claramente definida
- ⚠️ Enfoque genérico sin diferenciación
- ⚠️ Deadline < 3 días para artículo complejo

### 6.2 Investigación y Curación de Fuentes

#### 6.2.1 Tipos de Fuentes Confiables

**Jerarquía de autoridad:**

```
NIVEL 1 - Máxima Autoridad (Preferir siempre):
├─ Gobierno: Secretarías, CNSP, STPS, organismos oficiales
├─ Instituciones: Universidades, centros de investigación
├─ Normativas: NOMs, leyes federales, reglamentos
└─ Estadísticas oficiales: INEGI, Bancos de México

NIVEL 2 - Alta Autoridad:
├─ Asociaciones de industria: Cámaras, federaciones
├─ Medios especializados: Publicaciones de industria
├─ Empresas líderes: Informes corporativos, white papers
└─ Expertos reconocidos: Entrevistas, columnas

NIVEL 3 - Autoridad Moderada (Validar):
├─ Medios generalistas: Periódicos, revistas
├─ Blogs especializados: Con trayectoria comprobable
└─ Redes sociales: Solo para tendencias, no como fuente principal

NIVEL 4 - Baja Autoridad (Evitar):
├─ Wikipedia (usar solo como punto de partida)
├─ Foros/Yahoo Answers
└─ Sitios sin autor identificable
```

#### 6.2.2 Validación de Fuentes (Método CRAAP)

**CRAAP Test:**

| Criterio                   | Preguntas a Validar                             | Acción                                  |
| -------------------------- | ----------------------------------------------- | --------------------------------------- |
| **Currency** (Actualidad)  | ¿Cuándo se publicó? ¿Está actualizado?          | Preferir < 2 años                       |
| **Relevance** (Relevancia) | ¿Es relevante para el tema? ¿Para la audiencia? | Debe ser específico                     |
| **Authority** (Autoridad)  | ¿Quién es el autor? ¿Credenciales?              | Verificar expertise                     |
| **Accuracy** (Precisión)   | ¿Datos verificables? ¿Referencias?              | Contrastar con otras fuentes            |
| **Purpose** (Propósito)    | ¿Informar o vender? ¿Sesgos?                    | Evitar fuentes con conflicto de interés |

**Checklist de fuente confiable:**

```
☐ Autor identificable con credenciales verificables
☐ Fecha de publicación visible y reciente (< 2 años ideal)
☐ Organización/institución respaldatoria reconocida
☐ Datos con referencias a fuentes primarias
☐ Sin conflictos de interés evidentes
☐ Coincide con información de otras fuentes (triangulación)
☐ Formato profesional (no blog personal amateur)
```

#### 6.2.3 Documentación de Fuentes

**Sistema de registro:**

```markdown
## Fuentes Utilizadas - [Título del Artículo]

### Fuentes Primarias

1. **[Título/Nombre de documento]**

   - URL: [link completo]
   - Autor/Organización: [nombre]
   - Fecha: [YYYY-MM-DD]
   - Dato extraído: [cita o dato específico]
   - Ubicación en artículo: [sección donde se usa]

2. **[Siguiente fuente]**
   ...

### Fuentes Secundarias

[Mismo formato]

### Imágenes/Multimedia

- Imagen 1: [URL] - Licencia: [CC BY, dominio público, etc.]
- Imagen 2: [URL] - Licencia: [...]
```

**⚠️ IMPORTANTE**: Guardar este documento junto al artículo para futuras actualizaciones o auditorías.

### 6.3 Creación del Outline (Esquema)

#### 6.3.1 Metodología de Estructuración

**Proceso de 7 pasos:**

**PASO 1: Brainstorming de H2**

Listado libre de todos los H2 posibles:

```
- ¿Qué es seguridad privada?
- Marco legal en México
- Tipos de servicios
- Cómo elegir empresa
- Costos y presupuesto
- Certificaciones necesarias
- Beneficios vs seguridad pública
- Tendencias futuras
- Casos de éxito
- Errores comunes
- FAQ
- Conclusión
```

**PASO 2: Agrupación Temática**

Agrupar H2 relacionados:

```
GRUPO 1 - Fundamentos:
- ¿Qué es seguridad privada?
- Marco legal en México

GRUPO 2 - Oferta de servicios:
- Tipos de servicios
- Certificaciones necesarias

GRUPO 3 - Proceso de selección:
- Cómo elegir empresa
- Costos y presupuesto
- Errores comunes

GRUPO 4 - Valor:
- Beneficios vs seguridad pública
- Casos de éxito

GRUPO 5 - Futuro y cierre:
- Tendencias futuras
- Conclusión
- FAQ
```

**PASO 3: Priorización (Top 5-7 H2)**

Seleccionar los H2 esenciales:

```
H2 #1: Entendiendo la Seguridad Privada en México
H2 #2: El Marco Legal: Más Importante de lo que Imaginas
H2 #3: Los Diferentes Rostros de la Seguridad Privada
H2 #4: Cómo Elegir una Empresa Sin Morir en el Intento
H2 #5: Por Qué Vale la Pena Invertir en Seguridad
H2 #6: Hacia Dónde Va la Industria
H2 #7: Reflexión Final
H2 #8: Preguntas Frecuentes
```

**PASO 4: Añadir H3 donde aplique**

Expandir H2 complejos:

```
H2 #3: Los Diferentes Rostros de la Seguridad Privada
   H3: Seguridad Residencial
   H3: Seguridad Corporativa
   H3: Seguridad en Eventos
   H3: Protección Ejecutiva
```

**PASO 5: Asignar Longitudes Objetivo**

```
H1 + Lead: 200 palabras
H2 #1: 400 palabras
H2 #2: 450 palabras (incluye módulo de interés)
H2 #3: 500 palabras (incluye 4 H3 de 100 palabras cada uno + galería)
H2 #4: 400 palabras
H2 #5: 350 palabras (incluye módulo de interés)
H2 #6: 300 palabras (incluye módulo de interés)
H2 #7: 250 palabras
H2 #8 (FAQs): 500 palabras (5 FAQs de 100 palabras c/u)

TOTAL ESTIMADO: 3,350 palabras ✅
```

**PASO 6: Marcar Ubicación de Elementos Especiales**

```
- Imagen hero: Tras H1
- Galería: En H2 #3 (servicios)
- Módulo interés 1: Tras H2 #2 (marco legal)
- Módulo interés 2: En H2 #5 (beneficios)
- Módulo interés 3: Antes de H2 #7 (conclusión)
- Enlaces internos: 2 en H2 #3, 2 en H2 #4, 1 en conclusión
```

**PASO 7: Validar con Competencia**

Comparar con top 3 competidores:

```
Competidor 1: 8 H2, 2,900 palabras
Competidor 2: 7 H2, 3,200 palabras
Competidor 3: 6 H2, 2,500 palabras

Nuestro outline: 8 H2, ~3,350 palabras ✅ (superior al promedio)
```

#### 6.3.2 Template de Outline Completo

```markdown
# OUTLINE: [Título del Artículo]

**Keyword Principal**: [keyword]
**Longitud Objetivo**: 3,000-3,500 palabras
**Fecha de Inicio**: [YYYY-MM-DD]

---

## H1: [Título Principal]

**Palabras**: 50-100
**Elementos**: Título H1 único

## LEAD PARAGRAPH (Clase .lead)

**Palabras**: 100-150
**Elementos**:

- Hook emocional
- Promesa de valor
- Keyword principal incluida

---

## H2 #1: [Título Sección 1]

**Palabras**: 400
**Keywords**: [keyword secundaria o LSI]
**Contenido**:

- Punto clave 1
- Punto clave 2
- Ejemplo concreto

**Elementos especiales**: Ninguno

---

## H2 #2: [Título Sección 2]

**Palabras**: 450
**Keywords**: [keyword secundaria]
**Contenido**:

- Sub-tema A
- Sub-tema B
- Estadística relevante

**Elementos especiales**:

- 💡 Módulo de interés (estadística/dato duro)

---

## H2 #3: [Título Sección 3]

**Palabras**: 500
**Keywords**: [variación keyword principal]
**Estructura**:

### H3: [Sub-sección A]

- Contenido A (100 palabras)

### H3: [Sub-sección B]

- Contenido B (100 palabras)

### H3: [Sub-sección C]

- Contenido C (100 palabras)

### H3: [Sub-sección D]

- Contenido D (100 palabras)

**Elementos especiales**:

- Galería de 4 imágenes (tras H3s)
- 2 enlaces internos a empresas del directorio

---

## H2 #4: [Título Sección 4 - Guía Práctica]

**Palabras**: 400
**Keywords**: [long-tail transaccional]
**Contenido**:

- Checklist de criterios (lista ordenada)
- Proceso paso a paso
- Errores comunes a evitar

**Elementos especiales**:

- Lista numerada (6-8 items)
- 2 enlaces internos

---

## H2 #5: [Título Sección 5 - Beneficios]

**Palabras**: 350
**Keywords**: [LSI keywords]
**Contenido**:

- Beneficio 1 (ROI)
- Beneficio 2 (Seguridad/tranquilidad)
- Beneficio 3 (Compliance/legal)

**Elementos especiales**:

- ✅ Módulo de interés (tip práctico)

---

## H2 #6: [Título Sección 6 - Futuro/Tendencias]

**Palabras**: 300
**Keywords**: [keywords de tendencias]
**Contenido**:

- Tendencia 1 (tecnología)
- Tendencia 2 (regulaciones)
- Recomendación prospectiva

**Elementos especiales**:

- 📌 Módulo de interés (prospectiva)

---

## H2 #7: Reflexión Final

**Palabras**: 250
**Contenido**:

- Resumen de puntos clave (bullet points)
- Call to action (visitar directorio)
- Cierre inspirador

**Elementos especiales**:

- 1 enlace a categoría del directorio

---

## H2 #8: Preguntas Frecuentes

**Palabras**: 500 (5 FAQs × 100 palabras c/u)
**Estructura**:

1. ¿[Pregunta 1]?
   - Respuesta (100 palabras)
2. ¿[Pregunta 2]?
   - Respuesta (100 palabras)
3. ¿[Pregunta 3]?
   - Respuesta (100 palabras)
4. ¿[Pregunta 4]?
   - Respuesta (100 palabras)
5. ¿[Pregunta 5]?
   - Respuesta (100 palabras)

**Elementos especiales**:

- Schema FAQPage JSON-LD (obligatorio)

---

## RESUMEN DE ELEMENTOS

- **Total palabras**: ~3,350
- **Total H2**: 8
- **Total H3**: 4 (en H2 #3)
- **Módulos de interés**: 3
- **Galería de imágenes**: 1 (4 imágenes)
- **Enlaces internos**: Mínimo 5
- **FAQs**: 5 con Schema

---

## CHECKLIST PRE-REDACCIÓN

☐ Outline revisado por editor
☐ Keywords validadas con herramientas
☐ Longitud total ~3,000+ palabras
☐ Mínimo 5 H2 (sin contar FAQs)
☐ Enlaces internos planificados
☐ Módulos de interés ubicados
☐ FAQs definidas
☐ Fuentes de información identificadas
```

### 6.4 Redacción Profesional

#### 6.4.1 Principios de Estilo Editorial

**1. Tono y Voz (Voice & Tone)**

**Características obligatorias:**

- ✅ **Segunda persona** (tú/usted) de forma consistente
- ✅ **Conversacional pero profesional** (como asesor experto)
- ✅ **Autoridad sin arrogancia** (conocimiento compartido, no impuesto)
- ✅ **Empatía con el lector** (reconocer sus problemas/dudas)
- ✅ **Claridad sobre sofisticación** (explicar términos técnicos)

**Ejemplos de tono correcto:**

✅ **Bueno - Conversacional y profesional:**

```
\"Cuando buscas un proveedor de seguridad privada, la primera
pregunta que surge es: ¿cómo sé que es confiable? La respuesta
está en las certificaciones. El CNSP (Consejo Nacional de Seguridad
Privada) es el organismo que regula esta industria en México,
y verificar que una empresa esté registrada es más fácil de lo
que imaginas.\"
```

❌ **Malo - Demasiado formal/corporativo:**

```
\"La identificación de un proveedor de servicios de seguridad
privada confiable requiere la verificación de credenciales emitidas
por el organismo regulador competente, a saber, el Consejo Nacional
de Seguridad Privada (CNSP).\"
```

❌ **Malo - Demasiado casual/informal:**

```
\"Oye, ¿quieres saber cómo encontrar una empresa de seguridad
chida? Pues resulta que hay un rollo del CNSP que te ayuda
un chorro. ¡Es súper fácil!\"
```

**2. Estructura de Párrafos**

**Reglas de oro:**

```
Longitud óptima: 80-150 palabras
Oraciones por párrafo: 3-6
Palabras por oración: 15-25 (promedio)

Estructura interna:
1. Oración principal (tesis del párrafo)
2. Oraciones de soporte (2-4)
3. Oración de transición (conecta con siguiente párrafo)
```

**Ejemplo de párrafo bien estructurado:**

```
[ORACIÓN PRINCIPAL]
La certificación CNSP no es un simple trámite burocrático:
es tu principal garantía de que estás contratando un servicio
profesional y legal.

[SOPORTE 1]
Empresas certificadas han pasado por auditorías que verifican
desde la capacitación de su personal hasta la legalidad de sus
equipos de comunicación.

[SOPORTE 2]
Además, están sujetas a supervisión constante, lo que significa
que mantienen estándares de calidad año con año.

[TRANSICIÓN]
Pero verificar la certificación es solo el primer paso en tu
proceso de selección.

[ANÁLISIS]
- Palabras totales: 85 ✅
- Oraciones: 4 ✅
- Palabras por oración: 21 promedio ✅
- Transición al siguiente tema: ✅
```

**3. Uso de Ejemplos Concretos**

**Principio**: \"Show, don't tell\"

❌ **Malo - Abstracto:**

```
\"La seguridad privada ofrece múltiples beneficios para las empresas.\"
```

✅ **Bueno - Específico:**

```
\"Una empresa de logística en CDMX redujo sus pérdidas por robo
en 87% tras contratar vigilancia 24/7. En seis meses, el ahorro
superó el costo anual del servicio.\"
```

**Tipos de ejemplos efectivos:**

- Estadísticas específicas (87%, no \"la mayoría\")
- Casos de uso reales (empresa de logística)
- Números concretos (6 meses, costo anual)
- Comparativas antes/después

**4. Transiciones Suaves**

**Palabras y frases de transición:**

| Función          | Palabras/Frases                                             |
| ---------------- | ----------------------------------------------------------- |
| **Añadir info**  | Además, Asimismo, Por otro lado, También                    |
| **Contrastar**   | Sin embargo, No obstante, A diferencia de, Por el contrario |
| **Causa-efecto** | Por lo tanto, Como resultado, Debido a, Por esta razón      |
| **Secuencia**    | Primero, Luego, Finalmente, A continuación                  |
| **Ejemplificar** | Por ejemplo, Como es el caso de, Específicamente            |
| **Concluir**     | En resumen, Para concluir, Finalmente, En definitiva        |

**Ejemplo de transiciones fluidas:**

```
[PÁRRAFO 1 - Problema]
\"Las pequeñas empresas a menudo subestiman la importancia
de la seguridad profesional. [...]\"

[TRANSICIÓN]
Sin embargo, esta percepción cambia radicalmente tras el
primer incidente.

[PÁRRAFO 2 - Solución]
\"La prevención siempre es más económica que la reacción. [...]\"
```

#### 6.4.2 Técnicas de Engagement

**1. Preguntas Retóricas**

Uso estratégico:

- Inicio de secciones H2 (genera curiosidad)
- Antes de revelar información importante
- Para validar experiencia del lector

**Ejemplos:**

```
\"¿Alguna vez te has preguntado por qué algunas empresas de
seguridad cobran el doble que otras?\"
→ [Respuesta en párrafo siguiente]

\"¿Tu proveedor actual tiene certificación CNSP vigente?
Si no lo sabes con certeza, es momento de verificarlo.\"
→ [Call to action implícito]
```

**⚠️ Precaución**: No abusar (máximo 2-3 por artículo de 3,000 palabras)

**2. Listas y Enumeraciones**

**Cuándo usar listas:**

- ✅ Enumeraciones de 3+ items
- ✅ Pasos de un proceso
- ✅ Criterios de selección
- ✅ Checklist

**Formato de listas:**

```html
<!-- Lista ordenada (secuencia importa) -->
<ol>
  <li>Verifica certificación CNSP en registro oficial</li>
  <li>Solicita referencias de clientes actuales</li>
  <li>Revisa pólizas de seguro y garantías</li>
  <li>Compara propuestas de mínimo 3 proveedores</li>
</ol>

<!-- Lista desordenada (sin secuencia) -->
<ul>
  <li>Vigilancia 24/7 en instalaciones</li>
  <li>Monitoreo electrónico con CCTV</li>
  <li>Control de acceso biométrico</li>
  <li>Patrullaje perimetral</li>
</ul>
```

**3. Datos y Estadísticas**

**Reglas de uso:**

```
✅ Siempre citar fuente:
\"Según el INEGI, 70% de las empresas en México han sufrido
algún tipo de robo (Encuesta Nacional de Seguridad Pública
Urbana, 2024).\"

✅ Usar números específicos:
\"87%\" en lugar de \"la gran mayoría\"
\"6 meses\" en lugar de \"poco tiempo\"

✅ Contextualizar:
\"$12,000 MXN mensuales por guardia (aproximadamente $400 USD)\"
```

**Fuentes confiables para estadísticas México:**

- INEGI (Instituto Nacional de Estadística y Geografía)
- Secretaría de Seguridad y Protección Ciudadana
- Banxico (datos económicos)
- Cámaras de comercio e industria

#### 6.4.3 Optimización de Legibilidad

**Herramientas de medición:**

| Herramienta              | Métrica                 | Objetivo                |
| ------------------------ | ----------------------- | ----------------------- |
| **Hemingway Editor**     | Grado de lectura        | Grado 9-10 (secundaria) |
| **Flesch Reading Ease**  | Score 0-100             | 60-70 (estándar)        |
| **Flesch-Kincaid Grade** | Nivel escolar           | 9-10                    |
| **Yoast SEO**            | Análisis de legibilidad | Verde (bueno)           |

**Principios de legibilidad:**

**1. Oraciones cortas:**

```
❌ Malo (42 palabras):
\"La seguridad privada en México, que está regulada por el Consejo
Nacional de Seguridad Privada (CNSP), requiere que todas las empresas
que ofrecen estos servicios cuenten con un registro oficial que
garantice que cumplen con los estándares mínimos de calidad y
profesionalismo establecidos por la autoridad competente.\"

✅ Bueno (3 oraciones, 15 palabras promedio):
\"La seguridad privada en México está regulada por el CNSP. Todas
las empresas deben contar con registro oficial. Este requisito
garantiza estándares mínimos de calidad y profesionalismo.\"
```

**2. Voz activa sobre pasiva:**

```
❌ Pasiva:
\"Las regulaciones son establecidas por el CNSP.\"

✅ Activa:
\"El CNSP establece las regulaciones.\"
```

**3. Evitar jerga innecesaria:**

```
❌ Con jerga:
\"El sistema implementa protocolos de failover redundantes con
alta disponibilidad mediante clustering activo-pasivo.\"

✅ Claro:
\"El sistema cuenta con respaldo automático: si un componente
falla, otro toma su lugar inmediatamente sin interrumpir el servicio.\"
```

**4. Palabras de transición (30% mínimo):**

- Hemingway Editor marca en verde los párrafos con buenas transiciones
- Objetivo: Mínimo 30% de párrafos con palabras de transición

**5. Distribución de oraciones:**

```
Ideal por párrafo:
- 0-1 oraciones muy cortas (< 10 palabras)
- 2-3 oraciones medias (10-20 palabras)
- 1-2 oraciones largas (20-30 palabras)
- 0 oraciones muy largas (> 30 palabras)
```

### 6.5 Integración de Keywords Naturales

#### 6.5.1 Técnica de Variación Semántica

**Evitar repetición mecánica:**

❌ **Keyword stuffing (detectado como spam):**

```
\"La seguridad privada es importante. Contratar seguridad privada
requiere investigación. Las empresas de seguridad privada ofrecen
servicios de seguridad privada variados. Si buscas seguridad
privada profesional...\"
```

✅ **Variación natural:**

```
\"La seguridad privada es importante. Contratar este servicio
requiere investigación. Los proveedores profesionales ofrecen
soluciones variadas. Si buscas protección confiable para tu
negocio...\"
```

**Banco de variaciones (ejemplo: \"seguridad privada\"):**

| Uso # | Variación                | Contexto                                       |
| ----- | ------------------------ | ---------------------------------------------- |
| 1     | seguridad privada        | Primera mención (keyword exacta)               |
| 2     | este servicio            | Referencia cercana                             |
| 3     | proveedores de seguridad | Mención de empresas                            |
| 4     | vigilancia profesional   | Servicio específico                            |
| 5     | protección privada       | Sinónimo                                       |
| 6     | empresas especializadas  | Genérico                                       |
| 7     | seguridad privada        | Repetición estratégica (cada 300-400 palabras) |
| 8     | soluciones de protección | Variante                                       |

#### 6.5.2 Ubicaciones Estratégicas (Repaso)

**Checklist de ubicación obligatoria:**

```
☐ Title tag (meta title)
☐ Meta description
☐ H1
☐ Primeras 100 palabras
☐ URL/slug
☐ Mínimo 1 H2
☐ Alt text imagen hero
☐ Último párrafo/conclusión
☐ Distribuido naturalmente en cuerpo (densidad 1-1.5%)
```

#### 6.5.3 LSI Keywords en Contexto

**Integración de LSI sin forzar:**

```
Keyword principal: \"seguridad privada\"

LSI keywords a incluir:
- vigilancia, guardias, monitoreo
- protección, custodia, resguardo
- CNSP, certificación, regulación
- empresas, proveedores, servicios
- residencial, corporativo, eventos

Integración natural:
\"Los servicios de seguridad privada en México abarcan desde
vigilancia residencial hasta protección corporativa compleja.
Las empresas certificadas por el CNSP ofrecen guardias capacitados,
monitoreo electrónico 24/7 y protocolos de resguardo adaptados
a cada sector.\"

[Análisis]
Keyword principal: 1 vez ✅
LSI incluidos: vigilancia, protección, empresas, certificadas,
               CNSP, guardias, monitoreo, resguardo ✅
Densidad natural: ✅
Lectura fluida: ✅
```
