# Contribuer par pull request — depuis le navigateur

Une *pull request* (PR) est une proposition de modification : elle n'entre dans le site
que si quelqu'un l'accepte. C'est le mode de travail visé — plus riche qu'un ticket,
parce qu'on discute sur le texte lui-même, ligne par ligne.

**Tout se fait dans le navigateur. Pas de Git, pas d'installation, pas de terminal.**

---

## Ce qu'il faut savoir d'abord

**Votre Claude n'a pas besoin d'être connecté à GitHub.** C'est le point qui trompe :
la connexion GitHub de Claude — le connecteur — demande un abonnement payant, mais elle
ne sert qu'à *confort*. Le circuit ci-dessous n'en dépend pas.

Répartition des rôles :

| Qui | Fait quoi |
|---|---|
| **Votre Claude** (gratuit) | rédige, relit, vérifie, maquette — dans le chat |
| **Vous** | copiez le résultat dans l'éditeur GitHub |
| **GitHub** | crée la branche et la PR tout seul |
| **La vérification automatique** | commente la forme de la fiche en une minute |
| **Le porteur du projet** | relit le fond, demande des corrections, fusionne |

---

## Le circuit, étape par étape

### 1. Rédiger dans Claude

Collez le [brief](01-BRIEF-CLAUDE.md), puis demandez la fiche
(prompts dans [`03-PROMPTS.md`](03-PROMPTS.md)). Demandez-la **au format de
[`contenus/MODELE.md`](../contenus/MODELE.md)** — bloc de métadonnées compris.

### 2. Créer le fichier sur GitHub

1. Ouvrez le dépôt, entrez dans le dossier `contenus/`.
2. Bouton **Add file** → **Create new file**.
3. Nommez-le `contenus/<section>-<sujet>.md` — par exemple `contenus/alliance-noe.md`.
4. Collez la fiche.

### 3. Proposer

En bas de page, choisissez **« Create a new branch for this commit and start a pull
request »**. Donnez un titre court. **Propose changes**, puis **Create pull request**.

GitHub crée la branche pour vous. Vous n'avez rien à savoir de plus sur Git.

### 4. Lire le rapport automatique

Une minute plus tard, un commentaire apparaît sur la PR : strates présentes, longueurs,
métadonnées, références marquées `[À VÉRIFIER]`, rattachement déclaré.

Il ne juge que la forme — jamais la justesse d'une citation ni le ton. Corrigez ce qu'il
signale en modifiant le fichier **dans la PR** (crayon ✏️ sur le fichier) : le rapport se
met à jour tout seul.

### 5. Discuter

Le relecteur commente des passages précis. Répondez sous le commentaire, corrigez,
ou expliquez pourquoi vous maintenez. Quand c'est réglé, la PR est fusionnée et la fiche
est transposée en page du site.

---

## Modifier une page existante

Ouvrez le fichier, cliquez le crayon ✏️, modifiez, choisissez à nouveau
« Create a new branch… ». Même circuit.

> **Attention aux `.html`.** Le texte des pages n'est pas dans le HTML : il vit dans un
> objet JavaScript `C` avec une clé par langue (`fr`, `en`, `ar`), en bas du fichier.
> Modifier le HTML visible ne change rien à l'affichage et casse la cohérence.
> Cherchez `const C={` et modifiez la bonne langue.

---

## L'éditeur complet, si le cœur vous en dit

Depuis n'importe quelle page du dépôt, appuyez sur la touche **`.`** (point).
GitHub ouvre un éditeur complet dans le navigateur : arborescence, recherche, plusieurs
fichiers ouverts. Gratuit, rien à installer. Le bouton « Source Control » à gauche
propose les modifications en PR de la même façon.

Utile pour une PR qui touche plusieurs fichiers. Inutile pour une fiche unique.

---

## Ce qui accélère une PR

- **Une PR = une fiche.** Trois fiches dans une PR, c'est trois discussions mêlées.
- **Remplissez le rattachement.** `mene-vers` et `vient-de` dans les métadonnées :
  quatorze pages du site sont déjà inaccessibles, on n'en ajoute pas une quinzième.
- **Marquez vos doutes.** `[À VÉRIFIER]` sur une référence incertaine fait gagner un
  aller-retour. Le masquer en fait perdre trois.
- **Ne rouvrez pas une PR fusionnée.** Une nouvelle idée = une nouvelle PR.

## Ce qui ne passe pas par une PR

Une idée pas encore rédigée, une remarque de structure, une proposition visuelle :
ce sont des **tickets**, pas des PR (voir [`05-CIRCUIT-DES-PROPOSITIONS.md`](05-CIRCUIT-DES-PROPOSITIONS.md)).
On valide l'intention avant d'écrire — une PR de 3 000 mots refusée sur le principe,
c'est une soirée perdue.
