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
**Statut :** tranchée le 31 août 2026 — **voir D-015**
**La question :** l'accueil est le Fil Rouge, un diagramme. `seuil-landing.html`
(« une porte, des salles ») joue aussi ce rôle et reçoit le seul lien de l'accueil.
Deux pages se disputent la porte d'entrée, et le seuil ne mène nulle part.
**Options :** le diagramme d'abord, saisissant mais abstrait · le seuil d'abord, plus
guidant mais moins singulier · fondre les deux.
**Réponse :** ni l'un ni l'autre en concurrence — un seul hall (le Fil Rouge), et le
seuil réduit à ce qu'il annonce, une porte. Le détail est en D-015.

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

### D-016 — Le ciel des connaissances est lancé, sous trois garde-fous
**Date :** 1ᵉʳ septembre 2026 — **Statut :** tranchée — **Dossier :** `15-dossier-ciel-connaissances.md`
**La question :** le porteur veut explorer le site comme un graphe de connaissances —
plonger dans une constellation, remonter jusqu'à l'Agneau, tirer le détail dans un
panneau. Vision forte, et dangereuse : elle peut recréer une deuxième maison, creuser
une profondeur infinie, et faire diverger les vues de la donnée.
**Ce qui a été décidé :** on construit, sous trois garde-fous. Le ciel montre la
structure, la page porte l'enseignement — le panneau tient en trois phrases, jamais le
contenu des strates. Trois niveaux nommés, pas un de plus : le ciel, la constellation,
l'étoile et son panneau. Et la donnée d'abord : `connaissances.yml`, miroir déclaré de
ce que les pages portent, contrôlé en CI dans les deux sens.
**Les choix du porteur :** le niveau 1 reste la carte des pages, avec un descriptif en
bas de page de ce qui attend dans l'étoile choisie ; la première constellation ouverte
sera la Bibliothèque, la deuxième les 153 correspondances — les 70 événements du relevé
Cavins viendront ensuite, en constellation du temps.
**Pourquoi c'est dans l'esprit du site :** la nomenclature D-013 est exactement le
typage d'arêtes d'un graphe de connaissances. Le ciel des connaissances, c'est D-013
rendu visible.

### D-015 — Un seul hall, et un seuil qui n'offre qu'une porte
**Date :** 31 août 2026 — **Statut :** tranchée — **Referme :** D-001
**La question :** l'accueil et le seuil listaient **les six mêmes destinations**, dans
deux ordres différents et sous deux vocabulaires différents. Le lecteur croyait
découvrir de nouvelles salles, puis comprenait que non. Deux salles portaient même deux
noms : « La bibliothèque » ici, « Qu'est-ce que la Bible ? » là. Et le seuil, dont le
sur-titre annonce « une seule porte », en offrait huit — la page se contredisait.
**Ce qui a été décidé :** un seul hall, l'accueil. Il garde la liste des six salles,
avec le vocabulaire qui dit au lecteur ce qu'il va trouver — *le fil en personne, celui
qui parle, la table, la source, vérifier, les dates* — et non l'état de production de
la salle. Les étiquettes « Ouverte » et « Nouvelle salle » disparaissent : elles
renseignaient sur le calendrier éditorial, et « nouvelle » est périssable.
**L'ordre suit la charte.** L'Agneau vient en premier, puis ce qui l'entoure — Celui qui
parle, La table — puis ce qui le vérifie — La source, Vérifier, Les dates. On descend
du Christ ; on ne remonte pas vers lui depuis la documentation.
**Le seuil redevient un seuil.** Une entrée depuis l'extérieur, pour un lien partagé :
une phrase, une porte — la route d'Emmaüs — et un renvoi discret vers le fil rouge.
Aucune page du site n'y mène, et c'est voulu : un lecteur déjà entré n'a pas à repasser
par la porte. `navigation.yml` le déclare `racine`, comme l'accueil.
**Ce qu'on abandonne :** la carte « À venir · D'autres salles », qui promettait ce qui
n'existe pas et ne menait nulle part. Le site dira ses nouvelles salles quand elles
existeront.

### D-014 — Un déploiement doit prouver qu'il a eu lieu
**Date :** 30 août 2026 — **Statut :** tranchée
**La question :** la PR #8 a été fusionnée sur une CI verte, et son déploiement a
échoué — `ssh-keyscan` n'a pas obtenu de réponse du VPS. Le site est resté en arrière
sans que rien ne le signale. La règle D-010 dit « fusion auto dès que la CI est verte » ;
elle supposait sans le dire que fusionné vaut publié.
**Ce qui a été décidé :** le déploiement se prouve, en trois temps. Il **reprend** sur
panne réseau (quatre essais espacés, sur `ssh-keyscan` comme sur `rsync`), plutôt que de
conclure d'un silence d'une seconde que la porte est close. Il **refuse** un lot qui
ferait fondre le site de plus de moitié — même garde-fou que dans `poser-situation.py`,
parce que `rsync --delete` obéit sans discuter. Il **vérifie** : empreintes comparées
fichier par fichier, puis le titre d'`index.html` redemandé au serveur web.
**Ce que cela implique :** un échec ne peut plus être silencieux. Il ouvre un ticket
« Déploiement bloqué » que le premier déploiement réussi referme. Un signal qui ne
s'éteint jamais cesse d'être un signal.
**Effet de bord utile :** les contrôles tournent aussi avant de publier, donc ce qui est
en ligne les a passés même si la page est arrivée par une poussée directe sur `main`.
**Ce qu'on abandonne :** rien. Un déploiement qui échoue bruyamment vaut mieux qu'un
déploiement qui réussit à moitié.

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
