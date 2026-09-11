# État et exploitation

État du 11 septembre 2026.

## Contenus publiés

Les deux lots sous `operations/publication/` ont été publiés et relus via l’API publique :

- FR/EN : AI Act, codes de conduite et de bonnes pratiques IA, Cyber Resilience Act, NIS2, Data Act.
- ES/DE : AI Act et codes de conduite et de bonnes pratiques IA.

Les dossiers `before` conservent les originaux ; `after` contient le texte prévu. Le manifeste associe les pages aux révisions de départ et aux empreintes du texte. Ces lots sont une archive de publication, pas un moyen de restaurer automatiquement une version ancienne. Toute nouvelle modification doit partir d’une lecture récente du wiki.

Chaque copie archivée propose `verify` (prévisualisation) et `verify-live` (comparaison aux pages publiées). Le mode `publish` est désactivé dans ce dépôt : les anciens scripts vérifiaient la révision avant écriture, mais sans protection atomique contre une modification concurrente entre la lecture et l’écriture. Un prochain outil de publication devra utiliser une protection atomique des conflits avant d’être activé. MediaWiki peut supprimer les sauts de ligne finaux ; la comparaison tolère uniquement cette normalisation.

Les contrôles de rendu vérifient les liens internes d’articles et les erreurs de parsing. Ils ne prouvent pas l’exactitude juridique des textes ni la réciprocité de tous les liens de langues.

## SEO : travaux préparés, non déployés

`operations/seo/` contient les propositions de correction : hreflang vers la langue courante, exclusions communes aux robots et génération horaire des sitemaps. Ces scripts ne doivent pas être lancés avant inspection de la configuration protégée actuelle et revue du plan de retour arrière.

La validation de syntaxe PHP seule ne suffit pas. Après déploiement, vérifier les réponses HTTP, les liens canoniques et hreflang, robots.txt et les dates de sitemap pour les cinq langues. Les liens réciproques entre traductions restent à compléter. Une meilleure indexabilité ne garantit pas le classement ni la citation par les moteurs d’IA.

## Données exclues

Ne pas committer LocalSettings.php, mots de passe, clés, fichiers d’environnement, exports SQL ou sauvegardes système. Utiliser l’API publique pour les exports éditoriaux. Les scripts de ce dépôt ne demandent aucun secret pour lire le wiki.

## GitHub et production

Aucun déploiement automatique n’est configuré. Mettre à jour GitHub et publier sur MediaWiki sont deux opérations distinctes. Après une publication, refaire un export public, vérifier ses empreintes et examiner le diff avant commit.
