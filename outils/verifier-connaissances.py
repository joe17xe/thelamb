#!/usr/bin/env python3
"""La base de connaissances reflète les pages — ou la CI s'arrête.

Deux miroirs sont tenus : connaissances.yml (la déclaration lisible) et le
bloc CONSTEL de carte-du-ciel.html (la projection que les constellations du
ciel affichent). Les deux se régénèrent depuis la même mesure ; la CI refuse
tout écart de l'un comme de l'autre.

    python3 outils/verifier-connaissances.py            compare, échoue sur écart
    python3 outils/verifier-connaissances.py --ecrire   régénère connaissances.yml

Le site est statique : les pages porteront toujours leur donnée en ligne.
`connaissances.yml` n'est donc pas leur source d'exécution, c'est leur miroir
déclaré — le même pacte que navigation.yml avec le maillage. L'extracteur
(`extraire-connaissances.mjs`) mesure ce que les pages portent ; ce contrôle
refuse tout écart entre la mesure et la déclaration, dans les deux sens.
"""
import json
import os
import subprocess
import sys

import yaml

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
FICHIER = os.path.join(RACINE, "connaissances.yml")


def mesure():
    sortie = subprocess.run(
        ["node", os.path.join(ICI, "extraire-connaissances.mjs")],
        capture_output=True, text=True, cwd=RACINE)
    if sortie.returncode != 0:
        raise SystemExit("l'extracteur a échoué :\n" + sortie.stderr)
    d = json.loads(sortie.stdout)
    # Les référentiels déclarés ailleurs entrent au miroir par référence :
    # periodes.yml et navigation.yml restent leurs propres sources de vérité.
    d["periodes"] = [p["cle"] for p in
                     yaml.safe_load(open(os.path.join(RACINE, "periodes.yml"),
                                         encoding="utf-8"))["periodes"]]
    pages = []
    def visite(o):
        if isinstance(o, dict):
            if "fichier" in o:
                pages.append(o["fichier"])
            for v in o.values():
                visite(v)
        elif isinstance(o, list):
            for x in o:
                visite(x)
    carte = yaml.safe_load(open(os.path.join(RACINE, "navigation.yml"),
                                encoding="utf-8"))
    # Les ateliers et les pages retirées ne font pas partie du parcours : le
    # miroir compte les pages que le lecteur peut atteindre.
    visite({k: v for k, v in carte.items() if k not in ("ateliers", "obsoletes")})
    d["pages"] = sorted(pages)
    return d


def coherence(d):
    """Ce que le miroir doit respecter en lui-même, avant toute comparaison."""
    fautes = []
    pers = set(d["periodes"])
    for l in d["livres"]:
        for p in (l["periodes"] or []):
            if p not in pers:
                fautes.append("livre %s : période inconnue %r" % (l["id"], p))
        # Une place non tranchée est une hypothèse, pas un parcours : on ne peut
        # pas en même temps ignorer où le récit se situe et le couper en deux
        # tranches de chapitres.
        if not all(l.get("christ", {}).get(k) for k in ("fr", "en", "ar")):
            fautes.append("livre %s : le fil vers le Christ manque dans une langue"
                          % l["id"])
        if "debat" in l:
            if l.get("tranches"):
                fautes.append("livre %s : place débattue et tranches à la fois" % l["id"])
            if not all(l["debat"].get(k) for k in ("fr", "en", "ar")):
                fautes.append("livre %s : la raison du débat manque dans une langue" % l["id"])
    for p in d["prophetes"]:
        if p["epoque"] not in pers:
            fautes.append("prophète %s : époque inconnue %r" % (p["id"], p["epoque"]))
    for g in d["generations"]:
        if g.get("periode") and g["periode"] not in pers:
            fautes.append("génération %s : période inconnue %r"
                          % (g["nom"]["fr"], g["periode"]))
    if sum(t["compte"] for t in d["themes"].values()) != len(d["correspondances"]):
        fautes.append("les thèmes ne comptent pas les correspondances")
    return fautes


def compare(a, b, chemin=""):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a:
                yield "%s.%s : déclaré mais non mesuré" % (chemin, k)
            elif k not in b:
                yield "%s.%s : mesuré mais non déclaré" % (chemin, k)
            else:
                yield from compare(a[k], b[k], "%s.%s" % (chemin, k))
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            yield "%s : %d mesuré(s) contre %d déclaré(s)" % (chemin, len(a), len(b))
        for i, (x, y) in enumerate(zip(a, b)):
            yield from compare(x, y, "%s[%d]" % (chemin, i))
    elif a != b:
        yield "%s : mesuré %r ≠ déclaré %r" % (chemin, a, b)


MARQUE_A = "/*<CONSTEL>*/"
MARQUE_B = "/*</CONSTEL>*/"
CARTE = os.path.join(RACINE, "carte-du-ciel.html")


def bloc_constel(d):
    """La projection de la mesure que les constellations affichent."""
    pers = yaml.safe_load(open(os.path.join(RACINE, "periodes.yml"),
                               encoding="utf-8"))["periodes"]
    constel = {
        "etageres": d["etageres"],
        "periodes": {p["cle"]: {"c": p["couleur"],
                                "fr": p["fr"]["nom"], "en": p["en"]["nom"],
                                "ar": p["ar"]["nom"],
                                "d": {l: p[l]["dates"] for l in ("fr", "en", "ar")},
                                "t": {l: p[l]["texte"] for l in ("fr", "en", "ar")},
                                "f": {l: p[l]["figures"] for l in ("fr", "en", "ar")},
                                "e": {l: p[l].get("evenements", []) for l in ("fr", "en", "ar")}}
                     for p in pers},
        "livres": [[l["id"], l["etagere"], l["periodes"],
                    [l["nom"]["fr"], l["nom"]["en"], l["nom"]["ar"]],
                    [l["w"]["fr"], l["w"]["en"], l["w"]["ar"]],
                    ([l["lien"]["fr"], l["lien"]["en"], l["lien"]["ar"]]
                     if "lien" in l else None),
                    l.get("tranches"),
                    ([l["debat"]["fr"], l["debat"]["en"], l["debat"]["ar"]]
                     if "debat" in l else None),
                    [l["christ"]["fr"], l["christ"]["en"], l["christ"]["ar"]],
                    ([l["nuance"]["fr"], l["nuance"]["en"], l["nuance"]["ar"]]
                     if "nuance" in l else None)]
                   for l in d["livres"]],
        "themes": d["themes"],
        "prophetes": [[p["id"], p["epoque"], p["pos"],
                       [p["nom"]["fr"], p["nom"]["en"], p["nom"]["ar"]],
                       [p["date"]["fr"], p["date"]["en"], p["date"]["ar"]],
                       [p["vers"]["fr"], p["vers"]["en"], p["vers"]["ar"]]]
                      for p in d["prophetes"]],
        "generations": [[g.get("periode"),
                         [g["nom"]["fr"], g["nom"]["en"], g["nom"]["ar"]],
                         1 if g.get("fourche") else 0,
                         [g["note"]["fr"], g["note"]["en"], g["note"]["ar"]]]
                        for g in d["generations"]],
        "corr": [[c["theme"],
                  [c["titre"]["fr"], c["at"]["fr"], c["nt"]["fr"]],
                  [c["titre"]["en"], c["at"]["en"], c["nt"]["en"]],
                  [c["titre"]["ar"], c["at"]["ar"], c["nt"]["ar"]]]
                 for c in d["correspondances"]],
    }
    return (MARQUE_A + "const CONSTEL="
            + json.dumps(constel, ensure_ascii=False, separators=(",", ":"))
            + ";" + MARQUE_B)


def lire_bloc():
    src = open(CARTE, encoding="utf-8").read()
    a, b = src.find(MARQUE_A), src.find(MARQUE_B)
    if a < 0 or b < 0:
        return src, None
    return src, src[a:b + len(MARQUE_B)]


def main(argv):
    d = mesure()
    fautes = coherence(d)
    if fautes:
        print("## Base de connaissances\n")
        for f in fautes:
            print("- ❌ **%s**" % f)
        return 1

    if "--ecrire" in argv:
        entete = (
            "# connaissances.yml — le miroir déclaré de ce que les pages portent\n"
            "#\n"
            "# NE PAS ÉDITER À LA MAIN : ce fichier se régénère par\n"
            "#     python3 outils/verifier-connaissances.py --ecrire\n"
            "# La connaissance se corrige DANS les pages (objets C, constantes),\n"
            "# puis se régénère ici ; la CI refuse tout écart entre les deux.\n"
            "# Dossier d'architecture : 15-dossier-ciel-connaissances.md (phase 0).\n")
        contenu = entete + yaml.dump(d, allow_unicode=True, sort_keys=True,
                                     default_flow_style=False, width=100)
        ancien = open(FICHIER, encoding="utf-8").read() if os.path.exists(FICHIER) else ""
        open(FICHIER, "w", encoding="utf-8").write(contenu)
        src, bloc = lire_bloc()
        if bloc is None:
            print("carte-du-ciel.html : pas de marqueurs CONSTEL — bloc non posé")
        else:
            neuf = bloc_constel(d)
            if neuf != bloc:
                open(CARTE, "w", encoding="utf-8").write(src.replace(bloc, neuf, 1))
                print("carte-du-ciel.html : bloc CONSTEL régénéré (%d octets)" % len(neuf))
            else:
                print("carte-du-ciel.html : bloc CONSTEL inchangé")
        print("connaissances.yml : %d livres · %d correspondances · %d prophètes · "
              "%d générations · %d pages%s"
              % (len(d["livres"]), len(d["correspondances"]), len(d["prophetes"]),
                 len(d["generations"]), len(d["pages"]),
                 "" if contenu != ancien else " (inchangé)"))
        return 0

    if not os.path.exists(FICHIER):
        print("## Base de connaissances\n")
        print("- ❌ **connaissances.yml est absent** — le régénérer :"
              " `python3 outils/verifier-connaissances.py --ecrire`")
        return 1
    declare = yaml.safe_load(open(FICHIER, encoding="utf-8"))
    ecarts = list(compare(d, declare))
    _, bloc = lire_bloc()
    if bloc is not None and bloc != bloc_constel(d):
        ecarts.append("carte-du-ciel.html : le bloc CONSTEL a divergé de la mesure"
                      " — régénérer avec --ecrire")
    print("## Base de connaissances\n")
    print("%d livres · %d correspondances · %d prophètes · %d générations · "
          "%d périodes · %d pages" %
          (len(d["livres"]), len(d["correspondances"]), len(d["prophetes"]),
           len(d["generations"]), len(d["periodes"]), len(d["pages"])))
    if ecarts:
        print("\nLe miroir a divergé des pages — corriger la page ou régénérer :\n")
        for e in ecarts[:20]:
            print("- ❌ **%s**" % e)
        if len(ecarts) > 20:
            print("- … et %d autre(s)" % (len(ecarts) - 20))
        return 1
    print("\nAucun écart entre les pages et connaissances.yml.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
