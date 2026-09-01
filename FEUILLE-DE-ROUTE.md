# Feuille de route

Ce fichier est lu par la boucle autonome du VPS. Elle traite **une entrée par
exécution**, dans l'ordre du fichier, et ouvre une pull request. Elle ne pousse
jamais sur `main`.

## Écrire une entrée

```markdown
## R-0XX Le titre, à l'infinitif
- zone: verte | orange | rouge
- statut: à faire | en cours | fait | bloqué
- pourquoi: ce que ça règle, en une phrase
- fait quand: le critère qui permet de dire que c'est terminé
```

`zone` décide de l'autonomie : **verte** = mécanique et vérifiable, la PR se
fusionne seule si la CI est verte · **orange** = le robot prépare, tu valides ·
**rouge** = jamais automatisé, c'est une décision.

L'état ne vit pas ici mais dans les PR : « R-012 est-elle faite ? » se répond par
« existe-t-il une PR fusionnée `[R-012]` ? ». On garde `statut` à jour à la main
pour la lisibilité, mais la boucle vérifie les PR avant de commencer.

**Coupe-circuit :** créer un fichier `PAUSE` à la racine, depuis GitHub, arrête la
boucle à l'exécution suivante. Le supprimer la relance.

---

## R-001 Trancher les six questions structurantes
- zone: rouge
- statut: en cours — 1 sur 6 tranchée
- pourquoi: rien ne s'automatise correctement tant que la structure cible est inconnue
- fait quand: les six entrées de producteur/06-JOURNAL-DES-DECISIONS.md sont tranchées et écrites
- avancement: D-001 (par où entre-t-on) tranchée le 31 août par D-015. Restent D-002
  (les six piliers), D-003 (les trois strates), D-004 (l'anglais), D-005, D-006.

## R-002 Écrire navigation.yml — la structure décidée, en donnée
- zone: rouge
- statut: fait
- pourquoi: transforme l'accord en contrainte tenue ; c'est le fichier dont dépend tout le reste
- fait quand: chaque page du site y figure avec sa section, son entrée et sa suite
- résultat: carte écrite à partir de l'intention déjà inscrite dans les pages, pas inventée

## R-003 Réparer le maillage d'après navigation.yml
- zone: verte
- statut: fait
- pourquoi: 14 pages sur 24 sont inaccessibles ; c'est le plus gros défaut du site
- fait quand: aucune page n'a zéro lien entrant, et verifier-liens ne signale plus d'écart
- résultat: zéro orpheline, zéro cul-de-sac, zéro écart — les neuf blocs « page suivante »
  qui pointaient sur href="#" ont reçu leur adresse, et cinq liens secondaires ont ouvert
  les chaînes qui restaient sans entrée

## R-009 Poser la carte du temps sur les pages
- zone: verte
- statut: fait
- pourquoi: le lecteur remonte le temps ; il doit savoir en permanence où il se trouve
- fait quand: chaque page historiquement située porte son bandeau, dérivé d'une source unique
- résultat: periodes.yml (huit périodes trilingues) + outils/poser-situation.py, posé sur
  14 pages ; la frise alignée sur D-008 pour la période intertestamentaire

## R-010 Écrire les références au complet, page par page
- zone: orange
- statut: à faire
- pourquoi: 375 références sont écrites « (12:10) » sans nom de livre. Le lecteur doit
  deviner le livre depuis la phrase précédente — sur téléphone, dans une carte, il ne le
  peut pas. Et le vérificateur ne les contrôle pas : elles sont hors de portée du filet.
- fait quand: verifier-references ne signale plus de référence sans livre
- attention: pas automatisable. Une passe mécanique par « dernier livre cité » produit des
  faux — « (6:16) » devient Zacharie alors que le contexte est l'Apocalypse. Se fait à la
  main, page par page, dans les trois langues à la fois.
- ordre suggéré: emmaüs (48) — fait — puis salle-bibliotheque (123), la plus lourde
- reste: 327 références nues sur 18 pages

## R-011 Enrichir la page d'Emmaüs — les sept seuils
- zone: orange
- statut: fait
- pourquoi: les points du fil ne mènent à rien ; la matière existe pour en faire les sept
  seuils du récit, de la déception au témoignage
- fait quand: chaque point ouvre son seuil, avec son texte et sa référence complète
- résultat: les sept points sont devenus des boutons ; les 48 références nues de la page
  sont complétées ; trois courts fragments de Luc sont nouveaux et restent à vérifier
  contre le texte de référence quand R-004 sera fait

## R-012 Montrer les livres deutérocanoniques, pas seulement les nommer
- zone: rouge
- statut: fait
- pourquoi: la décision D-008 dit qu'on les présente et qu'on ne les écarte pas. La salle
  de la bibliothèque les nomme déjà dans une note honnête, en trois langues — mais le site
  affirme « 66 livres » 27 fois, et ses données n'en connaissent que 66. Ils sont
  mentionnés, pas montrés.
- fait quand: le lecteur peut voir ces livres et leur place, sans que le site décrète pour
  autant qu'ils sont canoniques pour tous
- attention: c'est une décision éditoriale avant d'être une tâche. Trois voies possibles :
  laisser la note seule (le site ne change pas), ajouter une étagère distincte marquée
  comme reçue diversement, ou ouvrir une page dédiée à la question du canon. La deuxième
  respecte le mieux les trois cercles, mais elle touche le décompte affiché partout.

## R-013 Étendre la nomenclature des liens aux pages qui en ont besoin
- zone: orange
- statut: à faire
- pourquoi: le site montre environ mille renvois sans jamais dire de quelle nature ils
  sont. Une citation explicite, une allusion reconnue et une lecture typologique n'ont pas
  la même force, et le lecteur ne peut pas les distinguer.
- fait quand: les liens dont la nature se discute portent leur badge et leur nuance
- attention: ne pas badger ce qui n'en a pas besoin. Un renvoi évident alourdirait la page
  pour rien. La nomenclature sert là où un lecteur averti pourrait objecter.
- première application: 2 Maccabées et Hébreux 11:35, sur l'étagère deutérocanonique

## R-014 Rendre le déploiement démontrable
- zone: verte
- statut: fait
- pourquoi: la fusion de la PR #8 est passée alors que son déploiement échouait — le site est resté en arrière sans que rien ne le dise, ce qui vide de sens la règle « fusion auto dès que la CI est verte »
- fait quand: un déploiement reprend sur panne réseau, refuse un lot qui viderait le site, prouve que ce qui est servi correspond au dépôt, et ouvre un ticket s'il échoue
- résultat: contrôles avant publication, quatre reprises sur ssh-keyscan et sur rsync,
  garde-fou de moitié sur le nombre de pages, comparaison d'empreintes puis
  requête au serveur web, ticket « Déploiement bloqué » ouvert puis refermé
  automatiquement (D-014)

## R-015 Monter les actions GitHub d'une version majeure
- zone: rouge
- statut: à faire
- pourquoi: actions/checkout@v4 et actions/github-script@v7 visent Node 20, que les runners forcent déjà sur Node 24 — ça marche aujourd'hui, ça cassera un jour sans prévenir
- fait quand: checkout@v5 et github-script@v8, un déploiement vert derrière, plus aucun avertissement de dépréciation dans le journal
- pourquoi rouge: l'entrée touche `.github/workflows/`, que la consigne de la boucle
  interdit au robot. Verte, elle l'aurait fait choisir une tâche qu'il n'a pas le
  droit de faire — son premier tour autonome aurait échoué à coup sûr.

## R-016 Un seul hall — dégrouper l'accueil et le seuil
- zone: rouge
- statut: fait
- pourquoi: l'accueil et le seuil listaient les six mêmes salles, dans deux ordres et sous deux vocabulaires — le lecteur croyait en découvrir de nouvelles, puis comprenait que non
- fait quand: une seule page liste les salles, les noms sont uniformes, l'ordre suit la charte, et le seuil n'offre qu'une porte
- résultat: l'accueil devient le hall unique, portes réordonnées l'Agneau d'abord,
  noms alignés sur ceux du seuil, badges d'état supprimés ; le seuil réduit à une
  porte vers Emmaüs et déclaré `racine` ; fil d'Ariane de la bibliothèque redirigé
  vers le hall ; carte « À venir » retirée (D-015, referme D-001)

## R-017 La Bible en temps réel — l'histoire biblique face au monde datable
- zone: rouge
- statut: fait
- pourquoi: la section « Une Bible fiable » argumentait par les manuscrits et les prophéties, mais ne montrait pas que le récit traverse une histoire datable — c'était l'apport principal du dépliant de Cavins (voir contenus/frise-cavins-releve.md)
- fait quand: chaque période de periodes.yml se lit face à des jalons du monde vérifiables indépendamment, dans les trois langues
- résultat: section « La Bible en temps réel » posée entre les repères chiffrés et le
  cadre d'honnêteté — huit périodes aux couleurs de periodes.yml, « dans la Bible » /
  « dans le monde » en face à face, nuance sur les marges de datation (l'Exode
  notamment). Choisi par le porteur le 1ᵉʳ septembre (« A puis B puis C »).

## R-018 Chaque livre reçoit son moment — les pastilles de période au pupitre
- zone: rouge
- statut: fait
- pourquoi: les étagères disent ce que contient la bibliothèque, pas quand se situe le récit de chaque livre — c'était le deuxième apport du dépliant de Cavins
- fait quand: chaque pupitre affiche la ou les périodes du récit, aux couleurs et aux noms de periodes.yml, dans les trois langues
- résultat: 49 livres pastillés, 24 sans pastille à dessein — les Actes, les lettres
  et l'Apocalypse sont au-delà de notre carte, et Joël est débattu (le site le dit
  déjà pour sa date). Au passage, la période de l'exil courait jusqu'en 587 alors
  que le retour commence en 538 : les quarante-neuf ans de captivité n'étaient
  dans aucune période — l'exil court maintenant jusqu'à l'édit de Cyrus (538).

## R-019 La généalogie remontante — de Jésus à Adam sur la frise
- zone: rouge
- statut: fait
- pourquoi: le dépliant de Cavins trace Adam → Jésus en descendant ; Luc 3:23-38 fait l'inverse — l'Écriture fait elle-même notre mouvement éditorial, il suffisait de le montrer
- fait quand: la frise des veilleurs porte la chaîne des générations remontée depuis Jésus, aux couleurs de periodes.yml, avec la nuance sur les deux généalogies, dans les trois langues
- résultat: vingt maillons de Jésus à Adam, chacun à la couleur de sa période ; les
  femmes que Matthieu nomme (Tamar, Rahab, Ruth) portées aux maillons ; la fourche
  Matthieu/Luc entre Jésus et David traitée en « Débat interprétatif » selon la
  nomenclature D-013 — lectures présentées côte à côte, sans arbitrer.

## R-020 La carte du ciel — tout le site d'un seul regard, l'Agneau au centre
- zone: rouge
- statut: fait
- pourquoi: demandé par le porteur — une carte mentale de tout le site, façon univers, le Christ au centre, les connexions visibles
- fait quand: une page montre les 23 pages en étoiles autour de l'Agneau, avec les liens réels du site, dans les trois langues
- résultat: carte-du-ciel.html — trois orbites (le fil, les salles, les piliers), deux
  entrées au bord, 34 arêtes tirées de navigation.yml (la carte est mesurée, pas
  dessinée) ; palette des familles validée par calcul (daltonisme, contraste) sur le
  fond du site ; toucher une étoile allume ses liens, la retoucher fait entrer ;
  vérifiée par captures réelles en mobile, bureau et arabe. Verset socle :
  Colossiens 1:17. Affinée le même jour sur une référence visuelle du porteur
  (graphe de connaissances) : lueurs en dégradés, taille des étoiles selon leur
  nombre de liens, positions relâchées par simulation hors ligne puis figées,
  respiration lente du centre — toujours sans bibliothèque.

## R-021 Ciel des connaissances, phase 0 — le miroir déclaré
- zone: verte
- statut: fait
- pourquoi: la connaissance vivait éparpillée dans les objets des pages ; sans source déclarée ni contrôle, les vues du ciel divergeraient à la première retouche (dossier 15)
- fait quand: connaissances.yml déclare livres, correspondances, prophètes, générations, périodes et pages, et la CI refuse tout écart avec les pages
- résultat: 73 livres · 153 correspondances · 8 thèmes · 14 prophètes · 20 générations ·
  8 périodes · 24 pages ; extraire-connaissances.mjs mesure, verifier-connaissances.py
  compare dans les deux sens et régénère (--ecrire), huitième contrôle du banc.
  Le contrôle a attrapé son premier bug à sa première exécution (une clé de période
  tronquée à sa première lettre) — il mord.

## R-022 Ciel des connaissances, phase 1 — le panneau enrichi
- zone: orange
- statut: fait
- pourquoi: le panneau du ciel ne disait que le nom ; le porteur voulait un descriptif en bas de page de ce qui attend dans l'étoile choisie, et des liens nommés navigables
- fait quand: rôle en une phrase, liens réels nommés (toucher un nom déplace la sélection), descriptif en bas — trois phrases maximum, trilingue, sans dupliquer les strates
- résultat: 23 descriptions d'une phrase × 3 langues ; puces de passages aux points de
  famille, un toucher déplace la sélection ; le choix « ouvrir la constellation »
  viendra avec la première constellation (phase 2), on ne construit pas de bouton mort.
  Au passage, le signalement du porteur (« je ne vois pas le lien ») a mis au jour un
  vrai bug de R-020 : le lien vers la carte se rendait dans le panneau des arcs du
  diagramme, pas sous les six portes — un remplacement avait frappé la première
  occurrence du gabarit fermant. Corrigé, et deux accès posés : l'étoile « ✦ La
  carte » dans la barre du haut (visible sans défiler), et une bande de ciel sous
  les portes.

## R-023 Ciel des connaissances, phase 2 — la constellation de la Bibliothèque
- zone: orange
- statut: fait
- pourquoi: première descente — 73 étoiles-livres aux couleurs de leur période, arêtes tirées des liens vers le Christ déjà écrits, badges D-013
- fait quand: la scène lit la même donnée que le pupitre (zéro copie), captures mobiles validées, trois langues
- résultat: la carte porte deux scènes — le ciel des 23 pages, et la constellation
  de la Bibliothèque : 73 étoiles-livres en onze amas d'étagère autour de l'Agneau,
  chacune à la couleur de sa période (gris hors carte du temps), le lien D-013 déjà
  écrit au pupitre tirant un fil d'or jusqu'au centre. Toute la donnée vient du bloc
  CONSTEL, généré par `verifier-connaissances.py --ecrire` depuis la même mesure que
  `connaissances.yml` — le banc refuse toute divergence. Un livre touché ouvre sa
  fiche (étagère, description, période, badge du lien) ; touché encore, son pupitre.
  L'étoile Bibliothèque du ciel gagne « ✦ Ouvrir la constellation », une barre
  « ← Le ciel » remonte, l'adresse `#bibliotheque` est partageable. Étiquettes
  d'amas mesurées au rendu et ramenées dans le cadre, halo sombre pour rester
  lisibles à travers les étoiles ; vérifié dans les trois langues au rendu réel.

## R-024 Ciel des connaissances, phase 3 — la constellation des correspondances
- zone: orange
- statut: fait
- pourquoi: choisie par le porteur avant les 70 événements — les 153 correspondances AT↔NT en ciel thématique, les 8 thèmes en amas
- fait quand: même donnée que le diagramme du Fil Rouge (zéro copie), captures validées, trois langues
- résultat: troisième scène de la carte — les 153 correspondances en huit amas de
  thème autour de l'Agneau, chacune à la couleur de son thème du fil rouge, mêmes
  teintes que le diagramme de l'accueil. L'étoile « Le fil rouge » du ciel gagne
  « ✦ Ouvrir la constellation ». Une correspondance touchée ouvre sa fiche —
  thème, titre, références AT → NT ; touchée encore, elle s'ouvre **au bon arc**
  du diagramme : l'accueil comprend désormais l'adresse `#c=N` (1..153), qui
  sélectionne la correspondance et centre le panneau. La donnée vient du même
  bloc CONSTEL mesuré ; adresse `#correspondances` partageable ; trois langues
  vérifiées au rendu réel, geste des deux touchers jusqu'au diagramme compris.

## R-025 Ciel des connaissances, phase 4 — le fil d'Ariane du ciel
- zone: orange
- statut: à faire
- pourquoi: remonter doit être aussi simple que descendre — l'Agneau · le ciel · la constellation · l'étoile
- fait quand: depuis n'importe quel niveau, l'Agneau est à deux gestes ; transitions communes aux trois niveaux

## R-004 Choisir et importer les textes bibliques de référence
- zone: rouge
- statut: à faire
- pourquoi: sans eux, la vérification des citations est impossible — et la fusion automatique du contenu repose dessus
- fait quand: textes/ contient les trois traductions au format normalisé, avec leur licence documentée

## R-005 Vérifier toutes les citations existantes contre les textes
- zone: verte
- statut: bloqué
- pourquoi: 998 références sont citées sur le site ; aucune n'a jamais été vérifiée au mot près
- fait quand: verifier-citations passe sur les 24 pages, ou signale les écarts dans une issue
- bloqué par: R-004

## R-006 Donner les trois strates aux 15 pages qui ne les ont pas
- zone: orange
- statut: bloqué
- pourquoi: les trois profondeurs sont la promesse de lecture du site ; elles ne sont tenues que sur 9 pages
- fait quand: chaque page de contenu a ses trois strates aux longueurs prévues
- bloqué par: R-001

## R-007 Ramener les six pages hors gabarit dans l'objet C trilingue
- zone: orange
- statut: à faire
- pourquoi: index, seuil, les deux salles, la frise et le prototype n'ont pas d'objet C — leur contenu n'est donc pas traduisible ni vérifiable
- fait quand: verifier-langues ne signale plus « page hors gabarit »

## R-008 Nettoyer le dépôt
- zone: verte
- statut: fait
- pourquoi: README.md contient le HTML de Morija ; deux .md sont des doublons exacts sous des noms trompeurs ; un fichier est vide
- fait quand: README.md présente le projet, les doublons sont supprimés, arborescence-site-agneau.md est la seule arborescence
- résultat: README réécrit, deux doublons exacts et un fichier vide supprimés après
  vérification d'empreinte, prototype-fil-rouge-v3.html retiré
