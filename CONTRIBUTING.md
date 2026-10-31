# Contribuer au Wiki du numérique responsable

Les corrections, traductions et propositions de fiches sont les bienvenues. Le [wiki en ligne](https://fr.wiki.isit-europe.org/nr/Accueil) reste la référence éditoriale ; une modification acceptée sur GitHub n’y est pas publiée automatiquement.

## Par où commencer ?

1. **Cherchez d’abord** si le sujet existe déjà : index de la langue concernée dans le [README](README.md), puis barre de recherche des [issues](https://github.com/Institut-du-Numerique-Responsable/wiki-nr/issues).
2. Choisissez la méthode adaptée grâce au [tableau des méthodes](docs/contribuer-via-github.md#choisir-la-bonne-méthode) : issue, édition dans le navigateur (sans installation) ou Git.
3. Ouvrez une issue via les [formulaires dédiés](https://github.com/Institut-du-Numerique-Responsable/wiki-nr/issues/new/choose) (*Correction d’une fiche*, *Traduction*, *Nouvelle fiche*), ou proposez directement une pull request depuis le navigateur.
4. Suivez l’avancement avec les [étiquettes](https://github.com/Institut-du-Numerique-Responsable/wiki-nr/labels) (langue, type, statut). Les issues [`good first issue`](https://github.com/Institut-du-Numerique-Responsable/wiki-nr/labels/good%20first%20issue) sont idéales pour débuter.

## Signaler un contenu problématique

Une fiche contient une donnée personnelle, un contenu illicite ou une atteinte à des droits ? Ouvrez une issue en décrivant le problème **sans recopier la donnée ou le passage concerné**. Ne publiez jamais de donnée personnelle, d’information confidentielle, de clé ou de mot de passe — y compris dans une issue ou une pull request.

## Proposer une modification

Le [guide de contribution via GitHub](docs/contribuer-via-github.md) détaille chaque étape, depuis le navigateur ou avec Git.

1. Chercher la fiche dans l’index de sa langue, accessible depuis le README.
2. Ouvrir une issue pour signaler une erreur ou discuter d’un nouveau sujet. Indiquer le titre, la langue, le lien de la fiche et les sources utiles.
3. Pour proposer un texte, modifier le fichier `.wiki` dans une branche ou un fork, puis ouvrir une pull request. Décrire le changement et sa raison, avec les références utilisées.
4. Un mainteneur relit la proposition, vérifie les sources et compare la version actuelle du wiki avant toute publication. Après publication, il actualise l’export et son manifeste.

Pour une correction éditoriale, ne pas modifier à la main les numéros de révision, dates ou empreintes du manifeste afin de faire passer une vérification. Ces données décrivent le dernier export publié ; un texte proposé peut donc différer de son empreinte jusqu’à son intégration sur le wiki et au nouvel export.

## Qualité des fiches

- Expliquer le sujet dans une langue claire, avec des exemples utiles aux équipes informatiques. Privilégier la qualité à la quantité.
- Relier le sujet au numérique responsable : impacts environnementaux, accessibilité, inclusion, sécurité, résilience ou gouvernance selon sa pertinence.
- Appuyer les faits sur des sources identifiables. Privilégier les textes officiels, travaux scientifiques et publications originales ; préciser la date et le périmètre des chiffres.
- Pour une réglementation, distinguer entrée en vigueur, application et transposition nationale. Séparer obligations légales, recommandations et engagements volontaires.
- Éviter le discours commercial, les affirmations générales sans preuve et les liens ajoutés uniquement pour promouvoir un site.
- Respecter le format MediaWiki, vérifier les liens internes et conserver les références pertinentes.

## Traductions — contribuer dans une langue étrangère

Le wiki existe en français, anglais, espagnol, allemand et néerlandais. Contribuer dans une langue autre que le français suit le même cheminement qu’une correction (issue, édition navigateur ou Git), avec une exigence supplémentaire : la **relecture native**.

1. **Vérifier l’existant.** Cherchez la fiche dans l’index de la langue cible (liens « Consulter les contenus » dans le [README](README.md)). Si elle n’existe pas, la traduction part de la fiche française de référence.
2. **Ouvrir une issue** avec le formulaire *Traduction* : indiquez la langue cible, la fiche source et si vous êtes locuteur natif de cette langue. L’issue reçoit les étiquettes `langue : xx` et `traduction`.
3. **Proposer la traduction** dans `content/<langue>/<Titre>.wiki` (méthodes dans le [guide GitHub](docs/contribuer-via-github.md)), en conservant la syntaxe MediaWiki. Ne modifiez pas `content/manifest.json`.
4. **Relier les versions.** Ajoutez en fin de fiche traduite le lien interlangue vers la source (ex. `[[fr:Titre]]` sur la version anglaise) ; depuis la fiche source, complétez les liens vers les langues déjà disponibles.
5. **Relecture native.** La traduction reçoit l’étiquette `statut : relecture native` jusqu’à sa relecture par une personne dont c’est la langue maternelle ou principale. Cette relecture porte sur le sens, les nuances et les termes techniques ou juridiques — pas seulement sur la grammaire.

### Règles de traduction

- Traduire le **sens, les exemples et les nuances**, pas mot à mot ; adapter les exemples au contexte de la langue cible.
- Pour les termes techniques et juridiques, s’appuyer de préférence sur une **source officielle dans la langue cible** (texte traduit, vocabulaire officiel) ; sinon indiquer la langue de la source utilisée.
- Conserver les références telles quelles, avec leur formulation d’origine ; ne pas traduire un titre d’ouvrage cité sans conserver l’original.
- Signaler les écarts entre source et traduction qui impliqueraient une mise à jour des autres langues (issue ou commentaire de pull request).

L’usage d’un outil d’IA est possible comme brouillon, mais ne remplace pas la relecture humaine : la personne qui propose le texte vérifie chaque référence, chaque chiffre et la cohérence d’ensemble.

## Droits et échanges

En proposant un contenu original destiné au wiki, vous acceptez sa diffusion sous CC0 1.0, conformément à la [licence des contenus](docs/licensing.md). Ne soumettez que des textes que vous avez le droit de diffuser ainsi. Citer un rapport ne permet pas d’en reproduire librement des passages importants, ses tableaux ou ses illustrations.

Ne publier aucune donnée personnelle non nécessaire, information confidentielle, clé ou mot de passe. Dans les échanges, discuter les faits et les propositions avec respect ; les attaques personnelles et le harcèlement n’ont pas leur place.

## Outils techniques

Les changements de scripts doivent expliquer le comportement attendu et les vérifications effectuées. L’export doit rester lisible sans identifiants et conserver les révisions et empreintes des pages. Les outils de publication archivés sont désactivés ; voir [les règles d’exploitation](docs/operations.md).
