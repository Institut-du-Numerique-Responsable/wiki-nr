# Traductions EN et ES proposées le 11 septembre 2026

Statut : publié et vérifié le 11 septembre 2026. Les pages à jour figurent dans `content/` ; ce dossier conserve le lot et ses sources de départ.

| Source française | English | Español |
| --- | --- | --- |
| Dette technique | [Technical debt](en/Technical%20debt.wiki) | [Deuda técnica](es/Deuda%20t%C3%A9cnica.wiki) |
| Coût total de possession | [Total cost of ownership](en/Total%20cost%20of%20ownership.wiki) | [Coste total de propiedad](es/Coste%20total%20de%20propiedad.wiki) |
| Service numérique | [Digital service](en/Digital%20service.wiki) | [Servicio digital](es/Servicio%20digital.wiki) |

Traductions adaptées depuis les révisions françaises conservées dans `content/manifest.json`. Références vérifiées le 11 septembre 2026 : Software Engineering Institute, Commission européenne et Mission interministérielle Numérique écoresponsable.

Précisions éditoriales : la dette technique n’augmente pas systématiquement la consommation ; le TCO est un indicateur financier et ne prouve pas une division proportionnelle des émissions. Des corrections des sources françaises sont incluses dans ce lot.

`python3 check.py` vérifie l’absence des titres proposés et leur rendu via l’API publique. Ce script ne publie rien. Après publication, ajouter les liens réciproques aux fiches françaises et refaire l’export GitHub. Les textes proposés relèvent de la même licence CC0 que les contributions éditoriales du wiki.

## Corrections françaises proposées

- [Dette technique](fr/Dette%20technique.wiki) : distinguer maintenabilité et consommation, ajouter une méthode de priorisation et un exemple NR.
- [Coût total de possession](fr/Co%C3%BBt%20total%20de%20possession.wiki) : retirer la baisse automatique des coûts et émissions, expliciter le périmètre et les hypothèses.

Les corrections françaises et les liens de langues sont publiés ; voir `published.json` pour les révisions vérifiées.

## Lot préparé pour publication

Neuf changements : six créations EN/ES, deux corrections de fond FR et les liens de langues de la fiche française « Service numérique ». `publication.json` contient les révisions vérifiées et les empreintes ; `before/` conserve les originaux.

Commande sur le serveur :

```sh
sudo python3 /home/ggallon/wiki-drafts/2026-09-11-en-es/publish.py
```

La commande vérifie toutes les révisions avant de commencer. Chaque écriture utilise `PageUpdater::hasEditConflict` puis `saveRevision`, dont le mécanisme compare-and-swap refuse une modification concurrente. Chaque contenu enregistré est relu via l’API publique. Une erreur interrompt le lot ; les pages déjà publiées sont conservées et reconnues lors d’une relance. Le lot n’est pas une transaction globale.

Validation avant publication : neuf prévisualisations, comparaison des sources FR et syntaxe PHP vérifiées ; revue de code effectuée. Les neuf contenus enregistrés ont été relus après exécution réelle de la publication avec sudo.
