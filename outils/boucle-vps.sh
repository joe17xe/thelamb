#!/usr/bin/env bash
# Boucle autonome — lit la feuille de route, traite UNE entrée, ouvre une PR.
#
# Installé sur le VPS, déclenché par une minuterie systemd.
# Ne pousse JAMAIS sur main : le déploiement fait `rsync --delete` vers le site
# public, donc toute erreur arrivée sur main est en ligne dans la minute.
#
#   ./outils/boucle-vps.sh            traite une entrée
#   ./outils/boucle-vps.sh --a-vide   montre ce qu'il ferait, sans rien faire

set -euo pipefail

DEPOT="${DEPOT:-/srv/agneau}"
BRANCHE_BASE="${BRANCHE_BASE:-main}"
JOURNAL="${JOURNAL:-/var/log/agneau-boucle.log}"
VERROU="/tmp/agneau-boucle.lock"
A_VIDE=0
[ "${1:-}" = "--a-vide" ] && A_VIDE=1

dire(){ printf '%s  %s\n' "$(date -Is)" "$*" | tee -a "$JOURNAL" >&2; }
abandon(){ dire "ARRÊT — $*"; exit "${2:-0}"; }

# — un seul passage à la fois : une exécution qui traîne ne doit pas être doublée —
exec 9>"$VERROU"
flock -n 9 || abandon "une exécution est déjà en cours"

cd "$DEPOT"

# — les deux outils dont tout dépend, vérifiés avant de commencer —
for outil in claude gh git python3 node; do
  command -v "$outil" >/dev/null || abandon "$outil est introuvable dans le PATH du service" 1
done
gh auth status >/dev/null 2>&1 \
  || abandon "gh n'est pas authentifié (gh auth login, ou GH_TOKEN dans /etc/agneau/boucle.env)" 1

# — coupe-circuit : créer un fichier PAUSE à la racine depuis GitHub suffit à tout arrêter —
git fetch --quiet --no-tags origin "$BRANCHE_BASE"
git checkout --quiet "$BRANCHE_BASE"
git reset --hard --quiet "origin/$BRANCHE_BASE"
[ -f PAUSE ] && abandon "fichier PAUSE présent — boucle désactivée volontairement"

[ -f FEUILLE-DE-ROUTE.md ] || abandon "pas de feuille de route" 1

# — choisir l'entrée : la première « à faire », en respectant l'ordre du fichier —
entree=$(python3 outils/choisir-entree.py FEUILLE-DE-ROUTE.md ${ZONES:-} || true)

[ -n "$entree" ] || abandon "aucune entrée « à faire »"

id=$(cut -f1 <<<"$entree")
zone=$(cut -f2 <<<"$entree")
titre=$(cut -f3 <<<"$entree")
dire "entrée retenue : $id [$zone] $titre"

# — ne pas refaire ce qui est déjà en cours ou fait : l'état vit dans les PR —
if gh pr list --search "$id" --state all --json number --jq 'length' 2>/dev/null | grep -qv '^0$'; then
  abandon "$id a déjà une PR — rien à faire"
fi

branche="robot/${id,,}"
[ "$A_VIDE" = 1 ] && abandon "à vide — j'aurais créé $branche pour $id"

git checkout --quiet -b "$branche"

# — Claude fait le travail ; CLAUDE.md lui donne le contexte du projet tout seul —
consigne=$(cat <<EOP
Tu travailles dans le dépôt du site « L'Agneau de Dieu ». Lis CLAUDE.md d'abord.

Traite UNIQUEMENT l'entrée $id de FEUILLE-DE-ROUTE.md, dont le titre est :
$titre

Règles absolues :
- ne touche à aucune autre entrée, à aucun autre sujet
- ne modifie jamais le HTML rendu à la main : le contenu vit dans l'objet C
  trilingue, et toute modification doit être portée dans fr, en ET ar
- n'invente jamais un verset ni une référence
- n'écris jamais [À VÉRIFIER] dans une page publiée : c'est un jeton d'atelier,
  la CI le refuse (D-013). Dans une page, ce qui se dit au lecteur c'est la
  nature du lien — citation explicite, allusion largement reconnue, écho
  thématique, lecture chrétienne, débat interprétatif — avec une nuance
  dépliable dès la deuxième catégorie. Si tu n'es pas sûr de la référence
  elle-même, ne l'écris pas : ouvre un BLOCAGE.md
- ne tranche aucune des questions de producteur/06-JOURNAL-DES-DECISIONS.md
- ne modifie ni .github/workflows/ ni outils/ ni FEUILLE-DE-ROUTE.md

Quand tu as fini, lance les contrôles :
  bash outils/tout-verifier.sh
et corrige tout ce qu'ils signalent.

Si la tâche dépasse ce que tu peux faire sûrement, ne produis AUCUNE modification :
écris seulement un fichier BLOCAGE.md expliquant ce qui manque pour décider.
EOP
)

if ! claude -p "$consigne" >>"$JOURNAL" 2>&1; then
  dire "claude a échoué — branche abandonnée"
  git checkout --quiet "$BRANCHE_BASE"; git branch -D "$branche" >/dev/null; exit 1
fi

# — un blocage n'est pas un échec : c'est une question posée à un humain —
if [ -f BLOCAGE.md ]; then
  corps=$(cat BLOCAGE.md)
  git checkout --quiet -- . 2>/dev/null || true
  git clean -fdq
  git checkout --quiet "$BRANCHE_BASE"; git branch -D "$branche" >/dev/null
  gh issue create --title "[$id] intervention nécessaire" \
     --body "$corps"$'\n\n---\n_Ouvert par la boucle autonome du VPS._' \
     --label intervention >>"$JOURNAL"
  abandon "$id demande une décision humaine — issue ouverte"
fi

git diff --quiet && abandon "aucune modification produite pour $id"

# — les contrôles tournent ici aussi : une branche poussée rouge fait perdre un cycle —
bash outils/tout-verifier.sh >>"$JOURNAL" 2>&1 \
  || abandon "les contrôles du dépôt échouent — rien n'est poussé (voir $JOURNAL)" 1

git add -A
git commit --quiet -m "$id — $titre" -m "Traité par la boucle autonome. Zone : $zone."
git push --quiet -u origin "$branche"

gh pr create --base "$BRANCHE_BASE" --head "$branche" \
   --title "[$id] $titre" \
   --body "$(printf 'Entrée **%s** de la feuille de route, zone **%s**.\n\nContrôles du dépôt passés localement avant poussée (outils/tout-verifier.sh).\n\n---\n_Ouvert par la boucle autonome du VPS._' "$id" "$zone")" \
   >>"$JOURNAL"

dire "$id — PR ouverte depuis $branche"
git checkout --quiet "$BRANCHE_BASE"
