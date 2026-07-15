#!/usr/bin/env python3
"""
public/categoria/{slug}.html -> src/content/categorias/{slug}.md

El listado de negocios NO se extrae: se genera desde la coleccion 'negocios'
en tiempo de build. Aqui solo va lo que es propio de la categoria (hero,
subcategorias, filtros, prosa SEO, CTA).

Los conteos de los filtros del HTML original son datos curados a mano. Se
guardan como `esperado` para poder contrastarlos con lo que de la coleccion:
si no cuadran, alguien los dejo desactualizados.
"""
import re, json, os, sys
from bs4 import BeautifulSoup
from collections import OrderedDict

ROOT = "/Users/frankoropeza/Desktop/CLIENTES/PAGINASAMARILLAS"
SRC = os.path.join(ROOT, "public/categoria")
OUT = os.path.join(ROOT, "src/content/categorias")
ICONS = os.path.join(ROOT, "src/lib/icons.ts")

CATS = ["seguridad-privada", "entretenimiento", "equipos-contra-incendios"]

# registro de iconos ya generado por extract_negocios.py: se reutiliza
ICON_REGISTRY = {}


def cargar_iconos():
    if not os.path.exists(ICONS):
        return
    txt = open(ICONS, encoding="utf-8").read()
    for m in re.finditer(r'"([^"]+)":\s*`(.*?)`,\n', txt, re.S):
        ICON_REGISTRY[m.group(2).strip()] = m.group(1)


NUEVOS = OrderedDict()


def slugify(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("ñ", "n")).strip("-")


def icono(svg, hint=""):
    if svg is None:
        return None
    inner = re.sub(r"\s+", " ", "".join(str(c) for c in svg.contents)).strip()
    inner = re.sub(r"<title.*?</title>", "", inner).strip()
    if inner in ICON_REGISTRY:
        return ICON_REGISTRY[inner]
    if inner in NUEVOS:
        return NUEVOS[inner]
    base = "-".join(slugify(hint).split("-")[:3]) or "icon"
    nombre = base
    i = 2
    while nombre in ICON_REGISTRY.values() or nombre in NUEVOS.values():
        nombre = f"{base}-{i}"
        i += 1
    NUEVOS[inner] = nombre
    return nombre


def txt(el):
    if el is None:
        return None
    s = re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()
    return s or None


def md_inline(el):
    out = []
    for n in el.children:
        if isinstance(n, str):
            out.append(n)
        elif n.name in ("strong", "b"):
            out.append(f"**{n.get_text(' ', strip=True)}**")
        elif n.name in ("em", "i"):
            out.append(f"*{n.get_text(' ', strip=True)}*")
        elif n.name == "a":
            out.append(f"[{n.get_text(' ', strip=True)}]({n.get('href','')})")
        elif n.name == "br":
            out.append(" ")
        elif n.name == "svg":
            continue
        else:
            out.append(n.get_text(" ", strip=True))
    return re.sub(r"\s+", " ", "".join(out)).strip()


def meta(soup, **kw):
    t = soup.find("meta", attrs=kw)
    return t.get("content") if t else None


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


def process(cat):
    p = os.path.join(SRC, cat + ".html")
    soup = BeautifulSoup(open(p, encoding="utf-8").read(), "lxml")

    fm = OrderedDict()
    fm["slug"] = cat
    fm["titulo"] = txt(soup.select_one(".category-title"))
    fm["descripcion"] = txt(soup.select_one(".category-description"))
    fm["seoTitle"] = txt(soup.find("title"))
    fm["metaDescripcion"] = meta(soup, attrs={"name": "description"}) or meta(soup, name="description")
    kw = meta(soup, name="keywords")
    if kw:
        fm["keywords"] = [k.strip() for k in kw.split(",") if k.strip()]
    fm["og"] = {k: v for k, v in {
        "titulo": meta(soup, property="og:title"),
        "descripcion": meta(soup, property="og:description"),
        "imagen": meta(soup, property="og:image"),
    }.items() if v}

    ic = soup.select_one(".category-icon-large svg")
    if ic is not None:
        fm["icono"] = icono(ic, fm["titulo"] or cat)
        t = ic.find("title")
        if t:
            fm["iconoTitulo"] = txt(t)

    # buscador
    qs = soup.select_one(".quick-search")
    if qs:
        ins = qs.select("input[placeholder]")
        fm["busqueda"] = {k: v for k, v in {
            "placeholder": ins[0].get("placeholder") if ins else None,
            "placeholderUbicacion": ins[1].get("placeholder") if len(ins) > 1 else None,
            "boton": txt(qs.select_one("button")),
        }.items() if v}

    # subcategorias
    sec = soup.select_one("section.subcategories")
    if sec:
        fm["subcategoriasTitulo"] = txt(sec.select_one(".section-title-small"))
        chips = []
        for a in sec.select(".subcategory-chip"):
            chips.append({"texto": txt(a), "ancla": (a.get("href") or "").lstrip("#"),
                          "icono": icono(a.find("svg"), txt(a) or "")})
        if chips:
            fm["subcategorias"] = chips

    # cabecera de resultados
    fm["resultadosSubtitulo"] = txt(soup.select_one(".results-info p"))
    orden = []
    for o in soup.select(".sort-select option"):
        orden.append({"value": o.get("value", ""), "texto": txt(o)})
    if orden:
        fm["ordenTitulo"] = txt(soup.select_one(".results-sort label"))
        fm["orden"] = orden

    # Filtros: hay 3 tipos de control (checkbox, radio y switch). Los conteos
    # del original son curados a mano: se guardan como `esperado` para poder
    # contrastarlos contra la coleccion.
    grupos = []
    for g in soup.select(".filter-group"):
        toggle = g.select_one(".filter-toggle")
        titulo = txt(toggle.select_one("span")) if toggle else None
        ops, tipo = [], None
        for l in g.select(".filter-checkbox, .filter-radio, .filter-switch"):
            i = l.find("input")
            if not i:
                continue
            clases = l.get("class") or []
            tipo = ("switch" if "filter-switch" in clases
                    else "radio" if "filter-radio" in clases else "checkbox")
            # el switch no tiene .count; el radio lleva estrellas + texto + count
            spans = [s for s in l.find_all("span") if "switch-slider" not in (s.get("class") or [])]
            etiquetas = [s for s in spans if "count" not in (s.get("class") or [])
                         and "stars" not in (s.get("class") or [])]
            cuenta_el = l.select_one(".count")
            cuenta = None
            if cuenta_el:
                m = re.search(r"(\d+)", txt(cuenta_el) or "")
                cuenta = int(m.group(1)) if m else None
            estrellas = l.select_one(".stars")
            ops.append({k: v for k, v in {
                "name": i.get("name"),
                "value": i.get("value"),
                "texto": txt(etiquetas[0]) if etiquetas else None,
                "estrellas": txt(estrellas) if estrellas else None,
                "marcado": i.has_attr("checked"),
                "esperado": cuenta,
            }.items() if v is not None})
        if ops:
            # el grupo del switch no lleva .filter-toggle ni titulo
            grupos.append({k: v for k, v in {
                "titulo": titulo,
                "tipo": tipo,
                "abierto": "active" in (toggle.get("class") or []) if toggle else None,
                "opciones": ops,
            }.items() if v is not None})
    if grupos:
        fm["filtrosTitulo"] = txt(soup.select_one(".filters-header h3"))
        fm["filtrosLimpiar"] = txt(soup.select_one(".btn-clear-filters"))
        fm["filtros"] = grupos

    # CTA
    cta = soup.select_one(".business-cta")
    if cta:
        a = cta.select_one("a")
        fm["cta"] = {k: v for k, v in {
            "titulo": txt(cta.select_one(".cta-title")),
            "texto": txt(cta.select_one(".cta-description")),
            "botonTexto": txt(a) if a else None,
            "botonHref": a.get("href") if a else None,
        }.items() if v}

    # prosa SEO -> cuerpo markdown
    art = soup.select_one(".seo-article")
    cuerpo = []
    if art:
        fm["seoTitulo"] = txt(art.find("h2"))
        for el in art.find_all(["p", "h3", "ul"], recursive=False):
            if el.name == "p":
                cuerpo.append(md_inline(el))
            elif el.name == "h3":
                cuerpo.append(f"### {txt(el)}")
            elif el.name == "ul":
                for li in el.find_all("li", recursive=False):
                    cuerpo.append(f"- {md_inline(li)}")

    fm["legacyUrl"] = f"/categoria/{cat}.html"
    fm = OrderedDict((k, v) for k, v in fm.items() if v not in (None, "", [], {}))

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, cat + ".md"), "w", encoding="utf-8") as f:
        f.write("---\n" + to_yaml(fm) + "\n---\n\n" + "\n\n".join(cuerpo) + "\n")

    # guarda: si el HTML tiene mas grupos/controles de los extraidos, algo se perdio
    esperado = {
        "grupos": len(soup.select(".filter-group")),
        "controles": len(soup.select(".filter-checkbox, .filter-radio, .filter-switch")),
        "subcats": len(soup.select(".subcategory-chip")),
        "orden": len(soup.select(".sort-select option")),
        "parrafos": len(soup.select(".seo-article p")),
    }
    obtenido = {
        "grupos": len(fm.get("filtros", [])),
        "controles": sum(len(g["opciones"]) for g in fm.get("filtros", [])),
        "subcats": len(fm.get("subcategorias", [])),
        "orden": len(fm.get("orden", [])),
        "parrafos": len([c for c in cuerpo if not c.startswith(("#", "-"))]),
    }
    perdidas = {k: (esperado[k], obtenido[k]) for k in esperado if esperado[k] != obtenido[k]}

    return {
        "cat": cat,
        "subcats": obtenido["subcats"],
        "grupos": obtenido["grupos"],
        "opciones": obtenido["controles"],
        "orden": obtenido["orden"],
        "chars": sum(len(c) for c in cuerpo),
        "negociosListados": len(soup.select(".business-card")),
        "perdidas": perdidas,
    }


def main():
    cargar_iconos()
    print(f"iconos ya registrados: {len(ICON_REGISTRY)}")
    filas = [process(c) for c in CATS]
    for r in filas:
        marca = "OK" if not r["perdidas"] else "!!"
        print(f"  {marca} {r['cat']:<26} {r['subcats']} subcats · {r['grupos']} grupos "
              f"({r['opciones']} controles) · {r['orden']} orden · {r['chars']} chars prosa "
              f"· listaba {r['negociosListados']} negocios")
        for k, (esp, obt) in r["perdidas"].items():
            print(f"      PERDIDA {k}: el HTML tiene {esp}, extraje {obt}")

    if any(r["perdidas"] for r in filas):
        print("\n!! Hay perdidas — no continuar hasta arreglarlas")
    else:
        print("\n✓ 0 bloques perdidos en las 3 categorias")

    if NUEVOS:
        print(f"\n{len(NUEVOS)} iconos nuevos -> se anaden a src/lib/icons.ts")
        with open(ICONS, "a", encoding="utf-8") as f:
            f.write("\n// Anadidos por extract_categorias.py\n")
            f.write("Object.assign(icons, {\n")
            for inner, nombre in NUEVOS.items():
                esc = inner.replace("\\", "\\\\").replace("`", "\\`")
                f.write(f"  {json.dumps(nombre)}: `{esc}`,\n")
            f.write("});\n")
        for n in NUEVOS.values():
            print(f"   - {n}")


if __name__ == "__main__":
    main()
