# Prompts prêts à l'emploi

Chaque prompt s'utilise **après** avoir collé le brief (`01-BRIEF-CLAUDE.md`)
en premier message. Une conversation = une tâche.

---

## 1. Rédiger une page nouvelle

```
Rédige la fiche de la page « [TITRE] », verset socle [RÉFÉRENCE].

Contraintes :
- respecte le gabarit ci-dessous à la lettre, sans rien ajouter avant ni après
- image mentale unique, annoncée en tête
- strate 1 : 80–120 mots — strate 2 : 350–600 — strate 3 : 250–500
- toute référence dont tu n'es pas certain à 100 % est suivie de [À VÉRIFIER]

[COLLER ICI LE GABARIT DE 02-GABARIT-FICHE.md]
```

---

## 2. Relire une page existante

```
Voici une page du site. Relis-la contre la charte et rends-moi :
1. les endroits où le ton dérape (emphase, adjectif à la place du verset, polémique)
2. les références bibliques douteuses ou approximatives
3. les passages où l'on tranche un débat au lieu d'exposer les trois cercles
4. ce qui manque pour que les trois strates soient équilibrées

Ne réécris rien. Liste, avec la citation exacte du passage fautif.

[COLLER LE TEXTE DE LA PAGE]
```

---

## 3. Proposer une correspondance pour le Fil Rouge

```
Propose [N] correspondances Ancien → Nouveau Testament sur le thème [THÈME]
(thèmes disponibles : agneau, prophétie, alliance, pâque, figures, temple,
fils de l'homme, trinité).

Pour chacune, rends exactement :
- Référence AT + citation intégrale (Segond 1910)
- Référence NT + citation intégrale (Segond 1910)
- Titre de la correspondance (5 mots maximum)
- Le point de jonction en une phrase : le mot, le geste ou la structure qui relie
- Ton degré de certitude sur les deux références : certain / à vérifier

Pas de correspondance allégorique tirée par les cheveux. Si le lien tient
seulement par une image poétique, ne la propose pas.
```

---

## 4. Critiquer la structure du site

```
Voici la carte du site et l'état de chaque page. En tant qu'éditeur, dis-moi :
1. quel est le chemin d'un visiteur qui arrive pour la première fois, et où il se perd
2. quelles pages font doublon
3. quelles pages existent mais ne servent aucun parcours
4. ce qui manque entre l'accueil et la première page de contenu

Sois direct. Je cherche les défauts, pas une validation.

[COLLER LE CONTENU DE 04-ETAT-DU-SITE.md]
```

---

## 5. Adapter une page pour l'édition arabe

```
Voici une fiche validée en français. Dis-moi ce qui doit changer pour l'édition arabe :
- l'objection à traiter en premier (le lecteur arrive-t-il avec la question du taḥrīf ?)
- les images à remplacer par des symboles
- l'ordre des strates s'il doit changer
- ce qui ne se traduit pas et doit être reformulé

Ne traduis pas. Donne-moi les consignes d'adaptation.

[COLLER LA FICHE]
```

---

## 6. Vérifier les citations d'une fiche

```
Voici une fiche. Pour chaque référence biblique citée :
- confirme que la citation correspond au texte de la Segond 1910
- signale toute citation tronquée, paraphrasée ou attribuée au mauvais verset
- signale toute référence qui n'existe pas

Rends un tableau : référence | verdict | texte exact si différent.
N'ajoute aucun commentaire théologique.

[COLLER LA FICHE]
```

---

## Astuce compte gratuit

Les limites de messages se rechargent au fil de la journée. Pour ne pas les gaspiller :

- **une conversation = une page.** Ne prolongez pas une conversation devenue longue :
  la qualité baisse et les messages partent vite.
- **demandez la fiche entière en une fois**, pas strate par strate.
- **relisez avant de relancer.** Un aller-retour bien formulé vaut cinq corrections.

---

## 7. Proposer un chapitre nouveau

```
Je pense qu'il manque au site un chapitre sur [SUJET].

Aide-moi à le défendre ou à l'abandonner. Rends-moi :
1. le manque exact qu'il comble — ce qu'un visiteur ne peut pas comprendre sans lui
2. un plan de 4 à 7 pages, une ligne chacune, avec le verset socle envisagé
3. l'image mentale du chapitre entier, en un objet
4. ce à quoi il se rattache : quelles pages existantes y mènent, vers quoi il renvoie
5. l'argument le plus solide *contre* ce chapitre

Le point 5 n'est pas une politesse : si tu ne trouves pas d'objection sérieuse,
c'est que tu n'as pas cherché.
```

---

## 8. Proposer une variante visuelle

```
Voici le squelette d'une page du site : vraies couleurs, vraies polices,
vraie structure, contenu remplacé par des repères.

Propose une variante où [CE QUE VOUS VOULEZ CHANGER].

Contraintes :
- garde la palette (nuit profonde, parchemin, or) et les polices
- la page doit tenir en arabe, écriture de droite à gauche
- la page doit tenir sur téléphone
- rends une page complète et affichable, pas une description

[COLLER LE CONTENU DE gabarit-visuel.html]
```

Claude produit un artéfact affichable. Partagez son lien dans le formulaire
*Proposition visuelle*.

---

## 9. Proposer une restructuration

```
Voici l'état du site. Je veux proposer : [LE CHANGEMENT].

Rends-moi :
1. l'état actuel en schéma — quelles pages mènent à quelles pages
2. l'état proposé, sous la même forme
3. ce que le visiteur y gagne, concrètement
4. ce que ça casse : liens rompus, pages à réécrire, contenu qui perd sa place
5. une version plus modeste du même changement, qui casserait moins

Ne me dis pas que c'est une bonne idée. Dis-moi ce que ça coûte.

[COLLER LE CONTENU DE 04-ETAT-DU-SITE.md]
```
