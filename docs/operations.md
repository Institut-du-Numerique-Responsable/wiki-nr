# État et exploitation

État du 11 septembre 2026.

## Contenus publiés

Les deux lots sous `operations/publication/` ont été publiés et relus via l’API publique :

- FR/EN : AI Act, codes de conduite et de bonnes pratiques IA, Cyber Resilience Act, NIS2, Data Act.
- ES/DE : AI Act et codes de conduite et de bonnes pratiques IA.

Les dossiers `before` conservent les originaux ; `after` contient le texte prévu. Le manifeste associe les pages aux révisions de départ et aux empreintes du texte. Ces lots sont une archive de publication, pas un moyen de restaurer automatiquement une version ancienne. Toute nouvelle modification doit partir d’une lecture récente du wiki.

Chaque copie archivée propose `verify` (prévisualisation) et `verify-live` (comparaison aux pages publiées). Le mode `publish` est désactivé dans ce dépôt : les anciens scripts vérifiaient la révision avant écriture, mais sans protection atomique contre une modification concurrente entre la lecture et l’écriture. Un prochain outil de publication devra utiliser une protection atomique des conflits avant d’être activé. MediaWiki peut supprimer les sauts de ligne finaux ; la comparaison tolère uniquement cette normalisation.

Les contrôles de rendu vérifient les liens internes d’articles et les erreurs de parsing. Ils ne prouvent pas l’exactitude juridique des textes ni la réciprocité de tous les liens de langues.

## SEO : corrections déployées le 11 septembre 2026

Les cinq sitemaps ont été régénérés. Une tâche cron les actualise à la minute 17 de chaque heure, avec verrouillage contre les exécutions simultanées et remplacement des fichiers générés complets. Le cache HTTP des sitemaps est limité à une heure.

Le hook SEO inclut désormais la langue de la page courante dans les liens hreflang. Les groupes de robots partagent les exclusions des URLs techniques et des variantes de requête. Les articles restent explorables.

Le rapport `operations/seo/reports/2026-09-11.json` conserve les contrôles publics effectués après déploiement : une page par langue, URL canonique, hreflang propre, absence de noindex, règles robots et lecture des index et fichiers sitemap. Cela ne constitue pas un audit de chaque article. Les liens réciproques entre toutes les traductions restent à compléter.

Sauvegardes de configuration protégées conservées sur le serveur sous `/home/ggallon/wiki-seo-20260911/backups/20260911T124153Z/`. Elles ne sont pas dans GitHub. Le script d’installation est une trace du déploiement ponctuel et refuse d’ajouter deux fois le même hook ; ne pas le relancer sans inspection de l’état courant. `verify.py` permet un contrôle public sans écriture.

La syntaxe PHP et la configuration nginx ont été validées. Une meilleure indexabilité ne garantit ni classement ni citation par les moteurs d’IA. Aucun fichier spécifique aux IA n’est requis pour ces contrôles.

## Données exclues

Ne pas committer LocalSettings.php, mots de passe, clés, fichiers d’environnement, exports SQL ou sauvegardes système. Utiliser l’API publique pour les exports éditoriaux. Les scripts de ce dépôt ne demandent aucun secret pour lire le wiki.

## GitHub et production

Aucun déploiement automatique n’est configuré. Mettre à jour GitHub et publier sur MediaWiki sont deux opérations distinctes. Après une publication, refaire un export public, vérifier ses empreintes et examiner le diff avant commit.

## Nettoyage du serveur — 11 septembre 2026

Après vérification du commit GitHub et des 116 fichiers wikitexte archivés, les copies serveur `wiki-drafts`, les deux lots réglementaires initiaux et les cinq exports intermédiaires ont été supprimés. Les commandes historiques des README de lots nécessitent désormais de restaurer le lot depuis GitHub avant utilisation ; ne pas les relancer pour republier des versions anciennes.

L’archive d’installation MediaWiki 1.43.9 et le cache de paquets APT ont également été supprimés. Les données applicatives, configurations, sauvegardes SQL et journaux binaires MySQL sont conservés. La carte `.Codex` reste sur le serveur.

La rotation nginx échouait parce que le compte `www-data` ne pouvait pas créer les archives dans `/var/log/nginx`, propriété de `root:adm`. La règle de rotation de ce seul répertoire utilise désormais `su root adm`, avec sauvegarde de l’ancienne configuration dans `/root/maintenance-backups-20260911/`. Le service logrotate s’est terminé avec succès. Les règles des autres sites n’ont pas été modifiées.
