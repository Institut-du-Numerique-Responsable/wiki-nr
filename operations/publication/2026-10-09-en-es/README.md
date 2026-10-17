# Traductions anglaises et espagnoles — lot du 9 octobre 2026

Statut : publié et vérifié le 9 octobre 2026. Les douze révisions figurent dans `published.json` ; l’instantané `content/` est synchronisé.

Cinq nouvelles fiches, traduites depuis les fiches françaises lues le jour même : Agentic AI (EN), IA agéntica, GHG Protocol, Shadow AI et Low tech (ES). Les liens internes ne pointent que vers des fiches existantes ou vers des fiches de ce lot. Les notions sans fiche dans la langue cible (IA générative, inférence, RGPD, Bilan Carbone, ISO 14064, CSRD en espagnol) restent en texte simple.

Sept modifications FR/EN ajoutent les liens de langue réciproques : IA agentique, GHG Protocol, Shadow AI et Low Tech en français ; GHG Protocol, Shadow AI et Low tech en anglais. Shadow AI et Low tech existaient déjà en anglais sans lien avec la fiche française.

Les douze prévisualisations ont réussi. Les révisions de départ et empreintes sont dans `publication.json`, les originaux dans `before/`. Les contenus proposés relèvent de CC0 comme les contributions éditoriales au wiki.

Publication sur le serveur (la résolution DNS du serveur doit fonctionner, le script relit l’API publique) :

```sh
sudo python3 /home/ggallon/wiki-drafts/2026-10-09-en-es/publish.py
```

Le script contrôle les conflits de révision et relit chaque page enregistrée. En cas d’échec, il interrompt le lot ; une relance reconnaît les pages déjà publiées. Après publication, vérifier les douze pages et actualiser l’export GitHub.
