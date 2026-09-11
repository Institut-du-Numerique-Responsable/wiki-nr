# Liens multilingues — 11 septembre 2026

Statut : 19 corrections publiées et vérifiées le 11 septembre 2026. Les révisions figurent dans `published.json` ; l’instantané GitHub et les sitemaps sont actualisés.

L’audit des liens de langue explicites des articles du dernier export a identifié 17 pages avec des liens réciproques incomplets. Aucun lien déclaré ne pointait vers une cible absente, et aucun groupe relié n’avait plusieurs articles canoniques d’une même langue. Les redirections connues ont été suivies pour identifier les cibles.

Les corrections complètent les groupes AI Act, codes de conduite et dix notions d’IA. Deux liens FR/EN GHG Protocol ont été ajoutés après vérification éditoriale de leur correspondance. Cet audit ne détecte pas toutes les traductions qui ne déclarent aucun lien entre elles, ni les liens générés par des modèles.

Les 19 textes conservent le corps des articles. Les prévisualisations ne présentent pas de nouveau lien interne cassé ; les révisions et empreintes sont dans `publication.json`, les originaux dans `before/`.

Sur le serveur :

```sh
sudo python3 /home/ggallon/wiki-drafts/2026-09-11-language-links/publish.py
```

Le script contrôle les conflits et relit chaque texte après écriture. Une erreur interrompt le lot sans annuler les pages déjà enregistrées ; une relance les reconnaît. Après publication, vérifier les liens hreflang publics et actualiser l’export GitHub.
