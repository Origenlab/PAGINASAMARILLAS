#!/usr/bin/env python3
"""
Extrae las 18 fichas HTML de negocios -> Markdown + frontmatter tipado.
Fuente:  public/negocios/{categoria}/{slug}.html
Destino: src/content/negocios/{categoria}/{slug}.md
Extra:   src/components/icons.ts  (registro de iconos SVG unicos)
"""
import re, json, glob, os, sys, unicodedata
from bs4 import BeautifulSoup
from collections import OrderedDict

ROOT = "/Users/frankoropeza/Desktop/CLIENTES/PAGINASAMARILLAS"
# El HTML original vive en _legacy/ (se movio de public/ al migrar a la coleccion).
SRC = os.path.join(ROOT, "_legacy/negocios-original")
OUT = os.path.join(ROOT, "src/content/negocios")
ICONS_OUT = os.path.join(ROOT, "src/lib/icons.ts")

ICON_REGISTRY = OrderedDict()   # normalized svg inner -> name
ICON_NAMES = {}                  # name -> inner

# Iconos con nombre canonico fijo: se registran primero para que no dependan
# del texto de la primera tarjeta donde aparecen.
PRESEED = {
    "check": '<polyline points="20 6 9 17 4 12"></polyline>',
}


def slugify(s):
    """'Ubicación' -> 'ubicacion' (translitera acentos en vez de comerselos)."""
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("ñ", "n")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def norm_svg(svg_tag):
    """Devuelve el contenido interno del <svg> normalizado (sin width/height)."""
    inner = "".join(str(c) for c in svg_tag.contents)
    inner = re.sub(r"\s+", " ", inner).strip()
    return inner


def icon_name_for(svg_tag, hint=""):
    if svg_tag is None:
        return None
    inner = norm_svg(svg_tag)
    if inner in ICON_REGISTRY:
        return ICON_REGISTRY[inner]
    base = slugify(hint) or "icon"
    base = "-".join(base.split("-")[:3]) or "icon"
    name = base
    i = 2
    while name in ICON_NAMES:
        name = f"{base}-{i}"
        i += 1
    ICON_REGISTRY[inner] = name
    ICON_NAMES[name] = inner
    return name


def txt(el):
    if el is None:
        return None
    s = el.get_text(" ", strip=True)
    s = re.sub(r"\s+", " ", s).strip()
    return s or None


def inner_md(el):
    """Convierte HTML inline simple (strong/em/a) a Markdown."""
    if el is None:
        return None
    out = []
    for node in el.children:
        if isinstance(node, str):
            out.append(node)
        elif node.name in ("strong", "b"):
            out.append(f"**{node.get_text(' ', strip=True)}**")
        elif node.name in ("em", "i"):
            out.append(f"*{node.get_text(' ', strip=True)}*")
        elif node.name == "a":
            href = node.get("href", "")
            out.append(f"[{node.get_text(' ', strip=True)}]({href})")
        elif node.name == "br":
            out.append(" ")
        elif node.name == "svg":
            continue
        else:
            out.append(node.get_text(" ", strip=True))
    s = re.sub(r"\s+", " ", "".join(out)).strip()
    return s or None


JSON_ERRORS = []
SIN_ACTION = []


def _loads_tolerante(raw, ctx=""):
    """json.loads normal; si falla, limpia comas colgantes y reintenta."""
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        fixed = re.sub(r",\s*([}\]])", r"\1", raw)
        try:
            d = json.loads(fixed)
            JSON_ERRORS.append(f"{ctx}: coma colgante reparada ({e.msg} @ linea {e.lineno})")
            return d
        except json.JSONDecodeError as e2:
            JSON_ERRORS.append(f"{ctx}: JSON-LD IRRECUPERABLE -> {e2}")
            return None


def jsonlds(soup, ctx=""):
    res = []
    for s in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = s.string or s.get_text()
        if not raw:
            continue
        d = _loads_tolerante(raw, ctx)
        if d is not None:
            res.extend(d if isinstance(d, list) else [d])
    return res


def first(v):
    """Desenvuelve listas: schema.org permite valor unico o array."""
    if isinstance(v, list):
        return v[0] if v else None
    return v


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def find_ld(lds, tipo):
    for d in lds:
        if d.get("@type") == tipo:
            return d
    return None


def meta(soup, **kw):
    t = soup.find("meta", attrs=kw)
    return t.get("content") if t else None


def clean_img(src):
    if not src:
        return None
    src = src.strip()
    src = re.sub(r"^(\.\./)+", "/", src)
    if not src.startswith("/") and not src.startswith("http"):
        src = "/" + src
    return src


def strip_domain(u):
    if not u:
        return None
    return re.sub(r"^https?://paginasamarillas\.mx", "", u) or "/"


# ---------- extractores por seccion ----------

def ex_hero(soup):
    hero = soup.select_one("section.business-hero")
    d = {}
    if not hero:
        return d
    main = hero.select_one(".business-main-image img")
    if main:
        d["imagen"] = clean_img(main.get("src"))
        d["imagenAlt"] = main.get("alt")
    d["badges"] = [txt(b) for b in hero.select(".business-hero-badges .badge") if txt(b)]
    gal = []
    for th in hero.select(".business-gallery-thumbs img"):
        gal.append({"src": clean_img(th.get("src")), "alt": th.get("alt")})
    if gal:
        d["galeria"] = gal
    d["titulo"] = txt(hero.select_one(".business-title"))
    d["tagline"] = txt(hero.select_one(".business-tagline"))
    # enlace al sitio del negocio junto al rating (solo en seguridad-privada)
    rl = hero.select_one(".rating-link")
    if rl and rl.get("href"):
        d["ratingLink"] = {"texto": txt(rl), "href": rl.get("href")}
    qi = []
    for card in hero.select(".quick-info-card"):
        strong = card.find("strong")
        p = card.find("p")
        if strong and p:
            qi.append({
                "icono": icon_name_for(card.find("svg"), txt(strong) or ""),
                "titulo": txt(strong),
                "texto": txt(p),
            })
    if qi:
        d["quickInfo"] = qi
    ctas = []
    for a in hero.select(".business-cta-buttons a"):
        ctas.append({
            "texto": txt(a),
            "href": a.get("href"),
            "estilo": "primary" if "btn-primary" in (a.get("class") or []) else "outline",
            "icono": icon_name_for(a.find("svg"), txt(a) or ""),
        })
    if ctas:
        d["ctas"] = ctas
    return d


def ex_servicios(soup):
    out = []
    for card in soup.select(".services-grid > .service-card"):
        out.append({
            "icono": icon_name_for(card.select_one(".service-icon svg"),
                                   txt(card.select_one(".service-title")) or ""),
            "titulo": txt(card.select_one(".service-title")),
            "descripcion": txt(card.select_one(".service-description")),
            "features": [txt(li) for li in card.select(".service-features li") if txt(li)],
        })
    return out


def ex_about(soup):
    sec = soup.select_one(".about-grid")
    if not sec:
        return {}, ""
    d = {}
    body = []
    h2 = sec.select_one(".section-title")
    if h2:
        d["aboutTitulo"] = txt(h2)
    for p in sec.select(".about-content > .about-text"):
        m = inner_md(p)
        if m:
            body.append(m)
    sub = sec.select_one(".subsection-title")
    if sub:
        d["beneficiosTitulo"] = txt(sub)
    bens = []
    for li in sec.select(".benefits-list > li"):
        m = inner_md(li)
        if m:
            bens.append(m)
    if bens:
        d["beneficios"] = bens
    stats = []
    for st in sec.select(".stat-card"):
        stats.append({
            "numero": txt(st.select_one(".stat-number")),
            "label": txt(st.select_one(".stat-label")),
        })
    if stats:
        d["stats"] = stats
    return d, "\n\n".join(body)


def ex_cobertura(soup):
    grid = soup.select_one(".coverage-grid")
    if not grid:
        return {}
    d = {}
    sec = grid.find_parent("section")
    if sec:
        d["coberturaTitulo"] = txt(sec.select_one(".section-title"))
        d["coberturaSubtitulo"] = txt(sec.select_one(".section-subtitle"))
    cols = []
    for col in grid.select(".coverage-column"):
        items = []
        for li in col.select(".coverage-list > li"):
            t = inner_md(li)
            if t:
                items.append({"texto": t,
                              "icono": icon_name_for(li.find("svg"), t)})
        cols.append({"titulo": txt(col.select_one(".coverage-title")), "items": items})
    if cols:
        d["cobertura"] = cols
    return d


def ex_faq(soup):
    out = []
    for item in soup.select(".faq-item"):
        q = pick(item, ".faq-question", "h3", "summary", "button")
        a = pick(item, ".faq-answer", ".faq-body", "p")
        pregunta = txt(q)
        respuesta = inner_md(a) if a else None
        if pregunta and respuesta:
            out.append({"pregunta": pregunta, "respuesta": respuesta})
    return out


def pick(el, *selectores):
    """select_one por prioridad real: prueba cada selector en orden, no como union CSS."""
    if el is None:
        return None
    for sel in selectores:
        found = el.select_one(sel)
        if found is not None:
            return found
    return None


def ex_resenas(soup):
    out = []
    for card in soup.select(".reviews-grid > .review-card"):
        # autor: el <strong> dentro de .review-author, no el bloque entero (trae avatar+fecha)
        autor = txt(pick(card, ".review-author strong", ".reviewer-name", "cite", ".review-name"))
        avatar = txt(card.select_one(".author-avatar"))
        texto = txt(pick(card, ".review-text", ".review-body", "blockquote"))
        fecha = txt(pick(card, ".review-date", "time"))
        stars = pick(card, ".stars", ".review-stars")
        rating = (txt(stars) or "").count("★") or None if stars else None
        # algunas resenas enlazan al sitio del cliente que la escribio
        web = card.select_one(".review-website")
        sitio = {"texto": txt(web), "href": web.get("href")} if web and web.get("href") else None
        if texto:
            out.append({k: v for k, v in {
                "autor": autor, "avatar": avatar, "texto": texto,
                "rating": rating, "fecha": fecha, "sitio": sitio,
            }.items() if v is not None})
    return out


def ex_contacto_extra(soup):
    """Bloques de contacto que no vienen del JSON-LD (horarios, mapa, etc.)."""
    grid = soup.select_one(".contact-grid")
    if not grid:
        return {}
    d = {}
    sec = grid.find_parent("section")
    if sec:
        d["contactoTitulo"] = txt(sec.select_one(".section-title"))
        d["contactoSubtitulo"] = txt(sec.select_one(".section-subtitle"))
    items = []
    for c in grid.select(".contact-card, .contact-item"):
        det = c.select_one(".contact-details") or c
        titulo_el = pick(det, ".contact-title", "h3", "h4", "strong")
        lineas = []
        for p in det.find_all("p"):
            lineas.extend(split_br(p))
        if titulo_el:
            items.append({
                "icono": icon_name_for(c.find("svg"), txt(titulo_el) or ""),
                "titulo": txt(titulo_el),
                "lineas": lineas,
            })
    if items:
        d["contactoItems"] = items
    return d


def split_br(p):
    """Parte un <p> por <br> en lineas; conserva el href de cada enlace."""
    lineas, buf, href = [], [], None

    def flush():
        nonlocal buf, href
        t = re.sub(r"\s+", " ", "".join(buf)).strip()
        if t:
            lineas.append({"texto": t, "href": href} if href else {"texto": t})
        buf, href = [], None

    for node in p.children:
        if getattr(node, "name", None) == "br":
            flush()
        elif isinstance(node, str):
            buf.append(node)
        elif node.name == "a":
            href = node.get("href")
            buf.append(node.get_text(" ", strip=True))
        elif node.name == "svg":
            continue
        else:
            buf.append(node.get_text(" ", strip=True))
    flush()
    return lineas


def ex_formulario(soup):
    """Form de cotizacion: identico en estructura, distinto en opciones por negocio."""
    wrap = soup.select_one(".contact-form-wrapper")
    if not wrap:
        return {}
    d = {}
    d["formTitulo"] = txt(wrap.select_one(".form-title"))
    d["formSubtitulo"] = txt(wrap.select_one(".form-subtitle"))
    form = wrap.select_one("form")
    if not form:
        return {k: v for k, v in d.items() if v}
    if form.get("action"):
        d["formAction"] = form.get("action")
    campos = []
    for el in form.select("input, select, textarea"):
        name = el.get("name") or el.get("id")
        if not name:
            continue
        label = form.select_one(f'label[for="{el.get("id")}"]') if el.get("id") else None
        campo = {
            "name": name,
            "label": txt(label),
            "tipo": el.get("type") or el.name,
            "requerido": el.has_attr("required"),
        }
        if el.name == "select":
            campo["tipo"] = "select"
            campo["opciones"] = [
                {"value": o.get("value", ""), "texto": txt(o)}
                for o in el.select("option") if txt(o)
            ]
        if el.get("placeholder"):
            campo["placeholder"] = el.get("placeholder")
        campos.append({k: v for k, v in campo.items() if v not in (None, "", [])})
    if campos:
        d["formCampos"] = campos
    btn = form.select_one("button, input[type=submit]")
    if btn:
        d["formBoton"] = txt(btn) or btn.get("value")
    return {k: v for k, v in d.items() if v not in (None, "", [])}


def ex_cta_final(soup):
    sec = soup.select_one("section.final-cta")
    if not sec:
        return {}
    d = {
        "ctaFinalTitulo": txt(sec.find(["h2", "h3"])),
        "ctaFinalTexto": txt(sec.find("p")),
    }
    btns = []
    for a in sec.select("a"):
        btns.append({"texto": txt(a), "href": a.get("href"),
                     "estilo": "primary" if "btn-primary" in (a.get("class") or []) else "outline"})
    if btns:
        d["ctaFinalBotones"] = btns
    return {k: v for k, v in d.items() if v}


def ex_directorio(soup):
    """Catalogo rico: <article class="service-directory-card"> (6 por ficha en 12 fichas)."""
    grid = soup.select_one(".services-directory-grid")
    if not grid:
        return {}
    d = {}
    sec = grid.find_parent("section")
    if sec:
        d["directorioTitulo"] = txt(sec.select_one(".section-title"))
        d["directorioSubtitulo"] = txt(sec.select_one(".section-subtitle"))
        # pestanas de filtro (las mueve perfil.js via data-category)
        tabs = []
        for t in sec.select(".category-tab"):
            tabs.append({
                "texto": txt(t),
                "filtro": t.get("data-category"),
                "icono": icon_name_for(t.find("svg"), txt(t) or "tab"),
                "activo": "active" in (t.get("class") or []),
            })
        if tabs:
            d["directorioTabs"] = tabs
        # CTA al pie del catalogo
        cta = sec.select_one(".services-directory-cta")
        if cta:
            d["directorioCtaTexto"] = txt(cta.select_one(".directory-cta-text"))
            botones = []
            for a in cta.select("a"):
                botones.append({
                    "texto": txt(a),
                    "href": a.get("href"),
                    "estilo": "primary" if "btn-primary" in (a.get("class") or []) else "outline",
                    "icono": icon_name_for(a.find("svg"), txt(a) or "cta"),
                })
            if botones:
                d["directorioCtaBotones"] = botones
    cards = []
    for c in grid.select("article.service-directory-card"):
        card = {}
        if c.get("data-category"):
            card["filtro"] = c.get("data-category")
        img = c.select_one(".service-card-image img")
        if img:
            card["imagen"] = clean_img(img.get("src"))
            card["imagenAlt"] = img.get("alt")
        badge = c.select_one(".service-badge")
        if badge:
            cls = [x for x in (badge.get("class") or []) if x.startswith("badge-")]
            card["badge"] = txt(badge)
            if cls:
                card["badgeTipo"] = cls[0].replace("badge-", "")
        card["titulo"] = txt(c.select_one(".service-card-title"))
        tag = c.select_one(".service-category-tag")
        if tag:
            card["tag"] = txt(tag)
            card["tagIcono"] = icon_name_for(tag.find("svg"), txt(tag) or "tag")
        card["descripcion"] = txt(c.select_one(".service-card-description"))
        feats = [txt(li) for li in c.select(".service-card-features > li")]
        card["features"] = [f for f in feats if f]
        loc = c.select_one(".service-location span")
        if loc:
            card["ubicacion"] = txt(loc)
        cta = c.select_one(".btn-service-contact")
        if cta:
            card["ctaTexto"] = txt(cta)
            card["ctaHref"] = cta.get("href")
        cards.append({k: v for k, v in card.items() if v not in (None, "", [])})
    if cards:
        d["directorio"] = cards
    return {k: v for k, v in d.items() if v}


def ex_ubicaciones(soup):
    """Sucursales: <div class="location-card"> con h4 + varios <p> (4 por ficha)."""
    grid = soup.select_one(".locations-grid")
    if not grid:
        return {}
    d = {}
    sec = grid.find_parent("section")
    if sec:
        d["ubicacionesTitulo"] = txt(sec.select_one(".section-title"))
        d["ubicacionesSubtitulo"] = txt(sec.select_one(".section-subtitle"))
    locs = []
    for c in grid.select(".location-card"):
        nombre = txt(c.find(["h4", "h3"]))
        lineas = [txt(p) for p in c.find_all("p") if txt(p)]
        if nombre:
            locs.append({"nombre": nombre, "lineas": lineas})
    if locs:
        d["ubicaciones"] = locs
    return {k: v for k, v in d.items() if v}


# ---------- YAML writer (sin dependencias) ----------

def yq(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def to_yaml(obj, indent=0):
    sp = "  " * indent
    lines = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if v is None or v == [] or v == {} or v == "":
                continue
            if isinstance(v, (dict, list)):
                lines.append(f"{sp}{k}:")
                lines.append(to_yaml(v, indent + 1))
            else:
                lines.append(f"{sp}{k}: {yq(v)}")
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict):
                body = to_yaml(item, indent + 1)
                body_lines = [l for l in body.split("\n") if l.strip()]
                if not body_lines:
                    continue
                first = body_lines[0].strip()
                lines.append(f"{sp}- {first}")
                for l in body_lines[1:]:
                    lines.append(l)
            elif isinstance(item, list):
                lines.append(f"{sp}-")
                lines.append(to_yaml(item, indent + 1))
            else:
                lines.append(f"{sp}- {yq(item)}")
    return "\n".join(lines)


# ---------- main ----------

def process(path):
    cat = os.path.basename(os.path.dirname(path))
    slug = os.path.splitext(os.path.basename(path))[0]
    if slug.endswith("-backup"):
        return None
    html = open(path, encoding="utf-8").read()
    soup = BeautifulSoup(html, "lxml")
    lds = jsonlds(soup, f"{cat}/{slug}")
    lb = find_ld(lds, "LocalBusiness") or {}
    bc = find_ld(lds, "BreadcrumbList") or {}
    faq_ld = find_ld(lds, "FAQPage")

    fm = OrderedDict()
    fm["nombre"] = lb.get("name") or txt(soup.select_one(".business-title"))
    fm["categoria"] = cat
    fm["titulo"] = txt(soup.find("title"))
    fm["descripcion"] = meta(soup, attrs={"name": "description"}) or meta(soup, name="description")
    kw = meta(soup, name="keywords")
    if kw:
        fm["keywords"] = [k.strip() for k in kw.split(",") if k.strip()]

    fm["og"] = {k: v for k, v in {
        "titulo": meta(soup, property="og:title"),
        "descripcion": meta(soup, property="og:description"),
        "imagen": meta(soup, property="og:image"),
        "tipo": meta(soup, property="og:type"),
    }.items() if v}

    fm["slogan"] = first(lb.get("slogan"))
    fm["descripcionLarga"] = first(lb.get("description"))
    fm["priceRange"] = first(lb.get("priceRange"))
    fm["fundacion"] = first(lb.get("foundingDate"))
    noe = first(lb.get("numberOfEmployees"))
    if isinstance(noe, dict):
        fm["empleados"] = noe.get("value")
    elif noe:
        fm["empleados"] = noe

    same = lb.get("sameAs") or []
    if isinstance(same, str):
        same = [same]

    fm["contacto"] = {k: v for k, v in {
        "telefono": first(lb.get("telephone")),
        "email": first(lb.get("email")),
        "sitioWeb": same[0] if same else None,
    }.items() if v}

    addr = first(lb.get("address")) or {}
    if isinstance(addr, dict) and addr:
        fm["direccion"] = {k: v for k, v in {
            "calle": addr.get("streetAddress"),
            "colonia": addr.get("addressLocality"),
            "estado": addr.get("addressRegion"),
            "cp": addr.get("postalCode"),
            "pais": addr.get("addressCountry") or "MX",
        }.items() if v}

    geo = first(lb.get("geo")) or {}
    if isinstance(geo, dict) and geo:
        lat, lng = num(geo.get("latitude")), num(geo.get("longitude"))
        if lat is not None and lng is not None:
            fm["geo"] = {"lat": lat, "lng": lng}

    ar = first(lb.get("aggregateRating")) or {}
    if isinstance(ar, dict) and ar:
        val, cnt = num(ar.get("ratingValue")), num(ar.get("reviewCount"))
        if val is not None and cnt is not None:
            fm["rating"] = {"valor": val, "resenas": int(cnt)}

    served = lb.get("areaServed") or []
    if isinstance(served, (dict, str)):
        served = [served]
    areas = []
    for a in served:
        if isinstance(a, dict) and a.get("name"):
            areas.append({"tipo": a.get("@type"), "nombre": a.get("name")})
        elif isinstance(a, str):
            areas.append({"tipo": "Place", "nombre": a})
    if areas:
        fm["areaServed"] = areas

    if same:
        fm["sameAs"] = same

    cat_ld = first(lb.get("hasOfferCatalog")) or {}
    if not isinstance(cat_ld, dict):
        cat_ld = {}
    ofertas = []
    for off in cat_ld.get("itemListElement", []):
        if not isinstance(off, dict):
            continue
        it = first(off.get("itemOffered")) or {}
        if isinstance(it, dict) and it.get("name"):
            ofertas.append({"nombre": it.get("name"),
                            "descripcion": first(it.get("description"))})
    if ofertas:
        fm["catalogoNombre"] = cat_ld.get("name")
        fm["catalogo"] = ofertas

    # breadcrumb -> nombre legible de la categoria
    for item in bc.get("itemListElement", []):
        if item.get("position") == 3:
            fm["categoriaNombre"] = item.get("name")

    hero = ex_hero(soup)
    fm.update({k: v for k, v in hero.items() if k != "titulo"})

    sec = soup.select_one(".services-grid")
    if sec:
        parent = sec.find_parent("section")
        fm["serviciosTitulo"] = txt(parent.select_one(".section-title")) if parent else None
        fm["serviciosSubtitulo"] = txt(parent.select_one(".section-subtitle")) if parent else None
    servicios = ex_servicios(soup)
    if servicios:
        fm["servicios"] = servicios

    about, body_md = ex_about(soup)
    fm.update(about)
    fm.update(ex_cobertura(soup))
    fm.update(ex_contacto_extra(soup))
    fm.update(ex_formulario(soup))
    dirc = ex_directorio(soup)
    fm.update(dirc)
    ubis = ex_ubicaciones(soup)
    fm.update(ubis)
    fm.update(ex_cta_final(soup))

    faqs = ex_faq(soup)
    if not faqs and faq_ld:
        for q in faq_ld.get("mainEntity", []):
            faqs.append({"pregunta": q.get("name"),
                         "respuesta": (q.get("acceptedAnswer") or {}).get("text")})
    if faqs:
        s = soup.select_one(".faq-item")
        parent = s.find_parent("section") if s else None
        fm["faqTitulo"] = txt(parent.select_one(".section-title")) if parent else "Preguntas Frecuentes"
        fm["faq"] = faqs

    resenas = ex_resenas(soup)
    if resenas:
        s = soup.select_one(".reviews-grid")
        parent = s.find_parent("section") if s else None
        fm["resenasTitulo"] = txt(parent.select_one(".section-title")) if parent else None
        fm["resenas"] = resenas

    fm["legacyUrl"] = f"/negocios/{cat}/{slug}.html"

    fm = OrderedDict((k, v) for k, v in fm.items()
                     if v is not None and v != [] and v != {} and v != "")

    md = "---\n" + to_yaml(fm) + "\n---\n\n" + (body_md or "") + "\n"

    dest_dir = os.path.join(OUT, cat)
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, slug + ".md")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(md)

    # --- verificacion: extraido vs presente en el HTML ---
    esperado = {
        "servicios": len(soup.select(".services-grid > .service-card")),
        "faq": len(soup.select(".faq-item")),
        "stats": len(soup.select(".stat-card")),
        "galeria": len(soup.select(".business-gallery-thumbs img")),
        "quickInfo": len(soup.select(".quick-info-card")),
        "cobertura": len(soup.select(".coverage-column")),
        "directorio": len(soup.select("article.service-directory-card")),
        "ubicaciones": len(soup.select(".location-card")),
        "resenas": len(soup.select(".reviews-grid > .review-card")),
        "contactoItems": len(soup.select(".contact-card, .contact-item")),
        "formCampos": len(soup.select(
            ".contact-form-wrapper input, .contact-form-wrapper select, "
            ".contact-form-wrapper textarea")),
        "directorioTabs": len(soup.select(".category-tab")),
        "directorioCtaBotones": len(soup.select(".services-directory-cta a")),
        "resenasConSitio": len(soup.select(".review-card .review-website")),
    }
    obtenido = {
        "servicios": len(servicios),
        "faq": len(faqs),
        "stats": len(about.get("stats", [])),
        "galeria": len(hero.get("galeria", [])),
        "quickInfo": len(hero.get("quickInfo", [])),
        "cobertura": len(fm.get("cobertura", [])),
        "directorio": len(fm.get("directorio", [])),
        "ubicaciones": len(fm.get("ubicaciones", [])),
        "resenas": len(resenas),
        "contactoItems": len(fm.get("contactoItems", [])),
        "formCampos": len(fm.get("formCampos", [])),
        "directorioTabs": len(fm.get("directorioTabs", [])),
        "directorioCtaBotones": len(fm.get("directorioCtaBotones", [])),
        "resenasConSitio": len([r for r in resenas if r.get("sitio")]),
    }
    if not fm.get("formAction") and fm.get("formCampos"):
        SIN_ACTION.append(f"{cat}/{slug}")
    perdidas = {k: (esperado[k], obtenido[k]) for k in esperado
                if esperado[k] != obtenido[k] and not (k == "faq" and obtenido[k] >= esperado[k])}

    return {
        "slug": slug, "cat": cat,
        "servicios": len(servicios), "faq": len(faqs), "resenas": len(resenas),
        "stats": len(about.get("stats", [])), "beneficios": len(about.get("beneficios", [])),
        "galeria": len(hero.get("galeria", [])), "body_chars": len(body_md or ""),
        "directorio": len(fm.get("directorio", [])),
        "ubicaciones": len(fm.get("ubicaciones", [])),
        "perdidas": perdidas,
    }


def main():
    for name, inner in PRESEED.items():
        ICON_REGISTRY[inner] = name
        ICON_NAMES[name] = inner

    files = sorted(glob.glob(os.path.join(SRC, "*", "*.html")))
    if not files:
        sys.exit(f"ERROR: 0 fichas HTML en {SRC} — nada que extraer. Abortando.")
    rows = []
    for f in files:
        r = process(f)
        if r:
            rows.append(r)
            flag = "OK " if not r["perdidas"] else "!! "
            print(f"  {flag}{r['cat']}/{r['slug']}: "
                  f"{r['servicios']} serv · {r['faq']} faq · {r['resenas']} res · "
                  f"{r['stats']} stats · {r['beneficios']} benef · {r['galeria']} img · "
                  f"{r['directorio']} cat · {r['ubicaciones']} suc · {r['body_chars']} chars")
            for k, (esp, obt) in r["perdidas"].items():
                print(f"      PERDIDA {k}: HTML tiene {esp}, extraje {obt}")

    # icon registry
    os.makedirs(os.path.dirname(ICONS_OUT), exist_ok=True)
    with open(ICONS_OUT, "w", encoding="utf-8") as f:
        f.write("// Auto-generado desde las fichas HTML originales. No editar a mano.\n")
        f.write("export const icons: Record<string, string> = {\n")
        for inner, name in ICON_REGISTRY.items():
            esc = inner.replace("\\", "\\\\").replace("`", "\\`")
            f.write(f"  {json.dumps(name)}: `{esc}`,\n")
        f.write("};\n\nexport type IconName = keyof typeof icons;\n")

    print(f"\n{len(rows)} fichas -> Markdown")
    print(f"{len(ICON_REGISTRY)} iconos -> src/lib/icons.ts")
    tot = lambda k: sum(r[k] for r in rows)
    print(f"TOTALES: {tot('servicios')} servicios · {tot('faq')} faq · "
          f"{tot('resenas')} resenas · {tot('stats')} stats · {tot('galeria')} imgs · "
          f"{tot('directorio')} catalogo · {tot('ubicaciones')} sucursales")

    con_perdidas = [r for r in rows if r["perdidas"]]
    if con_perdidas:
        print(f"\n!! {len(con_perdidas)} fichas con PERDIDA DE CONTENIDO — no continuar hasta arreglar")
    else:
        print("\n✓ Verificacion: 0 bloques perdidos. Todo el contenido del HTML esta en el MD.")

    if JSON_ERRORS:
        print(f"\n!! {len(JSON_ERRORS)} incidencias de JSON-LD en el HTML original:")
        for e in JSON_ERRORS:
            print(f"   - {e}")

    if SIN_ACTION:
        print(f"\n!! {len(SIN_ACTION)} formularios SIN action (no envian a ningun lado):")
        print(f"   {', '.join(SIN_ACTION)}")

    faltantes = [r for r in rows if r["servicios"] == 0 or r["body_chars"] < 200]
    if faltantes:
        print(f"\n!! {len(faltantes)} fichas con extraccion sospechosa (revisar):")
        for r in faltantes:
            print(f"   - {r['cat']}/{r['slug']}: {r['servicios']} serv, {r['body_chars']} chars")


if __name__ == "__main__":
    main()
