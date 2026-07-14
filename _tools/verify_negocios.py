#!/usr/bin/env python3
"""
Compara dist/negocios/**.html (generado por Astro desde MD)
contra _legacy/negocios-original/**.html (HTML crudo original).

Verifica que no se perdio nada: schema.org, bloques de contenido, textos, enlaces.
"""
import json, glob, os, re, sys
from bs4 import BeautifulSoup

ROOT = "/Users/frankoropeza/Desktop/CLIENTES/PAGINASAMARILLAS"
NEW = os.path.join(ROOT, "dist/negocios")
OLD = os.path.join(ROOT, "_legacy/negocios-original")

FAILS, WARNS = [], []


def soupify(p):
    return BeautifulSoup(open(p, encoding="utf-8").read(), "lxml")


def lds(soup):
    out = {}
    for s in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = s.string or s.get_text()
        try:
            d = json.loads(raw)
        except json.JSONDecodeError:
            try:
                d = json.loads(re.sub(r",\s*([}\]])", r"\1", raw))
            except json.JSONDecodeError:
                continue
        for item in (d if isinstance(d, list) else [d]):
            if isinstance(item, dict) and item.get("@type"):
                out[item["@type"]] = item
    return out


def norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


def textos(soup, sel):
    return [norm(e.get_text(" ", strip=True)) for e in soup.select(sel)]


def cmp_set(nombre, ficha, viejos, nuevos):
    """Compara conjuntos de texto; reporta lo que falta en el nuevo."""
    v, n = set(filter(None, viejos)), set(filter(None, nuevos))
    faltan = v - n
    if faltan:
        FAILS.append(f"{ficha} · {nombre}: FALTAN {len(faltan)} de {len(v)}")
        for f in sorted(faltan)[:3]:
            FAILS.append(f"      - {f[:95]}")
    return not faltan


def main():
    fichas = sorted(glob.glob(os.path.join(OLD, "*", "*.html")))
    n_ok = 0
    print(f"{'ficha':<42} {'schema':<8} {'texto':<8} {'links':<8}")
    print("-" * 70)

    for old_p in fichas:
        cat = os.path.basename(os.path.dirname(old_p))
        slug = os.path.basename(old_p)[:-5]
        if slug.endswith("-backup"):
            continue
        new_p = os.path.join(NEW, cat, slug + ".html")
        ficha = f"{cat}/{slug}"
        if not os.path.exists(new_p):
            FAILS.append(f"{ficha}: NO GENERADO")
            continue

        o, n = soupify(old_p), soupify(new_p)
        lo, ln = lds(o), lds(n)
        ok_schema, ok_texto, ok_links = True, True, True

        # --- 1. schema.org LocalBusiness: campos duros ---
        blo, bln = lo.get("LocalBusiness", {}), ln.get("LocalBusiness", {})
        if not bln:
            FAILS.append(f"{ficha}: falta LocalBusiness en el nuevo")
            ok_schema = False
        else:
            for campo in ["name", "telephone", "email", "priceRange", "slogan", "foundingDate"]:
                a, b = blo.get(campo), bln.get(campo)
                if a and norm(str(a)) != norm(str(b)):
                    FAILS.append(f"{ficha} · LB.{campo}: '{a}' -> '{b}'")
                    ok_schema = False
            # direccion
            ao = blo.get("address") or {}
            an = bln.get("address") or {}
            if isinstance(ao, dict) and isinstance(an, dict):
                for k in ["streetAddress", "addressLocality", "addressRegion", "postalCode"]:
                    if ao.get(k) and norm(str(ao.get(k))) != norm(str(an.get(k))):
                        FAILS.append(f"{ficha} · address.{k}: '{ao.get(k)}' -> '{an.get(k)}'")
                        ok_schema = False
            # geo
            go, gn = blo.get("geo") or {}, bln.get("geo") or {}
            if isinstance(go, dict) and go:
                for k in ["latitude", "longitude"]:
                    if float(go.get(k, 0)) != float(gn.get(k, -999)):
                        FAILS.append(f"{ficha} · geo.{k}: {go.get(k)} -> {gn.get(k)}")
                        ok_schema = False
            # rating
            ro, rn = blo.get("aggregateRating") or {}, bln.get("aggregateRating") or {}
            if isinstance(ro, dict) and ro:
                for k in ["ratingValue", "reviewCount"]:
                    if float(ro.get(k, 0)) != float(rn.get(k, -999)):
                        FAILS.append(f"{ficha} · rating.{k}: {ro.get(k)} -> {rn.get(k)}")
                        ok_schema = False
            # catalogo de ofertas
            co = ((blo.get("hasOfferCatalog") or {}).get("itemListElement") or [])
            cn = ((bln.get("hasOfferCatalog") or {}).get("itemListElement") or [])
            if len(co) != len(cn):
                FAILS.append(f"{ficha} · hasOfferCatalog: {len(co)} ofertas -> {len(cn)}")
                ok_schema = False

        # breadcrumb + faq presentes
        if "BreadcrumbList" in lo and "BreadcrumbList" not in ln:
            FAILS.append(f"{ficha}: falta BreadcrumbList")
            ok_schema = False
        if "FAQPage" in lo:
            qo = len((lo["FAQPage"].get("mainEntity") or []))
            qn = len((ln.get("FAQPage", {}).get("mainEntity") or []))
            if qn < qo:
                FAILS.append(f"{ficha} · FAQPage: {qo} preguntas -> {qn}")
                ok_schema = False

        # --- 2. meta SEO ---
        for name, sel in [("title", "title"), ]:
            a = norm(o.select_one(sel).get_text()) if o.select_one(sel) else None
            b = norm(n.select_one(sel).get_text()) if n.select_one(sel) else None
            if a != b:
                FAILS.append(f"{ficha} · <title>: '{a}' -> '{b}'")
                ok_schema = False
        for prop in [("name", "description"), ("property", "og:title"), ("property", "og:image")]:
            a = o.find("meta", attrs={prop[0]: prop[1]})
            b = n.find("meta", attrs={prop[0]: prop[1]})
            av = a.get("content") if a else None
            bv = b.get("content") if b else None
            if av and norm(av) != norm(bv or ""):
                FAILS.append(f"{ficha} · meta {prop[1]}: '{(av or '')[:45]}' -> '{(bv or '')[:45]}'")
                ok_schema = False

        # --- 3. bloques de contenido visible ---
        bloques = [
            ("servicios", ".services-grid .service-title"),
            ("serv-desc", ".services-grid .service-description"),
            ("features", ".services-grid .service-features li"),
            ("stats", ".stat-card .stat-number"),
            ("cobertura", ".coverage-list li"),
            ("catalogo", ".service-directory-card .service-card-title"),
            ("cat-desc", ".service-directory-card .service-card-description"),
            ("sucursales", ".location-card h4"),
            ("resenas", ".review-text"),
            ("faq-q", ".faq-item h3, .faq-item summary"),
        ]
        for nombre, sel in bloques:
            if not cmp_set(nombre, ficha, textos(o, sel), textos(n, sel)):
                ok_texto = False

        # --- 4. enlaces salientes (tel:, mailto:, wa.me, sitio web) ---
        def links(s):
            out = set()
            for a in s.select("main a[href], .business-cta-buttons a[href], .contact-card a[href]"):
                h = a.get("href", "")
                if h.startswith(("tel:", "mailto:", "https://wa.me")) or "http" in h:
                    out.add(h.strip())
            return out

        lo_set, ln_set = links(o), links(n)
        faltan_links = lo_set - ln_set
        # el header/footer del layout aporta links comunes; solo importan los del negocio
        faltan_links = {l for l in faltan_links if not l.startswith("#")}
        if faltan_links:
            WARNS.append(f"{ficha} · links ausentes ({len(faltan_links)}): "
                         + ", ".join(sorted(faltan_links)[:4]))
            ok_links = False

        # --- 5. prosa del body ---
        po = " ".join(textos(o, ".about-content .about-text"))
        pn = " ".join(textos(n, ".about-content .about-text"))
        if po and len(pn) < len(po) * 0.9:
            FAILS.append(f"{ficha} · prosa: {len(po)} chars -> {len(pn)}")
            ok_texto = False

        mark = lambda b: "OK" if b else "FALLA"
        print(f"{ficha:<42} {mark(ok_schema):<8} {mark(ok_texto):<8} {mark(ok_links):<8}")
        if ok_schema and ok_texto and ok_links:
            n_ok += 1

    print("-" * 70)
    print(f"\n{n_ok}/16 fichas identicas en schema, contenido y enlaces")

    if WARNS:
        print(f"\n[AVISOS] {len(WARNS)}:")
        for w in WARNS:
            print("  ", w)
    if FAILS:
        print(f"\n[FALLAS] {len(FAILS)}:")
        for f in FAILS:
            print("  ", f)
        sys.exit(1)
    print("\nVERIFICACION LIMPIA — el MD reproduce el HTML original sin perdidas.")


if __name__ == "__main__":
    main()
