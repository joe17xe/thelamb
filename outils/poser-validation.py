#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère `validation-liens.html` depuis `producteur/nature-des-liens.yml`.

    python3 outils/poser-validation.py

Le producteur ouvre la page, coche, et copie le relevé ; le porteur le reverse
dans le YAML. Le générateur est idempotent : on ne modifie pas la page à la
main, on modifie le fichier de données et on relance.

Le mot de passe n'est pas dans le dépôt : seule son empreinte y figure. Ce
n'est pas une sécurité — une page statique n'en a pas — mais une barrière de
courtoisie. Rien de sensible ne se trouve derrière : ce sont des références
bibliques, déjà publiques sur le site.
"""
import io
import os
import yaml

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DONNEE = os.path.join(RACINE, "producteur", "nature-des-liens.yml")
SORTIE = os.path.join(RACINE, "validation-liens.html")
EMPREINTE = "0x204c22c4"   # empreinte du mot de passe convenu, jamais le mot lui-même

THEMES = {
    "agneau": "L'Agneau", "alliance": "Alliances", "figures": "Figures",
    "filshomme": "Fils de l'homme", "paque": "Pâque & offrande",
    "prophetie": "Prophéties", "temple": "Temple",
    "trinite": "Un seul Dieu — Père, Fils, Esprit",
}


def page(donnee):
    natures = donnee["natures"]
    liens = donnee["liens"]
    ordre = ["cite", "allu", "echo", "lect", "debat"]
    import json
    js = json.dumps(
        {"natures": {k: natures[k] for k in ordre}, "ordre": ordre,
         "themes": THEMES, "liens": liens},
        ensure_ascii=False, separators=(",", ":"))
    return TEMPLATE.replace("/*<DONNEE>*/", "const D=" + js + ";").replace(
        "@@EMPREINTE@@", EMPREINTE).replace("@@COMPTE@@", str(len(liens)))


TEMPLATE = r"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Valider la nature des liens — L'Agneau de Dieu</title>
<meta name="robots" content="noindex,nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root{--bg:#0c0e18;--bg2:#11141f;--ink:#e9e3d3;--muted:#9a94a8;--gold:#d3a94f;--line:#23273a;--crimson:#a33}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:Georgia,serif;line-height:1.6}
  .top{border-bottom:1px solid var(--line);padding:14px 18px;display:flex;gap:14px;align-items:center;
    position:sticky;top:0;background:rgba(12,14,24,.96);backdrop-filter:blur(6px);z-index:5;flex-wrap:wrap}
  .brand{font-family:system-ui,sans-serif;font-size:11.5px;letter-spacing:.22em;color:var(--gold);text-transform:uppercase}
  .langs{margin-left:auto;display:flex;gap:6px}
  .langs button{background:none;border:1px solid var(--line);color:var(--muted);border-radius:999px;
    font-family:system-ui,sans-serif;font-size:12px;padding:4px 11px;cursor:pointer}
  .langs button[aria-pressed="true"]{color:var(--gold);border-color:var(--gold)}
  main{max-width:940px;margin:0 auto;padding:26px 18px 90px}
  h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;font-size:clamp(27px,5vw,40px);margin:.2em 0 .3em}
  .lede{color:#c6c0b2;font-size:15.5px;max-width:70ch}
  .avis{border-left:2px solid var(--crimson);padding:9px 0 9px 14px;margin:20px 0;color:var(--muted);font-size:14px;max-width:74ch}
  .porte{max-width:420px;margin:60px auto;text-align:center}
  .porte input{width:100%;background:var(--bg2);border:1px solid var(--line);color:var(--ink);
    font-family:system-ui,sans-serif;font-size:16px;padding:11px 14px;border-radius:8px;text-align:center}
  .porte button{margin-top:12px;background:none;border:1px solid var(--gold);color:var(--gold);
    font-family:system-ui,sans-serif;font-size:14px;padding:9px 22px;border-radius:999px;cursor:pointer}
  .porte .err{color:var(--crimson);font-size:13.5px;min-height:1.4em;margin-top:10px}
  .theme{margin:34px 0 12px;font-family:system-ui,sans-serif;font-size:11px;letter-spacing:.18em;
    text-transform:uppercase;color:var(--gold);border-bottom:1px solid var(--line);padding-bottom:7px}
  html[dir="rtl"] .theme,html[dir="rtl"] .brand{letter-spacing:.03em}
  .lien{border:1px solid var(--line);border-radius:11px;padding:13px 15px;margin-bottom:10px;background:var(--bg2)}
  .lien.fait{border-color:color-mix(in srgb,var(--gold) 40%,transparent)}
  .lien.change{border-color:var(--crimson)}
  .ltete{display:flex;gap:9px;align-items:baseline;flex-wrap:wrap}
  .num{font-family:system-ui,sans-serif;font-size:11px;color:var(--muted);min-width:2.2em}
  .ltitre{font-size:16px}
  .lref{font-family:system-ui,sans-serif;font-size:12.5px;color:var(--muted);margin:3px 0 0 2.6em}
  html[dir="rtl"] .lref{margin:3px 2.6em 0 0}
  .lind{font-size:13.5px;color:var(--muted);margin:7px 0 9px 2.6em;font-style:italic}
  html[dir="rtl"] .lind{margin:7px 2.6em 9px 0}
  .lment{font-size:13px;color:#c6c0b2;margin:0 0 9px 2.6em;border-left:2px solid var(--gold);padding-left:11px}
  html[dir="rtl"] .lment{margin:0 2.6em 9px 0;border-left:none;border-right:2px solid var(--gold);padding:0 11px 0 0}
  .choix{display:flex;gap:6px;flex-wrap:wrap;margin-left:2.6em}
  html[dir="rtl"] .choix{margin:0 2.6em 0 0}
  .choix label{font-family:system-ui,sans-serif;font-size:12px;border:1px solid var(--line);border-radius:999px;
    padding:5px 12px;cursor:pointer;color:var(--muted);user-select:none}
  .choix label.prop{border-style:dashed}
  .choix input{position:absolute;opacity:0;width:0;height:0}
  .choix input:checked+span{color:var(--gold)}
  .choix label:has(input:checked){border-color:var(--gold);color:var(--gold)}
  .note{margin:9px 0 0 2.6em;width:calc(100% - 2.6em);background:var(--bg);border:1px solid var(--line);
    color:var(--ink);font-family:Georgia,serif;font-size:13.5px;padding:7px 10px;border-radius:7px}
  html[dir="rtl"] .note{margin:9px 2.6em 0 0}
  .barre{position:fixed;left:0;right:0;bottom:0;background:rgba(12,14,24,.97);border-top:1px solid var(--line);
    padding:11px 18px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;z-index:6;backdrop-filter:blur(6px)}
  .barre .cpt{font-family:system-ui,sans-serif;font-size:12.5px;color:var(--muted)}
  .barre button{background:none;border:1px solid var(--gold);color:var(--gold);font-family:system-ui,sans-serif;
    font-size:13px;padding:8px 16px;border-radius:999px;cursor:pointer;margin-left:auto}
  .barre button.sec{border-color:var(--line);color:var(--muted);margin-left:0}
  #releve{width:100%;height:180px;background:var(--bg2);border:1px solid var(--line);color:var(--ink);
    font-family:ui-monospace,monospace;font-size:12px;padding:10px;border-radius:8px;margin-top:14px}
  [hidden]{display:none!important}
</style></head>
<body>
<div class="top"><span class="brand" id="brand"></span>
  <div class="langs"><button data-l="fr" aria-pressed="true">FR</button><button data-l="en" aria-pressed="false">EN</button><button data-l="ar" aria-pressed="false">عربي</button></div>
</div>

<div class="porte" id="porte">
  <h1 id="ptitre"></h1>
  <p class="lede" id="plede"></p>
  <input type="password" id="mdp" autocomplete="off">
  <div><button id="entrer"></button></div>
  <div class="err" id="perr"></div>
</div>

<main id="atelier" hidden>
  <h1 id="titre"></h1>
  <p class="lede" id="lede"></p>
  <p class="avis" id="avis"></p>
  <div id="liste"></div>
  <textarea id="releve" hidden readonly></textarea>
</main>

<div class="barre" id="barre" hidden>
  <span class="cpt" id="cpt"></span>
  <button class="sec" id="vider"></button>
  <button id="copier"></button>
</div>

<script>
/*<DONNEE>*/
const C={
 fr:{dir:"ltr",brand:"L'AGNEAU DE DIEU · ATELIER",
   ptitre:"Valider la nature des liens",
   plede:"Cette page est réservée au producteur. Entrez le mot convenu.",
   entrer:"Entrer", err:"Ce n'est pas le mot convenu.",
   titre:"De quelle nature est chacun de ces liens ?",
   lede:"@@COMPTE@@ correspondances. Pour chacune, une proposition est déjà cochée — en pointillé. Corrigez ce qui vous paraît faux, laissez le reste tel quel, puis copiez le relevé et transmettez-le. Votre travail est gardé sur cet appareil au fur et à mesure.",
   avis:"Cette page n'est pas protégée : le site est statique, sans serveur, et le mot convenu ne fait qu'écarter le passant. N'y mettez rien que le site ne puisse afficher — ce sont des références bibliques, déjà publiques.",
   cpt:"modifiée(s) sur", vider:"Tout remettre à la proposition", copier:"Copier le relevé",
   copie:"Relevé copié — collez-le dans un ticket ou dans un message.",
   note:"Une remarque ? (facultatif)", prop:"proposé",
   vers:"→", entete:"# Relevé de validation — nature des liens"},
 en:{dir:"ltr",brand:"THE LAMB OF GOD · WORKSHOP",
   ptitre:"Validate the nature of the links",
   plede:"This page is for the producer. Enter the agreed word.",
   entrer:"Enter", err:"That is not the agreed word.",
   titre:"What is the nature of each of these links?",
   lede:"@@COMPTE@@ correspondences. For each one a proposal is already ticked — dashed outline. Correct what seems wrong, leave the rest, then copy the record and send it. Your work is kept on this device as you go.",
   avis:"This page is not protected: the site is static, with no server, and the agreed word only keeps the passer-by out. Put nothing here the site could not display — these are Bible references, already public.",
   cpt:"changed out of", vider:"Reset all to the proposal", copier:"Copy the record",
   copie:"Record copied — paste it into an issue or a message.",
   note:"A remark? (optional)", prop:"proposed",
   vers:"→", entete:"# Validation record — nature of the links"},
 ar:{dir:"rtl",brand:"حمل الله · ورشة",
   ptitre:"التحقّق من طبيعة الصلات",
   plede:"هذه الصفحة للمنتِج. أدخل الكلمة المتّفق عليها.",
   entrer:"دخول", err:"ليست هذه الكلمة المتّفق عليها.",
   titre:"ما طبيعةُ كلٍّ من هذه الصلات؟",
   lede:"@@COMPTE@@ تناظرًا. لكلٍّ منها اقتراحٌ مؤشَّرٌ سلفًا — بإطارٍ متقطّع. صحِّح ما تراه خطأً، واترك الباقي، ثم انسخ الكشف وأرسله. يُحفظ عملُك على هذا الجهاز أوّلًا بأوّل.",
   avis:"هذه الصفحة غير محميّة: الموقع ثابتٌ بلا خادم، والكلمةُ المتّفق عليها تصرف العابرَ لا غير. لا تضع هنا ما لا يستطيع الموقعُ عرضَه — فهذه شواهدُ كتابية منشورة أصلًا.",
   cpt:"مُعدَّلة من أصل", vider:"إعادة الكل إلى الاقتراح", copier:"نسخ الكشف",
   copie:"نُسخ الكشف — الصقه في تذكرة أو رسالة.",
   note:"ملاحظة؟ (اختياري)", prop:"مقترَح",
   vers:"←", entete:"# كشف التحقّق — طبيعة الصلات"}
};
let LANG="fr";
const CLE="agneau.validation.liens";
const etat=(()=>{ try{return JSON.parse(localStorage.getItem(CLE)||"{}");}catch(e){return {};} })();
const garder=()=>{ try{localStorage.setItem(CLE,JSON.stringify(etat));}catch(e){} };
const empreinte=s=>{let h=0x811c9dc5;for(const ch of new TextEncoder().encode(s)){h^=ch;h=Math.imul(h,0x01000193)>>>0;}return "0x"+h.toString(16);};

function render(){
  const c=C[LANG];
  document.documentElement.lang=LANG;document.documentElement.dir=c.dir;
  document.getElementById('brand').textContent=c.brand;
  document.getElementById('ptitre').textContent=c.ptitre;
  document.getElementById('plede').textContent=c.plede;
  document.getElementById('entrer').textContent=c.entrer;
  document.getElementById('titre').textContent=c.titre;
  document.getElementById('lede').textContent=c.lede;
  document.getElementById('avis').textContent=c.avis;
  document.getElementById('vider').textContent=c.vider;
  document.getElementById('copier').textContent=c.copier;
  document.querySelectorAll('.langs button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.l===LANG?'true':'false'));
  batir();
}

function batir(){
  const c=C[LANG], hote=document.getElementById('liste');
  hote.innerHTML='';
  const par={};D.liens.forEach(l=>{(par[l.theme]=par[l.theme]||[]).push(l);});
  for(const [k,liens] of Object.entries(par)){
    const t=document.createElement('div');t.className='theme';
    t.textContent=(D.themes[k]||k)+' · '+liens.length;hote.appendChild(t);
    liens.forEach(l=>{
      const d=document.createElement('div');d.className='lien';d.dataset.n=l.n;
      const te=document.createElement('div');te.className='ltete';
      const nu=document.createElement('span');nu.className='num';nu.textContent=l.n;te.appendChild(nu);
      const ti=document.createElement('span');ti.className='ltitre';ti.textContent=l.titre;te.appendChild(ti);
      d.appendChild(te);
      const rf=document.createElement('div');rf.className='lref';
      rf.textContent=l.at+' '+c.vers+' '+l.nt;d.appendChild(rf);
      const ind=document.createElement('div');ind.className='lind';ind.textContent=l.indice;d.appendChild(ind);
      if(l.mention){const m=document.createElement('div');m.className='lment';m.textContent=l.mention;d.appendChild(m);}
      const ch=document.createElement('div');ch.className='choix';
      D.ordre.forEach(k2=>{
        const lb=document.createElement('label');
        if(k2===l.propose)lb.className='prop';
        const inp=document.createElement('input');inp.type='radio';inp.name='n'+l.n;inp.value=k2;
        inp.checked=(etat[l.n]&&etat[l.n].nature||l.propose)===k2;
        inp.addEventListener('change',()=>{
          etat[l.n]=Object.assign({},etat[l.n],{nature:k2});garder();marquer(d,l);compter();});
        const sp=document.createElement('span');
        sp.textContent=D.natures[k2][LANG]+(k2===l.propose?' · '+c.prop:'');
        lb.appendChild(inp);lb.appendChild(sp);ch.appendChild(lb);});
      d.appendChild(ch);
      const no=document.createElement('input');no.className='note';no.type='text';no.placeholder=c.note;
      no.value=(etat[l.n]&&etat[l.n].note)||'';
      no.addEventListener('input',()=>{etat[l.n]=Object.assign({},etat[l.n],{note:no.value});garder();marquer(d,l);compter();});
      d.appendChild(no);
      marquer(d,l);hote.appendChild(d);});
  }
  compter();
}

function marquer(d,l){
  const e=etat[l.n]||{};
  const change=e.nature&&e.nature!==l.propose;
  d.classList.toggle('change',!!change);
  d.classList.toggle('fait',!!(e.note&&e.note.trim())&&!change);
}
function compter(){
  const c=C[LANG];
  const n=D.liens.filter(l=>{const e=etat[l.n]||{};return (e.nature&&e.nature!==l.propose)||(e.note&&e.note.trim());}).length;
  document.getElementById('cpt').textContent=n+' '+c.cpt+' '+D.liens.length;
}
function releve(){
  const c=C[LANG];
  const li=D.liens.map(l=>{const e=etat[l.n]||{};
    const nat=e.nature||l.propose, chg=nat!==l.propose;
    const note=(e.note||'').trim();
    if(!chg&&!note)return null;
    return '- '+l.n+' · '+l.titre+'\n  nature: '+nat+(chg?'   (proposé : '+l.propose+')':'')+(note?'\n  note: '+note:'');
  }).filter(Boolean);
  return c.entete+'\n# '+li.length+' / '+D.liens.length+'\n\n'+(li.length?li.join('\n'):'(aucune correction : la proposition est validée telle quelle)')+'\n';
}

document.getElementById('entrer').addEventListener('click',ouvrir);
document.getElementById('mdp').addEventListener('keydown',e=>{if(e.key==='Enter')ouvrir();});
function ouvrir(){
  const v=document.getElementById('mdp').value;
  if(empreinte(v)==="@@EMPREINTE@@"){
    document.getElementById('porte').hidden=true;
    document.getElementById('atelier').hidden=false;
    document.getElementById('barre').hidden=false;
    try{sessionStorage.setItem(CLE+'.ouvert','1');}catch(e){}
  }else{document.getElementById('perr').textContent=C[LANG].err;}
}
document.getElementById('vider').addEventListener('click',()=>{
  for(const k of Object.keys(etat))delete etat[k];garder();batir();});
document.getElementById('copier').addEventListener('click',async()=>{
  const t=releve(), z=document.getElementById('releve');
  z.value=t;z.hidden=false;
  try{await navigator.clipboard.writeText(t);}catch(e){z.select();}
  document.getElementById('cpt').textContent=C[LANG].copie;});
document.querySelectorAll('.langs button').forEach(b=>
  b.addEventListener('click',()=>{LANG=b.dataset.l;render();}));
render();
try{ if(sessionStorage.getItem(CLE+'.ouvert')==='1'){
  document.getElementById('porte').hidden=true;
  document.getElementById('atelier').hidden=false;
  document.getElementById('barre').hidden=false;} }catch(e){}
</script>
</body></html>
"""

if __name__ == "__main__":
    donnee = yaml.safe_load(io.open(DONNEE, encoding="utf-8"))
    io.open(SORTIE, "w", encoding="utf-8").write(page(donnee))
    print("validation-liens.html : %d liens" % len(donnee["liens"]))
