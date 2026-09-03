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
- statut: en attente du porteur — le dossier de travail est prêt
- dossier: `producteur/10-NATURE-DES-LIENS.md` — la nomenclature rappelée avec un exemple
  réel par catégorie, les **trois décisions** qui commandent tout le reste (le niveau de
  preuve exigé d'une « citation explicite » tant que R-004 n'a pas livré les textes ; qui
  tranche entre écho thématique et lecture chrétienne quand les traditions divergent ; où
  la nature doit se voir), et **les 27 correspondances du thème « L'Agneau » déjà classées
  en proposition** — 14 citations, 6 allusions, 3 échos, 2 lectures chrétiennes, 2 débats,
  plus une référence à revoir (Genèse 22:13 → Romains 8:32 : la reprise verbale est en
  Genèse 22:16). Le porteur corrige ce qui lui paraît faux ; le silence vaut accord.
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
- statut: fait
- pourquoi: remonter doit être aussi simple que descendre — l'Agneau · le ciel · la constellation · l'étoile
- fait quand: depuis n'importe quel niveau, l'Agneau est à deux gestes ; transitions communes aux trois niveaux
- résultat: la barre « ← Le ciel » cède la place au fil d'Ariane complet, toujours
  visible : « ✦ L'Agneau › Le ciel › la constellation ». Chaque cran remonte —
  « ✦ L'Agneau » mène à l'accueil (la carte n'avait pas de chemin vers la maison :
  elle l'a), « Le ciel » remonte d'une constellation, le cran courant est à
  l'encre et inerte. Séparateur retourné en arabe (‹). Les scènes basculent en
  fondu commun (230 ms), immédiat quand le lecteur préfère un mouvement réduit.
  Un seul geste suffit désormais vers l'Agneau — mieux que les deux promis.

## R-026 Toucher l'Agneau rallume tout le ciel
- zone: verte
- statut: fait
- pourquoi: suggestion du porteur après les quatre phases — le centre de la carte était décoratif ; le toucher doit rallumer ou rendre visibles tous les points
- fait quand: le centre agit dans les trois scènes, au doigt comme au clavier, sans piéger les taps du voisinage
- résultat: le disque de l'Agneau est un bouton dans les trois scènes. Le toucher
  éteint la sélection, ferme la fiche, rend tous les points visibles — et le ciel
  entier s'éclaire un instant (immédiat sans lueur si le lecteur préfère un
  mouvement réduit). Le halo respirant ne capte pas les taps : seul le disque
  agit. Accessible au clavier (Entrée, espace), étiquette dans les trois
  langues ; l'indice du ciel gagne sa troisième phrase — « Touchez l'Agneau :
  tout se rallume. »

## R-027 La salle de la composition s'appelle « Le livre » (D-017)
- zone: verte
- statut: fait
- pourquoi: directive du porteur — « la Bible c'est un seul livre » ; le nom « La bibliothèque » contredisait la thèse d'unité que la salle enseigne
- fait quand: le nom change partout où c'est le nom, et nulle part ailleurs ; les trois langues ; aucun lien cassé
- résultat: « Le livre » (The book · الكتاب) sur la porte de l'accueil, le bandeau,
  le pied de la salle, l'étoile et la constellation du ciel ; adresse `#livre`,
  l'ancienne `#bibliotheque` toujours comprise. La composition passe dans la
  phrase (« Un seul livre, fait de 66 livres… », « 66 en commun, 7 reçus
  diversement ») sans trancher le canon. Intacts : les bibliothèques de la
  Trinité, la bibliothèque de Qumrân, la métaphore d'Emmaüs, le nom du fichier.

## R-028 Le livre en deux vues, sur douze époques (D-018)
- zone: orange
- statut: fait — trois PR : la donnée, la vue des époques (R-029), « Le livre » refaite
- résultat: « Le livre » refaite avec le moteur de secteurs des époques — onze sections
  cadrées d'un trait fin, étiquettes sur l'arc hors du champ d'étoiles (mesurées au rendu,
  réduites pour tenir, retournées en bas), halos à la couleur même de l'étoile sans blanc
  au centre, étoiles bicolores pour les quatre livres à deux époques (Samuel demi Juges,
  demi Royaume), légende à douze ; plus aucune étiquette sur une étoile. Les deux vues
  lisent la même donnée.
- pourquoi: la constellation mêle étagères et époques ; couleurs indistinctes, étiquettes sur les étoiles, sections sans cadre, Joël et le Nouveau Testament gris, un livre à deux époques invisible
- fait quand: periodes.yml à douze ; vue « Le livre » cadrée, étiquetée sur l'arc, palette validée, étoiles bicolores ; vue « Les époques » avec ses 70 événements ; trois langues ; captures réelles
- plan: dossier 15, section « Révision » — trois PR (la donnée · le livre · les époques)

## R-029 Le récit — la vue des époques, point de départ du débutant (D-019)
- zone: orange
- statut: fait
- résultat: quatrième scène de la carte — douze secteurs cadrés dans l'ordre du temps,
  l'Accomplissement en haut, chaque époque étiquetée sur son arc avec son cran du chemin
  (« 1 · L'Accomplissement » … « 12 · L'Église »). Les 77 étoiles-livres (73 livres, les
  quatre livres récit coupés paraissant dans leurs deux époques), les quatorze du récit
  cerclées d'or, et le fil d'or du chemin qui les relie de Luc aux origines, puis aux
  Actes. Toucher une époque : sa fiche — cran, dates, trois phrases, ce qui s'y passe
  (nos événements, d'après le relevé), et « où Jésus s'y trouve » : les correspondances
  du fil rouge dont le texte tombe dans l'époque, en puces vers le diagramme ; les 153
  trouvent toutes leur époque. Entrées : l'étoile « Le livre » offre les deux
  constellations, « Les veilleurs » offre les époques ; adresse `#epoques`.
- pourquoi: le but principal, convenu avec le product owner, est de raconter comment on trouve Jésus de la Genèse au dernier livre ; il faut une voie facile pour commencer — les quatorze livres du récit, par époques
- fait quand: la constellation « Les époques » existe, ses douze secteurs aux termes du dépliant, les quatorze livres du récit en étoiles principales par chapitres, chaque époque disant où Jésus s'y trouve (les correspondances du fil rouge situées dans l'époque), trois langues, captures réelles
- ordre: d'abord la donnée (periodes.yml à douze, remappage), puis cette vue, puis « Le livre » refaite — le plan de D-018 dans un autre ordre

## R-030 Le compte complet — 66 + 7 — et la note transparente sur la différence
- zone: verte
- statut: fait
- pourquoi: demande du porteur — afficher le nombre complet des livres, dire que les sept nous viennent des sources grecques, et expliquer pourquoi les traditions diffèrent, en toute transparence
- fait quand: plus aucun « 66 livres » affiché seul ; la mention grecque partout où le compte s'affiche ; la note explique la différence sans arbitrer
- résultat: « 66 + 7 » sur l'accueil (chiffres et porte), le seuil, la salle du livre
  (bandeau, entrée, chiffres, pied), la section fiable et la carte du ciel — trois
  langues. La note de la salle devient « Pourquoi 66 + 7 ? » : la Septante,
  Alexandrie, IIIᵉ siècle av. ; la liste hébraïque fixée entre le Iᵉʳ et le IIᵉ
  siècle ; Hippone 393 et Carthage 397 ; Jérôme ; Luther et l'annexe ; Trente 1546 ;
  les orthodoxes — 66 d'un côté, 73 de l'autre, davantage ailleurs, sans décréter
  pour personne (D-008 tenu).

## R-031 Les étoiles profondes s'annoncent d'elles-mêmes
- zone: verte
- statut: fait
- pourquoi: remarque du porteur — pour découvrir qu'une constellation se cache derrière une étoile, il fallait la toucher puis lire le panneau ; l'invitation doit se voir, pas s'expliquer
- fait quand: les trois étoiles qui ouvrent une constellation se signalent au ciel, sans un mot de plus, sans gêner le geste ni la sobriété du fond
- résultat: leur lueur respire, et une onde s'ouvre lentement autour d'elles — Le livre,
  Le fil rouge, Les veilleurs, décalées de 1,8 s l'une sur l'autre : une seule pulse à
  la fois, le ciel reste calme. Rien d'ajouté au texte. Sous mouvement réduit, l'anneau
  demeure posé, discret — l'invitation se voit encore. L'onde ne capte pas le toucher,
  et l'étiquette d'accessibilité dit « ouvre une constellation » dans les trois langues.

## R-032 Une seule carte du temps — la frise rattrapée, et la copie rendue impossible
- zone: verte
- statut: fait
- pourquoi: la migration aux douze époques (R-028) avait laissé la frise derrière — elle affichait encore six phases aux anciennes dates (« la division & l'exil ~930–587 » quand le site dit 930–722 puis 722–538), un maillon de la généalogie avait perdu son époque, et trois pages portaient une carte de couleurs recopiée que rien ne contrôlait
- fait quand: aucune page ne porte plus une carte du temps qui lui soit propre, et ce qui est copié est généré
- résultat: la frise montre les douze époques, **générées depuis periodes.yml** par
  `outils/poser-situation.py` — titre, dates, texte, figures, numéro, dans les trois
  langues ; ses filtres et ses prophètes suivent (Moïse à l'Égypte et Exode, Joël, Amos,
  Osée, Ésaïe et Michée au Royaume divisé), et l'axe prend ses couleurs de la même
  source au lieu de six variables figées. Les vingt maillons retrouvent leur époque —
  Abraham était rangé aux origines, Adam n'en avait plus. Les trois cartes de couleurs
  (`PCOULEURS`, `EPOCOULEURS`, `TCOULEURS`) sont désormais écrites par le générateur :
  le banc les rejoue et refuse la moindre divergence. La mesure expose enfin les
  quatorze prophètes (époque, date, place sur l'axe) et les vingt maillons aux
  constellations — c'est la donnée dont vivront « Les veilleurs » et « La généalogie ».

## R-033 Deux constellations de plus — les veilleurs, la généalogie remontante
- zone: orange
- statut: fait
- pourquoi: choisies par le porteur — la frise et la généalogie dormaient dans le site sans être des cartes ; il voulait pouvoir les parcourir comme les autres
- fait quand: les deux scènes lisent la même donnée mesurée, trois langues, captures réelles
- résultat: **Les veilleurs** — les quatorze prophètes posés sur le cadran des douze
  époques, chacun dans la sienne, et un rayon de chacun vers le centre : ils sont tous
  tournés vers le même point, c'est la thèse de la page devenue dessin. Sa fiche dit
  l'époque, la date, et ce qui le relie au Christ. **La généalogie** — les vingt maillons
  de Luc 3:23-38, du Christ à Adam, en spirale qui s'éloigne du centre : le mouvement du
  site, dessiné. Chaque maillon à la couleur de son époque, la fourche à part, et sa
  fiche dit son rang, son époque et sa précision (« par Ruth », « par Rahab »).
  Entrées : l'étoile « Les veilleurs » ouvre les deux ; adresses `#veilleurs` et
  `#genealogie`. Six vues déclarées en une liste — la barre des cartes s'y branchera.

## R-034 Les douze couleurs, aussi séparables que douze couleurs peuvent l'être
- zone: verte
- statut: fait
- pourquoi: deux paires étaient indistinguables — « Monde des origines » et « Le Royaume divisé » à ΔE 1,9, « L'Accomplissement » et « Le Retour » à ΔE 0,2 pour un daltonien ; le porteur l'avait signalé
- fait quand: la pire paire est aussi éloignée que le procédé le permet, mesurée au vérificateur, et la limite est dite
- résultat: la pire paire passe de **ΔE 1,9 à 9,8** — cinq fois mieux — l'or restant à
  l'Accomplissement et l'encre à l'Église. Les teintes suivent désormais la roue dans
  l'ordre du temps : le lecteur voit une progression, pas douze étiquettes.
  **La limite, dite franchement :** douze catégories ne se distinguent pas par la
  couleur seule — le seuil de lisibilité est à ΔE 15, aucune combinaison des douze ne
  l'atteint (le meilleur schéma à cinq familles de nuances plafonne à 7,9). La couleur
  groupe ; ce sont les étiquettes, le filtre et le tableau qui identifient.

## R-035 La barre des cartes — six vues, accessibles de partout
- zone: verte
- statut: fait
- pourquoi: demande du porteur — « toutes ces cartes doivent être accessibles de n'importe quel endroit » ; il fallait jusque-là remonter au ciel, trouver la bonne étoile et la toucher deux fois
- fait quand: depuis n'importe quelle vue, chacune des cinq autres est à un seul toucher, et la vue courante se voit
- résultat: le fil d'Ariane devient un commutateur — « ✦ L'Agneau › Le ciel · Le livre ·
  Les époques · Les correspondances · Les veilleurs · La généalogie », la vue courante
  à l'encre et inerte, les autres cliquables. Il tient sur une ligne et défile
  horizontalement sur téléphone plutôt que de s'empiler. La liste vient de la
  déclaration unique des vues : une carte de plus s'y ajoutera d'elle-même. Au passage,
  la légende se resserre sur petit écran — cinq lignes avant, quatre maintenant.

## R-036 La légende devient un filtre, cumulable, dans toutes les vues
- zone: verte
- statut: fait
- pourquoi: demande du porteur — « quand j'appuie sur la légende, elle se met en surbrillance et on voit les étoiles concernées » ; la légende ne servait qu'à lire les couleurs
- fait quand: dans les six vues, toucher une entrée de légende n'allume que les étoiles concernées, plusieurs se cumulent, et les noms s'affichent sur ce qui reste allumé
- résultat: chaque entrée devient un bouton — surbrillance, halo autour de sa pastille,
  `aria-pressed` pour les lecteurs d'écran. Les étoiles retenues restent pleines, les
  autres s'effacent presque entièrement. **Plusieurs filtres se cumulent** (deux époques,
  deux thèmes, deux familles). Sous douze étoiles retenues, chacune affiche son nom
  directement sur la carte ; au-delà, les noms restent au tableau — quarante étiquettes
  qui se chevauchent ne se lisent plus. Un « ✕ Tout rallumer » paraît dès qu'un filtre
  est actif, et **toucher l'Agneau efface tout**, comme il éteignait déjà la sélection.
  Le filtre survit au changement de langue et se vide en changeant de carte.

## R-037 Un tableau sous chaque carte, qui suit le filtre
- zone: verte
- statut: fait
- pourquoi: demande du porteur — « en affichant plus bas un tableau qui détaille ce qui a été filtré, avec une description », et pour les correspondances un tableau qui les liste toutes
- fait quand: chaque vue porte sa liste, repliée avec le compte, déployée dès qu'un filtre est actif, et chaque ligne ramène à son étoile
- résultat: sous chaque carte, un tableau tiré de la même donnée mesurée — zéro copie.
  Replié, il annonce ce qu'il contient : « 153 correspondances — voir la liste ».
  Filtré, il se déploie seul et dit « 17 sur 153 ». Une ligne porte la pastille de sa
  catégorie, son nom, et ce qui la classe : l'étagère et l'époque avec ses chapitres
  pour un livre, le thème et les deux références pour une correspondance, la date et
  l'époque pour un veilleur, le rang et la précision pour un maillon. **Toucher une
  ligne allume son étoile** sur la carte et ouvre sa fiche. Le tableau liste, il
  n'enseigne pas (D-016) : l'enseignement reste sur les pages.

## R-038 La barre des cartes est elle-même une constellation
- zone: verte
- statut: fait
- pourquoi: remarque du porteur — « on pourrait relier ces en-têtes comme une constellation, le fil entre, pour avoir une même logique » ; la barre parlait un autre langage que les cartes qu'elle ouvre
- fait quand: la barre se lit comme une constellation, sans perdre en lisibilité ni en cible de toucher
- résultat: les séparateurs deviennent un **fil d'or** et chaque carte une **étoile** sur ce
  fil ; la carte courante est l'étoile allumée, avec son halo. Le fil part de l'Agneau —
  ce n'est pas un décor : « toutes choses subsistent en lui » est ce que la page enseigne,
  et la barre le redit. Un bénéfice au passage : un segment de fil n'a pas de sens de
  lecture, là où le chevron devait se retourner en arabe. Défaut corrigé dans la foulée :
  le bouton « ✕ Tout rallumer » restait visible sans filtre — le `display` de la légende
  l'emportait sur l'attribut `hidden`.

## R-047 « Le substitut » renvoyait au mauvais verset
- zone: verte
- statut: fait
- pourquoi: demande du porteur, après le signalement fait en préparant R-013
- fait quand: la correspondance cite le verset que le Nouveau Testament reprend vraiment
- résultat: la correspondance renvoyait à **Genèse 22:13**, le bélier pris dans le buisson.
  Or ce que Romains 8:32 reprend, ce sont les mots de **Genèse 22:16** : « tu n'as pas
  refusé ton fils » répond à « il n'a point épargné son propre Fils ». La référence, la
  citation et le titre suivent — « Tu n'as pas refusé ton fils » —, dans les trois langues.
  Le commentaire n'a pas bougé : « Sur Morija, Dieu épargne le fils d'Abraham. Au Calvaire,
  il n'épargne pas le sien » — il visait déjà 22:16 sans le savoir.
  Le texte retenu vient des traductions importées le même jour (R-004) : c'est la première
  correction du site appuyée sur le texte plutôt que sur la mémoire.

## R-046 La page où le producteur valide la nature des 153 liens
- zone: verte
- statut: fait — en attente du relevé du producteur
- pourquoi: le porteur a tranché les trois décisions de R-013 et demandé une page à cocher, ouverte au producteur derrière un mot convenu
- fait quand: les 153 liens portent une proposition motivée, et le producteur peut la corriger depuis un téléphone
- résultat: **les 153 propositions sont écrites** dans `producteur/nature-des-liens.yml` —
  79 citations explicites, 44 allusions largement reconnues, 16 lectures chrétiennes,
  9 échos thématiques, 5 débats interprétatifs. Chacune porte l'indice qui la justifie
  (« afin que l'Écriture fût accomplie », « parallèle narratif », « la source exacte est
  discutée »). Sept relèvent de **D-021** : la lecture part de la tradition catholique et
  porte sa mention pour les autres Églises — Melchisédek, le pain du ciel de Jean 6, la
  coupe de bénédiction, la gloire de la seconde maison, la lecture trinitaire d'Ésaïe 48:16.
  **`validation-liens.html`** est générée depuis cette donnée par `outils/poser-validation.py`,
  idempotent comme le générateur du bandeau. Le producteur ouvre la page avec le mot convenu,
  corrige ce qui lui paraît faux, et copie un relevé qui ne contient que les écarts.
  Le maillage connaît désormais les **ateliers** : publiés, mais hors du parcours du lecteur —
  ni orphelins ni culs-de-sac, et déclarés pour qu'on ne les prenne pas pour un oubli.
- limite: la page n'est pas protégée. Le site est statique : le mot convenu écarte le
  passant, rien de plus, et seule son empreinte figure au dépôt. La page le dit elle-même.
- vérifié: mot refusé puis accepté, 153 liens et 8 thèmes affichés, une correction suivie
  jusqu'au relevé, mémoire tenue au rechargement, arabe en RTL ; les huit contrôles.

## R-045 Chaque fil dit pourquoi il existe
- zone: verte
- statut: fait
- pourquoi: le porteur, après le correctif de visibilité — « le fil, il est très bien ; moi je pense que le lien qui est fait entre l'Agneau et Maccabée n'est pas expliqué, on sait pas pourquoi il est là ; chaque lien doit donner sa raison d'être, une explication des correspondances »
- fait quand: toucher un livre dit pourquoi son fil va vers l'Agneau, et ce que la correspondance relie
- résultat: la raison **existait déjà** — chaque pupitre de la salle porte un champ « Le fil
  vers le Christ », rédigé dans les trois langues pour les 73 livres. La carte ne le
  remontait pas. Le miroir le porte désormais, avec la nuance de D-013 quand elle existe.
  Toucher 2 Maccabées affiche maintenant : « Hébreux 11:35 fait vraisemblablement écho aux
  martyrs de 2 Maccabées 6–7 : ils préfèrent la mort à l'infidélité, *afin d'obtenir une
  meilleure résurrection* », puis un dépliant « Lire la nuance » qui explique pourquoi
  c'est une allusion et non une citation.
  **Les correspondances disent ce qu'elles relient** : chaque pastille porte sa référence
  — « Le substitut · Genèse 22:13 → Romains 8:32 ». La fiche donne d'abord la raison,
  ensuite le détail.
  **Les 73 livres portent leur fil**, puisque les 73 peuvent dire pourquoi. L'épaisseur
  continue de mesurer les passages recensés par le fil rouge ; un livre dont aucun passage
  n'est encore recensé a son fil **en pointillé**, et sa fiche le dit.
- vérifié: 73 fils au rendu à 393 × 852 ; fiches de 2 Maccabées, Tobie et la Genèse
  relues ; la CI contrôle désormais que le fil vers le Christ existe dans les trois
  langues pour chaque livre ; les huit contrôles.

## R-044 Les fils se voient sur un téléphone, et celui qu'on touche s'allume
- zone: verte
- statut: fait
- pourquoi: signalement du porteur, capture à l'appui — « le fil d'or est toujours là, pas de changement, il est pas mobile, je vois pas les références les liens ou les correspondances »
- fait quand: les trente-neuf fils se voient sur un écran de téléphone, et toucher un livre montre ce qui le relie au Christ
- résultat: trois défauts, mesurés puis corrigés.
  **Les fils étaient invisibles.** Ils étaient réglés dans le repère du dessin, que
  l'écran d'un téléphone réduit de moitié (échelle mesurée : 0,52) : le plus ténu faisait
  **0,54 px de large à 14 % d'opacité** sur fond noir. Ils passent de 1,06 à 2,09 px
  réels, et de 38 à 75 % d'opacité. La gerbe de rayons vers l'Agneau se voit maintenant.
  **Le fil ne répondait pas au toucher.** Toucher un livre allume son fil — or plein,
  4,2 d'épaisseur — et éteint les trente-huit autres. Refermer la fiche leur rend leur
  poids ; le filtre les emporte comme il emporte les étoiles.
  **La fiche se taisait quand il n'y avait rien à dire.** Le porteur avait touché Tobie,
  qui ne porte aucune correspondance : la fiche n'affichait donc aucun lien, sans dire
  pourquoi. Elle le dit désormais — « aucun passage de ce livre n'est encore recensé dans
  le fil rouge, le recensement se poursuit » —, dans les trois langues.
- vérifié: rendu à 393 × 852, densité 3, l'écran du porteur ; largeurs et opacités
  mesurées à l'écran et non dans le repère du dessin ; les huit contrôles.

## R-043 Le chemin s'arrête à la Genèse ; l'Église suit le Christ, pas les origines
- zone: verte
- statut: fait
- pourquoi: signalement du porteur — « la ligne qui part de la Genèse vers Maccabée »
- fait quand: aucun trait du cadran ne dit une succession que l'histoire ne connaît pas
- résultat: le fil du récit reliait les quatorze livres d'un seul trait continu, la Genèse
  suivie des Actes. Ce dernier segment traversait tout le haut du cadran, passait sous
  l'étiquette de l'Accomplissement et frôlait celle des Maccabées — d'où la ligne que le
  porteur voyait partir de la Genèse. Elle était surtout **fausse** : les Actes ne suivent
  pas les origines, l'Église suit l'Accomplissement.
  Le trait plein descend désormais du Christ à la Genèse et s'arrête là — treize livres,
  le parcours du site (D-019). Les Actes, quatorzième livre du récit, sont rattachés à Luc
  par un trait pointillé court : ce qui suit l'Accomplissement dans le temps, et non ce qui
  prolongerait la remontée. Deux traits, deux natures, chacun juste.
- vérifié: trait plein de Luc à la Genèse en 13 points, pointillé de Luc aux Actes,
  quatorze étoiles du récit intactes ; les huit contrôles.

## R-042 Le fil vers l'Agneau se mesure, il ne se décrète pas
- zone: verte
- statut: fait
- pourquoi: question du porteur — « pourquoi ça commence par Maccabée, c'est quoi l'histoire, je vois pas le lien ; est-ce que c'est pas plutôt on fait le lien autrement par la Genèse ? »
- fait quand: le fil d'or dit une mesure du dépôt, et non le hasard d'un badge posé à la main
- résultat: le porteur avait raison. Le trait unique qui partait de 2 Maccabées venait
  d'un champ `lien` — un badge de nomenclature D-013 — que **un seul livre du dépôt
  portait**, parce que c'était le cas le plus contesté : un livre reçu diversement, un
  lien discuté (Hébreux 11:35 ↔ 2 Maccabées 6–7). Les liens évidents, eux, n'avaient
  jamais reçu de badge : ils n'avaient pas l'air d'en avoir besoin. La carte a donc promu
  au rang de seul fil visible le lien le plus faible du corpus, pendant que la Genèse,
  qui porte vingt correspondances en base, n'avait rien. Un échantillon de taille un qui
  se lit comme une thèse — et une thèse contraire à la charte.
  Le fil se **dérive maintenant des 153 correspondances** que le site porte déjà, comptées
  par livre et des deux côtés du lien : celui qui annonce et celui qui accomplit. Trente-neuf
  livres reçoivent leur fil, l'épaisseur suivant le nombre — Ésaïe 31, Matthieu 30, Jean 29,
  les Psaumes 27, la Genèse 20, l'Exode 19, Hébreux 19. Un livre qui porte un lien nommé
  sans correspondance chiffrée garde son fil, au plus ténu : 2 Maccabées n'est pas effacé,
  il reprend sa taille. La fiche d'un livre liste désormais ses passages, cliquables vers
  le diagramme, comme le faisait déjà celle d'une époque.
- vérifié: 39 fils mesurés au rendu, gradués de 0,14 à 0,32 d'opacité ; les 153
  correspondances rattachées des deux côtés, aucune orpheline ; les huit contrôles.

## R-041 Le contraste des époques voisines : ne plus délaver la couleur
- zone: verte
- statut: fait
- pourquoi: signalement du porteur — « the first kings / second colors are so close, increase contrast »
- fait quand: deux époques qui se touchent se distinguent à l'œil, mesures à l'appui
- résultat: deux causes mesurées, deux corrections.
  **La couleur était délavée avant d'atteindre l'œil.** Le halo d'une étoile était peint
  à 55 % d'opacité sur un dégradé qui retombait à 45 % dès le premier tiers : la couleur
  effective tournait autour de 25 %. Deux époques voisines à ΔE 10 en teinte pleine se
  retrouvaient à ΔE 5,9 à l'écran, et à 3,5 pour un lecteur daltonien. Le cœur plein —
  la seule surface qui portait vraiment l'époque — mesurait 4,6 de rayon. Il passe à 5,4
  (7,2 pour un livre du récit, 6,9 dans la vue du livre), le dégradé ne retombe plus
  qu'à 60 %, et l'opacité du halo monte de 55 à 70 %.
  **La palette elle-même séparait mal les voisines.** Chaque époque garde sa teinte à
  ±16° près — la terre des origines, le vert du désert, le bleu de l'exil, l'or du Christ,
  l'encre de l'Église — mais la clarté alterne désormais d'une époque à la suivante. La
  pire paire voisine passe de **ΔE 5,6 à 15,7** (mesure au pire des trois visions :
  normale, protanope, deutéranope), et la pire paire toutes distances confondues de
  4,7 à 6,7. Les paires que le porteur cite : le Royaume ↔ le Royaume divisé passe de
  16,9 à 15,7 après un détour par 25,2, et le Royaume divisé ↔ l'Exil de 7,8 à 16,2.
- limite: douze catégories ne peuvent pas toutes atteindre le seuil de 15 entre elles ;
  ce sont les **voisines** qui l'atteignent. La couleur groupe, l'étiquette et le filtre
  identifient.
- vérifié: validateur de palette du dépôt d'outils, toutes les paires ; rendu réel en
  430 × 932 sur les époques, le livre et la frise ; les huit contrôles.

## R-040 Tobie à l'exil, Judith non tranchée, et le récit compté quatorze
- zone: verte
- statut: fait
- pourquoi: trois signalements du porteur sur la donnée du livre — « Tobit is not under the divided kingdom → first exil », « Judith is not confirmed in the return », « narrative books, keep them 14 instead of 18 : they explain history of salvation »
- fait quand: la carte du temps dit vrai de Tobie, avoue son ignorance sur Judith, et le récit se compte quatorze partout
- résultat: **Tobie passe au Royaume divisé à l'Exil.** Son récit se déroule à Ninive,
  parmi les déportés de Nephtali (Tobie 1:2) : dans notre carte, l'exil s'ouvre en 722
  avec la chute de Samarie, il y est chez lui.
  **Judith reçoit ses deux époques et la raison du doute** (décision D-020) : le livre
  se donne pour cadre « Nabuchodonosor, roi des Assyriens », à Ninive (Judith 1:1), et
  situe pourtant son récit après le retour de l'exil, le Temple purifié (Judith 4:3).
  Étoile en pointillé, astérisque au nom, note dans le pupitre, la fiche et le tableau.
  **Le récit se compte quatorze.** La vue des époques dessinait dix-huit étoiles d'or
  pour quatorze livres : Genèse, 1 Samuel, 1 Rois et 2 Rois y paraissaient deux fois,
  une par époque. Un livre vaut désormais une étoile — posée sur la frontière de ses
  deux époques, le cœur partagé en deux couleurs. Le fil d'or passe par quatorze points
  au lieu de dix-huit, dans l'ordre du récit : Luc, puis on remonte jusqu'à la Genèse,
  et les Actes referment la boucle. La fiche d'un livre du récit porte son rang — « Récit
  9/14 » pour 2 Rois — sans concurrencer le numéro d'époque affiché sur le cadran.
- vérifié: quatorze `.noeud.recit` et quatorze points de chemin mesurés au rendu ;
  73 étoiles au lieu de 77 ; les quatre bicolores nommées ; les huit contrôles passent.

## R-039 Par où commencer sur un cadran — et ce que dit le fil d'or
- zone: verte
- statut: fait
- pourquoi: deux questions du porteur — « il faut qu'on regarde par où il faut commencer quand nous sommes sur un cercle », et « ce trait entre l'Agneau et 2 Maccabées, il tourne ou il est fixe, et pourquoi ? »
- fait quand: chaque cadran dit où l'on commence et dans quel sens, et le fil d'or ne se comprend plus seulement en touchant l'étoile
- résultat: les onze sections du livre sont **numérotées** comme les douze époques
  l'étaient — « 1 · La Loi (Torah) » … « 11 · L'Apocalypse » — et dans les trois cadrans
  **le départ est en or** : « 1 · La Loi » pour le livre, « 1 · L'Accomplissement » pour
  les époques et les veilleurs. Le numéro donne le point de départ, la suite donne le
  sens. Les indices le disent en une phrase, et nomment enfin **le fil d'or** : il relie
  au centre les livres dont le lien au Christ est nommé (D-013) — un seul aujourd'hui,
  2 Maccabées, dont Hébreux 11:35 reprend les sept frères. Rien ne tourne : le trait est
  fixe et mesuré. Les indices raccourcis tiennent en deux lignes sur téléphone.

## R-004 Choisir et importer les textes bibliques de référence
- zone: rouge
- statut: fait
- pourquoi: sans eux, la vérification des citations est impossible — et la fusion automatique du contenu repose dessus
- fait quand: textes/ contient les trois traductions au format normalisé, avec leur licence documentée
- résultat: les trois traductions de la charte sont importées, toutes **domaine public** :
  Segond 1910 (31 060 versets), World English Bible (30 959), Smith & Van Dyck
  (30 966). Format normalisé : un verset par ligne, aligné ligne à ligne sur
  `textes/vref.txt`, la liste canonique des 41 899 références. Le banc refuse tout
  fichier désaligné — un décalage d'une ligne ferait lire un verset pour un autre.
  **Une quatrième traduction est entrée avec elles** : la néo-Crampon libre. Les trois
  traductions de la charte sont des éditions à 66 livres et le site en présente 73 ; la
  Crampon est le seul texte libre qui porte les sept deutérocanoniques. Sans elle, Tobie,
  Judith, Sagesse, Siracide, Baruch et les deux Maccabées n'auraient aucun texte de
  référence. `textes/LICENCES.md` le documente, avec les trous connus.
  `outils/importer-textes.py` refait l'import ; `outils/citer.py "Genèse 22:16"` rend un
  verset dans les quatre textes ; `textes/livres.yml` relie les 73 noms de livres du site,
  dans les trois langues, aux codes de la versification.
- mesuré: sur les 306 références des 153 correspondances, **305 se lisent**. La seule qui
  manquait, « Malachie 4:5 », relevait d'une divergence de numérotation — la liste de
  référence suit l'hébreu et met Élie en Malachie 3:23 ; l'équivalence est posée.
- limite: l'extraction Segond s'arrête à Malachie 3:18 (la Crampon porte la fin) ; la Van
  Dyck disponible n'est pas vocalisée ; 136 de ses versets n'entrent pas dans la
  versification de référence. Tout est écrit dans `textes/LICENCES.md`.

## R-005 Vérifier toutes les citations existantes contre les textes
- zone: verte
- statut: à faire — débloqué par R-004
- pourquoi: 998 références sont citées sur le site ; aucune n'a jamais été vérifiée au mot près
- fait quand: verifier-citations passe sur les 24 pages, ou signale les écarts dans une issue
- ce qu'il faudra décider: les citations du site sont **abrégées** (« …par le sang précieux
  de Christ, comme d'un agneau sans défaut et sans tache »), et l'arabe du site est plus
  simple que la Van Dyck. La comparaison ne peut donc pas être une égalité de chaînes : il
  faudra dire ce qui est toléré — l'abrègement, la ponctuation, les diacritiques arabes —
  et ce qui ne l'est pas.

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
