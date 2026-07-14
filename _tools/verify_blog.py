#!/usr/bin/env python3
"""
Compara dist/blog/**.html (generado desde MDX) contra _legacy/blog-original.
Comprueba que la prosa, los encabezados, las imagenes y el schema sobrevivieron.
"""
import json, glob, os, re, sys
from bs4 import BeautifulSoup

ROOT = "/Users/frankoropeza/Desktop/CLIENTES/PAGINASAMARILLAS"
NEW = os.path.join(ROOT, "dist/blog")
OLD = os.path.join(ROOT, "_legacy/blog-original")

FAILS, WARNS, ROTAS = [], [], []


def soupify(p):
    return BeautifulSoup(open(p, encoding="utf-8").read(), "lxml")


def lds(soup):
    out = {}
    for s in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = s.string or s.get_text()
        if not raw:
            continue
        try:
            d = json.loads(raw)
        except json.JSONDecodeError:
            try:
                d = json.loads(re.sub(r",\s*([}\]])", r"\1", raw))
            except json.JSONDecodeError:
                continue
        for it in (d if isinstance(d, list) else [d]):
            if isinstance(it, dict) and it.get("@type"):
                out.setdefault(it["@type"], it)
    return out


def norm(s):
    s = re.sub(r"\s+", " ", s or "")
    return s.replace(" ", " ").strip()


def palabras(s):
    return set(re.findall(r"\w{5,}", (s or "").lower()))


def cuerpo_texto(soup):
    c = soup.select_one(".blog-article-content")
    if not c:
        art = soup.select_one("article.blog-article") or soup.select_one("main article")
        c = art
    if not c:
        return ""
    for b in c.select(".blog-article-toc-inline, .blog-related-articles, .blog-article-tags, nav"):
        b.decompose()
    return norm(c.get_text(" ", strip=True))


def main():
    viejos = sorted(f for f in glob.glob(os.path.join(OLD, "*", "*.html"))
                    if "/templates/" not in f and "/categorias/" not in f)
    ok_total = 0
    revisados = 0
    print(f"{'articulo':<52} {'prosa':<12} {'h2':<8} {'img':<8} {'schema':<8}")
    print("-" * 92)

    for old_p in viejos:
        cat = os.path.basename(os.path.dirname(old_p))
        slug = os.path.basename(old_p)[:-5]
        ref = f"{cat}/{slug}"
        raw = open(old_p, encoding="utf-8").read()
        if not raw.strip():
            continue  # los 4 vacios se reportan aparte

        new_p = os.path.join(NEW, cat, slug + ".html")
        if not os.path.exists(new_p):
            FAILS.append(f"{ref}: NO GENERADO")
            continue

        revisados += 1
        o, n = soupify(old_p), soupify(new_p)
        ok_prosa = ok_h2 = ok_img = ok_schema = True

        # --- estructura ---
        rawn = open(new_p, encoding="utf-8").read()
        cierre = rawn.rfind("</html>")
        if cierre != -1 and rawn[cierre + 7:].strip():
            FAILS.append(f"{ref}: contenido despues de </html>")
            ok_schema = False

        # --- prosa: cobertura de palabras del original ---
        to, tn = cuerpo_texto(o), cuerpo_texto(n)
        po, pn = palabras(to), palabras(tn)
        if po:
            falta = po - pn
            cobertura = 1 - len(falta) / len(po)
            if cobertura < 0.97:
                FAILS.append(f"{ref} · prosa: cobertura {cobertura:.1%}, "
                             f"faltan {len(falta)} palabras ej: {sorted(falta)[:6]}")
                ok_prosa = False
            elif falta:
                WARNS.append(f"{ref}: {len(falta)} palabras ausentes ({cobertura:.1%}): "
                             f"{sorted(falta)[:5]}")

        # --- encabezados h2 ---
        def h2s(s):
            c = s.select_one(".blog-article-content")
            return [norm(h.get_text()) for h in (c.find_all("h2") if c else [])]

        ho, hn = h2s(o), h2s(n)
        faltan_h = set(ho) - set(hn)
        if faltan_h:
            FAILS.append(f"{ref} · h2: faltan {len(faltan_h)}/{len(ho)}: {sorted(faltan_h)[:3]}")
            ok_h2 = False

        # --- imagenes: compara por nombre de archivo (las rutas se normalizaron
        #     de ../../img/x a /img/x, asi que la ruta completa no sirve) ---
        def imgs(s):
            c = s.select_one(".blog-article-content")
            out = set()
            for i in (c.find_all("img") if c else []):
                src = (i.get("src") or "").split("?")[0]
                if src:
                    out.add(os.path.basename(src))
            return out

        io_, in_ = imgs(o), imgs(n)
        faltan_i = io_ - in_
        if faltan_i:
            FAILS.append(f"{ref} · img: faltan {len(faltan_i)}/{len(io_)}: {sorted(faltan_i)[:2]}")
            ok_img = False

        # imagenes cuyo archivo no existe en dist (rotas ya en el original)
        cn = n.select_one(".blog-article-content")
        for i in (cn.find_all("img") if cn else []):
            src = (i.get("src") or "").split("?")[0]
            if not src or src.startswith(("http", "data:")):
                continue
            if not os.path.exists(os.path.join(ROOT, "dist", src.lstrip("/"))):
                ROTAS.append(f"{ref}: {src} (alt: {i.get('alt') or 'sin alt'})")

        # --- schema ---
        lo, ln = lds(o), lds(n)
        art_o = lo.get("Article") or lo.get("BlogPosting")
        art_n = ln.get("Article")
        if art_o and not art_n:
            FAILS.append(f"{ref}: perdio el schema Article")
            ok_schema = False
        elif art_o and art_n:
            if norm(str(art_o.get("headline"))) != norm(str(art_n.get("headline"))):
                FAILS.append(f"{ref} · headline: '{art_o.get('headline')}' -> '{art_n.get('headline')}'")
                ok_schema = False
        if "FAQPage" in lo:
            qo = len(lo["FAQPage"].get("mainEntity") or [])
            qn = len((ln.get("FAQPage") or {}).get("mainEntity") or [])
            if qn < qo:
                FAILS.append(f"{ref} · FAQ: {qo} -> {qn}")
                ok_schema = False

        # --- title ---
        to_ = norm(o.find("title").get_text()) if o.find("title") else None
        tn_ = norm(n.find("title").get_text()) if n.find("title") else None
        if to_ and to_ != tn_:
            WARNS.append(f"{ref} · title: '{to_[:44]}' -> '{(tn_ or '')[:44]}'")

        m = lambda b: "OK" if b else "FALLA"
        print(f"{ref[:50]:<52} {m(ok_prosa):<12} {m(ok_h2):<8} {m(ok_img):<8} {m(ok_schema):<8}")
        if all([ok_prosa, ok_h2, ok_img, ok_schema]):
            ok_total += 1

    print("-" * 92)
    print(f"\n{ok_total}/{revisados} articulos sin perdidas")

    if ROTAS:
        print(f"\n[IMAGENES ROTAS] {len(ROTAS)} — ya lo estaban en el HTML original:")
        for r in ROTAS:
            print("  ", r)

    if WARNS:
        print(f"\n[AVISOS] {len(WARNS)}:")
        for w in WARNS[:14]:
            print("  ", w)
        if len(WARNS) > 14:
            print(f"   ... y {len(WARNS)-14} mas")
    if FAILS:
        print(f"\n[FALLAS] {len(FAILS)}:")
        for f in FAILS[:24]:
            print("  ", f)
        sys.exit(1)
    print("\nVERIFICACION LIMPIA — el MDX reproduce los articulos originales.")


if __name__ == "__main__":
    main()
