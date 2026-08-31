# Claude sur le VPS — plan d'installation

Ce que la boucle autonome fait, ce qu'elle ne fait pas, et dans quel ordre
l'allumer. Quatre phases, chacune vérifiable avant de passer à la suivante.

**Ce qu'elle fait.** Une fois par nuit : elle lit `FEUILLE-DE-ROUTE.md`, prend
**une** entrée « à faire » dans les zones qu'on lui autorise, demande à Claude
de la traiter, lance les contrôles, et **ouvre une pull request**.

**Ce qu'elle ne fait jamais.** Pousser sur `main`. Le déploiement fait
`rsync --delete` vers le site public : une erreur arrivée sur `main` serait en
ligne dans la minute. Le robot propose, un humain dispose.

---

## Phase 0 — d'abord, comprendre la panne SSH

Aucune installation nécessaire. Le Claude déjà présent sur ton VPS est le seul
agent qui voit cette machine — moi je ne l'atteins pas.

Connecte-toi et lance `claude`, puis colle ceci :

```
Le port SSH 2222 de cette machine n'a pas répondu entre 07:13 et 08:19 UTC
ce 31 août, ni à 22:38 UTC la veille. Entre-temps il répondait normalement.
Aucune configuration n'a changé.

Trouve pourquoi. Regarde dans cet ordre, et donne-moi les extraits bruts :
  1. la machine a-t-elle redémarré     → last -x reboot | head ; uptime
  2. sshd s'est-il arrêté ou rechargé  → journalctl -u ssh -u sshd --since "2026-08-30 22:00" --until "2026-08-31 09:00" --no-pager
  3. un bannissement                   → fail2ban-client status sshd 2>/dev/null ; journalctl --since "2026-08-30 22:00" | grep -iE 'ban|drop|refus' | tail -40
  4. une tâche de nuit                 → systemctl list-timers --all | head -20 ; ls /etc/cron.daily
  5. la mémoire                        → journalctl --since "2026-08-30 22:00" | grep -i 'out of memory' | tail

Conclus par une cause probable et ce qu'il faut changer. Ne modifie rien.
```

Le « ne modifie rien » compte : on diagnostique avant de réparer.

**Suspect le plus probable :** un `fail2ban` qui bannit les adresses des
runners GitHub. Elles changent à chaque exécution, et un dépôt qui déploie
souvent finit par cogner à la porte assez vite pour se faire prendre pour une
attaque. Si c'est ça, la réponse n'est pas de désactiver fail2ban, mais de
mettre les plages de GitHub Actions en liste blanche (`ignoreip`).

---

## Phase 1 — installer la boucle, et prouver la plomberie

### 1.1 Le compte et le dépôt

Le foyer doit être **hors de `/home`** : l'unité systemd active
`ProtectHome=true`, qui rend `/home` inaccessible au service. Sans ça, ni
`claude` ni `gh` ne peuvent lire leurs identifiants, et ils échouent sans dire
pourquoi.

```bash
sudo useradd --system --home-dir /var/lib/agneau --create-home --shell /bin/bash agneau
sudo mkdir -p /srv/agneau
sudo chown agneau:agneau /srv/agneau
sudo -u agneau git clone https://github.com/joe17xe/thelamb /srv/agneau
sudo touch /var/log/agneau-boucle.log
sudo chown agneau:agneau /var/log/agneau-boucle.log
```

### 1.2 Les deux outils, authentifiés **en tant qu'`agneau`**

C'est l'étape qu'on rate. Ton `claude` à toi est authentifié sous **ton** foyer.
Le robot tourne sous un autre compte : il lui faut sa propre session.

```bash
sudo -u agneau HOME=/var/lib/agneau claude          # connexion interactive, une fois
sudo -u agneau HOME=/var/lib/agneau gh auth login   # portée « repo » suffit
```

`gh` peut aussi lire un jeton depuis un fichier, si tu préfères ne pas ouvrir
de session interactive :

```bash
sudo mkdir -p /etc/agneau
printf 'GH_TOKEN=ghp_xxx\n' | sudo tee /etc/agneau/boucle.env >/dev/null
sudo chmod 600 /etc/agneau/boucle.env
```

Le jeton n'a **pas** besoin de la portée `workflow` : la consigne du robot lui
interdit de toucher à `.github/workflows/`.

### 1.3 Un tour à vide

```bash
sudo -u agneau HOME=/var/lib/agneau DEPOT=/srv/agneau ZONES=verte \
  /srv/agneau/outils/boucle-vps.sh --a-vide
```

**Le résultat attendu aujourd'hui est `aucune entrée « à faire »`.** Ce n'est
pas une panne : la zone verte est vide (voir phase 2). Ça prouve que le compte,
le dépôt, le verrou et le coupe-circuit fonctionnent.

Si tu lis autre chose, c'est un vrai problème — le script nomme lui-même ce qui
manque : outil absent du `PATH`, `gh` non authentifié, dépôt introuvable.

---

## Phase 2 — lui donner du travail vert

**C'est ici que le plan bute, et il faut le dire.** Aujourd'hui la zone verte
ne contient aucune entrée « à faire ». Allumer la minuterie donnerait une
boucle qui, chaque nuit, ne fait correctement rien.

Une entrée est **verte** quand elle réunit trois conditions :

1. **Mécanique** — le quoi ne se discute pas, seul le comment demande du soin.
2. **Vérifiable par un outil** — `tout-verifier.sh` sait dire si c'est réussi.
3. **Sans jugement éditorial** — ni théologie, ni ton, ni règle des trois cercles.

R-010 (les références nues) échoue au test 3 : la tentative automatique a
produit « Isaïe 587 » à partir d'une date et « Matthieu 28 » à partir d'une
coordonnée. R-013 (la nomenclature des liens) échoue aussi : classer un lien
entre allusion et écho est un jugement.

R-015 était verte à tort : elle touche `.github/workflows/`, que la consigne du
robot lui interdit. Elle serait tombée dessus au premier tour et n'aurait rien
pu faire. Elle est passée en rouge.

**Écris donc une ou deux entrées vraiment vertes avant d'allumer la
minuterie.** Sinon la boucle tourne à blanc et tu perds confiance en elle pour
de mauvaises raisons.

---

## Phase 3 — la minuterie

Seulement une fois qu'un tour manuel a produit une PR correcte.

```bash
sudo cp /srv/agneau/outils/systemd/agneau-boucle.* /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now agneau-boucle.timer
systemctl list-timers agneau-boucle.timer
```

Une fois par nuit à 03:30, avec un délai aléatoire d'un quart d'heure.
`ZONES=verte` est posé dans l'unité : le robot ne voit que la zone verte tant
qu'il n'a pas fait ses preuves. Retirer cette ligne lui ouvre l'orange — il y
ouvrira des PR, que tu liras avant de fusionner.

**Monte en fréquence seulement après plusieurs semaines sans incident.**

---

## Phase 4 — savoir ce qu'elle fait

```bash
tail -f /var/log/agneau-boucle.log          # ce que le robot raconte
journalctl -u agneau-boucle.service -n 50   # ce que systemd en pense
```

Trois signaux à surveiller :

| Ce que tu vois | Ce que ça veut dire |
|---|---|
| une PR `[R-0XX]` ouverte | tour réussi — à relire |
| un ticket « intervention nécessaire » | le robot a buté et a posé une question |
| rien du tout, plusieurs nuits | zone verte vide, ou minuterie arrêtée |

**Le coupe-circuit.** Créer un fichier `PAUSE` à la racine du dépôt, depuis
l'interface GitHub, arrête la boucle à l'exécution suivante. Le supprimer la
relance. Pas besoin d'accès SSH — ce qui compte le jour où SSH est justement
ce qui ne marche pas.

---

## Ce qui peut mal tourner

| Risque | Ce qui le contient |
|---|---|
| le robot casse une page | il n'ouvre que des PR ; la CI les refuse rouges |
| deux tours se chevauchent | `flock` — un seul passage à la fois |
| il refait ce qui est fait | il cherche une PR existante portant l'identifiant |
| il part en boucle sur une entrée | une entrée par exécution, jamais deux |
| il touche à ses propres garde-fous | sa consigne lui interdit `.github/`, `outils/`, la feuille de route |
| il invente un verset | sa consigne le lui interdit ; en cas de doute il ouvre un `BLOCAGE.md` |

Aucun de ces garde-fous ne remplace la relecture. La zone verte veut dire
« fusionnable si la CI est verte », pas « juste sans lecture humaine ».
