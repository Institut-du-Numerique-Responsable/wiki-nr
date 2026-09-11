# Wiki du numérique responsable

Sources publiques du wiki de l’Institut du Numérique Responsable, en français, anglais, espagnol, allemand et néerlandais.

Le wiki en ligne reste la référence éditoriale. Ce dépôt conserve un instantané de ses articles et catégories, les outils d’export et les lots de publication documentés. Un push GitHub ne modifie pas le wiki.

## Consulter les contenus

Les fichiers `content/<langue>/<titre>.wiki` contiennent le wikitexte original. `content/manifest.json` associe chaque fichier au titre, à l’URL publique, au numéro de révision, à la date de modification et à une empreinte SHA-256. Les noms reprennent les titres. Les caractères incompatibles avec les chemins sont remplacés ; un identifiant départage les éventuelles collisions. Les identifiants MediaWiki restent dans le manifeste.

Parcourir les fiches : [Français](content/fr/README.md) · [English](content/en/README.md) · [Español](content/es/README.md) · [Deutsch](content/de/README.md) · [Nederlands](content/nl/README.md).

Les exports incluent les redirections et les catégories, mais pas les historiques, comptes, médias binaires, modèles ou configurations du serveur. Ils ne constituent donc pas une sauvegarde complète de MediaWiki.

## Vérifier et actualiser

Python 3, sans dépendance supplémentaire :

```sh
python3 scripts/verify_snapshot.py content
python3 scripts/export_public.py /tmp/wiki-nr-new-snapshot
python3 scripts/verify_snapshot.py /tmp/wiki-nr-new-snapshot
```

Choisir un nouveau répertoire pour chaque export. Comparer les manifestes et les changements avant de remplacer l’instantané suivi dans Git. Un export interrompu est incomplet et ne doit pas être intégré.

## Publication et exploitation

Voir [la procédure](docs/operations.md). Les lots publiés sont archivés avec leurs outils de lecture ; leur mode d’écriture est désactivé dans cette copie. Aucun outil de publication n’est exécuté par GitHub Actions.

Les contenus conservent les références et le régime de réutilisation indiqués par le wiki et les sources citées. Ce dépôt ne concède pas de droits supplémentaires sur les rapports externes, marques ou illustrations.
