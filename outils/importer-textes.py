#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Importe les textes bibliques de référence dans `textes/` — chantier R-004.

    python3 outils/importer-textes.py

Les textes ne sont pas publiés : le déploiement ne pousse que les `*.html` de la
racine. Ils servent à vérifier les citations du site au mot près (R-005).

Format normalisé : un fichier par traduction, **un verset par ligne**, aligné
ligne à ligne sur `textes/vref.txt` — la liste canonique des références. Une
ligne vide signifie que la traduction ne porte pas ce verset. C'est le format le
plus compact qui reste lisible et diffable ; l'index se fait en une passe.

Les sources sont publiques et redistribuables ; `textes/LICENCES.md` les
documente. L'outil demande le réseau : il ne tourne pas en CI, seulement quand
on veut rafraîchir les textes.
"""
import io
import os
import sys
import json
import urllib.request

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TEXTES = os.path.join(RACINE, "textes")
EBIBLE = "https://raw.githubusercontent.com/BibleNLP/ebible/main"

# Les traductions de la charte, plus la néo-Crampon : les trois traductions de
# référence sont des éditions à 66 livres, et le site en présente 73. La Crampon
# est le seul texte libre qui porte les sept deutérocanoniques (décision D-022).
EBIBLE_TEXTES = [
    ("fra-Segond1910.txt", "corpus/fra-fraLSG.txt"),
    ("eng-WEB.txt", "corpus/eng-engwebp.txt"),
    ("fra-Crampon.txt", "corpus/fra-francl.txt"),
]
# La Van Dyck de eBible est vide à la source ; on la prend là où elle est complète.
VANDYCK = "https://raw.githubusercontent.com/thiagobodruk/bible/master/json/ar_svd.json"
VANDYCK_ORDRE = [
    "GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT", "1SA", "2SA",
    "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "EST", "JOB", "PSA", "PRO",
    "ECC", "SNG", "ISA", "JER", "LAM", "EZK", "DAN", "HOS", "JOL", "AMO",
    "OBA", "JON", "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL",
    "MAT", "MRK", "LUK", "JHN", "ACT", "ROM", "1CO", "2CO", "GAL", "EPH",
    "PHP", "COL", "1TH", "2TH", "1TI", "2TI", "TIT", "PHM", "HEB", "JAS",
    "1PE", "2PE", "1JN", "2JN", "3JN", "JUD", "REV",
]


def prendre(url):
    print("  ← %s" % url.split("/")[-1], flush=True)
    with urllib.request.urlopen(url, timeout=180) as r:
        return r.read().decode("utf-8-sig")


def main():
    os.makedirs(TEXTES, exist_ok=True)

    vref = prendre(EBIBLE + "/metadata/vref.txt")
    io.open(os.path.join(TEXTES, "vref.txt"), "w", encoding="utf-8").write(vref)
    refs = [l.strip() for l in vref.split("\n") if l.strip()]
    place = {r: i for i, r in enumerate(refs)}
    print("vref : %d références" % len(refs))

    for nom, chemin in EBIBLE_TEXTES:
        txt = prendre(EBIBLE + "/" + chemin)
        lignes = txt.split("\n")
        while len(lignes) < len(refs):
            lignes.append("")
        lignes = lignes[:len(refs)]
        io.open(os.path.join(TEXTES, nom), "w", encoding="utf-8").write(
            "\n".join(lignes) + "\n")
        print("%-22s %d versets" % (nom, sum(1 for l in lignes if l.strip())))

    # La Van Dyck arrive en JSON par livre et chapitre : on la range à la place
    # que `vref` donne à chaque référence, et l'on compte ce qui n'y entre pas.
    d = json.loads(prendre(VANDYCK))
    lignes = [""] * len(refs)
    hors = 0
    for i, livre in enumerate(d):
        code = VANDYCK_ORDRE[i]
        for ch, versets in enumerate(livre["chapters"], 1):
            for v, texte in enumerate(versets, 1):
                r = "%s %d:%d" % (code, ch, v)
                if r in place:
                    lignes[place[r]] = texte.strip()
                else:
                    hors += 1
    io.open(os.path.join(TEXTES, "arb-VanDyck.txt"), "w", encoding="utf-8").write(
        "\n".join(lignes) + "\n")
    print("%-22s %d versets · %d hors de la versification de référence"
          % ("arb-VanDyck.txt", sum(1 for l in lignes if l.strip()), hors))
    return 0


if __name__ == "__main__":
    sys.exit(main())
