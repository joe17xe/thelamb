// Extrait la connaissance que les pages portent déjà — livres, correspondances,
// prophètes, générations — et la rend en JSON canonique. C'est la moitié
// « mesure » de verifier-connaissances.py : les pages restent la matière,
// connaissances.yml en est le miroir déclaré, la CI refuse l'écart.
//
//     node outils/extraire-connaissances.mjs > /tmp/connaissances.json
import { readFileSync } from 'fs';
import { lireC } from './lire-C.mjs';

const desaccentue = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '');
const slug = (s) => desaccentue(s).toLowerCase()
  .replace(/[''·]/g, ' ').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

// ── les 73 livres, leurs trois noms, leur étagère, leurs périodes ──────────
const bib = lireC('salle-bibliotheque.html');
const srcBib = readFileSync('salle-bibliotheque.html', 'utf8');
const PERIODE_LIVRE = eval('(' + srcBib
  .match(/const PERIODE_LIVRE=\{([\s\S]*?)\};/)[0]
  .replace('const PERIODE_LIVRE=', '').replace(/;$/, '') + ')');

const TRANCHES = (srcBib.match(/const TRANCHES=\{([\s\S]*?)\};/) || [null])[0]
  ? eval('(' + srcBib.match(/const TRANCHES=\{([\s\S]*?)\};/)[0].replace('const TRANCHES=', '').replace(/;$/, '') + ')')
  : {};

const livres = [];
const etageres = {};
for (const [gi, g] of [...bib.fr.groups, ...bib.fr.groupsNT].entries()) {
  const gEn = [...bib.en.groups, ...bib.en.groupsNT][gi];
  const gAr = [...bib.ar.groups, ...bib.ar.groupsNT][gi];
  etageres[g.k] = { fr: g.t, en: gEn.t, ar: gAr.t };
  g.books.forEach((b, i) => {
    const entree = {
      id: slug(b.n), etagere: g.k,
      nom: { fr: b.n, en: gEn.books[i].n, ar: gAr.books[i].n },
      w: { fr: b.w, en: gEn.books[i].w, ar: gAr.books[i].w },
      periodes: (PERIODE_LIVRE[g.k] || [])[i] || null,
    };
    if (b.lien)   // badge D-013 déjà posé sur le pupitre, dans les trois langues
      entree.lien = { fr: b.lien, en: gEn.books[i].lien, ar: gAr.books[i].lien };
    const tr = (TRANCHES[g.k] || {})[i];   // un livre récit coupé entre deux époques
    if (tr) entree.tranches = tr;
    livres.push(entree);
  });
}

// ── les 153 correspondances du Fil Rouge ───────────────────────────────────
const srcIndex = readFileSync('index.html', 'utf8');
const D = eval(srcIndex.match(/const D=(\[[\s\S]*?\]);/)[1]);
const TR = eval('(' + srcIndex.match(/const TR=(\{[\s\S]*?\});\n/)[1] + ')');
const THEMES = eval('(' + srcIndex.match(/const THEMES=(\{[\s\S]*?\});/)[1] + ')');
const correspondances = D.map((d, i) => ({
  theme: d[6],
  at: { fr: d[2], en: TR.en[i][1], ar: TR.ar[i][1] },
  nt: { fr: d[5], en: TR.en[i][3], ar: TR.ar[i][3] },
  titre: { fr: d[7], en: TR.en[i][0], ar: TR.ar[i][0] },
}));
const themes = {};
correspondances.forEach(c => {
  const t = THEMES[c.theme];
  themes[c.theme] = themes[c.theme] ||
    { compte: 0, hex: t.hex, nom: { fr: t.fr, en: t.en, ar: t.ar } };
  themes[c.theme].compte += 1;
});

// ── les 14 veilleurs et les 20 générations de la frise ─────────────────────
const fr = lireC('frise-prophetes.html');
const prophetes = fr.fr.prophets.map((p, i) => ({
  id: p.k, epoque: p.phase, pos: +p.x.toFixed(2),   // pos : place sur l'axe, 0 = −1500, 100 = +30
  nom: { fr: p.n, en: fr.en.prophets[i].n, ar: fr.ar.prophets[i].n },
  date: { fr: p.d, en: fr.en.prophets[i].d, ar: fr.ar.prophets[i].d },
  vers: { fr: p.christ, en: fr.en.prophets[i].christ, ar: fr.ar.prophets[i].christ },
}));
const srcFrise = readFileSync('frise-prophetes.html', 'utf8');
const GENCLES = eval(srcFrise.match(/const GENCLES=(\[[^\]]*\]);/)[1]);
const generations = fr.fr.gen.map((g, i) => ({
  nom: { fr: g[0], en: fr.en.gen[i][0], ar: fr.ar.gen[i][0] },
  note: { fr: g[1] || '', en: fr.en.gen[i][1] || '', ar: fr.ar.gen[i][1] || '' },
  periode: GENCLES[i] === 'fourche' ? null : GENCLES[i],
  fourche: GENCLES[i] === 'fourche' || undefined,
}));

process.stdout.write(JSON.stringify(
  { livres, etageres, correspondances, themes, prophetes, generations }, null, 1));
