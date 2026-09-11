# Code map
README.md — repository scope, content format and usage.
content/manifest.json — public page metadata, revision IDs and hashes for five languages.
content/{fr,en,es,de,nl}/*.wiki — verbatim public article/category snapshots, named by page ID.
scripts/export_public.py — export(destination), paginated anonymous MediaWiki export.
scripts/verify_snapshot.py — verify(root), offline integrity and inventory checks.
operations/publication/ — reviewed EU article batches with revision guards and originals.
operations/seo/ — proposed server changes, not yet deployed or validated against current protected configuration.
docs/operations.md — publication boundaries and operational status.
