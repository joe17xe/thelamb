#!/usr/bin/env node
// Lit l'objet de contenu trilingue d'une page.
//
//   node outils/lire-C.mjs page.html            l'objet entier, en JSON
//   node outils/lire-C.mjs page.html eyebrow    une clé, pour les trois langues
//
// Les pages ne nomment pas toutes leur objet pareil (`C` sur le gabarit, `T`
// sur la frise et le seuil) et certaines le construisent en appelant leurs
// propres fonctions. On exécute donc le script de la page dans un DOM factice,
// puis on récupère la première variable qui porte des clés de langue.

import { readFileSync } from 'node:fs';
import vm from 'node:vm';

/** DOM minimal : assez pour qu'un script de page s'exécute et rende. */
export function domFactice() {
  // Tout élément créé est retenu : certaines pages posent leurs liens par
  // `createElement` + `appendChild`, sans jamais écrire de HTML. Sans ce
  // registre, ces liens-là seraient invisibles au contrôle.
  const crees = [];
  const faire = () => enregistrer({
    innerHTML: '', textContent: '', className: '', value: '',
    style: { setProperty() {} }, dataset: {}, children: [], classList: { add() {}, remove() {}, toggle() {} },
    appendChild(e) { this.children.push(e); return e; },
    removeChild() {}, insertBefore(e) { this.children.push(e); return e; },
    href: undefined, attributs: {},
    setAttribute(k, v) { this.attributs[k] = v; if (k === 'href') this.href = v; },
    getAttribute(k) { return this.attributs[k] ?? null; },
    removeAttribute(k) { delete this.attributs[k]; },
    addEventListener() {}, querySelector: () => faire(), querySelectorAll: () => [],
    getBoundingClientRect: () => ({ width: 1200, height: 600, top: 0, left: 0 }),
    focus() {}, scrollIntoView() {},
  });
  const enregistrer = (n) => { crees.push(n); return n; };
  const noeuds = new Map();
  const document = {
    documentElement: faire(), body: faire(), head: faire(),
    _ancres: noeuds, _crees: crees,
    getElementById(id) { if (!noeuds.has(id)) noeuds.set(id, faire()); return noeuds.get(id); },
    createElement: faire, createElementNS: faire, createTextNode: faire,
    querySelector: () => faire(), querySelectorAll: () => [], addEventListener() {},
  };
  return document;
}

export function lireC(chemin) {
  const src = readFileSync(chemin, 'utf8');
  const bloc = src.match(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/);
  if (!bloc) return null;

  const document = domFactice();
  const bac = {
    document, console: { log() {}, warn() {}, error() {} },
    setTimeout: () => 0, clearTimeout() {}, setInterval: () => 0, clearInterval() {},
    requestAnimationFrame: () => 0, matchMedia: () => ({ matches: false, addEventListener() {} }),
    location: { hash: '', search: '' }, navigator: { language: 'fr' },
    localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
  };
  bac.window = bac; bac.globalThis = bac;

  // Les `const` de haut niveau ne remontent pas au global d'un contexte vm, et
  // les pages ne nomment pas leur objet pareil (C, T, LIB…). On relève donc les
  // noms déclarés dans la source et on demande au script de les exposer.
  const noms = [...new Set([...bloc[1].matchAll(/\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*\{/g)]
    .map((m) => m[1]))];
  const exposition = ';globalThis.__langues=(()=>{' + noms.map(
    (n) => `try{if(typeof ${n}!=="undefined"&&${n}&&${n}.fr&&${n}.ar)return ${n};}catch(e){}`).join('')
    + 'return null;})();';

  try {
    vm.runInNewContext(bloc[1] + exposition, bac, { timeout: 5000, filename: chemin });
  } catch {
    return null;
  }
  return bac.__langues || null;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const [chemin, cle] = process.argv.slice(2);
  const C = lireC(chemin);
  if (!C) { console.error("pas d'objet de langue dans " + chemin); process.exit(1); }
  if (cle) {
    for (const l of ['fr', 'en', 'ar']) {
      if (C[l]) console.log(l + '\t' + String(C[l][cle] ?? '—').slice(0, 90));
    }
  } else {
    console.log(JSON.stringify(C, null, 1));
  }
}
