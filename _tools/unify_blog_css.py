#!/usr/bin/env python3
"""
Los 42 articulos del blog llevaban ~8 KB de CSS inline cada uno (336 KB en
total) con 9 variantes del mismo sistema de estilos. Esto lo funde en un solo
src/styles/blog.css y reporta EXACTAMENTE que articulos cambian de aspecto.

Ante un conflicto gana la variante usada por mas articulos.
"""
import re, glob, os
from collections import defaultdict, Counter
from bs4 import BeautifulSoup

ROOT = "/Users/frankoropeza/Desktop/CLIENTES/PAGINASAMARILLAS"
SRC = os.path.join(ROOT, "_legacy/blog-original")
OUT = os.path.join(ROOT, "src/styles/blog.css")


def norm_dec(d):
    """Normaliza declaraciones para comparar: espacios y orden fuera."""
    d = re.sub(r"/\*.*?\*/", "", d, flags=re.S)
    props = []
    for p in d.split(";"):
        p = p.strip()
        if not p or ":" not in p:
            continue
        k, v = p.split(":", 1)
        props.append((k.strip().lower(), re.sub(r"\s+", " ", v).strip()))
    return tuple(sorted(props))


def dec_a_texto(props):
    return "\n".join(f"  {k}: {v};" for k, v in props)


def parse(css):
    """Devuelve [(contexto_media, selector, props)]. Naive pero suficiente."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    reglas = []

    # extrae bloques @media primero
    def comer_media(texto):
        salida, resto, i = [], [], 0
        while i < len(texto):
            m = re.search(r"@media([^{]+)\{", texto[i:])
            if not m:
                resto.append(texto[i:])
                break
            ini = i + m.start()
            resto.append(texto[i:ini])
            j = i + m.end()
            prof, k = 1, j
            while k < len(texto) and prof:
                if texto[k] == "{":
                    prof += 1
                elif texto[k] == "}":
                    prof -= 1
                k += 1
            salida.append((f"@media{m.group(1).strip()}", texto[j:k - 1]))
            i = k
        return salida, "".join(resto)

    medias, plano = comer_media(css)

    def reglas_de(texto, ctx):
        for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", texto):
            sel = re.sub(r"\s+", " ", m.group(1)).strip()
            if not sel or sel.startswith("@"):
                continue
            props = norm_dec(m.group(2))
            if props:
                reglas.append((ctx, sel, props))

    reglas_de(plano, "")
    for ctx, cuerpo in medias:
        reglas_de(cuerpo, ctx)
    return reglas


def main():
    por_art = {}
    for f in sorted(glob.glob(os.path.join(SRC, "*", "*.html"))):
        if "/templates/" in f or "/categorias/" in f:
            continue
        raw = open(f, encoding="utf-8").read()
        if not raw.strip():
            continue
        s = BeautifulSoup(raw, "lxml")
        css = "".join(x.string or "" for x in s.find_all("style"))
        if css.strip():
            por_art[f"{os.path.basename(os.path.dirname(f))}/{os.path.basename(f)[:-5]}"] = css

    # (ctx, sel) -> props -> [articulos]
    votos = defaultdict(lambda: defaultdict(list))
    for art, css in por_art.items():
        for ctx, sel, props in parse(css):
            votos[(ctx, sel)][props].append(art)

    # Fusion por PROPIEDAD, no por bloque entero: si una variante declara
    # `position: relative` y otra no, se conserva. Solo se vota cuando dos
    # variantes dan valores distintos a la MISMA propiedad. Asi nunca se
    # pierde una declaracion que algun articulo necesitaba.
    ganadoras = {}
    perdedores = defaultdict(list)  # articulo -> [(sel, prop, suyo, gana)]

    for clave, opciones in votos.items():
        # prop -> valor -> [articulos]
        por_prop = defaultdict(lambda: defaultdict(list))
        for props, arts in opciones.items():
            for k, v in props:
                por_prop[k][v].extend(arts)

        final = []
        for prop, valores in por_prop.items():
            gana = max(valores.items(), key=lambda kv: len(kv[1]))[0]
            final.append((prop, gana))
            for v, arts in valores.items():
                if v != gana:
                    for a in arts:
                        perdedores[a].append((clave[1], prop, v, gana))
        ganadoras[clave] = tuple(sorted(final))

    # escribe el css unificado
    por_ctx = defaultdict(list)
    for (ctx, sel), props in ganadoras.items():
        por_ctx[ctx].append((sel, props))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("/* Estilos del blog.\n"
                "   Generado por _tools/unify_blog_css.py a partir del CSS inline que\n"
                "   los 42 articulos repetian (336 KB -> este archivo).\n"
                "   Ante variantes en conflicto gano la usada por mas articulos. */\n\n")
        for sel, props in sorted(por_ctx[""]):
            f.write(f"{sel} {{\n{dec_a_texto(props)}\n}}\n\n")
        for ctx in sorted(k for k in por_ctx if k):
            f.write(f"{ctx} {{\n")
            for sel, props in sorted(por_ctx[ctx]):
                cuerpo = "\n".join(f"    {k}: {v};" for k, v in props)
                f.write(f"  {sel} {{\n{cuerpo}\n  }}\n\n")
            f.write("}\n\n")

    total_reglas = sum(len(v) for v in por_ctx.values())
    inline_total = sum(len(c) for c in por_art.values())
    nuevo = os.path.getsize(OUT)
    print(f"{len(por_art)} articulos con CSS inline")
    print(f"CSS inline total : {inline_total:,} bytes")
    print(f"blog.css unificado: {nuevo:,} bytes ({total_reglas} reglas)")
    print(f"ahorro: {inline_total - nuevo:,} bytes ({100*(1-nuevo/inline_total):.0f}%)")

    # Un cambio es "cosmetico" si solo normaliza un literal a su variable
    # equivalente o reordena espacios; el resto son cambios visuales reales.
    def cosmetico(viejo, nuevo):
        v = re.sub(r"[\s,]+", "", viejo.lower())
        n = re.sub(r"[\s,]+", "", nuevo.lower())
        return v == n or nuevo.startswith("var(")

    reales = defaultdict(list)
    n_cosm = 0
    for art, difs in perdedores.items():
        for sel, prop, viejo, nuevo in difs:
            if cosmetico(viejo, nuevo):
                n_cosm += 1
            else:
                reales[art].append((sel, prop, viejo, nuevo))

    print(f"\ncambios cosmeticos (literal -> variable, espacios): {n_cosm}")
    print(f"articulos con CAMBIO VISUAL REAL: {len(reales)}")
    for art, difs in sorted(reales.items(), key=lambda kv: -len(kv[1])):
        print(f"\n  {art}  ({len(difs)})")
        for sel, prop, viejo, nuevo in difs[:4]:
            print(f"     {sel} · {prop}: {viejo} -> {nuevo}")
        if len(difs) > 4:
            print(f"     ... y {len(difs)-4} mas")


if __name__ == "__main__":
    main()
