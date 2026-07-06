# Architecture technique — VPS Hostinger, base de données gratuite

## Choix recommandé (le plus simple qui soit une vraie référence)

**Next.js 14+ (App Router) · SQLite via Prisma au lancement · PostgreSQL quand le trafic grandit · Nginx + Certbot · PM2 · Cloudflare gratuit devant.**
Coût logiciel total : 0 € au-delà du VPS. Tout tourne sur la machine que vous payez déjà.

### Pourquoi ces choix
- **Next.js** : pages multilingues par routes (`/fr`, `/en`, `/ar` avec `dir="rtl"` natif), formulaires et espace admin dans le même projet, rendu statique des pages de contenu (rapide, bon SEO — indispensable pour être « une référence »).
- **SQLite d'abord** : gratuit, zéro service à administrer, un simple fichier `data.db` sur le VPS ; largement suffisant pour les propositions de correspondances et leur modération (écritures rares, lectures cachées). **Migration Postgres en une ligne de configuration Prisma** le jour où nécessaire — Postgres est lui aussi 100 % gratuit, installé sur le même VPS.
- **Le contenu éditorial n'est PAS en base** : les pages (étalon, parcours, dossiers) vivent en fichiers MDX dans le dépôt Git — versionnées, relisibles, traduisibles fichier par fichier. La base ne contient que ce qui est dynamique : correspondances du Fil Rouge et propositions.

## Schéma de données (Prisma)
```prisma
model Link {            // une correspondance AT→NT
  id        Int      @id @default(autoincrement())
  theme     String   // agneau | prophetie | alliance | paque | figures | temple | filshomme | trinite
  otBook    String   // "Gen"
  otChapter Int
  otRef     String   // "Genèse 22:8"
  otTextFr  String
  otTextEn  String?
  otTextAr  String?
  ntBook    String
  ntChapter Int
  ntRef     String
  ntTextFr  String
  ntTextEn  String?
  ntTextAr  String?
  title     String
  note      String?
  status    String   @default("pending") // pending | approved | rejected
  proposedBy String?
  reviewedBy String?
  createdAt DateTime @default(now())
}
model Admin {
  id       Int    @id @default(autoincrement())
  email    String @unique
  hash     String // mot de passe haché (bcrypt)
}
```

## Mise en place sur le VPS (Ubuntu 24) — ordre des opérations
1. `ufw` (22/80/443) + utilisateur non-root + clés SSH.
2. Node LTS + PM2 (`pm2 startup`).
3. Nginx en reverse proxy vers le port de l'app ; Certbot pour le HTTPS.
4. Dépôt GitHub privé ; déploiement par GitHub Action (SSH → `git pull && npm run build && pm2 reload`).
5. Sauvegarde : cron quotidien qui copie `data.db` (ou `pg_dump`) horodaté + envoi hors du VPS (même un dépôt privé suffit au début).
6. Cloudflare gratuit : cache des pages statiques, protection du formulaire, statistiques.

## Reprise des prototypes
- Le **Fil Rouge v2** devient un composant React : ses 101 correspondances sont importées en base (script de seed fourni à partir du fichier actuel), le formulaire poste sur `/api/propose`, la modération devient une vraie page `/admin` avec session.
- La **page étalon** devient le gabarit MDX `parcours/agneau/etape-1` ; ses textes FR/EN/AR sont déjà découpés par langue — la migration est mécanique.

## Alternatives écartées (et pourquoi)
- Supabase cloud (gratuit mais dépendance externe et limites du palier gratuit ; inutile puisque vous avez un VPS).
- WordPress (poussif pour le Fil Rouge interactif et le trilinguisme RTL exigeant).
- Astro pur (excellent pour le contenu, mais l'admin + formulaires est plus naturel dans Next.js — un seul projet à maintenir).
