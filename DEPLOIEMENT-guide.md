# Mise en ligne de demo.joefr.cloud — guide en une page

> Rappel : je n'ai pas accès à votre VPS ni à votre GitHub. Voici les commandes à exécuter vous-même. Comptez ~15 min.

## Étape 0 — Récupérer le projet
Téléchargez `thelamb-next.tar.gz` (livré à côté de ce guide) et décompressez-le sur votre machine :
```bash
tar xzf thelamb-next.tar.gz && cd thelamb-next
```

## Étape 1 — Pousser dans Git (dépôt joe17xe/thelamb ou un nouveau)
Le dépôt actuel `joe17xe/thelamb` contient les prototypes/docs. Deux options :

**Option A — nouveau dépôt dédié à l'app (recommandé)**
```bash
git init && git add . && git commit -m "Socle Next.js : accueil trilingue, Fil Rouge (153), API + modération, déploiement VPS"
git branch -M main
git remote add origin git@github.com:joe17xe/thelamb-next.git   # créez ce dépôt vide sur GitHub d'abord
git push -u origin main
```

**Option B — dans un sous-dossier du dépôt existant**
```bash
# depuis votre clone de joe17xe/thelamb
mkdir app-next && cp -r /chemin/thelamb-next/* app-next/
git add app-next && git commit -m "Ajout du socle Next.js déployable" && git push
```

## Étape 2 — Déployer sur le VPS
Envoyez le code sur le serveur, puis lancez le script (il fait tout : Node, Nginx, Certbot, PM2, build, HTTPS) :
```bash
# depuis votre machine — pousser le code
rsync -az --exclude node_modules --exclude .next ./ root@72.61.199.160:/var/www/thelamb/

# puis en SSH sur le VPS
ssh root@72.61.199.160
cd /var/www/thelamb
bash deploy/deploy.sh
```
Si vous préférez que le serveur clone depuis GitHub, exportez l'URL avant de lancer :
```bash
REPO_URL=git@github.com:joe17xe/thelamb-next.git bash deploy/deploy.sh
```

## Étape 3 — Vérifier
- Ouvrez **https://demo.joefr.cloud** → l'accueil trilingue.
- **https://demo.joefr.cloud/pages/fil-rouge.html** → le Fil Rouge (153 arcs).
- **https://demo.joefr.cloud/admin** → modération (jeton dans `/var/www/thelamb/.env.local`).

## Ce que le script installe
Node.js 20, build-essential + python3 (pour better-sqlite3), Nginx, Certbot, PM2. Il crée le vhost `demo.joefr.cloud`, un certificat Let's Encrypt, et lance l'app via PM2 sur le port 3000 derrière Nginx.

## Commandes d'exploitation
| Besoin | Commande |
|---|---|
| Redémarrer l'app | `pm2 restart thelamb` |
| Voir les logs | `pm2 logs thelamb` |
| Recharger Nginx | `sudo systemctl reload nginx` |
| Tester la conf Nginx | `sudo nginx -t` |
| Refaire un build après mise à jour | `cd /var/www/thelamb && git pull && npm install && npm run build && pm2 restart thelamb` |
| Renouveler le HTTPS (auto, mais manuel possible) | `sudo certbot renew` |

## Notes
- Le script est **idempotent** : relançable sans casse. Il **sauvegarde** tout vhost Nginx existant en `.bak-<horodatage>`.
- Base **SQLite** (fichier `data/thelamb.db`), migration PostgreSQL prévue via `lib/db.js` sans toucher aux routes.
- Le contenu éditorial (11 pages) est servi statiquement depuis `public/pages/` — rapide et sûr ; le formulaire de contribution et la modération passent par l'API Next.
