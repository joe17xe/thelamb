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
