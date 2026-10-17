# Liens de langue manquants : lot du 17 octobre 2026

Statut : préparé et prévisualisé le 17 octobre 2026, **non publié**.

L’audit du 17 octobre 2026 a relevé 26 articles EN, ES ou DE sans aucun lien de langue alors que leur équivalent existe en français. Les pages françaises correspondantes n’avaient pas non plus de lien vers ces traductions. Ce lot ajoute les liens réciproques sur 52 pages réparties en 25 groupes ; il ne modifie pas le texte des fiches.

Pages modifiées :

- **DE** (1) : Digitale Gemeingüter
- **EN** (24) : AI governance, Algorithmic bias, Bilan Carbone, CSRD, Digital commons, Digital divide, Digital resilience, GR491, Generative AI, Greenwashing, Hallucination, Human for IT, ISO 14064, IT for Green, IT for Human, Inference, Jevons paradox, LLM, Prompt injection, RGAA, Reversibility, Robustness, Vendor lock-in, WCAG
- **ES** (2) : Bien común digital, Instituto de TI Responsable
- **FR** (25) : Biais algorithmique, Bilan Carbone, CSRD, Commun numérique, Fracture Numérique, GR491, Gouvernance de l'IA, Green Washing, Hallucination, Human for IT, IA générative, ISO 14064, IT for Green, IT for Human, Inférence, Institut du Numérique Responsable, LLM, Paradoxe de Jevons, Prompt injection, RGAA, Robustesse numérique, Résilience numérique, Réversibilité, Vendor lock-in, WCAG

Groupes à vérifier en relecture, car les titres diffèrent : Digital divide et Fracture Numérique, Greenwashing et Green Washing, Robustness et Robustesse numérique, Digital commons, Commun numérique, Bien común digital et Digitale Gemeingüter, Instituto de TI Responsable et Institut du Numérique Responsable.

`prepare.py` a relevé les révisions de départ et vérifié la prévisualisation de chaque page : aucune erreur de parsing, aucun nouveau lien rouge. Les révisions et empreintes sont dans `publication.json`, les originaux dans `before/`.

Publication sur le serveur, après relecture et fusion de la pull request (la résolution DNS du serveur doit fonctionner, le script relit l’API publique) :

```sh
sudo python3 /home/ggallon/wiki-drafts/2026-10-17-language-links/publish.py
```

Le script refuse de publier si une page a changé depuis la préparation. Après publication, refaire un export public, vérifier ses empreintes, déplacer ce lot dans `operations/publication/` et désactiver son mode `publish`.
