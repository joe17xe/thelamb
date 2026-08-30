# textes/

Les traductions bibliques de référence, en local, pour vérifier les citations
**au mot près**. Ce dossier est vide tant que l'entrée R-004 de la feuille de
route n'est pas traitée.

## Pourquoi c'est nécessaire

La charte dit : *n'invente jamais un verset ni une référence*. Un modèle qui
rédige finira par produire une citation subtilement fausse — un verset attribué
au mauvais chapitre, une paraphrase donnée pour du Segond. Sur un site dont
l'argument central est « les manuscrits sont fiables, voici les textes exacts »,
ce n'est pas une coquille : c'est l'erreur qui discrédite tout le reste.

`outils/verifier-references.py` contrôle déjà ce qui se contrôle sans les textes :
le livre existe, le chapitre existe. Il ne peut pas dire si la citation
correspond au texte réel. C'est ce dossier qui le permettra.

**Tant que ce dossier est vide, la fusion automatique d'une PR qui modifie du
contenu doit être refusée.** Le contrôle échoue fermé : pas de texte, pas de
vérification, pas de fusion.

## Format normalisé

Un fichier par traduction, `textes/<code>.json` :

```json
{
  "traduction": "ls1910",
  "langue": "fr",
  "nom": "Louis Segond 1910",
  "licence": "domaine public",
  "source": "https://…",
  "livres": {
    "Genèse": { "22": { "8": "Abraham répondit: Mon fils, Dieu se pourvoira…" } }
  }
}
```

Les noms de livres sont ceux de `outils/verifier-references.py` — en français,
accentués, pour les trois traductions. C'est le convertisseur qui fait
correspondre, pas le vérificateur.

## Les trois traductions à importer

| Code | Traduction | Langue | Statut du texte |
|---|---|---|---|
| `ls1910` | Louis Segond 1910 | fr | domaine public (Segond mort en 1885) |
| `web` | World English Bible | en | domaine public, versé volontairement |
| `arabicsv` | Smith & Van Dyck | ar | domaine public (1865) |

## Sources repérées

Attention : le **texte** peut être dans le domaine public alors que la
**compilation** qui le distribue porte sa propre licence. Vérifier les deux.

- **`getbible/v2`** — son catalogue nomme exactement `ls1910`, `arabicsv` et `web`,
  c'est-à-dire nos trois traductions. Les données passent par
  `https://api.getbible.net/v2/<code>.json`. *Inaccessible depuis l'environnement
  où ce dossier a été préparé (proxy), mais joignable depuis le VPS* — c'est donc
  au robot de faire l'import.
- **`seven1m/open-bibles`** — dépôt qui ne retient que des bibles au statut clair.
  `eng-web.usfx.xml` y est marqué domaine public. Format USFX (XML), à convertir.
  Pas de Segond ni d'arabe.
- **`thiagobodruk/bible`** — a bien `ar_svd.json` (Van Dyck), mais la compilation
  entière est publiée sous **CC BY-NC**. À écarter si le site doit rester
  librement réutilisable.

## Ce qu'il reste à décider

Le choix de la source n'est pas technique : il engage la licence du site.
C'est une décision, pas une tâche — d'où la zone rouge de l'entrée R-004.
