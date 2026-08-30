#!/usr/bin/env python3
"""Vérifie la forme d'une fiche de contenu. Ne juge pas le fond.

    python3 outils/verifier-fiche.py contenus/*.md

Sortie : un rapport Markdown sur stdout. Code 1 si une fiche a une erreur bloquante.
"""
import re
import sys

CHAMPS = ["titre", "section", "verset-socle", "image-mentale", "mene-vers", "vient-de"]
STRATES = [
    ("Strate 1", "L'essentiel", 80, 120),
    ("Strate 2", "Comprendre", 350, 600),
    ("Strate 3", "Aller plus loin", 250, 500),
]
SECTIONS = {"parcours", "pilier", "salle", "offrande", "bible",
            "alliance", "figure", "guide", "apropos", "transversale"}


def entete(texte):
    """Lit le bloc de métadonnées entre --- en tête de fiche."""
    m = re.match(r"^---\n(.*?)\n---\n", texte, re.S)
    if not m:
        return None
    champs = {}
    for ligne in m.group(1).splitlines():
        if ":" in ligne:
            cle, _, val = ligne.partition(":")
            champs[cle.strip()] = val.strip()
    return champs


def corps_strate(texte, titre):
    """Extrait le texte d'une strate, jusqu'au titre de niveau 2 suivant."""
    m = re.search(r"^##\s+%s\b.*?$(.*?)(?=^##\s|\Z)" % re.escape(titre),
                  texte, re.S | re.M)
    return m.group(1) if m else None


def mots(bloc):
    """Compte les mots hors citations de gabarit, commentaires et tableaux vides."""
    bloc = re.sub(r"<!--.*?-->", " ", bloc, flags=re.S)
    bloc = re.sub(r"\[[^\]]*\]", " ", bloc)          # [repères du modèle]
    bloc = re.sub(r"^\s*\|[\s|:-]*\|\s*$", " ", bloc, flags=re.M)  # lignes de tableau vides
    bloc = re.sub(r"[#>*_`|-]", " ", bloc)
    return len(bloc.split())


def verifier(chemin):
    texte = open(chemin, encoding="utf-8").read()
    erreurs, avis, notes = [], [], []

    meta = entete(texte)
    if meta is None:
        erreurs.append("pas de bloc de métadonnées `---` en tête de fiche")
        meta = {}
    else:
        for champ in CHAMPS:
            if not meta.get(champ):
                erreurs.append("métadonnée `%s` vide ou absente" % champ)
        section = meta.get("section", "")
        if section and section not in SECTIONS:
            avis.append("section « %s » inconnue — attendu : %s"
                        % (section, ", ".join(sorted(SECTIONS))))

    for titre, nom, mini, maxi in STRATES:
        bloc = corps_strate(texte, titre)
        if bloc is None:
            erreurs.append("strate absente : `## %s — %s`" % (titre, nom))
            continue
        n = mots(bloc)
        if n < mini:
            avis.append("%s : %d mots, attendu %d–%d — trop court" % (titre, n, mini, maxi))
        elif n > maxi:
            avis.append("%s : %d mots, attendu %d–%d — trop long" % (titre, n, mini, maxi))
        else:
            notes.append("%s : %d mots" % (titre, n))

    if not re.search(r"^##\s+Sources\b", texte, re.M):
        erreurs.append("section `## Sources` absente")

    if meta.get("mene-vers") and meta.get("vient-de"):
        notes.append("rattachement déclaré : %s → cette page → %s"
                     % (meta["vient-de"], meta["mene-vers"]))

    a_verifier = len(re.findall(r"\[À VÉRIFIER\]", texte))
    if a_verifier:
        notes.append("%d référence(s) marquée(s) [À VÉRIFIER] — à lever avant publication"
                     % a_verifier)

    restes = re.findall(r"\[(?:Titre de la page|référence|Le verset socle[^\]]*)\]", texte)
    if restes:
        avis.append("%d repère(s) du modèle non remplacé(s)" % len(restes))

    citations = len(re.findall(r"^>\s+", texte, re.M))
    if citations == 0:
        avis.append("aucune citation en bloc — une page du site en porte au moins une")

    return erreurs, avis, notes


def main(chemins):
    lignes, bloquant = [], False
    for chemin in chemins:
        if chemin.endswith(("MODELE.md", "README.md")):
            continue
        erreurs, avis, notes = verifier(chemin)
        etat = "❌ à reprendre" if erreurs else ("⚠️ relire" if avis else "✅ conforme")
        lignes.append("### `%s` — %s\n" % (chemin, etat))
        for e in erreurs:
            lignes.append("- ❌ **%s**" % e)
        for a in avis:
            lignes.append("- ⚠️ %s" % a)
        for n in notes:
            lignes.append("- %s" % n)
        lignes.append("")
        bloquant |= bool(erreurs)

    if not lignes:
        print("Aucune fiche à vérifier.")
        return 0

    print("## Vérification de forme des fiches\n")
    print("\n".join(lignes))
    print("_Cette vérification ne porte que sur la forme : structure, longueurs, "
          "rattachement. La justesse des citations, le ton et le cadre œcuménique "
          "relèvent de la relecture humaine._")
    return 1 if bloquant else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
