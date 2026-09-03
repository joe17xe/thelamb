#!/usr/bin/env python3
"""Compare le maillage réel du site à ce que déclare navigation.yml.

    python3 outils/verifier-liens.py

Trois défauts recherchés :
  · orpheline  — aucune page ne mène à elle
  · cul-de-sac — elle ne mène nulle part
  · écart      — un lien déclaré dans navigation.yml n'existe pas dans la page

Le fichier navigation.yml est la source de vérité. Une page qui n'y figure pas
n'est pas « tolérée » : elle est signalée, parce que c'est ainsi qu'on se
retrouve avec quatorze pages inaccessibles.
"""
import json
import os
import subprocess
import sys

import yaml

CARTE = "navigation.yml"


def declarees(noeud, acc=None):
    """Parcourt navigation.yml et renvoie {fichier: {entree, suite, annexes, approfondit}}."""
    acc = {} if acc is None else acc
    if isinstance(noeud, dict):
        if "fichier" in noeud:
            f = noeud["fichier"]
            fiche = acc.setdefault(f, {"racine": False, "sorties": set(), "role": noeud.get("role")})
            if noeud.get("racine"):
                fiche["racine"] = True
            for cle in ("suite", "approfondit"):
                if noeud.get(cle):
                    fiche["sorties"].add(noeud[cle])
            for a in noeud.get("annexes") or []:
                fiche["sorties"].add(a)
        for cle, valeur in noeud.items():
            if cle in ("fichier", "role", "raison", "racine", "entree"):
                continue
            declarees(valeur, acc)
        # `suite` posé au niveau d'un groupe s'applique à sa dernière page.
    elif isinstance(noeud, list):
        for el in noeud:
            declarees(el, acc)
    return acc


def liens_rendus(fichiers):
    """Relève les liens que chaque page produit réellement, dans les trois langues.

    Chercher `href=` dans la source ne suffit pas : ces pages construisent leur
    DOM en JavaScript, et une adresse peut vivre dans un tableau de constantes.
    Seul le rendu dit la vérité — c'est donc lui qu'on interroge.
    """
    sortie = subprocess.run(
        ["node", os.path.join(os.path.dirname(__file__), "essai-rendu.mjs"), "--json", *fichiers],
        capture_output=True, text=True)
    if not sortie.stdout.strip():
        raise SystemExit("essai-rendu.mjs n'a rien renvoyé :\n" + sortie.stderr)
    brut = json.loads(sortie.stdout)
    return ({f: set(v["liens"]) for f, v in brut.items()},
            {f: v["morts"] for f, v in brut.items() if v["morts"]})


def main():
    if not os.path.exists(CARTE):
        print("Pas de %s — la structure n'est pas encore déclarée." % CARTE)
        return 2

    carte = yaml.safe_load(open(CARTE, encoding="utf-8"))
    obsoletes = {e["fichier"] for e in (carte.get("obsoletes") or [])}
    # Les ateliers sont publiés mais ne font pas partie du parcours : ni orphelines
    # ni culs-de-sac, ce sont des outils de travail. On les nomme pour qu'on ne les
    # prenne pas pour un oubli.
    ateliers = {e["fichier"] for e in (carte.get("ateliers") or [])}
    plan = declarees({k: v for k, v in carte.items()
                      if k not in ("obsoletes", "ateliers")})

    sur_disque = {f for f in os.listdir(".") if f.endswith(".html")}
    non_declarees = sorted(sur_disque - set(plan) - obsoletes - ateliers)
    fantomes = sorted(set(plan) - sur_disque)

    reels, morts = liens_rendus(sorted(set(plan) & sur_disque))
    cibles = set()
    for liens in reels.values():
        cibles |= liens

    orphelines, culs_de_sac, ecarts = [], [], []
    for f, fiche in sorted(plan.items()):
        if f not in sur_disque:
            continue
        if f not in cibles and not fiche["racine"]:
            orphelines.append(f)
        if not reels[f]:
            culs_de_sac.append(f)
        manquants = sorted(fiche["sorties"] - reels[f])
        if manquants:
            ecarts.append((f, manquants))

    print("## Maillage du site\n")
    print("%d pages déclarées · %d sur disque · %d obsolète(s) · %d atelier(s)\n"
          % (len(plan), len(sur_disque), len(obsoletes), len(ateliers)))

    def bloc(titre, elements, rendu):
        if not elements:
            print("- ✅ %s : aucune" % titre)
            return False
        print("\n### %s — %d\n" % (titre, len(elements)))
        for e in elements:
            print(rendu(e))
        return True

    dur = False
    dur |= bloc("Orphelines (aucune page n'y mène)", orphelines, lambda f: "- ❌ `%s`" % f)
    dur |= bloc("Culs-de-sac (elles ne mènent nulle part)", culs_de_sac, lambda f: "- ❌ `%s`" % f)
    dur |= bloc("Écarts avec navigation.yml", ecarts,
                lambda e: "- ❌ `%s` devrait mener à : %s" % (e[0], ", ".join("`%s`" % m for m in e[1])))
    dur |= bloc("Liens morts (href=\"#\" ou vide)", sorted(morts.items()),
                lambda e: "- ❌ `%s` — %d bouton(s) qui ne mènent nulle part" % e)
    bloc("Pages non déclarées dans navigation.yml", non_declarees, lambda f: "- ⚠️ `%s`" % f)
    bloc("Déclarées mais absentes du disque", fantomes, lambda f: "- ⚠️ `%s`" % f)

    return 1 if dur else 0


if __name__ == "__main__":
    sys.exit(main())
