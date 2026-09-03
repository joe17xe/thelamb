# La nature des liens — dossier de travail R-013

Ce document sert à trancher **une seule question**, répétée cent cinquante-trois fois :
de quelle nature est le lien entre ce texte de l'Ancien Testament et ce texte du Nouveau ?

Il n'est pas publié. C'est un atelier.

---

## Pourquoi cette question se pose

Le site montre aujourd'hui, sur la carte du ciel, un fil d'or entre chaque livre et
l'Agneau, et son épaisseur dit **combien** de passages relient ce livre au Christ. Trente-neuf
livres en portent un — Ésaïe 31, Matthieu 30, Jean 29, les Psaumes 27, la Genèse 20.

Mais le fil ne dit pas **de quelle nature** est chacun de ces passages. Or ils n'ont pas
la même force, et un lecteur averti le voit tout de suite :

- quand Jean écrit « afin que l'Écriture fût accomplie : aucun de ses os ne sera brisé »
  (Jean 19:36), il **cite** l'Exode. Personne ne peut le contester ;
- quand la carte relie « le fils porte le bois » (Genèse 22:6) à Jésus portant sa croix
  (Jean 19:17), aucun texte ne fait le rapprochement : c'est une **lecture** chrétienne,
  ancienne et reçue, mais une lecture.

Présenter les deux de la même façon affaiblit le premier et surexpose le second. La
décision D-013 a déjà fixé le vocabulaire ; il reste à l'appliquer.

---

## Le vocabulaire (décision D-013, déjà tranchée)

| nature | ce qui la caractérise | exemple dans nos données |
|---|---|---|
| **Citation explicite** | le texte nomme ou cite l'autre texte | Zacharie 12:10 → Jean 19:37 (« Ils verront celui qu'ils ont percé ») |
| **Allusion largement reconnue** | correspondances précises, sans formule de citation | Exode 12:5 → 1 Pierre 1:19 (« un agneau sans défaut et sans tache ») |
| **Écho thématique** | motif partagé, lien plausible mais moins serré | Exode 12:13 → Romains 5:9 (le sang qui protège / justifiés par son sang) |
| **Lecture chrétienne** | lecture typologique reçue dans une tradition | Genèse 22:6 → Jean 19:17 (le fils porte le bois) |
| **Débat interprétatif** | plusieurs lectures sérieuses restent possibles | Psaume 22:17 → Jean 20:25 (« ils ont percé mes mains ») |

Une nature au-delà de la première s'accompagne d'une **nuance dépliable** disant pourquoi
elle n'est pas de la première. C'est déjà le cas pour 2 Maccabées, seul lien du dépôt à
porter aujourd'hui son badge.

---

## Les trois décisions — tranchées le 3 septembre 2026

Le porteur a répondu. Ce qui suit est acquis ; la suite du document garde la trace du
raisonnement.

**1. Niveau de preuve — on avance sur la proposition, qu'il valide.** Claude classe les
153 liens ; le producteur relit et corrige sur la page `validation-liens.html` ; le porteur
valide. La garantie est humaine tant que R-004 n'a pas livré les textes en base ; le jour
où ils y seront, un contrôle automatique confrontera les « citations explicites » au texte.

**2. La lecture part de la tradition catholique, avec toujours une mention pour les autres
Églises** — décision **D-021**, qui modifie la règle des trois cercles dans la charte. La
mention n'est ni facultative ni à charge. Sept des 153 correspondances sont dans ce cas à
ce jour ; la donnée les nomme.

**3. La nature se voit dans la fiche.** Pas sur la carte, pas sur les pages — pour l'instant.

---

## Comment le producteur travaille

La page **`validation-liens.html`**, publiée sur le site, s'ouvre avec le mot convenu.
Elle présente les 153 liens groupés par thème ; pour chacun, la proposition est déjà
cochée, en pointillé, avec l'indice qui la justifie. Le producteur corrige ce qui lui
paraît faux, ajoute une remarque s'il le souhaite, puis **copie le relevé** et le transmet.
Son travail est gardé sur son appareil au fur et à mesure.

Le relevé ne contient que les écarts : ce qui n'a pas été touché vaut accord.

> **La page n'est pas protégée.** Le site est statique, sans serveur : le mot convenu ne
> fait qu'écarter le passant, et son empreinte seule figure au dépôt. La page le dit
> elle-même. Rien de ce qu'elle contient n'est sensible — ce sont des références bibliques,
> déjà publiques sur le site.

La donnée vit dans `producteur/nature-des-liens.yml` ; la page s'en génère :

```
python3 outils/poser-validation.py
```

Le générateur est idempotent, comme celui du bandeau de situation : on ne modifie pas la
page à la main.

---

## Le raisonnement qui a conduit à ces décisions

Le reste est mécanique. Ces trois-là ne le sont pas.

### 1. Le niveau de preuve exigé pour « citation explicite »

Le dépôt n'a pas encore les textes bibliques en base (chantier R-004). Sans eux, je
qualifie **de mémoire**, et la charte interdit d'approximer.

- **(a)** On attend R-004 : les trois traductions entrent dans `textes/`, puis un contrôle
  automatique vérifie qu'une « citation explicite » en est bien une — reprise verbale, ou
  formule d'introduction. Plus lent, mais rien ne s'affiche qui n'ait été vérifié au mot près.
- **(b)** On avance maintenant sur ma proposition, que vous relisez. Plus rapide, mais la
  garantie est humaine, pas mécanique.
- **(c)** Les deux : on classe maintenant, et on n'affiche que les catégories qui ne
  demandent pas la lettre du texte, les « citations explicites » attendant leur contrôle.

*Ma recommandation : (c).* Une lecture chrétienne se nomme sans vérification textuelle ;
une citation, non.

### 2. Qui tranche entre « écho thématique » et « lecture chrétienne » ?

La frontière n'est pas technique, elle est théologique. Melchisédek offrant le pain et le
vin (Genèse 14:18) lu comme figure eucharistique est une **lecture reçue** dans la
tradition catholique, un **écho** pour beaucoup de lecteurs évangéliques.

La règle des trois cercles interdit d'arbitrer. Trois sorties possibles :

- **(a)** On classe au plus prudent : en cas d'écart entre traditions, « écho thématique ».
- **(b)** On ajoute la mention de la tradition : « lecture chrétienne — catholique », etc.
- **(c)** On crée un cas « lu diversement », qui déplie les deux lectures côte à côte.

*Ma recommandation : (c)* pour la poignée de cas concernés, *(a)* pour le reste. C'est la
règle des trois cercles appliquée au fil lui-même.

### 3. Où la nature doit-elle se voir ?

- dans la **fiche** d'une correspondance seulement (sobre, mais peu visible) ;
- sur la **carte** — la nature changerait l'aspect du fil : plein pour une citation,
  pointillé pour une lecture, par exemple ;
- sur les **pages** elles-mêmes, à côté de chaque renvoi.

*Ma recommandation : la fiche d'abord, la carte ensuite.* Les pages en dernier, et
seulement là où un lecteur averti pourrait objecter — c'est l'avertissement déjà inscrit
dans R-013 : ne pas badger ce qui n'en a pas besoin.

---

## Un thème entier, déjà classé — pour que vous jugiez sur pièces

Voici les **27 correspondances du thème « L'Agneau »**, avec ma proposition. C'est un
cinquième du travail. Si vous validez la méthode sur celui-ci, les sept autres thèmes
suivent de la même façon.

**Ces propositions sont des propositions.** Elles n'entrent nulle part avant votre
relecture, et les « citations explicites » demandent en plus le contrôle textuel (R-004).

| # | le lien | nature proposée | pourquoi |
|---|---|---|---|
| 1 | Genèse 4:4 → Hébreux 11:4 | Citation explicite | Hébreux nomme Abel et son offrande |
| 2 | Genèse 22:8 → Jean 1:29 | Allusion largement reconnue | « l'agneau de Dieu » sans formule de citation |
| 3 | Genèse 22:6 → Jean 19:17 | Lecture chrétienne | parallèle narratif, aucun texte ne le fait |
| 4 | Genèse 22:13 → Romains 8:32 | Allusion largement reconnue | « n'a pas épargné son propre Fils » — **mais la reprise verbale est en Genèse 22:16, pas 22:13 : la référence est peut-être à corriger** |
| 5 | Exode 12:5 → 1 Pierre 1:19 | Allusion largement reconnue | vocabulaire repris, pas de formule |
| 6 | Exode 12:13 → Romains 5:9 | Écho thématique | le sang qui protège ; lien conceptuel |
| 7 | Exode 12:46 → Jean 19:36 | Citation explicite | « afin que l'Écriture fût accomplie » |
| 8 | Lévitique 16:22 → Hébreux 9:28 | Allusion largement reconnue | « porter les péchés de plusieurs » |
| 9 | Lévitique 17:11 → Hébreux 9:22 | Allusion largement reconnue | la logique de Lévitique 17:11 reprise |
| 10 | Nombres 21:9 → Jean 3:14 | Citation explicite | « comme Moïse éleva le serpent dans le désert » |
| 11 | Ésaïe 53:5 → 1 Pierre 2:24 | Citation explicite | « par ses meurtrissures vous avez été guéris » |
| 12 | Ésaïe 53:7 → Actes 8:32-35 | Citation explicite | le passage est cité au long |
| 13 | Ésaïe 53:6 → 1 Pierre 2:25 | Allusion largement reconnue | « vous étiez comme des brebis errantes » |
| 14 | Ésaïe 53:12 → Luc 22:37 | Citation explicite | citation avec formule d'accomplissement |
| 15 | Psaume 22:2 → Matthieu 27:46 | Citation explicite | Jésus cite le psaume |
| 16 | Psaume 22:19 → Jean 19:24 | Citation explicite | cité avec formule |
| 17 | Psaume 22:17 → Jean 20:25 | Débat interprétatif | Jean ne cite pas le psaume, et la leçon hébraïque de 22:17 est discutée |
| 18 | Zacharie 12:10 → Jean 19:37 | Citation explicite | cité avec formule |
| 19 | Zacharie 13:7 → Matthieu 26:31 | Citation explicite | « il est écrit : je frapperai le berger » |
| 20 | Ésaïe 53:7 → Apocalypse 5:6 | Lecture chrétienne | l'Agneau immolé debout ; aucune citation |
| 119 | Lévitique 1:4 → 2 Corinthiens 5:21 | Écho thématique | l'imposition des mains, lien conceptuel |
| 120 | Deutéronome 21:23 → Galates 3:13 | Citation explicite | « maudit est quiconque est pendu au bois » |
| 121 | Ésaïe 53:4 → Matthieu 8:17 | Citation explicite | « afin que s'accomplît… il a pris nos infirmités » |
| 122 | Ésaïe 53:9 → 1 Pierre 2:22 | Citation explicite | reprise verbale serrée |
| 123 | Psaume 34:21 → Jean 19:36 | Débat interprétatif | Jean cite « aucun de ses os ne sera brisé » : la source est Exode 12:46 ou ce psaume, les commentateurs discutent |
| 124 | Lévitique 16:27 → Hébreux 13:12 | Citation explicite | Hébreux nomme le rite du bouc brûlé hors du camp |
| 125 | Nombres 19:9 → Hébreux 9:13-14 | Citation explicite | Hébreux nomme « la cendre d'une vache » |

Répartition proposée : **14 citations explicites · 6 allusions · 3 échos · 2 lectures
chrétiennes · 2 débats**. Et une référence à revoir (n° 4).

---

## Comment répondre

Le plus simple pour vous, le plus sûr pour le dépôt :

1. **Les trois décisions ci-dessus** — une lettre suffit : « 1c, 2a, 3 la fiche ».
2. **Le tableau** — ne corrigez que ce qui vous paraît faux. Le silence vaut accord.
   « 3 → écho », « 20 → allusion », il n'en faut pas plus.
3. Si un lien vous semble **à retirer** ou **à ajouter**, dites-le : la liste des 153 n'est
   pas sacrée non plus.

Une fois ce thème réglé, les sept autres suivent — Prophéties (41), Alliances (18),
Pâque & offrande (17), Temple (15), Un seul Dieu (14), Figures (13), Fils de l'homme (8) —
au même format, par lots que vous relisez.

---

## Ce qui bloque, dit franchement

Sans les textes bibliques dans `textes/` (R-004), la CI ne peut pas vérifier qu'une
citation en est une : elle vous croit sur parole, et moi aussi. C'est acceptable pour les
quatre dernières catégories, qui portent un jugement et non une mesure. Ce ne l'est pas
tout à fait pour la première, qui prétend à un fait vérifiable.

C'est pourquoi la décision **1** commande les autres.
