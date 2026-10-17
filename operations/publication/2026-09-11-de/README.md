# Enrichissement allemand — 11 septembre 2026

Statut : publié et vérifié le 11 septembre 2026. L’instantané `content/` contient les quatre fiches actualisées ; voir `published.json`.

- [Green IT](de/Green%20IT.wiki) : cycle de vie, achats et logiciels, exemple de consolidation, liens avec sécurité et accessibilité.
- [Digitale Suffizienz](de/Digitale%20Suffizienz.wiki) : besoins, conservation des données, effets rebond et limites de la réduction des ressources.
- [Digitale Barrierefreiheit](de/Digitale%20Barrierefreiheit.wiki) : vérifications humaines et automatiques, parcours complets, articulation avec l’écoconception et périmètre du BFSG.
- [Rechenzentrum](de/Rechenzentrum.wiki) : correction du calcul PUE, limites des indicateurs, cloud et décisions d’exploitation.

Sources : Umweltbundesamt, Bundesfachstelle Barrierefreiheit et W3C WAI. Liens internes renforcés, liens de langues conservés. Les données chiffrées non étayées et les généralisations ont été corrigées. Les contenus éditoriaux proposés relèvent de CC0, comme les contributions au wiki.

Les quatre sources allemandes correspondent aux révisions de départ ; le rendu ne présente pas d’erreur de parsing ni de nouveau lien d’article cassé. `before/` conserve les textes originaux, `publication.json` les révisions et empreintes.

Sur le serveur :

```sh
sudo python3 /home/ggallon/wiki-drafts/2026-09-11-de/publish.py
```

Le script vérifie toutes les révisions avant écriture puis utilise la protection native contre les conflits MediaWiki pour chaque page. Il relit chaque contenu enregistré. Un échec interrompt le lot ; une relance reconnaît les pages déjà publiées. Le lot ne constitue pas une transaction globale. Les quatre contenus enregistrés ont été relus après exécution réelle de la publication avec sudo.

Après publication, refaire l’export du wiki pour actualiser `content/` et son manifeste. Ne pas présenter ces brouillons comme déjà publiés.
