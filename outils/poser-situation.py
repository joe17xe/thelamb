#!/usr/bin/env python3
"""Pose sur chaque page ancrée le bandeau « où nous sommes dans l'histoire ».

    python3 outils/poser-situation.py            applique
    python3 outils/poser-situation.py --retirer  enlève tout

La source est `periodes.yml`. Le générateur est idempotent : relancé, il met à
jour au lieu de dupliquer. Il n'entre pas dans le corps de `render` — il
l'enveloppe juste avant que les boutons de langue s'y accrochent, pour ne rien
risquer d'une fonction qu'il ne comprend pas.

Le bandeau est un repère, pas un chemin : le parcours du site descend du Christ
vers la Genèse, la frise dit seulement quand (décision D-007).
"""
import json
import re
import sys

import yaml

DEBUT = "/* ——— bandeau de situation (généré : outils/poser-situation.py) ——— */"
FIN = "/* ——— fin du bandeau de situation ——— */"
MARQUE_JS_DEBUT = "/* situation — généré */"
MARQUE_JS_FIN = "/* fin situation */"

CSS = DEBUT + """
  .situation{max-width:1060px;margin:24px auto 0;padding:0 20px}
  .situation a{display:block;text-decoration:none;color:inherit}
  .situation a:focus-visible{outline:2px solid var(--gold);outline-offset:4px;border-radius:6px}
  .sitlbl{font-family:system-ui,sans-serif;font-size:10px;letter-spacing:.28em;text-transform:uppercase;color:var(--muted);text-align:center;margin-bottom:9px}
  html[dir="rtl"] .sitlbl{letter-spacing:.05em;font-family:'Amiri',sans-serif;font-size:12.5px}
  .sitbar{display:flex;gap:3px}
  .sitseg{flex:1;height:5px;border-radius:2px;background:var(--sc);opacity:.2;transition:opacity .25s}
  .sitseg.on{opacity:1;box-shadow:0 0 10px var(--sc)}
  .situation a:hover .sitseg{opacity:.42}
  .situation a:hover .sitseg.on{opacity:1}
  .sitnow{margin-top:10px;text-align:center;font-family:system-ui,sans-serif;font-size:11.5px;color:var(--muted)}
  html[dir="rtl"] .sitnow{font-family:'Amiri',sans-serif;font-size:14px}
  .sitnow b{font-weight:600}
""" + FIN + "\n"

GABARIT_JS = MARQUE_JS_DEBUT + """
const PERIODES=%s;
const PERIODE_ICI=%s;
const PERIODE_LBL=%s;
function posSituation(l){
  const zone=document.getElementById('situation');
  if(!zone) return;
  const liste=PERIODES[l]||PERIODES.fr;
  const i=liste.findIndex(p=>p[0]===PERIODE_ICI);
  const ici=liste[i];
  zone.innerHTML='<a href="frise-prophetes.html">'
    +'<div class="sitlbl">'+PERIODE_LBL[l]+'</div>'
    +'<div class="sitbar">'+liste.map((p,k)=>
        '<span class="sitseg'+(k===i?' on':'')+'" style="--sc:'+p[3]+'"></span>').join('')
    +'</div>'
    +'<div class="sitnow"><b style="color:'+ici[3]+'">'+ici[1]+'</b> · '+ici[2]+'</div>'
    +'</a>';
}
const _renduSansSituation=render;
render=function(l){_renduSansSituation(l);posSituation(l);};
""" + MARQUE_JS_FIN + "\n"

ANCRE_HTML = '<div class="situation" id="situation"></div>\n\n'
CROCHET = "document.querySelectorAll('.langs button').forEach(b=>b.addEventListener('click'"

LBL = {"fr": "Où nous sommes dans l'histoire",
       "en": "Where we are in the story",
       "ar": "أين نحن من التاريخ"}


def ecrire(chemin, contenu, origine):
    """Écrit, sauf si le résultat a fondu — un générateur ne doit jamais vider une page.

    `open(chemin, "w")` tronque le fichier avant même que l'argument de write()
    soit évalué : lire et écrire dans la même expression détruit la page. On lit
    d'abord, on contrôle, on écrit ensuite.
    """
    if len(contenu) < len(origine) * 0.5:
        raise SystemExit("%s : le résultat fait %d octets contre %d — écriture refusée"
                         % (chemin, len(contenu), len(origine)))
    open(chemin, "w", encoding="utf-8").write(contenu)


def nettoyer(t):
    """Retire une pose précédente, pour que le générateur soit rejouable."""
    t = re.sub(re.escape(DEBUT) + r".*?" + re.escape(FIN) + r"\n?", "", t, flags=re.S)
    t = re.sub(re.escape(MARQUE_JS_DEBUT) + r".*?" + re.escape(MARQUE_JS_FIN) + r"\n?", "", t, flags=re.S)
    t = t.replace(ANCRE_HTML, "")
    return t


def poser(chemin, cle, periodes):
    origine = open(chemin, encoding="utf-8").read()
    t = nettoyer(origine)

    tables = {l: [[p["cle"], p[l]["nom"], p[l]["dates"], p["couleur"]] for p in periodes]
              for l in ("fr", "en", "ar")}
    js = GABARIT_JS % (json.dumps(tables, ensure_ascii=False),
                       json.dumps(cle), json.dumps(LBL, ensure_ascii=False))

    if "</style>" not in t or '<div class="hero">' not in t or CROCHET not in t:
        raise SystemExit("%s : structure inattendue, rien n'est modifié" % chemin)

    t = t.replace("</style>", CSS + "</style>", 1)
    t = t.replace('<div class="hero">', ANCRE_HTML + '<div class="hero">', 1)
    t = t.replace(CROCHET, js + CROCHET, 1)
    ecrire(chemin, t, origine)


def main(argv):
    doc = yaml.safe_load(open("periodes.yml", encoding="utf-8"))
    periodes, ancrages = doc["periodes"], doc["ancrages"]
    retirer = "--retirer" in argv

    for chemin, cle in ancrages.items():
        if retirer:
            origine = open(chemin, encoding="utf-8").read()
            ecrire(chemin, nettoyer(origine), origine)
            print("  retiré   %s" % chemin)
            continue
        nom = next(p["fr"]["nom"] for p in periodes if p["cle"] == cle)
        poser(chemin, cle, periodes)
        print("  %-32s %s" % (chemin, nom))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
