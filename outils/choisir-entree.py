#!/usr/bin/env python3
"""Renvoie la première entrée « à faire » de la feuille de route.

    python3 outils/choisir-entree.py FEUILLE-DE-ROUTE.md [zone-autorisée ...]

Sortie : «id<TAB>zone<TAB>titre», ou rien s'il n'y a pas d'entrée à traiter.
L'ordre du fichier est l'ordre de priorité : la feuille de route est un plan,
pas un sac.
"""
import re
import sys


def entrees(chemin):
    titre_re = re.compile(r"^##\s+(R-\d+)\s+(.*?)\s*$")
    champ_re = re.compile(r"^-\s*(zone|statut)\s*:\s*(.+?)\s*$")
    courante = None
    for ligne in open(chemin, encoding="utf-8"):
        m = titre_re.match(ligne)
        if m:
            if courante:
                yield courante
            courante = {"id": m.group(1), "titre": m.group(2)}
            continue
        if courante:
            m = champ_re.match(ligne)
            if m:
                courante[m.group(1)] = m.group(2)
    if courante:
        yield courante


def main(argv):
    if not argv:
        return 2
    chemin, zones = argv[0], set(argv[1:])
    for e in entrees(chemin):
        if e.get("statut") != "à faire":
            continue
        zone = e.get("zone", "")
        if zones and zone not in zones:
            continue
        print("%s\t%s\t%s" % (e["id"], zone, e["titre"]))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
