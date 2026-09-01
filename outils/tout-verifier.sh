#!/usr/bin/env bash
# Les contrôles du dépôt, en un seul endroit.
#
#     bash outils/tout-verifier.sh
#
# Le même script tourne en CI et sur le poste d'un contributeur : ce qui passe
# ici passe là-bas. On ne s'arrête pas au premier échec — mieux vaut voir tout
# ce qui cloche en une fois que de le découvrir contrôle après contrôle.
set -uo pipefail
cd "$(dirname "$0")/.."

echecs=()

controle() {
  local titre="$1"; shift
  printf '\n── %s\n' "$titre"
  if "$@"; then return 0; fi
  echecs+=("$titre")
  echo "::error::$titre"
}

# Le générateur du bandeau est idempotent : s'il produit une différence, c'est
# qu'une page a été modifiée à la main et diverge de periodes.yml. On laisse la
# correction appliquée — l'auteur n'a plus qu'à la relire et la committer.
#
# On compare les pages à elles-mêmes avant/après, jamais à `git diff` : sur un
# poste où l'auteur a du travail en cours, `git diff` est non vide de toute
# façon, et le contrôle échouerait pour rien.
situation() {
  local avant apres
  avant=$(md5sum ./*.html | sort)
  python3 outils/poser-situation.py >/dev/null || return 1
  apres=$(md5sum ./*.html | sort)
  [ "$avant" = "$apres" ] && return 0
  echo "Ces pages divergeaient de periodes.yml. Le générateur vient de les"
  echo "remettre d'aplomb : relisez la modification et committez-la."
  diff <(printf '%s\n' "$avant") <(printf '%s\n' "$apres") \
    | awk '/^>/ {print "  · "$3}'
  return 1
}

# Échoue ouvert tant que textes/ est vide : sans traductions de référence, la
# vérification au mot près est impossible. Le jour où R-004 les importe, ce
# contrôle devient bloquant (R-005).
citations() {
  if ls textes/*.json >/dev/null 2>&1; then
    echo "Textes présents — vérification au mot près à brancher (R-005)."
  else
    echo "::warning::textes/ est vide — les citations ne sont pas vérifiées au mot près (R-004)."
  fi
}

controle "Syntaxe des scripts de page" \
  node outils/verifier-script.mjs ./*.html
controle "Intégrité trilingue de l'objet de contenu" \
  node outils/verifier-langues.mjs ./*.html
controle "Rendu effectif des trois langues" \
  node outils/essai-rendu.mjs ./*.html
controle "Maillage — ni orpheline, ni cul-de-sac" \
  python3 outils/verifier-liens.py
controle "Le bandeau de situation reflète periodes.yml" situation
controle "Références bibliques et jetons d'atelier" \
  python3 outils/verifier-references.py ./*.html contenus/*.md
controle "La base de connaissances reflète les pages" \
  python3 outils/verifier-connaissances.py
controle "Texte des citations" citations

echo
if [ ${#echecs[@]} -eq 0 ]; then
  echo "Tous les contrôles passent."
  exit 0
fi
echo "${#echecs[@]} contrôle(s) en échec :"
printf '  · %s\n' "${echecs[@]}"
exit 1
