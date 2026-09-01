#!/usr/bin/env python3
"""La base de connaissances reflète les pages — ou la CI s'arrête.

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
    visite(yaml.safe_load(open(os.path.join(RACINE, "navigation.yml"),
                               encoding="utf-8")))
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
    for g in d["generations"]:
        if g.get("periode") and g["periode"] not in pers:
            fautes.append("génération %s : période inconnue %r"
                          % (g["nom"]["fr"], g["periode"]))
    if sum(d["themes"].values()) != len(d["correspondances"]):
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
