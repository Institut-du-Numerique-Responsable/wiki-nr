"""Export public article/category wikitext and provenance, without credentials."""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.parse
import urllib.request

LANGUAGES = ('fr', 'en', 'es', 'de', 'nl')

def export(destination):
    destination = Path(destination)
    if destination.exists():
        raise SystemExit('Choose a new destination; existing snapshots are never overwritten')
    destination.mkdir(parents=True)
    manifest = []
    for lang in LANGUAGES:
        directory = destination / lang
        directory.mkdir()
        for namespace in (0, 14):
            continuation = {}
            while True:
                params = dict(action='query', format='json', generator='allpages', gapnamespace=namespace,
                              gaplimit=50, prop='revisions', rvprop='ids|timestamp|content', rvslots='main', **continuation)
                request = urllib.request.Request('https://' + lang + '.wiki.isit-europe.org/api.php',
                    data=urllib.parse.urlencode(params).encode(), headers={'User-Agent': 'INR-Wiki-Public-Export/1.0'})
                with urllib.request.urlopen(request, timeout=60) as response:
                    result = json.load(response)
                if 'error' in result:
                    raise RuntimeError(result['error'])
                for page in result.get('query', {}).get('pages', {}).values():
                    revision = page['revisions'][0]
                    content = revision['slots']['main']['*'].encode('utf-8')
                    filename = str(page['pageid']) + '.wiki'
                    (directory / filename).write_bytes(content)
                    manifest.append(dict(language=lang, title=page['title'], pageid=page['pageid'],
                        namespace=page['ns'], revision=revision['revid'], timestamp=revision['timestamp'],
                        file=lang+'/'+filename, sha256=hashlib.sha256(content).hexdigest(),
                        url='https://'+lang+'.wiki.isit-europe.org/nr/'+urllib.parse.quote(page['title'].replace(' ', '_'), safe='')))
                if 'continue' not in result:
                    break
                continuation = result['continue']
        print(lang, sum(p['language']==lang for p in manifest), flush=True)
    (destination/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    print('Export complete:', len(manifest), flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination')
    export(parser.parse_args().destination)
