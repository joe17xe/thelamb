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

# Les textes de référence sont importés (R-004) : ce contrôle vérifie qu'ils sont
# entiers et alignés — même nombre de lignes que `vref.txt`, sans quoi toute
# lecture par référence serait décalée d'un verset sans qu'on le voie. La
# comparaison des citations au mot près reste à brancher (R-005).
citations() {
  local vref=textes/vref.txt
  if [ ! -f "$vref" ]; then
    echo "::warning::textes/ est vide — les citations ne sont pas vérifiées au mot près (R-004)."
    return 0
  fi
  local n dur=0
  n=$(wc -l < "$vref")
  echo "vref.txt : $n références"
  for f in textes/*.txt; do
    [ "$f" = "$vref" ] && continue
    local m plein
    m=$(wc -l < "$f")
    plein=$(grep -c '[^[:space:]]' "$f" || true)
    if [ "$m" != "$n" ]; then
      echo "::error::$f : $m lignes contre $n — l'alignement sur vref.txt est rompu"
      dur=1
    else
      echo "  ✅ $(basename "$f") — $plein versets, alignés"
    fi
  done
  python3 outils/citer.py --existe "Genèse 22:16" >/dev/null || dur=1
  [ "$dur" = 0 ] && echo "Vérification au mot près à brancher (R-005)."
  return $dur
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
