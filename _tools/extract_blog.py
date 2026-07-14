#!/usr/bin/env python3
"""
Extrae los articulos del blog HTML -> MDX + frontmatter tipado.
Fuente:  public/blog/{categoria}/{slug}.html
Destino: src/content/blog/{categoria}/{slug}.mdx

La prosa se convierte a Markdown; los modulos repetidos (stat, tip, aviso,
cita, galeria, pasos) se emiten como componentes.
"""
import re, json, glob, os, sys
from bs4 import BeautifulSoup, NavigableString
from collections import OrderedDict
from markdownify import MarkdownConverter

ROOT = "/Users/frankoropeza/Desktop/CLIENTES/PAGINASAMARILLAS"
# El HTML original vive en _legacy/ (se movio de public/ al migrar a la coleccion).
SRC = os.path.join(ROOT, "_legacy/blog-original")
OUT = os.path.join(ROOT, "src/content/blog")

VACIOS, SIN_SCHEMA, AVISOS, DIVERGEN = [], [], [], []


def norm_txt(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


# ---------- HTML -> Markdown ----------

class Conv(MarkdownConverter):
    """Markdownify con las rutas de imagen normalizadas y sin SVG sueltos."""

    def convert_img(self, el, text, parent_tags=None):
        el["src"] = clean_img(el.get("src"))
        return super().convert_img(el, text, parent_tags)

    def convert_a(self, el, text, parent_tags=None):
        href = el.get("href") or ""
        if href.endswith(".html"):
            el["href"] = re.sub(r"\.html$", "", href)
        return super().convert_a(el, text, parent_tags)

    def convert_svg(self, el, text, parent_tags=None):
        return ""


def md(el):
    if el is None:
        return ""
    out = Conv(heading_style="ATX", bullets="-", escape_asterisks=False,
               escape_underscores=False, code_language="").convert_soup(el)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip()


def clean_img(src):
    if not src:
        return src
    src = src.strip()
    src = re.sub(r"^(\.\./)+", "/", src)
    if not src.startswith(("/", "http", "data:")):
        src = "/" + src
    return src


def txt(el):
    if el is None:
        return None
    s = re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()
    return s or None


def attr(v):
    """Escapa un valor para meterlo en un atributo JSX."""
    return json.dumps(v or "", ensure_ascii=False)


# ---------- emisores de componentes ----------

def em_stat(el):
    numero = txt(el.select_one(".stat-number")) or ""
    cont = el.select_one(".stat-content")
    titulo = txt(cont.find("h4")) if cont else None
    cuerpo = ""
    if cont:
        h4 = cont.find("h4")
        if h4:
            h4.decompose()
        cuerpo = md(cont)
    return f"<Stat numero={attr(numero)} titulo={attr(titulo)}>\n\n{cuerpo}\n\n</Stat>"


def em_tip(el):
    cont = el.select_one(".tip-content")
    titulo = txt(cont.find("h4")) if cont else None
    if cont and cont.find("h4"):
        cont.find("h4").decompose()
    return f"<Tip titulo={attr(titulo)}>\n\n{md(cont)}\n\n</Tip>"


def em_aviso(el):
    cont = el.select_one(".alert-content")
    titulo = txt(cont.find("h4")) if cont else None
    if cont and cont.find("h4"):
        cont.find("h4").decompose()
    return f"<Aviso titulo={attr(titulo)}>\n\n{md(cont)}\n\n</Aviso>"


def em_cita(el):
    q = el.find("blockquote")
    autor = txt(el.find("cite"))
    return f"<Cita autor={attr(autor)}>\n\n{md(q)}\n\n</Cita>"


def em_galeria(el):
    titulo = txt(el.find(["h3", "h2"]))
    imgs = []
    for item in el.select(".gallery-item"):
        i = item.find("img")
        if not i:
            continue
        imgs.append({
            "src": clean_img(i.get("src")),
            "alt": i.get("alt") or "",
            "caption": txt(item.select_one(".gallery-caption")) or "",
        })
    data = json.dumps(imgs, ensure_ascii=False, indent=2)
    return f"<Galeria titulo={attr(titulo)} imagenes={{{data}}} />"


def em_pasos(el):
    partes = ["<Pasos>"]
    for st in el.select(".process-step"):
        n = txt(st.select_one(".step-number")) or ""
        cont = st.select_one(".step-content")
        titulo = txt(cont.find("h4")) if cont else None
        if cont and cont.find("h4"):
            cont.find("h4").decompose()
        partes.append(f'  <Paso n={attr(n)} titulo={attr(titulo)}>\n\n{md(cont)}\n\n  </Paso>')
    partes.append("</Pasos>")
    return "\n".join(partes)


# ---------- recorrido del cuerpo ----------

def render(el, dentro_seccion=False):
    """Convierte los hijos de el a MDX, emitiendo componentes donde toca."""
    trozos, buffer = [], []

    def vaciar():
        if not buffer:
            return
        envoltorio = BeautifulSoup("<div></div>", "lxml").div
        for n in buffer:
            envoltorio.append(n)
        t = md(envoltorio)
        if t:
            trozos.append(t)
        buffer.clear()

    for hijo in list(el.children):
        if isinstance(hijo, NavigableString):
            if hijo.strip():
                buffer.append(hijo)
            continue
        if hijo.name in ("script", "style"):
            continue

        clases = hijo.get("class") or []

        if hijo.name == "section" and ("content-section" in clases or "intro-section" in clases):
            vaciar()
            sid = hijo.get("id") or ""
            intro = "intro-section" in clases
            interior = render(hijo, dentro_seccion=True)
            extra = " intro" if intro else ""
            trozos.append(f'<Seccion id={attr(sid)}{extra}>\n\n{interior}\n\n</Seccion>')
        elif "stat-module" in clases:
            vaciar(); trozos.append(em_stat(hijo))
        elif "tip-module" in clases:
            vaciar(); trozos.append(em_tip(hijo))
        elif "alert-module" in clases:
            vaciar(); trozos.append(em_aviso(hijo))
        elif "quote-module" in clases:
            vaciar(); trozos.append(em_cita(hijo))
        elif "blog-image-gallery" in clases:
            vaciar(); trozos.append(em_galeria(hijo))
        elif "process-steps" in clases:
            vaciar(); trozos.append(em_pasos(hijo))
        else:
            buffer.append(hijo)

    vaciar()
    return "\n\n".join(t for t in trozos if t.strip())


# ---------- JSON-LD ----------

def lds(soup, ctx=""):
    out = []
    for s in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = s.string or s.get_text()
        if not raw:
            continue
        try:
            d = json.loads(raw)
        except json.JSONDecodeError:
            try:
                d = json.loads(re.sub(r",\s*([}\]])", r"\1", raw))
                AVISOS.append(f"{ctx}: JSON-LD con coma colgante (reparado)")
            except json.JSONDecodeError as e:
                AVISOS.append(f"{ctx}: JSON-LD irrecuperable: {e}")
                continue
        out.extend(d if isinstance(d, list) else [d])
    return out


def find_ld(l, *tipos):
    for d in l:
        if isinstance(d, dict) and d.get("@type") in tipos:
            return d
    return None


def meta(soup, **kw):
    t = soup.find("meta", attrs=kw)
    return t.get("content") if t else None


# ---------- YAML ----------

def yq(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def to_yaml(o, ind=0):
    sp = "  " * ind
    out = []
    if isinstance(o, dict):
        for k, v in o.items():
            if v is None or v == [] or v == {} or v == "":
                continue
            if isinstance(v, (dict, list)):
                out.append(f"{sp}{k}:")
                out.append(to_yaml(v, ind + 1))
            else:
                out.append(f"{sp}{k}: {yq(v)}")
    elif isinstance(o, list):
        for it in o:
            if isinstance(it, dict):
                cuerpo = [l for l in to_yaml(it, ind + 1).split("\n") if l.strip()]
                if not cuerpo:
                    continue
                out.append(f"{sp}- {cuerpo[0].strip()}")
                out.extend(cuerpo[1:])
            else:
                out.append(f"{sp}- {yq(it)}")
    return "\n".join(out)


# ---------- proceso ----------

def process(path):
    cat = os.path.basename(os.path.dirname(path))
    slug = os.path.splitext(os.path.basename(path))[0]
    ref = f"{cat}/{slug}"

    raw = open(path, encoding="utf-8").read()
    if not raw.strip():
        VACIOS.append(ref)
        return None

    soup = BeautifulSoup(raw, "lxml")

    # 3 estructuras distintas conviven en el blog original:
    #   1) .blog-article-content            (la mayoria)
    #   2) article.blog-article > .container
    #   3) main > article sin clases        (articulos minificados)
    cont = soup.select_one(".blog-article-content")
    if cont is None:
        art = soup.select_one("article.blog-article")
        cont = art.select_one(".container") if art else None
    if cont is None:
        cont = soup.select_one("main article")
        if cont is not None:
            AVISOS.append(f"{ref}: estructura atipica (main > article sin clases)")
    if cont is None:
        AVISOS.append(f"{ref}: SIN CUERPO RECONOCIBLE — omitido")
        return None

    # Tags e indice se leen ANTES de limpiar: en algunas estructuras viven
    # dentro de cont y el decompose de abajo se los llevaria por delante.
    tags = [txt(t) for t in soup.select(".blog-article-tags .tag")]
    tags = [t for t in tags if t and not t.lower().startswith("temas relacionados")]

    toc = []
    for a in soup.select(".blog-article-toc-inline a[href^='#'], .blog-toc a[href^='#']"):
        t, anc = txt(a), a.get("href", "")[1:]
        if t and anc and not any(x["ancla"] == anc for x in toc):
            toc.append({"texto": t, "ancla": anc})

    # el indice y los bloques de navegacion no son contenido del articulo
    for basura in cont.select(".blog-article-toc-inline, .blog-related-articles, "
                              ".blog-article-tags, nav"):
        basura.decompose()

    L = lds(soup, ref)
    art_ld = find_ld(L, "Article", "BlogPosting") or {}
    faq_ld = find_ld(L, "FAQPage")
    if not art_ld:
        SIN_SCHEMA.append(ref)

    # Cabecera: 42 articulos usan .blog-hero-section (imagen + gancho +
    # tiempo de lectura); los otros 9 solo un .blog-article-header con h1.
    hero = soup.select_one(".blog-hero-section")
    h1 = soup.find("h1")

    # El h1 visible y el headline del JSON-LD NO coinciden en varios articulos
    # (unos sin acentos, otros con titulo distinto). Se preservan los dos tal
    # cual: cambiar cualquiera alteraria lo que ve el usuario o lo que lee Google.
    fm = OrderedDict()
    titulo = (txt(h1) if h1 else None) or art_ld.get("headline") or txt(soup.find("title"))
    headline = art_ld.get("headline")
    fm["titulo"] = titulo
    if headline and norm_txt(headline) != norm_txt(titulo):
        fm["headline"] = headline
        DIVERGEN.append(f"{ref}:\n       h1:       {titulo}\n       headline: {headline}")
    fm["descripcion"] = (art_ld.get("description")
                         or meta(soup, attrs={"name": "description"})
                         or meta(soup, name="description"))
    fm["categoria"] = cat
    fm["seoTitle"] = txt(soup.find("title"))

    kw = art_ld.get("keywords") or meta(soup, name="keywords")
    if isinstance(kw, str):
        kw = [k.strip() for k in kw.split(",") if k.strip()]
    if kw:
        fm["keywords"] = kw

    img = art_ld.get("image")
    if isinstance(img, list):
        img = img[0] if img else None
    if isinstance(img, dict):
        img = img.get("url")
    fm["imagen"] = clean_img(img) if img else None

    if hero:
        himg = hero.select_one(".blog-hero-image img")
        if himg:
            fm["heroImagen"] = clean_img(himg.get("src"))
            fm["heroImagenAlt"] = himg.get("alt")
        fm["gancho"] = txt(hero.select_one(".hero-hook"))
        # "7 min lectura" -> 7
        meta_txt = txt(hero.select_one(".hero-meta")) or ""
        m = re.search(r"(\d+)\s*min", meta_txt)
        if m:
            fm["minutosLectura"] = int(m.group(1))
        fm["badge"] = txt(hero.select_one(".category-badge"))

    autor = art_ld.get("author")
    if isinstance(autor, dict):
        fm["autor"] = autor.get("name")
    elif isinstance(autor, str):
        fm["autor"] = autor

    pub = art_ld.get("publisher")
    if isinstance(pub, dict) and pub.get("name"):
        fm["publisher"] = pub.get("name")

    if art_ld.get("datePublished"):
        fm["publicado"] = art_ld["datePublished"][:10]
    if art_ld.get("dateModified"):
        fm["modificado"] = art_ld["dateModified"][:10]

    if tags:
        fm["tags"] = tags

    # El indice original lleva etiquetas cortas curadas a mano y sus anclas
    # apuntan a los id de <Seccion> (#que-es), no al slug del h2.
    if toc:
        fm["toc"] = toc

    if faq_ld:
        faqs = []
        for q in faq_ld.get("mainEntity", []) or []:
            if not isinstance(q, dict):
                continue
            a = q.get("acceptedAnswer") or {}
            if q.get("name") and a.get("text"):
                faqs.append({"pregunta": q["name"], "respuesta": a["text"]})
        if faqs:
            fm["faq"] = faqs

    fm["legacyUrl"] = f"/blog/{cat}/{slug}.html"
    fm = OrderedDict((k, v) for k, v in fm.items() if v not in (None, "", [], {}))

    # Contar ANTES de render(): render muta el arbol (decompose, reparenting)
    # y despues los conteos salen en cero.
    esperado = {
        "h2": len(cont.find_all("h2")),
        "h3": len(cont.find_all("h3")),
        "img": len(cont.find_all("img")),
        "tablas": len(cont.find_all("table")),
        "secciones": len(cont.select(".content-section, .intro-section")),
        "modulos": len(cont.select(".interest-module")),
        "galerias": len(cont.select(".blog-image-gallery")),
        "pasos": len(cont.select(".process-step")),
        "enlaces": len(cont.find_all("a")),
    }

    cuerpo = render(cont)

    usados = sorted({c for c in ["Seccion", "Stat", "Tip", "Aviso", "Cita", "Galeria", "Pasos", "Paso"]
                     if re.search(rf"<{c}[\s/>]", cuerpo)})
    imports = "\n".join(f"import {c} from '../../../components/blog/{c}.astro';" for c in usados)

    mdx = "---\n" + to_yaml(fm) + "\n---\n\n"
    if imports:
        mdx += imports + "\n\n"
    mdx += cuerpo + "\n"

    dest_dir = os.path.join(OUT, cat)
    os.makedirs(dest_dir, exist_ok=True)
    with open(os.path.join(dest_dir, slug + ".mdx"), "w", encoding="utf-8") as f:
        f.write(mdx)

    return {
        "ref": ref, "slug": slug, "cat": cat,
        "chars": len(cuerpo), "faq": len(fm.get("faq", [])),
        "comp": len(usados), "esperado": esperado,
    }


def main():
    files = sorted(f for f in glob.glob(os.path.join(SRC, "*", "*.html"))
                   if "/templates/" not in f and "/categorias/" not in f
                   and not f.endswith("/index.html"))
    if not files:
        sys.exit(f"ERROR: 0 articulos en {SRC}")

    rows = []
    for f in files:
        r = process(f)
        if r:
            rows.append(r)
            print(f"  OK {r['ref'][:52]:<54} {r['chars']:>6} chars · "
                  f"{r['faq']} faq · {r['comp']} comp")

    print(f"\n{len(rows)}/{len(files)} articulos -> MDX")
    tot = lambda k: sum(r["esperado"][k] for r in rows)
    print(f"TOTALES: {tot('h2')} h2 · {tot('h3')} h3 · {tot('img')} imgs · "
          f"{tot('tablas')} tablas · {tot('secciones')} secciones · "
          f"{tot('modulos')} modulos · {tot('galerias')} galerias · {tot('pasos')} pasos")
    print(f"FAQ: {sum(r['faq'] for r in rows)}")

    if VACIOS:
        print(f"\n!! {len(VACIOS)} articulos VACIOS (0 bytes) — sirven 200 con pagina en blanco:")
        for v in VACIOS:
            print(f"   - {v}")
    if SIN_SCHEMA:
        print(f"\n!! {len(SIN_SCHEMA)} articulos sin schema Article/BlogPosting:")
        for s in SIN_SCHEMA:
            print(f"   - {s}")
    if DIVERGEN:
        print(f"\n!! {len(DIVERGEN)} articulos donde el h1 y el headline de Google NO coinciden:")
        for d in DIVERGEN:
            print(f"   - {d}")
    if AVISOS:
        print(f"\n[avisos] {len(AVISOS)}:")
        for a in AVISOS:
            print(f"   - {a}")


if __name__ == "__main__":
    main()
