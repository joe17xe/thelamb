# outils/

Les contrôles automatiques. Tous s'exécutent hors ligne, sans dépendance à
installer : `python3` et `node` suffisent — ils sont déjà présents sur le VPS,
puisque Claude Code en a besoin.

**Un seul point d'entrée : `bash outils/tout-verifier.sh`.** Il enchaîne les
contrôles ci-dessous et rend le même verdict que la CI — c'est littéralement le
script qu'elle exécute. Il ne s'arrête pas au premier échec : on voit tout ce
qui cloche en une fois.

| Outil | Ce qu'il vérifie | Bloque ? |
|---|---|---|
| `tout-verifier.sh` | enchaîne tout ce qui suit, en CI comme en local | oui |
| `verifier-script.mjs` | le script d'une page s'analyse — un script cassé rend une page vide | oui |
| `verifier-langues.mjs` | l'objet `C` a bien `fr`, `en`, `ar`, avec les mêmes clés et les mêmes longueurs de listes | oui |
| `essai-rendu.mjs` | les trois langues se rendent vraiment, et leurs liens aboutissent | oui |
| `verifier-liens.py` | le maillage réel correspond à `navigation.yml` : ni orpheline, ni cul-de-sac | oui |
| `poser-situation.py` | le bandeau des 14 pages ancrées reflète `periodes.yml` | oui |
| `verifier-references.py` | chaque référence citée désigne un livre et un chapitre qui existent, et aucune page publiée ne porte de jeton d'atelier | oui |
| `extraire-connaissances.mjs` | mesure la connaissance que les pages portent — livres, correspondances, prophètes, générations | — |
| `verifier-connaissances.py` | `connaissances.yml` reflète les pages, dans les deux sens (`--ecrire` régénère) | oui |
| `verifier-fiche.py` | la forme d'une fiche : strates, longueurs, métadonnées, rattachement | oui sur la structure |
| `choisir-entree.py` | renvoie la première entrée « à faire » de la feuille de route | — |
| `boucle-vps.sh` | orchestre une exécution autonome : une entrée, une branche, une PR — installation dans [`producteur/09-CLAUDE-SUR-LE-VPS.md`](../producteur/09-CLAUDE-SUR-LE-VPS.md) | — |

```bash
bash outils/tout-verifier.sh                    # tout, comme la CI
python3 outils/verifier-fiche.py contenus/*.md  # les fiches soumises
```

## Ce qu'aucun de ces outils ne vérifie

La justesse d'une citation au mot près (il faut les textes de référence,
voir `textes/README.md`), la justesse théologique, le ton, et le respect de la
règle des trois cercles. Ces quatre-là restent humains — et c'est pour ça que la
zone orange existe.
