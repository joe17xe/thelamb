# contenus/

Les fiches rédigées, en Markdown, **avant** leur transposition en page du site.

Une fiche = un fichier. Elle arrive ici par une *pull request*, elle est relue,
discutée, corrigée dans la même PR, puis transposée dans la page `.html`
correspondante — parce que le contenu des pages vit dans un objet JavaScript
trilingue et ne se recopie pas à la main (voir `CLAUDE.md`).

## Nommer un fichier

```
contenus/<section>-<sujet>.md
```

`section` parmi : `parcours` · `pilier` · `salle` · `offrande` · `bible` ·
`alliance` · `figure` · `guide` · `apropos` · `transversale`

Exemples : `contenus/alliance-noe.md` · `contenus/figure-melchisedek.md`

## Écrire une fiche

Copiez [`MODELE.md`](MODELE.md), renommez, remplissez. Le modèle porte en tête
un bloc de métadonnées entre `---` : il est lu par la vérification automatique,
n'en changez pas les noms de champs.

## Ce qui se passe ensuite

À l'ouverture de la PR, une vérification automatique lit la fiche et commente :
strates présentes, longueurs, références marquées `[À VÉRIFIER]`, liens déclarés.
Elle ne juge pas le fond — elle évite les allers-retours sur la forme.

Ensuite, relecture humaine : justesse des citations, ton, cadre œcuménique.
