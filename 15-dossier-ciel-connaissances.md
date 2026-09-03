# Le ciel des connaissances — dossier d'architecture

**Document évolutif · v2 — tranché par le porteur le 1ᵉʳ septembre 2026.**
Réponse à la vision exprimée le 1ᵉʳ septembre : faire du ciel un explorateur de
connaissances — plonger d'un niveau quand on touche une constellation, remonter
jusqu'à l'Agneau, tirer le détail dans un panneau.

---

## La vision du porteur

Les étoiles ne devraient pas s'arrêter aux pages du site. Toucher « la Bible »
devrait descendre d'un cran — visuellement — dans ce qu'elle contient ; chaque
niveau devrait permettre de remonter, jusqu'à l'Agneau ; un clic sur une
constellation devrait ouvrir un panneau qui tire l'information en détail.
Une base de connaissances, explorée comme un ciel.

## Le challenge — trois dangers réels

**1. La deuxième maison.** Le site *est déjà* la descente : le ciel → une
étoile → la page, et la page porte trois strates écrites, traduites, relues.
Si les panneaux du ciel se mettent à raconter ce que racontent les pages, on
recrée le problème des deux halls (D-015) au niveau du contenu : deux endroits
qui disent la même chose, dont un pourrira. → **Règle : le ciel montre la
structure, la page porte l'enseignement.** Un panneau du ciel dit ce qu'une
chose *est*, *quand* elle se situe, *à quoi* elle se relie, et où *entrer* —
jamais plus de trois phrases, jamais le contenu des strates.

**2. La profondeur infinie.** Un zoom continu à niveaux illimités devient une
application, plus une page — et la charte exige qu'on puisse redessiner la page
de mémoire. → **Règle : trois niveaux, nommés, pas un de plus.**
Le ciel (tout le site) · la constellation (un domaine ouvert) · l'étoile et son
panneau. Chaque niveau est une scène séparée avec une transition — pas un zoom
pincé, injouable au pouce sur téléphone.

**3. Les vues qui divergent.** La connaissance vit aujourd'hui éparpillée dans
les objets des pages : 73 livres dans `LIB`, 153 correspondances AT↔NT dans le
diagramme du Fil Rouge (déjà thématisées), 14 prophètes sur la frise, 20
maillons de généalogie, 70 événements au relevé Cavins, 8 périodes dans
`periodes.yml`. Si le ciel copie ces données, elles divergeront à la première
retouche. → **Règle : la donnée d'abord.** Une source déclarée, des vues qui la
lisent, un contrôle CI qui refuse l'écart — le geste de `navigation.yml` et de
`periodes.yml`, étendu à la connaissance.

## Ce qui est fort dans la vision

Elle nomme ce que le site sait déjà sans le montrer : **tout est relié, et les
liens ont une nature.** La nomenclature D-013 (citation explicite · allusion
largement reconnue · écho thématique · lecture chrétienne · débat
interprétatif) est exactement le typage d'arêtes d'un graphe de connaissances.
Le ciel des connaissances, c'est D-013 rendu visible.

## L'architecture proposée

**`connaissances.yml` — la source.** Des entités typées (livre, personne,
événement, période, correspondance, page) et des liens typés par la
nomenclature D-013 + « se situe en » (période) + « mène à » (navigation).
Premier remplissage mécanique depuis ce qui existe : `LIB`, le diagramme `D`,
la frise, la généalogie, le relevé Cavins. Un `verifier-connaissances.py` :
chaque entité citée existe, chaque référence biblique est valide, aucun lien
vers une entité fantôme. **Ce chantier est vert** — mécanique, vérifiable,
sans jugement éditorial — donc donnable à la boucle du VPS.

**Le ciel — une vue parmi d'autres.** La carte actuelle devient la vue
« site » du graphe. Les constellations ouvrables en sont d'autres vues. La
bibliothèque, la frise, le Fil Rouge restent les vues *de contenu* — on ne les
reconstruit pas en étoiles, on leur donne la même grammaire (couleurs de
periodes.yml, geste toucher → panneau, fil d'Ariane commun).

**Les trois niveaux.**
1. **Le ciel** — existant. Le panneau s'enrichit : rôle en une phrase, liens
   réels *nommés* (toucher un nom déplace la sélection), et pour une étoile
   « constellation », le choix : *ouvrir la constellation* ou *entrer dans la
   page*.
2. **La constellation** — une scène par domaine ouvert. Première : **la
   Bibliothèque** — 73 étoiles-livres aux couleurs de leur période, arêtes =
   les liens vers le Christ déjà écrits dans `LIB`, badge D-013 quand il
   existe.
3. **L'étoile et son panneau** — trois phrases maximum, la nature du lien, et
   « entrer » vers la page (ancrée au bon endroit).

**Le fil d'Ariane du ciel :** l'Agneau · le ciel · la constellation · l'étoile
— toujours visible, chaque cran remonte.

## Le plan de construction

| Phase | Livrable | Critère « fait » | Zone |
|---|---|---|---|
| 0 | `connaissances.yml` + `verifier-connaissances.py`, remplis depuis l'existant | le contrôle passe en CI ; livres, correspondances, prophètes, maillons, périodes déclarés | verte |
| 1 | Panneau du ciel enrichi (rôle, liens nommés, choix constellation/page) **+ un descriptif en bas de page de ce qui attend dans l'étoile ou la constellation choisie** (demande du porteur ; il faudra des descriptions trilingues, à poser dans l'objet C de la carte) | naviguer le ciel sans le quitter ; aucune donnée dupliquée | orange |
| 2 | Constellation de la Bibliothèque (73 étoiles-livres) | même donnée que le pupitre — zéro copie ; captures mobiles validées | orange |
| 3 | **Les 153 correspondances en ciel thématique** — choisi par le porteur. Les 70 événements viendront après, en constellation du temps ; d'ici là ils vivent au relevé (`contenus/frise-cavins-releve.md`) | idem phase 2 | orange |
| 4 | Fil d'Ariane et transitions communs aux trois niveaux | remonter à l'Agneau depuis n'importe où en deux gestes | orange |

Chaque phase est une PR, fusion sur CI verte, captures réelles à l'appui.
Aucune phase n'ouvre la suivante sans l'accord du porteur.

## Les questions — tranchées le 1ᵉʳ septembre

1. **Phase 3 : les 153 correspondances d'abord.** Les 70 événements viendront
   ensuite, en constellation du temps ; d'ici là ils restent au relevé.
2. **Le niveau 1 reste la carte des pages** — avec, demande du porteur, **un
   descriptif affiché en bas de la page** disant ce qui attend dans l'étoile ou
   la constellation choisie. Le descriptif obéit à la règle des trois phrases.
3. **La règle des trois phrases au panneau : confirmée.**

## État

**Phase 0 : faite.** `connaissances.yml` déclare 73 livres, 153
correspondances, 8 thèmes, 14 prophètes, 20 générations, 8 périodes, 24 pages.
`outils/extraire-connaissances.mjs` mesure ce que les pages portent ;
`outils/verifier-connaissances.py` refuse tout écart dans les deux sens
(`--ecrire` régénère), et entre au banc `tout-verifier.sh` — huitième
contrôle. Le fichier n'est pas déployé : seul `*.html` part sur le site.

**Phase 1 : faite** (R-022). Le panneau du ciel dit le rôle de l'étoile en une
phrase, nomme ses passages réels (un toucher déplace la sélection), et les deux
accès depuis l'accueil sont posés — l'étoile « ✦ La carte » dans la barre du
haut et la bande de ciel sous les portes.

**Phase 2 : faite** (R-023). La constellation de la Bibliothèque : 73
étoiles-livres en onze amas d'étagère autour de l'Agneau, aux couleurs de leur
période, le lien D-013 du pupitre tirant un fil d'or vers le centre. La donnée
vit dans le bloc `CONSTEL` de la carte, généré et vérifié par
`verifier-connaissances.py` depuis la même mesure que `connaissances.yml` —
zéro copie éditée à la main. Fiche au premier toucher, pupitre au second,
« ✦ Ouvrir la constellation » sur l'étoile Bibliothèque, « ← Le ciel » pour
remonter, `#bibliotheque` partageable. Trois langues vérifiées au rendu réel.

**Phase 3 : faite** (R-024). La constellation des correspondances : les 153
en huit amas de thème autour de l'Agneau, aux couleurs mêmes du diagramme du
fil rouge. Fiche au premier toucher — thème, titre, références AT → NT ; au
second, la correspondance s'ouvre au bon arc du diagramme de l'accueil, qui
comprend désormais l'adresse `#c=N` (1..153). Entrée par l'étoile « Le fil
rouge » du ciel ; `#correspondances` partageable ; même bloc CONSTEL mesuré,
zéro copie.

**Phase 4 : faite** (R-025). Le fil d'Ariane complet, toujours visible :
« ✦ L'Agneau › Le ciel › la constellation ». Chaque cran remonte — l'Agneau
vers l'accueil, le ciel vers la carte des pages, le cran courant à l'encre.
Séparateur retourné en arabe. Les trois niveaux partagent la même transition
en fondu, immédiate quand le lecteur préfère un mouvement réduit. L'Agneau
est à un geste depuis n'importe où.

**Le plan de construction est achevé** : les quatre phases tranchées le
1ᵉʳ septembre sont sur le site. Prochaine descente possible, quand le
porteur le voudra : les 70 événements en constellation du temps, depuis
`contenus/frise-cavins-releve.md`.

## Révision — douze époques, deux vues (proposition à trancher, D-018)

Le porteur a regardé la constellation du livre et relevé sept choses. Chacune
avec sa correction.

**1. « Utilise les mêmes termes que Cavins. »** Notre carte du temps compte
huit périodes ; le dépliant en compte douze, et le relevé
(`contenus/frise-cavins-releve.md`) les met déjà en correspondance. On passe
`periodes.yml` à douze : **Monde des origines · Patriarches · Égypte et Exode ·
Désert · Conquête et Juges · Royaume · Royaume divisé · Exil · Retour · Révolte
des Maccabées · Accomplissement · L'Église** — aux dates du dépliant
(chronologie haute, Exode en 1446, à dire quand on l'emploie). Une seule carte
du temps, toujours : on remplace la nôtre, on n'en ajoute pas une deuxième.
Ce qui suit en cascade, par les miroirs : les bandeaux des quatorze pages
(chaque page reçoit son époque parmi les douze, puis `poser-situation.py`),
« La Bible en temps réel » (douze lignes — les jalons du monde par époque
sont au relevé), les couleurs de génération de la frise, les puces de période
de la salle, la légende de la carte. D-008 tient : « Révolte des Maccabées »
nomme un fait d'histoire, et le texte de l'époque garde « reçus diversement ».
Ce qui change par rapport à la ligne du relevé (« on ne reprend pas le
découpage en douze ») : le porteur choisit de l'adopter comme structure — c'est
D-018, et Cavins reste crédité en source. Les couleurs, elles, restent les
nôtres : le noir et le blanc du dépliant n'existent pas sur un ciel de nuit.

**2. « Les petits prophètes au-dessus du point, difficile à cliquer. »**
Corrigé aussitôt (PR #29) : les étiquettes ne captent plus le toucher. Dans la
refonte, elles quittent le champ d'étoiles : chaque étiquette suit l'arc
extérieur de sa section, retournée dans la moitié basse pour se lire à
l'endroit, réduite si l'arc est court. Plus jamais d'étiquette sur une étoile.

**3. « Séparer par un cadre léger les sections. »** Chaque section — la Loi,
les Historiques… — devient un secteur d'anneau dessiné d'un trait fin (la
couleur de ligne du site), fond à peine relevé, rayon intérieur au bord du halo
de l'Agneau, rayon extérieur sous l'étiquette. Les étoiles vivent dedans. Même
principe pour les douze époques de l'autre vue.

**4. « Les couleurs ne sont pas distinctables, surtout les jaunes ; les pères,
la Loi et le Royaume trop proches. »** Deux causes, deux corrections. Les halos
commencent par du blanc au centre : toutes les étoiles claires tirent vers le
même jaune blanchâtre — le halo prendra la couleur même de l'étoile, sans blanc,
avec un cœur plein et un anneau fin pour les teintes sombres. Et trois teintes
chaudes se suivaient (brun, ocre, or) : la palette de douze alterne chaud et
froid, et se valide au vérificateur (contraste sur le fond, séparation pour
les daltoniens) avant d'être posée. Les familles de teintes suivent l'ordre du
dépliant, pour qu'un lecteur qui le connaît s'y retrouve — sans en copier les
valeurs.

**5. « Selon Cavins, des chapitres peuvent appartenir à deux périodes —
Genèse, Rois ; Samuel est demi juge et demi roi. »** La donnée le sait déjà
(une liste de périodes par livre) ; le rendu ne le montrait pas. Deux réponses
selon la vue. Dans « Le livre », l'étoile devient **bicolore** — deux
demi-disques : Genèse origines | Patriarches · 1 Samuel Conquête et Juges |
Royaume · 1 Rois Royaume | Royaume divisé · 2 Rois Royaume divisé | Exil. Dans
« Les époques », le livre paraît dans chacune de ses époques **avec ses
chapitres**, comme le dépliant : « Genèse 1–11 » aux origines, « Genèse 12–50 »
chez les Patriarches ; « 1 Samuel 1–8 » et « 1 Samuel 9–31 ». La salle reçoit
ces tranches de chapitres dans sa donnée, et le miroir les mesure.

**6. « Petits prophètes : un seul gris — Joël doit être bleu, sinon explique
pourquoi. »** Joël était le seul livre sans période, parce que sa date est
disputée (IXᵉ siècle pour les uns, Vᵉ–IVᵉ pour les autres). Le dépliant
tranche : il range Joël parmi les prophètes du Sud au Royaume divisé, avec
Isaïe et Michée. On suit le dépliant — Joël prend la couleur du Royaume
divisé — et sa fiche porte la nuance « Débat interprétatif » sur la date. Au
passage, les gris du Nouveau Testament disparaissent aussi : Actes, les lettres
et l'Apocalypse étaient gris parce que notre carte s'arrêtait à
l'Accomplissement ; l'époque « L'Église » les accueille. Plus aucun livre hors
de la carte du temps.

**7. « On mélange les époques et les livres ; deux vues. »** C'est le vrai
diagnostic : la constellation range par étagère et colore par époque, si bien
qu'on ne lit le temps nulle part dans la disposition. Deux constellations, même
donnée :

- **« Le livre »** — le canon. Onze sections cadrées, étiquetées sur l'arc ;
  73 étoiles à la couleur de leur époque, bicolores quand il faut. Toucher un
  livre : sa fiche ; encore : son pupitre.
- **« Les époques »** — le récit. Douze secteurs cadrés dans l'ordre du temps,
  dans le sens des aiguilles depuis le haut, l'Église refermant le cercle sur
  les origines (le dernier événement du relevé est le retour du Christ). Dans
  chaque secteur : les livres « récit » de l'époque, par chapitres — ses
  étoiles principales — et ses livres « logés », plus petits. Toucher une
  étoile : la fiche du livre, avec sa tranche de chapitres. Toucher le secteur
  ou son étiquette : la fiche de l'époque — dates, figures, trois phrases, ses
  livres en puces, ses événements en puces (les 70 du relevé, enfin en ligne),
  « Entrer → la frise ».

Entrées : l'étoile « Le livre » du ciel offre les deux constellations ;
l'étoile « Les veilleurs » offre « Les époques ». Adresses `#livre` et
`#epoques`. Fil d'Ariane inchangé.

**Ordre de construction — trois PR après le Go :**

| | Livrable | Ce qui est vérifié |
|---|---|---|
| 1 | **La donnée** — `periodes.yml` à douze ; les quatorze pages remappées ; la salle reçoit ses époques depuis les « logés » du dépliant, avec les chapitres des livres récit ; temps réel à douze lignes ; frise remappée ; miroirs régénérés ; D-018 tranchée | les huit contrôles ; les bandeaux regénérés par le générateur, jamais à la main |
| 2 | **« Le livre » refaite** — cadres, étiquettes sur l'arc, halos, étoiles bicolores, légende à douze, palette validée | rendu réel trois langues ; aucune étiquette sur une étoile ; validateur de palette |
| 3 | **« Les époques »** — la nouvelle scène, la fiche d'époque, les deux entrées, l'adresse | rendu réel ; 70 événements et 73 livres tous placés ; fil d'Ariane |

Ce que le plan ne fait pas : renommer des fichiers, toucher aux strates des
pages, créer une deuxième carte du temps.

## Recentrage — le récit d'abord (3 septembre, D-019)

Le porteur et le product owner ont fixé le but principal : **raconter comment on
trouve Jésus depuis la création jusqu'au dernier livre — tout tourne autour de
lui** — et le point de départ pour un débutant : **le récit**, les quatorze livres
qui tiennent l'histoire d'un trait.

| # | Livre | Époques |
|---|---|---|
| 1 | Genèse | Monde des origines (1–11) · Patriarches (12–50) |
| 2 | Exode | Égypte et Exode |
| 3 | Nombres | Désert |
| 4 | Josué | Conquête |
| 5 | Juges | Juges |
| 6 | 1 Samuel | Conquête et Juges (1–8) · Royaume (9–31) |
| 7 | 2 Samuel | Royaume |
| 8 | 1 Rois | Royaume (1–11) · Royaume divisé (12–22) |
| 9 | 2 Rois | Royaume divisé (1–16) · Exil (17–25) |
| 10 | Esdras | Retour |
| 11 | Néhémie | Retour |
| 12 | 1 Maccabées | Révolte des Maccabées |
| 13 | Luc | Accomplissement |
| 14 | Actes | L'Église |

Ce que cela change au plan de la section précédente : **l'ordre**. La vue « Les
époques » passe devant « Le livre », et elle porte le récit : les quatorze livres
en étoiles principales, par chapitres, dans l'ordre ; les autres livres « logés »
autour ; et dans chaque époque, *où Jésus s'y trouve* — les correspondances du fil
rouge dont le texte de l'Ancien Testament tombe dans l'époque, en puces dans la
fiche. Le débutant lit ainsi la Bible comme une seule histoire, et voit à chaque
époque le fil qui la traverse.

**Le sens est tranché : on part du Christ.** Le chemin des époques commence à
l'Accomplissement, sous la lumière de l'Agneau, et remonte le temps de secteur
en secteur jusqu'aux origines ; le dernier pas est l'Église, voisine de
l'Accomplissement sur l'anneau — la boucle d'Emmaüs : on quitte Jérusalem, les
Écritures s'ouvrent « en commençant par Moïse », et l'on revient à Jérusalem, où
les Actes commencent. Un tour complet, à rebours du temps, qui ramène au Christ.
Les crans du chemin sont numérotés dans ce sens ; l'Accomplissement est le
premier.

**PR 1 — la donnée : faite.** `periodes.yml` compte douze époques aux termes du
dépliant, dates du dépliant (chronologie haute, dite), couleurs validées au
vérificateur sur le fond du site (bande de clarté, chroma, séparation
daltonienne et normale entre époques voisines, contraste), l'Église à l'encre.
Les quatorze pages remappées et leurs bandeaux régénérés ; la salle reçoit ses
époques depuis les « logés » du dépliant, avec les tranches de chapitres des
livres récit coupés (Genèse 1–11 / 12–50, 1 Samuel 1–8 / 9–31, 1 Rois 1–11 /
12–22, 2 Rois 1–16 / 17–25) ; Joël au Royaume divisé ; le Nouveau Testament à
l'Église — plus aucun livre hors de la carte. « La Bible en temps réel » passe
à douze lignes, la frise et la carte suivent par les miroirs.

**PR 2 — la vue des époques : faite** (R-029). Douze secteurs cadrés dans
l'ordre du temps, l'Accomplissement en haut ; chaque époque étiquetée sur son arc
avec son cran du chemin. Les 77 étoiles-livres — les quatre livres récit coupés
paraissent dans leurs deux époques —, les quatorze du récit cerclées d'or, et le
fil d'or du chemin qui les relie de Luc aux origines, puis aux Actes : la boucle
d'Emmaüs, dessinée. La fiche d'une époque dit son cran, ses dates, trois phrases,
ce qui s'y passe (nos événements, écrits d'après le relevé — la liste fermée des
soixante-dix reste celle du dépliant), et *où Jésus s'y trouve* : les
correspondances du fil rouge dont le texte de l'Ancien Testament tombe dans
l'époque, en puces qui ouvrent le diagramme au bon arc. Les 153 trouvent toutes
leur époque.

**PR 3 — « Le livre » refaite : faite.** Le même moteur de secteurs : onze
sections cadrées d'un trait fin, étiquettes sur l'arc hors du champ d'étoiles,
halos à la couleur même de l'étoile — c'est le blanc au centre des halos qui
brouillait les jaunes —, étoiles bicolores pour les quatre livres à deux
époques, légende à douze. **La révision est achevée** : les deux vues, « Le
livre » (le canon) et « Les époques » (le chemin), lisent la même donnée.

Le compte des livres, lui, est corrigé sans attendre (R-030) : **66 + 7**, les sept
venus de la Bible grecque, et la note « Pourquoi 66 + 7 ? » qui explique la
différence en toute transparence.

