# outils/

Les contrôles automatiques. Tous s'exécutent hors ligne, sans dépendance à
installer : `python3` et `node` suffisent — ils sont déjà présents sur le VPS,
puisque Claude Code en a besoin.

| Outil | Ce qu'il vérifie | Bloque ? |
|---|---|---|
| `verifier-langues.mjs` | l'objet `C` a bien `fr`, `en`, `ar`, avec les mêmes clés et les mêmes longueurs de listes | oui |
| `verifier-references.py` | chaque référence citée désigne un livre et un chapitre qui existent | oui |
| `verifier-fiche.py` | la forme d'une fiche : strates, longueurs, métadonnées, rattachement | oui sur la structure |
| `choisir-entree.py` | renvoie la première entrée « à faire » de la feuille de route | — |
| `boucle-vps.sh` | orchestre une exécution autonome : une entrée, une branche, une PR | — |

```bash
node   outils/verifier-langues.mjs ./*.html
python3 outils/verifier-references.py ./*.html contenus/*.md
python3 outils/verifier-fiche.py contenus/*.md
```

## Ce qu'aucun de ces outils ne vérifie

La justesse d'une citation au mot près (il faut les textes de référence,
voir `textes/README.md`), la justesse théologique, le ton, et le respect de la
règle des trois cercles. Ces quatre-là restent humains — et c'est pour ça que la
zone orange existe.
