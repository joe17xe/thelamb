# Journal des décisions

Les décisions qui engagent le site entier — la logique de navigation, la charte
visuelle, ce qu'on assume et ce qu'on abandonne. Une décision non écrite sera reprise
par le premier qui n'était pas dans la pièce.

Format : une entrée par décision, la plus récente en haut. On ne réécrit pas une entrée
tranchée ; on en ajoute une nouvelle qui la remplace, en le disant.

```
## D-00X — Le titre de la décision
**Date :** — **Statut :** à trancher / tranchée / remplacée par D-00Y
**La question :**
**Ce qui a été décidé :**
**Pourquoi :**
**Ce qu'on abandonne :**
```

---

## À trancher

Six questions ouvertes, relevées sur l'état du site. Elles ne sont pas des tickets :
elles se tranchent de vive voix, puis s'écrivent ici.

### D-001 — Par où entre-t-on dans le site ?
**Statut :** à trancher
**La question :** l'accueil est le Fil Rouge, un diagramme. `seuil-landing.html`
(« une porte, des salles ») joue aussi ce rôle et reçoit le seul lien de l'accueil.
Deux pages se disputent la porte d'entrée, et le seuil ne mène nulle part.
**Options :** le diagramme d'abord, saisissant mais abstrait · le seuil d'abord, plus
guidant mais moins singulier · fondre les deux.

### D-002 — Que fait-on des six piliers ?
**Statut :** à trancher
**La question :** environ 21 000 mots rédigés — le Sang, le Baptême, la Parole
éternelle, la Résurrection, le Temple détruit, la Transfiguration — que rien ne relie
au reste du site, ni en entrée ni en sortie.
**Options :** les rattacher au parcours en 7 étapes comme approfondissements ·
en faire une septième section à part entière · les fondre dans les étapes existantes.

### D-003 — Les trois strates : promesse ou option ?
**Statut :** à trancher
**La question :** *L'essentiel / Comprendre / Aller plus loin* est la promesse de
lecture du site. Elle est tenue sur 9 pages, absente des 15 autres — dont les plus
longues.
**Ce que ça coûte si c'est une promesse :** reprise de 15 pages. C'est le plus gros
chantier ouvert.

### D-004 — L'anglais : on le produit ou on l'assume absent ?
**Statut :** à trancher
**La question :** les trois langues sont déclarées sur chaque page, mais l'anglais
est marginal dans le contenu réel là où l'arabe est nourri. Un sélecteur qui promet
une langue vide coûte plus cher qu'un sélecteur à deux entrées.

### D-005 — Dans quel ordre produit-on ?
**Statut :** à trancher
**La question :** six chantiers ouverts au cadrage — les cinq alliances, la galerie
des figures, les trois parcours guidés, la page « À propos ». Lequel d'abord ?

### D-006 — Réparer avant d'ajouter ?
**Statut :** à trancher
**La question :** 14 pages sur 24 sont inaccessibles. Faut-il relier l'existant avant
d'écrire quoi que ce soit de neuf ? Un chapitre de plus dans un site où rien ne se
relie, c'est une quinzième page orpheline.

---

## Tranchées

### D-013 — On ne montre pas un doute, on nomme la nature du lien
**Date :** 30 août 2026 — **Statut :** tranchée — **Remplace :** D-012
**La question :** D-012 avait rendu `[À VÉRIFIER]` visible du lecteur, au nom de la
transparence. À la relecture, le raisonnement était faux sur ce cas précis : l'incertitude
ne portait pas sur la solidité du renvoi d'Hébreux 11:35 aux martyrs de 2 Maccabées 6–7 —
une allusion largement reconnue en exégèse — mais sur sa **nature** : allusion et non
citation. Afficher « à vérifier » faisait passer pour une erreur possible ce qui est un
lien bien établi.
**Ce qui a été décidé :** `[À VÉRIFIER]` redevient un jeton d'atelier, qui se lève avant
publication. Ce que le lecteur voit, c'est un **badge nommant le type de lien**, adossé à
une nuance dépliable qui explique le classement. Cinq catégories, stables et trilingues :
citation explicite · allusion largement reconnue · écho thématique · lecture chrétienne ·
débat interprétatif.
**Pourquoi c'est meilleur :** le doute brut infantilise et se lit comme un aveu de
faiblesse. Nommer la nature du lien est plus exact, plus utile au lecteur, et
intellectuellement plus fort — on ne cache rien, on classe. Le principe de D-012 survit :
on ne lisse pas. Seul le moyen change.
**Bénéfice œcuménique :** la question du lien littéraire entre Hébreux et 2 Maccabées est
distincte de celle du canon. La nuance le dit explicitement, ce qui permet à un lecteur
protestant d'examiner l'allusion sans avoir à trancher le canon d'abord.
**Ce qu'on abandonne :** rien de solide. D-012 aura duré une heure, et aura servi à
trouver la bonne formulation.
**Comment la règle tient :** `verifier-references.py` refuse désormais toute page publiée
qui contient un jeton d'atelier, et se tait sur `contenus/` où le jeton est à sa place.
Le contrôle cherche le crochet ouvrant, pas le mot seul : la croix dit d'un évangile qu'il
« s'expose à la vérification » (للتحقّق), et c'est de la prose, pas une marque.

### D-012 — La marque de vérification est visible du lecteur, et dans sa langue
**Date :** 30 août 2026 — **Statut :** remplacée par D-013 le jour même
**La question :** le renvoi d'Hébreux 11:35 à 2 Maccabées 7 est une lecture largement
reçue, mais pas une citation explicite. Fallait-il l'afficher marquée, la reformuler pour
noyer l'incertitude, ou retirer le renvoi ?
**Ce qui a été décidé :** garder la marque, et la rendre publique. Sur un site dont
l'argument central est la fiabilité des Écritures, montrer où l'on n'est pas certain vaut
mieux que de lisser. Un lecteur qui voit une marque de doute sur un point mineur croit
davantage le reste.
**Ce que cela implique :** la marque n'est plus un jeton d'atelier, c'est du contenu. Elle
se traduit donc — `[À VÉRIFIER]` en français, `[TO VERIFY]` en anglais, `[للتحقّق]` en
arabe. La laisser en français devant un lecteur arabophone aurait été un défaut, pas une
convention.
**Ce qu'on abandonne :** l'apparence d'une page entièrement assurée. C'est le but.

**Portée :** cette règle vaut pour toute référence dont l'attribution est discutée. Elle
ne dispense de rien : une référence marquée reste une dette, que l'entrée R-004 lèvera
mécaniquement quand les textes de référence seront dans le dépôt.

### D-011 — Les deutérocanoniques ont leur étagère, et les chiffres les nomment
**Date :** 30 août 2026 — **Statut :** tranchée
**La question :** D-008 disait de les présenter sans les écarter. La salle de la
bibliothèque les nommait déjà dans une note honnête, mais le site affirmait « 66 livres »
vingt-sept fois et ses étagères n'en montraient que 66. Mentionnés, pas montrés.
**Ce qui a été décidé :** une sixième étagère à l'Ancien Testament, tracée en pointillé,
portant la mention « reçus diversement selon les traditions » et un avertissement en
tête : *cette étagère ne dit pas que ces livres sont canoniques pour tous*. Les sept
livres y sont montrés comme les autres — Tobie, Judith, Sagesse, Siracide, Baruch, 1 et
2 Maccabées. Les chiffres affichés deviennent « 66 en commun · 73 avec les
deutérocanoniques », et la note sur le canon renvoie à l'étagère en rappelant que les
Églises orthodoxes en reçoivent davantage encore.
**Ce qu'on n'a pas fait :** le Fil Rouge garde son axe sur les 66 livres communs. Son jeu
de données ne contient aucune correspondance touchant ces livres ; déplacer l'axe
déplacerait les 153 arcs sans rien ajouter. C'est écrit en commentaire dans le fichier.
**Ce qu'on abandonne :** la simplicité d'un chiffre unique. Le site dira désormais deux
nombres et ce qui les sépare — c'est plus long à lire, et c'est plus vrai.

### D-010 — Claude fusionne les pull requests dont la CI est verte
**Date :** 30 août 2026 — **Statut :** tranchée
**La question :** chaque livraison demandait un aller-retour — Claude ouvre la PR,
attend, le porteur clique. Deux fois de suite, du travail terminé et vérifié est resté
invisible plusieurs heures faute de ce clic, et a été signalé comme un défaut du site.
**Ce qui a été décidé :** Claude fusionne lui-même une PR qu'il a ouverte, une fois la
CI verte et sans conflit. Le porteur garde le retour arrière : le déploiement est
réversible par `git revert`, et le site revient en une minute.
**Ce qu'on abandonne :** la relecture systématique avant publication. En contrepartie,
la CI doit rester digne de cette confiance — c'est elle, désormais, qui tient la porte.

### D-007 — La frise est la carte, pas le chemin
**Date :** 30 août 2026 — **Statut :** tranchée
**La question :** le cadre narratif de référence (périodisation de l'histoire du salut)
est chronologique et ascendant, de la Création à l'Église. Le premier principe du site
est descendant : on part du Christ révélé et on remonte. Fallait-il changer de sens ?
**Ce qui a été décidé :** garder le parcours descendant, et faire de la frise un repère
de situation. Le lecteur voyage à rebours, mais sait toujours où il se trouve dans
l'histoire. La frise répond à *quand*, le parcours répond à *pourquoi*.
**Ce qu'on abandonne :** l'ordre de lecture chronologique, qui aurait été plus familier
aux lecteurs venant d'un plan de lecture annuel.

### D-008 — Les livres deutérocanoniques sont présentés, pas écartés
**Date :** 30 août 2026 — **Statut :** tranchée
**La question :** le cadre de référence est catholique et compte 1 Maccabées parmi ses
livres narratifs, Tobie, Judith, Sagesse, Siracide et Baruch parmi les autres. La règle
des trois cercles interdit d'arbitrer entre traditions. Que faire de ces livres ?
**Ce qui a été décidé :** les présenter. Ce sont des livres qui ont le mérite d'exister
et les écarter fermerait une porte. On reste ouvert.
**Ce que cela implique concrètement :** on les situe et on les cite, sans les décréter
canoniques pour tous. La différence de canon devient elle-même un sujet traité en trois
cercles — sur la page de la bibliothèque, qui explique déjà la composition de la Bible.
Présenter n'est pas trancher : la formulation doit rester descriptive.

### D-009 — La périodisation est ré-exprimée, pas reprise
**Date :** 30 août 2026 — **Statut :** tranchée
**La question :** le document de référence est une œuvre déposée — marques enregistrées,
copyright sur la charte, sur le choix des couleurs, sur la sélection des livres narratifs.
**Ce qui a été décidé :** périodiser l'histoire du salut est une idée ancienne que
personne ne possède, et les faits racontés sont des faits. On garde donc la démarche et
on écrit la nôtre : nos noms de périodes, notre palette, nos formulations. La source
d'influence est citée en bibliographie.
**Ce qu'on abandonne :** la commodité de reprendre un système déjà fait et déjà connu
de certains lecteurs.
