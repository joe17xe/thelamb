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
- statut: à faire
- pourquoi: rien ne s'automatise correctement tant que la structure cible est inconnue
- fait quand: les six entrées de producteur/06-JOURNAL-DES-DECISIONS.md sont tranchées et écrites

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
