#!/usr/bin/env node
// Exécute le script de chaque page dans un DOM minimal et rend les trois langues.
//
//   node outils/essai-rendu.mjs *.html
//
// Un contrôle de syntaxe ne dit pas si la page s'affiche. Celui-ci vérifie que
// le rendu produit du contenu dans les trois langues et relève les liens
// réellement posés — c'est ce qui prouve qu'un lien ajouté arrive à l'écran.

import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { domFactice, bacASable } from './lire-C.mjs';

/** Somme le contenu rendu dans tous les points d'ancrage de la page. */
function rendu(document) {
  let html = '';
  for (const n of document._ancres.values()) html += n.innerHTML || '';
  return html;
}

/** Adresses posées par `createElement`, que le HTML rendu ne contient pas. */
function liensCrees(document) {
  return document._crees.map((n) => n.href).filter((h) => typeof h === 'string');
}

// --json : émet le graphe des liens réellement rendus, pour verifier-liens.py
const enJSON = process.argv.includes('--json');
const dire = (...a) => (enJSON ? console.error(...a) : console.log(...a));
const graphe = {};
let global = false;
for (const f of process.argv.slice(2)) {
  if (f === '--json') continue;
  const src = readFileSync(f, 'utf8');
  const bloc = src.match(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/);
  if (!bloc) {
    // page sans script : ses liens sont des attributs HTML ordinaires
    graphe[f] = [...new Set([...src.matchAll(/href="([^"#?]+\.html)"/g)].map((m) => m[1]))].sort();
    if (!enJSON) dire('  —  %s : pas de script en ligne', f);
    continue;
  }

  const document = domFactice();
  const bac = bacASable(document);

  try {
    vm.runInNewContext(bloc[1], bac, { timeout: 8000, filename: f });
  } catch (e) {
    dire("  ❌ %s — le script échoue à l'exécution : %s", f, e.message);
    global = true; continue;
  }

  const rendre = bac.render;
  if (typeof rendre !== 'function') { dire('  —  %s : pas de fonction render', f); continue; }

  // Un lien est réel s'il est écrit en dur dans la page OU produit au rendu.
  const bilan = [], cibles = new Set(
    [...src.matchAll(/<a\b[^>]*\bhref="([^"#?]+\.html)"/g)].map((m) => m[1]));
  let dur = false;
  for (const l of ['fr', 'en', 'ar']) {
    try {
      rendre(l);
      const html = rendu(document);
      for (const m of html.matchAll(/href="([^"#?]+\.html)"/g)) cibles.add(m[1]);
      for (const h of liensCrees(document)) {
        const p = h.split(/[#?]/)[0];
        if (p.endsWith('.html')) cibles.add(p);
      }
      bilan.push(`${l} ${html.length} car.`);
      if (html.length < 300) { dur = true; bilan.push(`${l} RENDU VIDE`); }
    } catch (e) {
      dur = true; bilan.push(`${l} ÉCHEC — ${e.message}`);
    }
  }
  global ||= dur;
  graphe[f] = [...cibles].sort();
  if (!enJSON) {
    console.log('  %s %s — %s\n      liens : %s',
      dur ? '❌' : '✅', f, bilan.join(' · '), [...cibles].join(', ') || 'aucun');
  }
}
if (enJSON) console.log(JSON.stringify(graphe));
process.exit(global ? 1 : 0);
