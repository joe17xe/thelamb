# Espace producteur — mode d'emploi

Ce dossier est le **kit de travail du producteur éditorial**. Il permet de contribuer
au site *L'Agneau de Dieu* sans installer quoi que ce soit, sans ligne de commande,
et avec un **compte Claude gratuit**.

## Ce dont vous avez besoin

| Outil | Version requise | Pourquoi |
|---|---|---|
| Un compte Claude | **gratuit suffit** | rédiger et retravailler les textes |
| Un compte GitHub | **gratuit suffit** | déposer vos fiches et vos remarques |
| Un navigateur | n'importe lequel | tout se fait en ligne |

Vous n'avez **jamais** besoin de Claude Code, de Git, ni d'éditeur de texte.

## Le circuit en 3 temps

**1. Se charger du contexte** — au début de *chaque* nouvelle conversation Claude,
collez le contenu de [`01-BRIEF-CLAUDE.md`](01-BRIEF-CLAUDE.md).
C'est la charte du site en une page : principes, ton, structure, interdits.
Sans ça, Claude écrit du contenu chrétien générique qui ne rentrera pas dans le site.

> Sur un compte gratuit il n'y a pas de « Projets » : le contexte ne se mémorise pas
> d'une conversation à l'autre. Gardez le brief dans une note et recollez-le.
> Une conversation = une page. C'est aussi mieux pour la qualité.

**2. Produire** — utilisez un des prompts de [`03-PROMPTS.md`](03-PROMPTS.md).
Le résultat doit sortir au format de [`02-GABARIT-FICHE.md`](02-GABARIT-FICHE.md) —
c'est ce format, et lui seul, qui permet de transformer votre texte en page du site
sans réécriture.

**3. Déposer** — sur GitHub, onglet **Issues** → **New issue** → choisissez le formulaire :

| Vous voulez… | Formulaire |
|---|---|
| déposer une page rédigée | **Fiche de contenu** |
| ajouter un arc au diagramme d'accueil | **Correspondance Fil Rouge** |
| signaler un problème d'organisation | **Revue de structure** |
| proposer un chapitre qui n'existe pas | **Proposition de chapitre** |
| changer une mise en page, une couleur, un composant | **Proposition visuelle** |
| déplacer, fusionner ou supprimer des pages | **Proposition de restructuration** |

Copiez-collez, cliquez **Submit**. C'est tout. Le ticket est horodaté, numéroté,
discutable en commentaires, et rien ne se perd.

Les trois derniers formulaires ne servent pas à déposer du contenu mais à proposer un
changement : leur mode d'emploi — qui tranche quoi, en combien de temps, et pourquoi
on valide l'intention avant d'écrire — est dans
[`05-CIRCUIT-DES-PROPOSITIONS.md`](05-CIRCUIT-DES-PROPOSITIONS.md).

## Proposer, et pas seulement produire

Le producteur n'est pas un fournisseur de texte. Les propositions de création, de
chapitre, de mise en page et de réorganisation sont attendues au même titre que les
pages — elles ont juste un circuit différent, décrit dans
[`05-CIRCUIT-DES-PROPOSITIONS.md`](05-CIRCUIT-DES-PROPOSITIONS.md) :

- **un apport** (une page, un arc) entre s'il est au format ;
- **une proposition** (un chapitre, une mise en page) se discute avant d'être rédigée ;
- **une décision structurante** (la navigation, la charte) se tranche de vive voix et
  s'écrit au [journal des décisions](06-JOURNAL-DES-DECISIONS.md).

Pour le visuel, ne décrivez pas : maquettez. Votre Claude gratuit produit des artéfacts
— des pages web affichables et partageables par lien. Le squelette
[`gabarit-visuel.html`](gabarit-visuel.html) est fait pour ça.

## Ce qu'il ne faut pas faire

- Ne modifiez pas les fichiers `.html` du site : leur contenu vit dans un objet
  JavaScript trilingue, et une retouche à la main casse une des trois langues.
- N'inventez jamais une référence biblique. Chaque verset cité est vérifié.
- Ne tranchez pas les débats confessionnels : voir la règle des trois cercles dans le brief.
