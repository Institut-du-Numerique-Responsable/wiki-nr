# Contribuer via GitHub

Ce guide explique comment proposer une correction, une traduction ou une nouvelle fiche au Wiki du numérique responsable depuis GitHub. Vous n’avez besoin que d’un compte GitHub gratuit. Aucune installation n’est nécessaire pour les deux premières méthodes.

Le wiki en ligne reste la référence. Une contribution acceptée sur GitHub est relue, puis publiée sur le wiki par un mainteneur. Avant d’écrire, lisez les [règles de qualité des fiches](../CONTRIBUTING.md#qualité-des-fiches).

## Choisir la bonne méthode

| Vous voulez… | Méthode | Niveau |
|---|---|---|
| Signaler une erreur, un lien cassé, une source datée | [Ouvrir une issue](#1-signaler-un-problème-avec-une-issue) | Aucune connaissance technique |
| Corriger ou compléter une fiche existante | [Modifier dans le navigateur](#2-modifier-une-fiche-dans-le-navigateur) | Savoir lire du wikitexte simple |
| Traduire une fiche ou en proposer une nouvelle | [Modifier dans le navigateur](#2-modifier-une-fiche-dans-le-navigateur) ou [avec Git](#3-contribuer-avec-git) | Wikitexte |
| Modifier les scripts d’export ou de contrôle | [Contribuer avec Git](#3-contribuer-avec-git) | Python |

## 1. Signaler un problème avec une issue

1. Ouvrez l’onglet [**Issues**](https://github.com/Institut-du-Numerique-Responsable/wiki-nr/issues), puis cliquez sur **New issue**.
2. Choisissez un formulaire : *Correction d’une fiche*, *Traduction* ou *Nouvelle fiche*.
3. Remplissez les champs : langue, titre ou lien de la fiche, problème constaté, sources.
4. Cliquez sur **Create**. Le formulaire ajoute les étiquettes de type et de statut ; un mainteneur ajoute la langue et vous répond dans l’issue.

Avant d’ouvrir une issue, cherchez si le sujet existe déjà avec la barre de recherche des issues.

## 2. Modifier une fiche dans le navigateur

GitHub crée pour vous une copie du dépôt (un *fork*) et la demande de modification (une *pull request*).

1. **Trouver la fiche.** Ouvrez l’index de votre langue : [Français](../content/fr/README.md), [English](../content/en/README.md), [Español](../content/es/README.md), [Deutsch](../content/de/README.md), [Nederlands](../content/nl/README.md). Cliquez sur le titre : la fiche est un fichier `.wiki`.
2. **Ouvrir l’éditeur.** Cliquez sur l’icône crayon ✏️ (*Edit this file*) en haut à droite du fichier. À la première modification, GitHub propose de créer votre fork : acceptez avec **Fork this repository**.
3. **Modifier le texte.** Gardez la syntaxe MediaWiki :
   - `'''gras'''`, `''italique''` ;
   - `== Titre de section ==` ;
   - `[[Titre d’une autre fiche]]` ou `[[Titre|texte affiché]]` pour un lien interne ;
   - `<ref>Auteur, titre, éditeur, date. URL</ref>` pour une source ;
   - `[[en:Title]]` en fin de page pour relier la traduction anglaise.
4. **Enregistrer.** Cliquez sur **Commit changes…**. Écrivez un message court qui dit ce que vous changez, par exemple « Corriger la date d’application de NIS2 ». Choisissez **Create a new branch** si on vous le propose, puis **Propose changes**.
5. **Ouvrir la pull request.** Sur la page suivante, cliquez sur **Create pull request**. Remplissez le modèle : fiche concernée, raison du changement, sources. Validez.

Pour **créer une nouvelle fiche** ou une traduction, ouvrez le dossier de la langue dans `content/`, cliquez sur **Add file → Create new file**, nommez le fichier `<Titre de la fiche>.wiki`, puis suivez les étapes 3 à 5. Ajoutez en bas de la fiche les liens vers ses versions dans les autres langues.

Ne modifiez pas `content/manifest.json` : il décrit le dernier export publié et le mainteneur l’actualise après publication.

## 3. Contribuer avec Git

```sh
gh repo fork Institut-du-Numerique-Responsable/wiki-nr --clone
cd wiki-nr
git switch -c correction/nis2-date
# modifier content/<langue>/<titre>.wiki
git commit -am "Corriger la date d'application de NIS2"
git push -u origin correction/nis2-date
gh pr create --fill
```

Pour un changement de script, vérifiez que l’instantané reste valide (Python 3, sans dépendance) :

```sh
python3 scripts/verify_snapshot.py content
```

Une fiche modifiée ne correspond plus à son empreinte du manifeste : c’est normal tant qu’elle n’est pas publiée. Ne corrigez pas l’empreinte à la main.

## 4. Après l’envoi

1. Un mainteneur relit la proposition et vérifie les sources. Il peut demander des changements dans la pull request : vous les faites dans la même branche, la pull request se met à jour.
2. Une traduction reçoit l’étiquette `statut : relecture native` jusqu’à sa relecture par une personne dont c’est la langue.
3. Une fois acceptée, la proposition reçoit `statut : prêt à publier`. Le mainteneur la publie sur le wiki, refait l’export public, puis ferme l’issue avec `statut : publié`.

## Étiquettes

Les étiquettes permettent de trouver une tâche et de suivre son avancement.

| Famille | Étiquettes | Usage |
|---|---|---|
| Langue | `langue : fr`, `langue : en`, `langue : es`, `langue : de`, `langue : nl` | Langue de la fiche concernée |
| Type | `correction`, `traduction`, `nouvelle fiche`, `sources et chiffres`, `réglementation`, `liens de langue`, `outillage`, `seo` | Nature de la contribution |
| Statut | `statut : à relire`, `statut : relecture native`, `statut : prêt à publier`, `statut : publié` | Avancement |
| Accueil | `good first issue`, `help wanted` | Tâches pour débuter, besoin d’aide |

Pour commencer, filtrez les issues [`good first issue`](https://github.com/Institut-du-Numerique-Responsable/wiki-nr/labels/good%20first%20issue) ou celles de votre langue.

## Droits

En proposant un texte original, vous acceptez sa diffusion sous CC0 1.0, comme le reste du wiki. Voir [Droits et échanges](../CONTRIBUTING.md#droits-et-échanges) et la [licence des contenus](licensing.md).
