# Les textes de référence — provenance et licences

Ces fichiers ne sont pas publiés : le déploiement ne pousse que les `*.html` de
la racine. Ils servent à vérifier au mot près ce que les pages citent (R-005).

## Ce qu'il y a ici

| fichier | traduction | versets | licence |
|---|---|---|---|
| `fra-Segond1910.txt` | Louis Segond 1910 | 31 060 | domaine public |
| `eng-WEB.txt` | World English Bible | 30 959 | domaine public |
| `arb-VanDyck.txt` | Smith & Van Dyck (arabe) | 30 966 | domaine public |
| `fra-Crampon.txt` | Sainte Bible néo-Crampon Libre | 35 128 | domaine public |
| `vref.txt` | la liste canonique des références | 41 899 lignes | — |
| `livres.yml` | les 73 livres du site vers les codes de `vref.txt` | 73 | — |

Les trois premières sont les traductions de la charte. La quatrième est là pour
une raison précise : **les trois traductions de référence sont des éditions à
66 livres**, et le site en présente 73. La néo-Crampon est le seul texte libre
qui porte les sept deutérocanoniques — Tobie, Judith, Sagesse, Siracide, Baruch,
1 et 2 Maccabées. Sans elle, sept livres du site n'auraient aucun texte de
référence.

## Le format

Un verset par ligne, **aligné ligne à ligne sur `vref.txt`**. La ligne *n* de
chaque traduction correspond à la ligne *n* de `vref.txt`. Une ligne vide
signifie que cette traduction ne porte pas ce verset. Le contrôle du banc refuse
tout fichier dont le nombre de lignes diffère : un décalage d'une ligne ferait
lire un verset pour un autre, sans que rien ne le montre.

Lire un verset :

```
python3 outils/citer.py "Genèse 22:16"
```

Réimporter (demande le réseau, ne tourne pas en CI) :

```
python3 outils/importer-textes.py
```

## Les sources

- **Segond 1910, World English Bible, néo-Crampon** — corpus
  [BibleNLP/ebible](https://github.com/BibleNLP/ebible), qui rassemble les textes
  de [eBible.org](https://ebible.org). Les trois y sont marquées
  redistribuables, domaine public.
- **Smith & Van Dyck** — l'extraction eBible de cette traduction est vide à la
  source ; le texte vient de
  [thiagobodruk/bible](https://github.com/thiagobodruk/bible) (`ar_svd.json`),
  puis a été rangé sur la versification de référence. Il est **non vocalisé** :
  la Van Dyck imprimée porte les signes, ce fichier ne les a pas. Pour une
  comparaison au mot près, c'est sans conséquence — on normalise les
  diacritiques de toute façon.

## Ce qu'il faut savoir avant de s'en servir

**136 versets de la Van Dyck n'entrent pas dans la versification de référence**
et ne sont donc pas dans le fichier. Ce sont des différences de découpage, pour
l'essentiel dans les Psaumes.

**Les traductions ne découpent pas les mêmes chapitres.** La liste de référence
suit la numérotation hébraïque ; Segond donne quatre chapitres à Malachie là où
elle n'en compte que trois. « Malachie 4:5 » et « Malachie 3:23 » sont le même
verset — celui d'Élie. `outils/citer.py` porte ces équivalences ; il en manque
sûrement d'autres, et elles se découvriront à l'usage.

**L'extraction Segond s'arrête à Malachie 3:18** : les six derniers versets du
livre lui manquent. La Crampon les porte. C'est le seul trou connu à ce jour.

**Sur les 306 références des 153 correspondances du fil rouge, 305 se lisent**
dans au moins une des quatre traductions. La seule qui manquait — Malachie 4:5 —
se lit maintenant par l'équivalence ci-dessus.
