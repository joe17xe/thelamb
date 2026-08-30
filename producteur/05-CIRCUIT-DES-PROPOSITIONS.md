# Le circuit des propositions

Le producteur ne fait pas qu'apporter du texte. Il propose des créations, des chapitres,
des changements de mise en page, des réorganisations. Ces propositions n'ont pas toutes
le même poids : une correction de verset et un déplacement de section ne se traitent pas
de la même façon.

Trois tailles. Chacune a son formulaire, son délai et son décideur.

---

## Taille 1 — L'apport

*Une page, un texte, un arc du Fil Rouge, une correction.*

Ça ne déplace rien. Ça remplit une case déjà prévue au cadrage.

| | |
|---|---|
| **Formulaire** | Fiche de contenu · Correspondance Fil Rouge |
| **Qui tranche** | personne — si c'est au format et que les références tiennent, ça entre |
| **Délai** | intégré à la mise en ligne suivante |
| **Ce qu'il faut fournir** | la fiche au gabarit, références vérifiées |

## Taille 2 — La proposition

*Un chapitre nouveau, une rubrique, une section qui change de place, une mise en page revue.*

Ça touche l'arborescence ou l'apparence. Ça se discute **avant** d'être rédigé — sinon
on écrit 3 000 mots qui finissent au placard.

| | |
|---|---|
| **Formulaire** | Proposition de chapitre · Proposition visuelle · Proposition de restructuration |
| **Qui tranche** | le porteur du projet, après échange dans le ticket |
| **Délai** | réponse sous quelques jours, pas dans l'heure |
| **Ce qu'il faut fournir** | l'état actuel, l'état proposé, ce que ça déplace, pourquoi |

**La règle qui fait gagner du temps : on valide l'intention avant d'écrire le contenu.**
Un ticket de proposition ne contient pas la page rédigée. Il contient l'argument.
La rédaction vient après le feu vert, et passe alors par une fiche de contenu.

## Taille 3 — La décision structurante

*La logique de navigation, la charte visuelle, l'ordre des langues, ce qu'on assume et ce
qu'on abandonne.*

Ça engage le site entier et ça se re-débat tous les trois mois si on ne l'écrit pas.

| | |
|---|---|
| **Formulaire** | Proposition de restructuration, marquée « structurante » |
| **Qui tranche** | le porteur du projet, explicitement |
| **Délai** | on en parle de vive voix, on tranche, on l'écrit |
| **Trace** | une entrée au [journal des décisions](06-JOURNAL-DES-DECISIONS.md) |

Une décision structurante non écrite n'existe pas : elle sera reprise par le premier
qui n'était pas dans la pièce.

---

## Le cas particulier du visuel

Décrire un changement visuel avec des mots ne marche pas. « Plus aéré », « moins
sombre », « le verset plus haut » : trois personnes comprennent trois choses.

**Faites-en une maquette.** Votre Claude gratuit sait produire un artéfact — une page
web complète, affichable, partageable par lien. C'est gratuit et ça ne demande aucun outil.

1. Ouvrez [`gabarit-visuel.html`](gabarit-visuel.html) — c'est le squelette d'une page du
   site : les vraies couleurs, les vraies polices, la vraie structure en trois strates,
   sans le contenu. Environ 200 lignes, ça se colle dans une conversation.
2. Collez-le dans Claude avec votre demande : *« Voici une page du site. Propose une
   version où [ce que vous voulez changer]. Garde les couleurs et les polices. »*
3. Claude produit un artéfact. Partagez le lien dans le formulaire de proposition visuelle.

On compare alors deux pages côte à côte, pas deux opinions.

> Ne collez pas une vraie page du site dans un Claude gratuit : elles font 30 000 à
> 190 000 caractères et vous brûleriez vos messages de la journée pour rien.
> Le gabarit existe pour ça.

---

## Cycle de vie d'un ticket

```
    ouvert  →  en discussion  →  accepté  →  en production  →  en ligne
                     ↓
                  refusé (avec la raison écrite, toujours)
```

Un refus est motivé par écrit. C'est la seule façon de ne pas voir revenir six fois
la même proposition — et c'est ce qui permet de la reproposer intelligemment plus tard.

## Étiquettes

| Étiquette | Sens |
|---|---|
| `contenu` | un apport de texte |
| `structure` | touche à l'arborescence ou à la navigation |
| `visuel` | touche à l'apparence |
| `fil-rouge` | un arc du diagramme |
| `structurante` | engage le site entier — décision explicite requise |
| `à relire` | en attente de vérification des références |
| `accepté` / `refusé` | tranché |

## Ce qui n'a pas besoin de formulaire

Une intuition, un doute, une question : dites-le en commentaire d'un ticket existant,
ou dans la conversation en cours. Le formulaire sert à ce qui doit être retrouvé
dans six mois — pas à ce qui se règle en deux phrases.
