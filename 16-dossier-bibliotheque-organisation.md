# LA SALLE « BIBLIOTHÈQUE » & L'ORGANISATION DU SITE — Dossier de référence

**Document évolutif · v1** — alimente `salle-bibliotheque.html` (= `bibliotheque.html` dans le projet) et cadre l'architecture globale.
Statuts : **[ÉTABLI] / [DÉBATTU] / [À INVESTIGUER]**.

---

## PARTIE I — LE CHALLENGE D'ORGANISATION (la vraie question posée)

### 1. Diagnostic
Le site atteint 23 pages. Le risque n'est pas le nombre mais la **lisibilité de la carte mentale**. Trois problèmes nommés :
- **A. Deux niveaux mélangés** : des *salles-thèmes* (Agneau, Trinité) et des *clés transversales* (Emmaüs = méthode, Déjà/pas encore = grammaire) étaient au même rang.
- **B. Pas de « vous êtes ici »** : rien n'indiquait, dans une page, à quelle salle elle appartient ni comment revenir.
- **C. Chevauchement** : « Bibliothèque » (composition) vs « Bible fiable » (confiance) risquaient d'être confondues.

### 2. Solution retenue : « Trois anneaux, une seule maison »
- **Anneau 1 — Le seuil** : une porte unique (le Christ). `seuil.html`. Inchangé.
- **Anneau 2 — Les salles** (les grands thèmes où l'on entre) : Agneau · Trinité · Offrande · **Bibliothèque (composition)** · Bible fiable (confiance) · Veilleurs. Chacune a une page-pivot et des sous-pages.
- **Anneau 3 — Les clés** (transversales, discrètes, tenues en main partout, jamais « visitées ») : Emmaüs (méthode), Déjà/pas encore (grammaire), les trois profondeurs.

### 3. Deux outils de navigation à généraliser
- **Fil d'Ariane** `Seuil › Salle › Page` en haut de chaque page (implémenté sur la Bibliothèque : `.crumb`). À rétro-appliquer aux autres pages — bloc HTML minimal, ~6 lignes.
- **Phrase-repère par salle** pour lever le chevauchement C :
  - Bibliothèque → « **De quoi est faite la Bible ?** » (affiché en tête, `.whichroom`).
  - Bible fiable → « **Peut-on lui faire confiance ?** » (à ajouter en tête de `bible.html`).

### 4. Règle de croissance (anti-dispersion, priorité de Joe)
Une nouvelle **salle** ne s'ouvre que pour un vrai grand thème (pas un sous-thème). Les approfondissements deviennent des **sous-pages d'une salle existante**, reliées par les portes 360°. Le vestibule liste les salles ouvertes + une carte grise « à venir ».

---

## PARTIE II — LA SALLE BIBLIOTHÈQUE (le contenu)

### 5. Concept : un objet, deux usages (méthode éprouvée)
Vue d'ensemble des **66 livres** rangés en **10 étagères** (5 AT + 5 NT) dépliables, chaque livre = un « dos » cliquable qui s'ouvre sur le **lutrin** : *de quoi ça parle* (une phrase) + *le fil vers le Christ* (le verset-clé). Le débutant balaie les étagères ; le curieux ouvre livre par livre. Aucun sous-thème créé.

### 6. Structure canonique [ÉTABLI]
| Testament | Étagères | Livres |
|---|---|---|
| Ancien (39) | Loi (5) · Historiques (12) · Sagesse (5) · Grands prophètes (5) · Petits prophètes (12) | 39 |
| Nouveau (27) | Évangiles (4) · Actes (1) · Lettres de Paul (13) · Lettres générales (8) · Apocalypse (1) | 27 |
Total **66** — vérifié dans les 3 langues (script de comptage). Chaque étagère a une **introduction** (sa logique + son fil christologique) répondant à la demande « faire des introductions ».

### 7. Rayon spécial « Les fêtes juives dans l'Évangile » (demande explicite)
7 fêtes, chacune avec *ce qu'elle est* + *ce que Jésus en fait* : Pâque (il meurt à l'heure des agneaux), Pains sans levain, Prémices (il ressuscite ce jour-là), Pentecôte (l'Esprit répandu), Trompettes, Yom Kippour (Hé 9, une fois pour toutes), Souccot (« si quelqu'un a soif »). Structuré par saisons (printemps/automne). C'est une **clé de lecture de l'Évangile**, pas une salle séparée → rangée dans la Bibliothèque.

### 8. Note honnête sur le canon [DÉBATTU — traité ouvertement]
Bloc dédié : les 66 livres = socle commun ; mention claire et non polémique des **deutérocanoniques** (catholiques/orthodoxes). Le site part du commun « sans trancher ce débat ancien : il le signale plutôt que de le masquer ». Cohérent avec le public catholique + évangélique et avec la règle de rigueur.

### 9. Datations [ÉTABLI / DÉBATTU]
Chaque livre porte une date approximative. Règle affichée en pied : « estimations d'historien ». Cas sensibles à formuler en strate 3 plus tard : Daniel (VIe/IIe), Joël (déjà signalé « débattu »), unité d'Ésaïe, Pentateuque (attribution mosaïque vs sources). Ne pas masquer.

### 10. Distinction avec « Bible fiable » (résout le chevauchement)
| Salle | Question | Contenu |
|---|---|---|
| **Bibliothèque** | de quoi est-elle faite ? | 66 livres, groupes, sujets, fêtes |
| **Bible fiable** | peut-on s'y fier ? | manuscrits, prophéties, cohérence, objections |
Les deux se renvoient l'une à l'autre (portes posées : bas de la Bibliothèque → Bible fiable + Fil Rouge).

---

## PARTIE III — INTÉGRATION & BACKLOG

### 11. Intégration [FAIT]
- `salle-bibliotheque.html` → `bibliotheque.html` (23 pages au total).
- Vestibule : carte « La bibliothèque » ajoutée (FR/EN/AR) avant « Bible fiable ».
- Fil d'Ariane implémenté sur la page (modèle réutilisable).
- Archive régénérée (349K, 23 pages, seed 157).

### 12. Backlog
| # | Tâche | Priorité |
|---|---|---|
| 1 | Rétro-appliquer le fil d'Ariane aux 22 autres pages | Haute |
| 2 | Ajouter la phrase-repère « Peut-on lui faire confiance ? » en tête de `bible.html` | Haute |
| 3 | Ajouter la carte « La bibliothèque » à l'accueil (`home-content.js`) | Haute |
| 4 | Relecture AR native (noms des 66 livres en Van Dyck, fêtes) | **Absolue avant mise en ligne AR** |
| 5 | Strate 3 datations (Daniel, Pentateuque, Ésaïe) — pages/notes dédiées | Moyenne |
| 6 | Lier chaque fête à l'arc correspondant du Fil Rouge | Moyenne |
| 7 | Cartes Instagram (voir §13) | Moyenne |
| 8 | Sous-pages possibles de la salle : « Comment lire un psaume », « Les 4 évangiles, pourquoi quatre ? » (sur feu vert) | En attente |

### 13. Instagram (salle Bibliothèque)
- Hook : *« 66 livres, 40 auteurs, 1500 ans, 3 continents — et un seul fil. Comment ? »*
- Hook (fêtes) : *« Jésus est mort exactement à l'heure où l'on immolait les agneaux. Hasard ? »*
- Carrousel : « L'Ancien Testament en 5 étagères » / « Le Nouveau en 5 étagères ».
- Hook (Souccot) : *« À la fête de l'eau, il crie : "si quelqu'un a soif…" Pourquoi ce jour-là ? »*

---

## PARTIE IV — CARTE COMPLÈTE DU SITE (état à ce jour, 23 pages)

**Anneau 1 — Seuil** : `seuil.html`
**Anneau 2 — Salles** :
- Agneau : `emmaus` · `etape-1..7` · `bapteme` · `transfiguration` · `le-sang` · `resurrection` · `temple-detruit` · `parole-eternelle` · `offrande`
- Trinité : `trinite` (grande salle bibliothèques) · `trinite-parcours` (guidé)
- Bibliothèque : `bibliotheque`
- Bible fiable : `bible`
- Veilleurs : `prophetes`
- Transversal explorable : `fil-rouge` (157)
**Anneau 3 — Clés** : `emmaus` (méthode) · `deja-pas-encore` (grammaire) · système 3 profondeurs
**Accueil actuel** : `app/page.js` (portes + parcours + sections).

**Décisions en attente (Joe)** :
1. Vestibule = accueil (option A) ou plan de la maison (option B, recommandé).
2. Généraliser le fil d'Ariane (validation du modèle).
3. Prochaine salle à ouvrir (candidates cadrées, non lancées) : la Prière · l'Église · la fin des temps · l'Esprit qui agit.
