# Deuxième enrichissement allemand — 11 septembre 2026

Statut : préparé et prévisualisé, non publié. L’instantané `content/` reste la version publiée.

- [CO₂-Fußabdruck](de/CO%E2%82%82-Fu%C3%9Fabdruck.wiki) : distinction entreprise/produit, scopes appliqués à l’IT, GHG Protocol ICT Sector Guidance, données et incertitudes.
- [Ökodesign](de/%C3%96kodesign.wiki) : besoin, compatibilité avec les équipements, RGESN, exemple de portail et mesure des résultats.
- [Verantwortungsvolle KI](de/Verantwortungsvolle%20KI.wiki) : charte INR conservée, choix du cas d’usage, tests, cycle de vie et responsabilités.

Sources primaires consultées : GHG Protocol, Umweltbundesamt, RGESN et charte INR/ISIT. Liens de langues conservés. Les trois rendus et leurs révisions de départ ont été vérifiés ; aucun nouveau lien d’article cassé. Les textes proposés suivent la licence CC0 du wiki.

Publication sur le serveur :

```sh
sudo python3 /home/ggallon/wiki-drafts/2026-09-11-de-2/publish.py
```

Le script relit les révisions, protège chaque écriture contre les modifications concurrentes et vérifie le contenu enregistré. Une erreur interrompt le lot ; une relance reconnaît les pages déjà publiées. Après publication, actualiser l’export GitHub. Les originaux figurent dans `before/` et les empreintes dans `publication.json`.
