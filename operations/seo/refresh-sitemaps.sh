#!/bin/bash
set -euo pipefail
wiki_root=/applis/wiki/www
exec 9>"$wiki_root/sitemap/.refresh.lock"
flock -n 9 || exit 0
staging=$(mktemp -d "$wiki_root/sitemap/.build.XXXXXX")
trap 'rmdir "$staging" 2>/dev/null || true' EXIT
for lang in fr en es de nl; do
    SERVER_NAME=wiki.isit-europe.org HTTP_HOST="$lang.wiki.isit-europe.org" \
      /usr/bin/php "$wiki_root/maintenance/run.php" generateSitemap \
      --wiki="${lang}_wiki" --fspath="$staging/" --urlpath=/sitemap/ \
      --server="https://${lang}.wiki.isit-europe.org" --skip-redirects --quiet
done
# Replace complete data files before their indexes; never serve partial XML.
for file in "$staging"/*.xml.gz; do mv "$file" "$wiki_root/sitemap/"; done
for file in "$staging"/*.xml; do mv "$file" "$wiki_root/sitemap/"; done
