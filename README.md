# L'Agneau de Dieu

Site chrétien trilingue (français · anglais · arabe) qui montre l'unité des Écritures
en remontant du Christ vers l'Ancien Testament.

**En ligne :** <https://laporte.joefr.cloud>

---

## Le principe

Toute page part du Christ révélé, puis remonte vers l'Ancien Testament. Jamais l'inverse.
On ne « prouve » pas le Christ à partir de l'AT : on éclaire l'AT par le Christ.

Chaque page tient sur **une seule image mentale** et se lit à **trois profondeurs** :
*L'essentiel* (90 secondes) · *Comprendre* · *Aller plus loin* (repliée par défaut).

Sur les sujets qui divisent, la **règle des trois cercles** : ce que tous les chrétiens
confessent, on l'affirme ; ce que les Écritures disent, on le cite intégralement ;
ce que les traditions interprètent, on le présente côte à côte — sans arbitrer.

La charte complète est dans [`CLAUDE.md`](CLAUDE.md).

## L'architecture

Site **statique** : une page = un fichier `.html` autonome à la racine, CSS et JS en ligne.
Pas de build, pas de dépendance.

**Le contenu est de la donnée.** Chaque page porte un objet JavaScript trilingue et
construit son DOM à partir de lui :

```js
const C = { fr:{ dir:"ltr", … }, en:{ … }, ar:{ dir:"rtl", … } };
```

Conséquence : **ne modifiez jamais le HTML rendu à la main** — une retouche directe casse
une des trois langues. Le contenu se modifie dans l'objet, langue par langue.

La structure du site est déclarée dans [`navigation.yml`](navigation.yml) : toute page
nouvelle doit y figurer avec ce qui y mène et ce vers quoi elle repart.

## Les contrôles

```bash
node    outils/verifier-langues.mjs ./*.html    # les trois langues restent alignées
node    outils/essai-rendu.mjs      ./*.html    # chaque page s'affiche vraiment
python3 outils/verifier-liens.py                # ni orpheline, ni cul-de-sac
python3 outils/verifier-references.py ./*.html  # les références bibliques existent
```

Ils tournent aussi en intégration continue à chaque pull request.
Voir [`outils/README.md`](outils/README.md) — et ce qu'aucun d'eux ne vérifie.

## Contribuer

Le kit de contribution éditoriale est dans [`producteur/`](producteur/00-LISEZMOI.md) :
il permet d'écrire, de proposer et de relire **avec un compte Claude gratuit**,
sans code ni installation.

- une page rédigée → une pull request, ou le formulaire *Fiche de contenu*
- une idée de chapitre, un changement visuel, une réorganisation → un ticket
  ([le circuit](producteur/05-CIRCUIT-DES-PROPOSITIONS.md))

## Déploiement

Poussée sur `main` → GitHub Actions → `rsync` des `*.html` de la racine vers le VPS.
Les sous-dossiers (`producteur/`, `contenus/`, `outils/`, `communication/`) ne sont
pas publiés : ce sont des dossiers de travail.

## Traductions bibliques

Louis Segond 1910 (fr) · World English Bible (en) · Smith & Van Dyck (ar).
Toujours la référence exacte ; jamais un verset inventé.
