#!/usr/bin/env node
// Vérifie l'intégrité trilingue de l'objet C d'une page.
//
//   node outils/verifier-langues.mjs *.html
//
// Le contenu des pages vit dans `const C = { fr:…, en:…, ar:… }`. Une modification
// qui touche une langue et oublie les autres ne se voit pas à l'œil : la page
// s'affiche normalement dans la langue éditée et se dégrade dans les deux autres.
// Ce contrôle compare les trois structures clé par clé.

import { readFileSync } from 'node:fs';
import { lireC } from './lire-C.mjs';

const LANGUES = ['fr', 'en', 'ar'];

/** Décrit la forme d'une valeur, sans son contenu : c'est la forme qu'on compare. */
function forme(valeur) {
  if (Array.isArray(valeur)) return { type: 'liste', taille: valeur.length };
  if (valeur && typeof valeur === 'object') return { type: 'objet', cles: Object.keys(valeur).length };
  return { type: typeof valeur };
}

function memeForme(a, b) {
  if (a.type !== b.type) return false;
  if (a.type === 'liste') return a.taille === b.taille;
  if (a.type === 'objet') return a.cles === b.cles;
  return true;
}

function verifier(chemin) {
  const C = lireC(chemin);
  if (!C) return { chemin, ignore: 'aucun objet de langue — page hors gabarit' };

  const erreurs = [], avis = [];
  const presentes = LANGUES.filter((l) => C[l]);
  for (const l of LANGUES) if (!C[l]) erreurs.push(`langue \`${l}\` absente de l'objet C`);
  if (presentes.length < 2) return { chemin, erreurs };

  // Toutes les pages ne déclarent pas `dir` dans l'objet : certaines l'appliquent
  // directement dans leur rendu. On ne contrôle la valeur que si la clé existe.
  if (C.ar && C.ar.dir !== undefined && C.ar.dir !== 'rtl') {
    erreurs.push('`ar.dir` vaut "' + C.ar.dir + '" au lieu de "rtl"');
  }
  for (const l of ['fr', 'en']) {
    if (C[l] && C[l].dir !== undefined && C[l].dir !== 'ltr') avis.push(`\`${l}.dir\` vaut "${C[l].dir}"`);
  }
  if (C.ar && C.ar.dir === undefined && !/documentElement\.dir\s*=/.test(readFileSync(chemin, 'utf8'))) {
    erreurs.push('aucune bascule droite-à-gauche : ni `ar.dir`, ni `documentElement.dir` dans le rendu');
  }

  // La langue de référence est le français : c'est elle qu'on édite en premier.
  const reference = C.fr ? 'fr' : presentes[0];
  const clesRef = Object.keys(C[reference]);

  for (const l of presentes) {
    if (l === reference) continue;
    const cles = new Set(Object.keys(C[l]));
    const manquantes = clesRef.filter((k) => !cles.has(k));
    const surnumeraires = [...cles].filter((k) => !clesRef.includes(k));
    if (manquantes.length) erreurs.push(`\`${l}\` : clé(s) absente(s) — ${manquantes.join(', ')}`);
    if (surnumeraires.length) avis.push(`\`${l}\` : clé(s) en trop — ${surnumeraires.join(', ')}`);

    for (const k of clesRef) {
      if (!cles.has(k)) continue;
      const a = forme(C[reference][k]), b = forme(C[l][k]);
      if (!memeForme(a, b)) {
        erreurs.push(`\`${l}.${k}\` : ${b.type}${b.taille !== undefined ? `(${b.taille})` : ''} ` +
                     `au lieu de ${a.type}${a.taille !== undefined ? `(${a.taille})` : ''} en ${reference}`);
      }
      // Les cartes sont des listes de listes : on compare aussi les sous-longueurs.
      if (Array.isArray(C[reference][k]) && Array.isArray(C[l][k])) {
        C[reference][k].forEach((el, i) => {
          const autre = C[l][k][i];
          if (Array.isArray(el) && Array.isArray(autre) && el.length !== autre.length) {
            erreurs.push(`\`${l}.${k}[${i}]\` : ${autre.length} éléments au lieu de ${el.length}`);
          }
        });
      }
    }

    // Une chaîne vide passe les contrôles de forme mais laisse un trou à l'écran.
    for (const k of clesRef) {
      if (typeof C[reference][k] === 'string' && C[l][k] === '') {
        avis.push(`\`${l}.${k}\` est vide`);
      }
    }
  }

  return { chemin, erreurs, avis, langues: presentes };
}

const fichiers = process.argv.slice(2);
let bloquant = false;
const lignes = ['## Intégrité trilingue de l\'objet `C`\n'];

for (const f of fichiers) {
  const r = verifier(f);
  if (r.ignore) { lignes.push(`- \`${f}\` — ignorée : ${r.ignore}`); continue; }
  const erreurs = r.erreurs || [], avis = r.avis || [];
  if (!erreurs.length && !avis.length) {
    lignes.push(`- ✅ \`${f}\` — ${r.langues.join(' / ')} cohérentes`);
    continue;
  }
  lignes.push(`\n### \`${f}\` — ${erreurs.length ? '❌ divergence' : '⚠️ à regarder'}\n`);
  erreurs.forEach((e) => lignes.push(`- ❌ ${e}`));
  avis.forEach((a) => lignes.push(`- ⚠️ ${a}`));
  bloquant ||= erreurs.length > 0;
}

console.log(lignes.join('\n'));
process.exit(bloquant ? 1 : 0);
