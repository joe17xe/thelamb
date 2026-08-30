#!/usr/bin/env python3
"""Contrôle la validité formelle des références bibliques citées.

    python3 outils/verifier-references.py *.html contenus/*.md

Ne vérifie pas le *texte* d'une citation — pour ça il faut les traductions
dans `textes/` (voir textes/README.md). Vérifie ce qui se contrôle sans elles :
le livre existe, le chapitre existe dans ce livre. C'est ce qui attrape
« Ésaïe 67 » ou « Habaquq 12 », l'erreur la plus courante d'un modèle.

Là où les éditions diffèrent (Joël, Malachie), on retient le compte le plus
large : ce contrôle doit se taire sur les cas discutables et ne parler que
sur les erreurs franches.
"""
import os
import re
import sys
import unicodedata

CHAPITRES = {
    "genèse": 50, "exode": 40, "lévitique": 27, "nombres": 36, "deutéronome": 34,
    "josué": 24, "juges": 21, "ruth": 4, "1 samuel": 31, "2 samuel": 24,
    "1 rois": 22, "2 rois": 25, "1 chroniques": 29, "2 chroniques": 36,
    "esdras": 10, "néhémie": 13, "esther": 10, "job": 42, "psaume": 150,
    "psaumes": 150, "proverbes": 31, "ecclésiaste": 12, "cantique": 8,
    "cantique des cantiques": 8, "ésaïe": 66, "esaïe": 66, "isaïe": 66,
    "jérémie": 52, "lamentations": 5, "ézéchiel": 48, "daniel": 12,
    "osée": 14, "joël": 4, "amos": 9, "abdias": 1, "jonas": 4, "michée": 7,
    "nahum": 3, "habacuc": 3, "sophonie": 3, "aggée": 2, "zacharie": 14,
    "malachie": 4,
    "matthieu": 28, "marc": 16, "luc": 24, "jean": 21, "actes": 28,
    "romains": 16, "1 corinthiens": 16, "2 corinthiens": 13, "galates": 6,
    "éphésiens": 6, "philippiens": 4, "colossiens": 4,
    "1 thessaloniciens": 5, "2 thessaloniciens": 3,
    "1 timothée": 6, "2 timothée": 4, "tite": 3, "philémon": 1,
    "hébreux": 13, "jacques": 5, "1 pierre": 5, "2 pierre": 3,
    "1 jean": 5, "2 jean": 1, "3 jean": 1, "jude": 1, "apocalypse": 22,
}

# Abréviations rencontrées dans les pages et les dossiers du dépôt.
ABREGES = {
    "gen": "genèse", "gn": "genèse", "ex": "exode", "lev": "lévitique",
    "lév": "lévitique", "nb": "nombres", "dt": "deutéronome", "deut": "deutéronome",
    "jos": "josué", "jg": "juges", "1 s": "1 samuel", "2 s": "2 samuel",
    "1 r": "1 rois", "2 r": "2 rois", "ps": "psaumes", "pr": "proverbes",
    "ec": "ecclésiaste", "ct": "cantique", "es": "ésaïe", "és": "ésaïe",
    "jr": "jérémie", "ez": "ézéchiel", "éz": "ézéchiel", "dn": "daniel",
    "os": "osée", "jl": "joël", "am": "amos", "jon": "jonas", "mi": "michée",
    "za": "zacharie", "ml": "malachie",
    "mt": "matthieu", "mc": "marc", "lc": "luc", "jn": "jean", "ac": "actes",
    "rm": "romains", "rom": "romains", "1 co": "1 corinthiens", "2 co": "2 corinthiens",
    "ga": "galates", "ep": "éphésiens", "ép": "éphésiens", "ph": "philippiens",
    "col": "colossiens", "1 th": "1 thessaloniciens", "2 th": "2 thessaloniciens",
    "1 tm": "1 timothée", "2 tm": "2 timothée", "tt": "tite", "phm": "philémon",
    "he": "hébreux", "hé": "hébreux", "jc": "jacques", "1 p": "1 pierre",
    "2 p": "2 pierre", "1 jn": "1 jean", "2 jn": "2 jean", "3 jn": "3 jean",
    "jud": "jude", "ap": "apocalypse",
}

LIVRES = sorted(set(CHAPITRES) | set(ABREGES), key=len, reverse=True)
MOTIF = re.compile(
    r"\b(" + "|".join(re.escape(l) for l in LIVRES) + r")\s*\.?\s+(\d{1,3})(?::(\d{1,3}))?",
    re.IGNORECASE,
)


def sans_balises(texte, chemin):
    if chemin.endswith(".html"):
        texte = re.sub(r"<(script|style)\b.*?</\1>", " ", texte, flags=re.S | re.I)
        texte = re.sub(r"<[^>]+>", " ", texte)
    return texte


def normaliser(mot):
    return unicodedata.normalize("NFC", mot.strip().lower())


def verifier(chemin):
    brut = open(chemin, encoding="utf-8").read()
    # Les pages portent leur contenu dans l'objet C : on garde le script.
    texte = brut if chemin.endswith(".html") else sans_balises(brut, chemin)
    texte = re.sub(r"<[^>]+>", " ", texte)

    erreurs, vues = [], 0
    for m in MOTIF.finditer(texte):
        livre = normaliser(m.group(1))
        livre = ABREGES.get(livre, livre)
        maxi = CHAPITRES.get(livre)
        if maxi is None:
            continue
        vues += 1
        chapitre = int(m.group(2))
        if chapitre == 0 or chapitre > maxi:
            erreurs.append("%s %s — %s n'a que %d chapitre%s"
                           % (m.group(1), m.group(2), livre.capitalize(), maxi,
                              "s" if maxi > 1 else ""))
    return vues, sorted(set(erreurs))


# Une référence « nue » : un chapitre:verset entre parenthèses sans nom de livre.
# La convention savante veut qu'on hérite du livre cité juste avant. À l'écran,
# sur un téléphone, le lecteur ne l'hérite pas — et le vérificateur non plus :
# ces références-là ne sont contrôlées par personne.
NUE = re.compile(r"[^(a-zA-Z\u0600-\u06ff](\(\s*[\d\u0660-\u0669]{1,3}\s*:\s*"
                 r"[\d\u0660-\u0669]{1,3}(?:-[\d\u0660-\u0669]{1,3})?\s*\))")
PSAUME_NU = re.compile(r"\((\d{1,3})\)")


# Jetons d'atelier : légitimes dans `contenus/`, jamais dans une page publiée.
# On ne cherche pas le mot seul — « s'expose à la vérification » (للتحقّق) est de la
# prose — mais le crochet ouvrant qui en fait une marque (décision D-013).
JETON = re.compile(r"\[\s*(?:À VÉRIFIER|A VERIFIER|TO VERIFY|TO BE VERIFIED|\u0644\u0644\u062a\u062d\u0642\u0651\u0642|\u0644\u0644\u062a\u062d\u0642\u0642)",
                   re.IGNORECASE)


def jetons(chemin):
    """Les marques d'atelier restées dans une page publiée."""
    src = open(chemin, encoding="utf-8").read()
    return [src[max(0, m.start()):m.start() + 90].replace("\n", " ")
            for m in JETON.finditer(src)]


def nues(chemin):
    src = open(chemin, encoding="utf-8").read()
    n = len(NUE.findall(src))
    for m in PSAUME_NU.finditer(src):
        avant = src[max(0, m.start() - 200):m.start()]
        proche = src[max(0, m.start() - 40):m.end() + 10]
        if re.search(r"(Psaume|Psalm|\u0645\u0632\u0645\u0648\u0631)\s*[\d\u0660-\u0669]", avant) \
           and not re.search(r"px\(|,x:|\d\s*(av|BC)", proche):
            n += 1
    return n


def main(chemins):
    lignes, bloquant, total = [], False, 0
    for chemin in chemins:
        vues, erreurs = verifier(chemin)
        total += vues
        # Une page à la racine est publiée : un jeton d'atelier y est une faute.
        # Le glob du shell préfixe `./` — normaliser avant de juger de la racine.
        if chemin.endswith(".html") and os.path.dirname(os.path.normpath(chemin)) == "":
            for extrait in jetons(chemin):
                erreurs.append("marque d'atelier laissée au lecteur : `%s…`" % extrait)
        if erreurs:
            bloquant = True
            lignes.append("\n### `%s`\n" % chemin)
            for e in erreurs:
                lignes.append("- ❌ **%s**" % e)

    print("## Références bibliques\n")
    print("%d référence(s) reconnue(s) dans %d fichier(s)." % (total, len(chemins)))
    if lignes:
        print("\n".join(lignes))
    else:
        print("\nAucun chapitre inexistant, aucune marque d'atelier publiée. "
              "_Le texte des citations n'est pas vérifié ici — voir `textes/README.md`._")

    compte = {c: nues(c) for c in chemins if nues(c)}
    if compte:
        print("\n### Références sans nom de livre — %d\n" % sum(compte.values()))
        print("Écrites `(12:10)` plutôt que `(Zacharie 12:10)`. Le lecteur doit "
              "deviner le livre depuis la phrase précédente, et ce contrôle ne peut "
              "pas les vérifier. Ne bloque pas : c'est une dette à résorber page à page.\n")
        for c, n in sorted(compte.items(), key=lambda x: -x[1]):
            print("- ⚠️ `%s` — %d" % (c, n))

    return 1 if bloquant else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
