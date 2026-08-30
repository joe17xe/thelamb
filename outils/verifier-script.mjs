#!/usr/bin/env node
// Contrôle que le JavaScript en ligne de chaque page parse encore.
// Une page dont le script est cassé s'affiche vide : le HTML est bien là,
// mais rien ne le remplit. C'est invisible à la lecture du fichier.

import { readFileSync } from 'node:fs';
import vm from 'node:vm';

let dur = false;
for (const f of process.argv.slice(2)) {
  const src = readFileSync(f, 'utf8');
  const blocs = [...src.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g)];
  if (!blocs.length) { console.log('  —  %s : pas de script en ligne', f); continue; }
  let ok = true;
  blocs.forEach((m, i) => {
    try { new vm.Script(m[1], { filename: `${f}#${i}` }); }
    catch (e) { ok = false; dur = true; console.log('  ❌ %s bloc %d — %s', f, i, e.message); }
  });
  if (ok) console.log('  ✅ %s — %d bloc(s) valide(s)', f, blocs.length);
}
process.exit(dur ? 1 : 0);
