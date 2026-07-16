#!/usr/bin/env python3
"""
Los filtros de las paginas de categoria nunca filtraron nada: las tarjetas no
llevaban ningun atributo de datos y categoria.js solo hacia console.log.

Para que filtren de verdad hace falta saber que negocio cumple que filtro.
Ese dato no existe en ningun sitio... salvo en los conteos "(3)", "(4)" que
alguien escribio a mano en el HTML.

Este script deduce las etiquetas de cada negocio a partir de sus datos reales
(direccion, rating, badges, servicios, horarios) y CONTRASTA el resultado
contra esos conteos. Si no cuadran, lo dice: no se inventa nada.
"""
import re, os, glob, sys, unicodedata
import yaml

ROOT = "/Users/frankoropeza/Desktop/CLIENTES/PAGINASAMARILLAS"
NEG = os.path.join(ROOT, "src/content/negocios")
CAT = os.path.join(ROOT, "src/content/categorias")

SIN_DATO = []


def sinacentos(s):
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def cargar(path):
    raw = open(path, encoding="utf-8").read()
    partes = raw.split("---", 2)
    return yaml.safe_load(partes[1]), partes[2], raw


def texto_negocio(d):
    """Todo el texto util del negocio, para buscar palabras clave."""
    trozos = [d.get("nombre"), d.get("tagline"), d.get("descripcionLarga"), d.get("slogan")]
    for s in d.get("servicios", []) or []:
        trozos += [s.get("titulo"), s.get("descripcion")] + (s.get("features") or [])
    for c in d.get("catalogo", []) or []:
        trozos += [c.get("nombre"), c.get("descripcion")]
    for c in d.get("directorio", []) or []:
        trozos += [c.get("titulo"), c.get("descripcion"), c.get("tag")]
    for q in d.get("quickInfo", []) or []:
        trozos += [q.get("titulo"), q.get("texto")]
    for col in d.get("cobertura", []) or []:
        trozos.append(col.get("titulo"))
        trozos += [i.get("texto") for i in (col.get("items") or [])]
    trozos += d.get("badges", []) or []
    trozos += d.get("keywords", []) or []
    return sinacentos(" ".join(t for t in trozos if t))


# Palabras que identifican cada filtro. Solo se usan para PROPONER; el conteo
# original manda como verificacion.
CLAVES = {
    "guardias": ["guardia", "vigilante", "vigilancia", "custodio"],
    "escoltas": ["escolta", "proteccion ejecutiva", "vip", "guardaespalda"],
    "eventos": ["evento", "concierto", "festival", "boda"],
    "monitoreo": ["monitoreo", "cctv", "camara", "alarma", "24/7"],
    "condominios": ["condominio", "residencial", "fraccionamiento"],
    "iluminacion": ["iluminacion", "luces", "led", "guirnalda"],
    "sonido": ["sonido", "audio", "bocina", "bafle"],
    "escenarios": ["escenario", "tarima", "templete", "podium"],
    "inflables": ["inflable", "brincolin", "castillo"],
    "tecnologia": ["pantalla", "led", "tecnologia", "video", "proyecc"],
    "extintores": ["extintor", "extincion"],
    "sistemas": ["sistema automatico", "rociador", "sprinkler", "deteccion", "alarma contra"],
    "bomberos": ["bombero", "traje", "casco", "scba", "epp"],
    "mangueras": ["manguera", "monitor", "hidrante", "boquilla"],
    "cnsp": ["cnsp"],
    "ssc": ["ssc"],
    "nfpa": ["nfpa"],
    "elkhart": ["elkhart"],
    "verificado": ["verificad"],
    "24h": ["24/7", "24 horas", "24h"],
}

ESTADOS = {
    "cdmx": ["cdmx", "ciudad de mexico", "df"],
    "edomex": ["estado de mexico", "edomex", "naucalpan", "tlalnepantla", "mex."],
    "qro": ["queretaro", "qro"],
}


def etiquetas_de(d):
    """
    Solo se etiqueta lo que se puede afirmar con un dato duro.

    Buscar palabras clave en la prosa NO sirve: casi toda ficha de
    entretenimiento menciona "iluminacion" aunque no la ofrezca, y salian
    6 de 7 donde el original decia 4. Un filtro que devuelve resultados
    falsos es peor que uno que no filtra.
    """
    et = set()

    # UBICACION <- direccion fisica. areaServed queda fuera a proposito:
    # dice donde da servicio, no donde esta.
    dirn = d.get("direccion") or {}
    est = sinacentos(f"{dirn.get('estado','')} {dirn.get('colonia','')} {dirn.get('calle','')}")
    for k, palabras in ESTADOS.items():
        if any(p in est for p in palabras):
            et.add(k)

    # CERTIFICACIONES <- badges, que son afirmaciones explicitas
    badges = sinacentos(" ".join(d.get("badges", []) or []))
    if "cnsp" in badges:
        et.add("cnsp")
    if "ssc" in badges:
        et.add("ssc")
    if "nfpa" in badges:
        et.add("nfpa")
    if "elkhart" in badges:
        et.add("elkhart")
    if "verificad" in badges:
        et.add("verificado")

    # RATING: el control es un radio con valores 4.9 / 4.8 / 4.6, y la etiqueta
    # del original dice "4.6+ estrellas" -> es un umbral, no un valor exacto.
    # No se etiqueta aqui: el filtrado compara rating >= valor en el cliente.

    return et


def main():
    # negocios por categoria
    negocios = {}
    for f in sorted(glob.glob(os.path.join(NEG, "*", "*.md"))):
        cat = os.path.basename(os.path.dirname(f))
        slug = os.path.basename(f)[:-3]
        d, cuerpo, raw = cargar(f)
        negocios.setdefault(cat, []).append((slug, d, f))

    propuestas = {}
    for cat, lista in negocios.items():
        for slug, d, f in lista:
            propuestas[(cat, slug)] = etiquetas_de(d)

    # contrasta contra los conteos curados del HTML original
    print("CONTRASTE: conteo escrito a mano en el HTML  vs  lo que sale de los datos\n")
    total_ok = total_mal = 0
    todas = set().union(*propuestas.values()) if propuestas else set()
    for cf in sorted(glob.glob(os.path.join(CAT, "*.md"))):
        cat = os.path.basename(cf)[:-3]
        d, _, _ = cargar(cf)
        print(f"=== {cat} ({len(negocios.get(cat, []))} negocios) ===")
        for g in d.get("filtros", []) or []:
            titulo = g.get("titulo") or g.get("tipo")
            for o in g.get("opciones", []):
                esp = o.get("esperado")
                val = o.get("value")
                if esp is None or val is None:
                    continue
                if o.get("name") == "rating":
                    # umbral: cuenta los negocios con rating >= valor
                    umbral = float(val)
                    real = sum(1 for s, dd, _ in negocios.get(cat, [])
                               if (dd.get("rating") or {}).get("valor", 0) >= umbral)
                    marca = "ok " if real == esp else "MAL"
                    total_ok, total_mal = (total_ok + 1, total_mal) if real == esp else (total_ok, total_mal + 1)
                    print(f"   {marca} {titulo:<16} {o.get('texto','')[:26]:<28} "
                          f"escrito:{esp}  real:{real}")
                    continue

                clave = val
                if clave not in todas:
                    SIN_DATO.append(f"{cat} · {titulo} · {o.get('texto','')} (decia {esp})")
                    print(f"   -   {titulo:<16} {o.get('texto','')[:26]:<28} "
                          f"escrito:{esp}  sin dato que lo sustente")
                    continue

                real = sum(1 for (c, s), et in propuestas.items()
                           if c == cat and clave in et)
                marca = "ok " if real == esp else "MAL"
                if real == esp:
                    total_ok += 1
                else:
                    total_mal += 1
                print(f"   {marca} {titulo:<16} {o.get('texto','')[:26]:<28} "
                      f"escrito:{esp}  real:{real}")
        print()

    print(f"coinciden: {total_ok} · NO coinciden: {total_mal}")
    if SIN_DATO:
        print(f"\n{len(SIN_DATO)} filtros que NO se pueden alimentar con datos existentes:")
        for s in SIN_DATO:
            print(f"   - {s}")
        print("\n  Saber que empresa ofrece 'Escoltas Ejecutivos' es informacion que\n"
              "  nadie guardo nunca: solo existia como un numero escrito a mano.\n"
              "  Estos grupos no se renderizan hasta que las fichas se etiqueten;\n"
              "  es preferible a mostrar un filtro que miente.")

    # escribe las etiquetas en el frontmatter de cada negocio
    escritos = 0
    for (cat, slug), et in sorted(propuestas.items()):
        f = os.path.join(NEG, cat, slug + ".md")
        raw = open(f, encoding="utf-8").read()
        if "\netiquetas:" in raw:
            raw = re.sub(r"\netiquetas:\n(?:  - .*\n)+", "\n", raw)
        bloque = "\n".join(f'  - "{e}"' for e in sorted(et))
        raw = raw.replace("\nlegacyUrl:", f"\netiquetas:\n{bloque}\nlegacyUrl:", 1)
        open(f, "w", encoding="utf-8").write(raw)
        escritos += 1

    print(f"\netiquetas escritas en {escritos} fichas")
    for (cat, slug), et in sorted(propuestas.items()):
        print(f"   {cat}/{slug:<32} {' '.join(sorted(et))}")


if __name__ == "__main__":
    main()
