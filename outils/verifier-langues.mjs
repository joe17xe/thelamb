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
import { runInNewContext } from 'node:vm';

const LANGUES = ['fr', 'en', 'ar'];

/** Isole le littéral de l'objet C en suivant l'imbrication, chaînes comprises. */
function extraireC(source) {
  const debut = source.search(/\bconst\s+C\s*=\s*\{/);
  if (debut === -1) return null;
  const ouvrante = source.indexOf('{', debut);
  let profondeur = 0, chaine = null, echappe = false;
  for (let i = ouvrante; i < source.length; i++) {
    const c = source[i];
    if (chaine) {
      if (echappe) echappe = false;
      else if (c === '\\') echappe = true;
      else if (c === chaine) chaine = null;
      continue;
    }
    if (c === '"' || c === "'" || c === '`') { chaine = c; continue; }
    if (c === '{') profondeur++;
    else if (c === '}' && --profondeur === 0) return source.slice(ouvrante, i + 1);
  }
  return null;
}

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
  const source = readFileSync(chemin, 'utf8');
  const litteral = extraireC(source);
  if (!litteral) return { chemin, ignore: 'pas d\'objet C — page hors gabarit' };

  let C;
  try {
    C = runInNewContext('(' + litteral + ')', Object.create(null), { timeout: 2000 });
  } catch (e) {
    return { chemin, erreurs: ['objet C illisible : ' + e.message] };
  }

  const erreurs = [], avis = [];
  const presentes = LANGUES.filter((l) => C[l]);
  for (const l of LANGUES) if (!C[l]) erreurs.push(`langue \`${l}\` absente de l'objet C`);
  if (presentes.length < 2) return { chemin, erreurs };

  if (C.ar && C.ar.dir !== 'rtl') erreurs.push('`ar.dir` devrait valoir "rtl"');
  for (const l of ['fr', 'en']) {
    if (C[l] && C[l].dir && C[l].dir !== 'ltr') avis.push(`\`${l}.dir\` vaut "${C[l].dir}"`);
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
