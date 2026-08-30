# L'Agneau de Dieu — contexte du projet

Site chrétien trilingue (FR / EN / AR) qui montre l'unité des Écritures en remontant
du Christ vers l'Ancien Testament. Public : du débutant complet au lecteur avancé.

Ce fichier est lu automatiquement par Claude au démarrage. Il contient ce qu'il faut
savoir pour ne pas produire du contenu hors charte ni casser l'architecture.

---

## Charte éditoriale — non négociable

1. **Christocentrique et descendant.** Toute page part du Christ révélé, puis remonte
   vers l'Ancien Testament. Jamais l'inverse. On ne « prouve » pas le Christ à partir
   de l'AT : on éclaire l'AT par le Christ.
2. **Une seule image mentale par page.** L'agneau, le fil, le voile, le pain, le bois.
   Le lecteur doit pouvoir redessiner la page de mémoire le lendemain.
3. **Trois profondeurs sur chaque page.** Voir « structure d'une page » ci-dessous.
4. **Les Écritures, pas les gestes.** Les sujets sensibles (l'Eucharistie) sont traités
   comme offrande et accomplissement de la Pâque, par les textes.
5. **Règle des trois cercles** sur tout sujet qui divise :
   ce que tous les chrétiens confessent → on l'affirme ;
   ce que les Écritures disent → on cite intégralement ;
   ce que les traditions interprètent → catholique et évangélique côte à côte,
   **sans arbitrer**.

**Ton.** Sobre, dense, respectueux. Pas d'exclamation, pas d'emphase publicitaire, pas
d'« incroyable » ni de « bouleversant ». Phrases courtes. Le verset porte l'émotion,
pas l'adjectif. Jamais de polémique contre une autre religion : sur les objections
(notamment musulmanes), factuel et fraternel.

**Traductions.** Segond 1910 (FR) · World English Bible (EN) · Van Dyck (AR).
Toujours la référence exacte. **N'invente jamais un verset ni une référence.**
En cas de doute, écrire `[À VÉRIFIER]` plutôt qu'approximer.

**Édition arabe.** « Une Bible digne de confiance » et le « chemin du chercheur »
remontent en tête de navigation. Le *taḥrīf* se traite par la datation des manuscrits
antérieurs à l'islam, sans triomphalisme. Privilégier le symbole aux représentations
figuratives du Christ.

---

## Architecture technique

Site **statique**, sans build, sans dépendances. Une page = un fichier `.html`
autonome à la racine, avec son CSS et son JS en ligne.

**Le contenu est de la donnée, pas du balisage.** Chaque page porte un objet
JavaScript `C` avec une clé par langue, et construit son DOM à partir de cet objet :

```js
const C = {
  fr: { dir:"ltr", brand:"L'AGNEAU DE DIEU", steplbl:…, steps:[…],
        eyebrow:…, verse:…, scene:…,
        s1:"L'essentiel · 90 secondes", s1p:[…], mental:…,
        s2:"Comprendre", h1:…, cards:[[ref,titre,corps,clé],…], s2b:[…],
        s3:"Aller plus loin", deep:[[titre,corps],…],
        nlbl:…, ntitle:…, ntext:…, foot:… },
  en: { … }, ar: { dir:"rtl", … }
}
```

**Conséquence : ne modifie jamais le HTML rendu à la main.** Une retouche directe dans
le corps de la page casse une des trois langues ou se perd au premier rendu. Le contenu
se modifie dans l'objet `C`, langue par langue.

**Système visuel** (identique sur toutes les pages, dans `:root`) :
`--bg:#0c0e18` `--bg2:#11141f` `--ink:#e9e3d3` `--muted:#9a94a8`
`--gold:#d3a94f` `--line:#23273a` `--crimson:#a33`
Polices : Cormorant Garamond (titres) · Georgia (corps) · system-ui (interface) ·
Amiri (arabe, avec `html[dir="rtl"]` pour chaque règle typographique).

**Déploiement.** `.github/workflows/deploy.yml` — à chaque poussée sur `main`,
rsync des `*.html` **de la racine uniquement** vers le VPS. Les sous-dossiers
(`producteur/`, `contenus/`, `communication/`) ne sont pas publiés : ce sont des
dossiers de travail.

---

## Structure d'une page

| Strate | Nom | Contenu | Longueur |
|---|---|---|---|
| 1 | L'essentiel | 90 secondes : l'image, le verset socle, trois phrases | 80–120 mots |
| 2 | Comprendre | le développement, les textes AT et NT en face à face | 350–600 mots |
| 3 | Aller plus loin | hébreu/grec, contexte, sources, objections — repliée par défaut | 250–500 mots |

Classes du squelette : `.top` `.thread/.dots/.dot` `.hero/.eyebrow/.verse/.scene`
`main > .strate > .shead/.snum` `.mental` `.cards/.cardE` `details.deep` `.next` `footer`.
Le squelette nu, prêt à coller dans une conversation, est dans
`producteur/gabarit-visuel.html` (11 Ko).

---

## Ce que contient le dépôt

- **Racine, `*.html`** — les 24 pages publiées.
- **`producteur/`** — kit de contribution éditoriale : charte à coller dans un Claude
  gratuit, gabarits, prompts, circuit des propositions, journal des décisions.
- **`contenus/`** — les fiches soumises, en Markdown, avant transposition en page.
- **`communication/`** — stratégie, calendrier, visuels.
- **`.github/ISSUE_TEMPLATE/`** — les six formulaires de soumission.

## État du maillage

La structure du site est déclarée dans `navigation.yml` : c'est la source de vérité.
`outils/verifier-liens.py` compare le site réel à cette carte en **mesurant les liens
sur le rendu**, pas sur le texte source — ces pages construisent leur DOM en
JavaScript, et une adresse peut vivre dans un tableau de constantes.

État au 30 août 2026 : **aucune orpheline, aucun cul-de-sac, aucun écart**.
Les six piliers sont reliés en deux chaînes ouvertes depuis le parcours et la salle
de la Trinité. Il a suffi de donner leur adresse aux blocs « page suivante » : ils
étaient rédigés et traduits dans les trois langues, mais pointaient tous sur `href="#"`.

**Toute page nouvelle doit se déclarer dans `navigation.yml`** avec ce qui y mène et
ce vers quoi elle repart. Sinon la CI la refuse.

Les questions structurantes encore ouvertes sont dans
`producteur/06-JOURNAL-DES-DECISIONS.md`. Ne les tranche pas à la place du porteur
du projet : signale-les.

## Pièges du dépôt

- `salle-bibliotheque.html` nomme son objet de contenu `LIB`, la frise et le seuil
  l'appellent `T`, les autres `C`. Les outils découvrent le nom tout seuls.
- `index.html` n'a pas de clé `dir` : il applique la direction dans son rendu
  (`documentElement.dir=(l==='ar')?'rtl':'ltr'`). C'est correct, ne pas « corriger ».
- La vraie arborescence de cadrage est dans `arborescence-site-agneau.md`.

## Langue

Le projet est francophone : commits, tickets, documentation et commentaires en français.
