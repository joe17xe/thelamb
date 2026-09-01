# Le ciel des connaissances — dossier d'architecture

**Document évolutif · v1 — proposition, à trancher par le porteur.**
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
| 1 | Panneau du ciel enrichi (rôle, liens nommés, choix constellation/page) | naviguer le ciel sans le quitter ; aucune donnée dupliquée | orange |
| 2 | Constellation de la Bibliothèque (73 étoiles-livres) | même donnée que le pupitre — zéro copie ; captures mobiles validées | orange |
| 3 | Deuxième constellation, **au choix du porteur** : les 153 correspondances en ciel thématique, ou les 70 événements sur le temps | idem phase 2 | orange |
| 4 | Fil d'Ariane et transitions communs aux trois niveaux | remonter à l'Agneau depuis n'importe où en deux gestes | orange |

Chaque phase est une PR, fusion sur CI verte, captures réelles à l'appui.
Aucune phase n'ouvre la suivante sans l'accord du porteur.

## Les questions au porteur

1. **Phase 3 :** les correspondances (le cœur théologique — 153 arcs déjà
   thématisés) ou les événements (le temps — le relevé Cavins entre au site) ?
2. **Le niveau 1 actuel reste-t-il la carte des pages ?** Proposition : oui —
   c'est le plan honnête de la maison ; la connaissance s'ouvre *dans* les
   constellations. L'alternative (des étoiles-concepts dès le niveau 1) rend la
   carte plus abstraite et casse « la carte est mesurée ».
3. **Le panneau : trois phrases maximum, jamais le contenu des strates** — la
   règle anti-deuxième-maison. Confirmée ?
