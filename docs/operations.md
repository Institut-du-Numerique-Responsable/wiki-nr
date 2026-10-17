# État et exploitation

État du 17 octobre 2026.

## État des contenus

L’instantané `content/` correspond au wiki en ligne au 17 octobre 2026 : un nouvel export public de 500 pages est identique, fichier par fichier, à la copie suivie dans Git.

| Langue | Articles | Redirections et catégories | Total exporté |
|---|---:|---:|---:|
| Français | 207 | 102 | 309 |
| English | 69 | 7 | 76 |
| Español | 54 | 1 | 55 |
| Deutsch | 38 | 5 | 43 |
| Nederlands | 15 | 2 | 17 |

Audit des liens de langue du 17 octobre 2026 : aucun lien vers une page absente et aucun lien non réciproque. 26 articles EN, ES ou DE n’ont aucun lien de langue alors que leur équivalent existe dans une autre langue ; le lot `drafts/2026-10-17-language-links` les relie (voir plus bas).

## Lots de publication

Les lots publiés sont archivés dans `operations/publication/`. Leur mode `publish` est désactivé dans cette copie. Les dossiers `before` conservent les originaux.

| Lot | Contenu | Statut |
|---|---|---|
| `2026-09-11-eu-translations` | AI Act, codes de conduite IA, Cyber Resilience Act, NIS2, Data Act (FR/EN) | publié |
| `2026-09-11-eu-regulation` | AI Act et codes de conduite IA (ES/DE) | publié |
| `2026-09-11-de`, `2026-09-11-de-2` | Enrichissement des fiches allemandes | publié |
| `2026-09-11-en-es` | Traductions EN et ES | publié |
| `2026-09-11-es-regulation` | Cadre réglementaire européen en espagnol | publié |
| `2026-09-11-language-links` | 19 corrections de liens multilingues | publié |
| `2026-10-09-en-es` | Agentic AI, IA agéntica, GHG Protocol, Shadow AI, Low tech | publié |

Les lots en attente de publication restent dans `drafts/` :

| Lot | Contenu | Statut |
|---|---|---|
| `2026-10-17-language-links` | Ajout de liens de langue sur 52 pages (25 groupes FR/EN/ES/DE) | préparé, prévisualisations réussies, à publier |

Les archives `2026-09-11-eu-*` proposent `verify` (prévisualisation) et `verify-live` (comparaison aux pages publiées). Les autres lots contiennent `check.py`, `prepare.py`, `publication.json` et `published.json`. Toute nouvelle modification doit partir d’une lecture récente du wiki ; un lot archivé ne sert pas à restaurer une ancienne version.

Les contrôles de rendu vérifient les liens internes d’articles et les erreurs de parsing. Ils ne prouvent pas l’exactitude juridique des textes. MediaWiki peut supprimer les sauts de ligne finaux ; la comparaison tolère uniquement cette normalisation.

## SEO

Contrôle public du 17 octobre 2026 (`operations/seo/verify.py`) : URL canonique, hreflang, absence de noindex, règles robots et sitemaps valides dans les cinq langues ; sitemaps régénérés le jour même.

### Corrections déployées le 11 septembre 2026

Les cinq sitemaps ont été régénérés. Une tâche cron les actualise à la minute 17 de chaque heure, avec verrouillage contre les exécutions simultanées et remplacement des fichiers générés complets. Le cache HTTP des sitemaps est limité à une heure.

Le hook SEO inclut désormais la langue de la page courante dans les liens hreflang. Les groupes de robots partagent les exclusions des URLs techniques et des variantes de requête. Les articles restent explorables.

Le rapport `operations/seo/reports/2026-09-11.json` conserve les contrôles publics effectués après déploiement : une page par langue, URL canonique, hreflang propre, absence de noindex, règles robots et lecture des index et fichiers sitemap. Cela ne constitue pas un audit de chaque article. Les liens réciproques ont été complétés depuis par les lots `2026-09-11-language-links` et `2026-10-09-en-es`.

Sauvegardes de configuration protégées conservées sur le serveur sous `/home/ggallon/wiki-seo-20260911/backups/20260911T124153Z/`. Elles ne sont pas dans GitHub. Le script d’installation est une trace du déploiement ponctuel et refuse d’ajouter deux fois le même hook ; ne pas le relancer sans inspection de l’état courant. `verify.py` permet un contrôle public sans écriture.

La syntaxe PHP et la configuration nginx ont été validées. Une meilleure indexabilité ne garantit ni classement ni citation par les moteurs d’IA. Aucun fichier spécifique aux IA n’est requis pour ces contrôles.

## Données exclues

Ne pas committer LocalSettings.php, mots de passe, clés, fichiers d’environnement, exports SQL ou sauvegardes système. Utiliser l’API publique pour les exports éditoriaux. Les scripts de ce dépôt ne demandent aucun secret pour lire le wiki.

## GitHub et production

Aucun déploiement automatique n’est configuré. Mettre à jour GitHub et publier sur MediaWiki sont deux opérations distinctes. Après une publication, refaire un export public, vérifier ses empreintes et examiner le diff avant commit.

## Nettoyage du serveur du 11 septembre 2026

Après vérification du commit GitHub et des 116 fichiers wikitexte archivés, les copies serveur `wiki-drafts`, les deux lots réglementaires initiaux et les cinq exports intermédiaires ont été supprimés. Les commandes historiques des README de lots nécessitent désormais de restaurer le lot depuis GitHub avant utilisation ; ne pas les relancer pour republier des versions anciennes.

L’archive d’installation MediaWiki 1.43.9 et le cache de paquets APT ont également été supprimés. Les données applicatives, configurations, sauvegardes SQL et journaux binaires MySQL sont conservés. La carte `.Codex` reste sur le serveur.

La rotation nginx échouait parce que le compte `www-data` ne pouvait pas créer les archives dans `/var/log/nginx`, propriété de `root:adm`. La règle de rotation de ce seul répertoire utilise désormais `su root adm`, avec sauvegarde de l’ancienne configuration dans `/root/maintenance-backups-20260911/`. Le service logrotate s’est terminé avec succès. Les règles des autres sites n’ont pas été modifiées.
