#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Donne un verset dans les textes de référence importés par R-004.

    python3 outils/citer.py "Genèse 22:16"
    python3 outils/citer.py "Psaume 22:2" "Actes 8:32-35"
    python3 outils/citer.py --existe "Genèse 22:16"    dit seulement si la référence existe

C'est la brique de R-005 : comparer ce que les pages citent à ce que les textes
portent. Ici, on lit ; la comparaison viendra ensuite.
"""
import io
import os
import re
import sys

import yaml

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TEXTES = os.path.join(RACINE, "textes")
VERSIONS = [("fr", "Segond 1910", "fra-Segond1910.txt"),
            ("fr", "Crampon", "fra-Crampon.txt"),
            ("en", "World English Bible", "eng-WEB.txt"),
            ("ar", "Van Dyck", "arb-VanDyck.txt")]


def charger():
    livres = yaml.safe_load(io.open(os.path.join(TEXTES, "livres.yml"),
                                    encoding="utf-8"))["livres"]
    noms = {}
    for l in livres:
        for cle in ("fr", "en", "ar"):
            noms[l[cle].lower()] = l["code"]
        for autre in l.get("autres", []):
            noms[autre.lower()] = l["code"]
    refs = [x.strip() for x in
            io.open(os.path.join(TEXTES, "vref.txt"), encoding="utf-8")]
    place = {r: i for i, r in enumerate(refs) if r}
    return noms, place


# Les traductions ne découpent pas toujours les mêmes chapitres. La liste de
# référence suit la numérotation hébraïque ; Segond, elle, donne quatre chapitres
# à Malachie. « Malachie 4:5 » et « Malachie 3:23 » sont le même verset — celui
# d'Élie. On le dit ici plutôt que de laisser une référence juste passer pour fausse.
EQUIV = {("MAL", 4): lambda v: ("MAL", 3, v + 18)}


def analyser(ref, noms):
    """« Actes 8:32-35 » → ('ACT', 8, [32, 33, 34, 35])."""
    m = re.match(r"^\s*(.+?)\s+(\d+)\s*:\s*(\d+)(?:\s*[-–]\s*(\d+))?\s*$", ref)
    if not m:
        return None
    code = noms.get(m.group(1).strip().lower())
    if not code:
        return None
    ch, v1 = int(m.group(2)), int(m.group(3))
    v2 = int(m.group(4)) if m.group(4) else v1
    versets = list(range(v1, v2 + 1))
    if (code, ch) in EQUIV:
        deplace = [EQUIV[(code, ch)](v) for v in versets]
        code, ch = deplace[0][0], deplace[0][1]
        versets = [d[2] for d in deplace]
    return code, ch, versets


def main(argv):
    seulement = "--existe" in argv
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    noms, place = charger()
    textes = {}
    for lang, titre, fichier in VERSIONS:
        chemin = os.path.join(TEXTES, fichier)
        if os.path.exists(chemin):
            textes[titre] = io.open(chemin, encoding="utf-8").read().split("\n")

    manque = 0
    for ref in args:
        a = analyser(ref, noms)
        if not a:
            print("%-24s ❌ référence illisible ou livre inconnu" % ref)
            manque += 1
            continue
        code, ch, versets = a
        cles = ["%s %d:%d" % (code, ch, v) for v in versets]
        absentes = [c for c in cles if c not in place]
        if absentes:
            print("%-24s ❌ hors de la versification de référence : %s"
                  % (ref, ", ".join(absentes)))
            manque += 1
            continue
        if seulement:
            print("%-24s ✅ %s" % (ref, " ".join(cles)))
            continue
        print("\n%s   (%s)" % (ref, " ".join(cles)))
        for titre, lignes in textes.items():
            bouts = [lignes[place[c]].strip() for c in cles]
            bouts = [b for b in bouts if b]
            print("  %-20s %s" % (titre, " ".join(bouts) if bouts
                                  else "— ce texte ne porte pas ce verset"))
    return 1 if manque else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
