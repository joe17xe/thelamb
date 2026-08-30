# État du site — relevé au 30 août 2026

Document de travail pour la revue de structure. Chiffres relevés automatiquement
sur les 23 pages HTML du dépôt, pas à l'estime.

## Vue d'ensemble

- **23 pages** publiées, ~112 000 mots
- **14 pages sur 24 sont orphelines** : aucune autre page du site n'y mène.
  Elles ne sont accessibles qu'en connaissant leur adresse.
- **10 liens internes en tout** sur l'ensemble du site.
- Les trois langues sont déclarées partout, mais **l'anglais est marginal** :
  1 occurrence par page contre 16 à 19 pour l'arabe.

## Le parcours en 7 étapes — la seule chaîne qui tient

```
page-etalon-voici-agneau  →  etape2-agneau-regne  →  etape3-la-croix
   →  etape4-isaie-53  →  etape5-la-paque  →  etape6-morija
   →  etape7-commencement  →  index
```

Les 7 pages ont bien les trois strates. **Mais la première page de la chaîne est
orpheline** : rien, nulle part, ne mène à « Voici l'Agneau ». Le parcours principal
du site n'a pas de porte d'entrée.

## Les pages isolées

| Page | Liens entrants | Liens sortants | Trois strates |
|---|---|---|---|
| `page-etalon-voici-agneau.html` | **0** | 1 | oui |
| `pilier-le-sang.html` | **0** | **0** | non |
| `pilier-bapteme.html` | **0** | **0** | non |
| `pilier-parole-eternelle.html` | **0** | **0** | non |
| `pilier-resurrection.html` | **0** | **0** | non |
| `pilier-temple-detruit.html` | **0** | **0** | non |
| `pilier-transfiguration.html` | **0** | **0** | non |
| `salle-trinite-bibliotheques.html` | **0** | 1 | non |
| `salle-bibliotheque.html` | **0** | 3 | non |
| `section-offrande.html` | **0** | **0** | non |
| `frise-prophetes.html` | **0** | **0** | non |
| `cle-deja-pas-encore.html` | **0** | 1 | oui |
| `page-fondatrice-emmaus.html` | **0** | 1 | oui |
| `prototype-fil-rouge-v3.html` | **0** | 1 | — (21 mots, coquille vide) |

Les **six piliers** — environ 21 000 mots de contenu rédigé — ne sont reliés
à rien du tout, ni en entrée ni en sortie.

## Les culs-de-sac

- `seuil-landing.html` (« Le seuil — une porte, des salles ») reçoit des liens
  mais **n'en émet aucun**. La porte du site ne mène nulle part.
- `section-bible-fiable.html` : même problème.
- `salle-trinite.html` : même problème.

## L'accueil

`index.html` (le Fil Rouge) ne pointe que vers `seuil-landing.html`.
Les **trois portes d'entrée** prévues au cadrage — *Je découvre* / *Je veux comprendre
l'Agneau* / *La Bible est-elle fiable ?* — ne sont pas sur la page.

## Ce qui est prévu au cadrage et n'existe pas

| Prévu | État |
|---|---|
| Les cinq alliances — Noé, Abraham, Moïse, David, Nouvelle | aucune page |
| Galerie des figures — 8 cartes recto/verso figure→accomplissement | aucune page |
| Parcours « Découverte » (7 étapes accompagnées, ~20 min) | aucune page |
| Parcours « Le Fil de l'Agneau » (10 étapes, textes intégraux) | aucune page |
| Parcours « Le chemin du chercheur » (édition arabe) | aucune page |
| À propos, cadre de foi, traductions, bibliographie, contact | aucune page |

## Incohérence de structure

Les trois strates (*L'essentiel* / *Comprendre* / *Aller plus loin*) sont la promesse
de lecture du site. Elles sont respectées sur 9 pages et absentes des 15 autres —
notamment sur les six piliers et les trois salles, qui sont pourtant les pages
les plus longues (3 000 à 6 500 mots chacune).

## Hygiène du dépôt

- `README.md` contient en réalité le code HTML de la page Morija, pas une présentation.
- `03-architecture-technique-vps.md` est vide (0 octet).
- `01-arborescence-du-site.md` est un doublon exact de `architecture-technique-vps.md`
  — et ne contient pas l'arborescence, malgré son nom.
- `04-installation-vps.md` est un doublon exact de `dossier-reference-agneau.md`.
- `prototype-fil-rouge-v3.html` est une coquille de 21 mots.

---

## Les six questions à trancher avec le producteur

1. **Par où entre-t-on ?** L'accueil est le Fil Rouge (un diagramme). Est-ce la bonne
   première image, ou faut-il le seuil devant ?
2. **Que fait-on des six piliers ?** 21 000 mots invisibles. On les rattache au
   parcours, on en fait une section à part, ou on les fond dans les étapes ?
3. **Le seuil et l'accueil font-ils doublon ?** Deux pages se disputent le rôle
   de porte d'entrée.
4. **Les trois strates : promesse ou option ?** Si c'est la promesse du site,
   les 15 pages hors format sont à reprendre. C'est le plus gros chantier.
5. **L'anglais.** Déclaré partout, présent nulle part. On assume deux langues
   (FR/AR) ou on produit l'anglais ?
6. **Priorité de production.** Six chantiers de contenu sont ouverts. Lequel d'abord ?
