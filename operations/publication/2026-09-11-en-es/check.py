"""Preview six proposed translations against the public wiki; never writes to it."""
import json
from pathlib import Path
import re
import urllib.parse
import urllib.request

ROOT=Path(__file__).resolve().parent

def request(lang,**params):
    with urllib.request.urlopen('https://'+lang+'.wiki.isit-europe.org/api.php',data=urllib.parse.urlencode(dict(params,format='json')).encode(),timeout=60) as response:
        result=json.load(response)
    if 'error' in result:
        raise RuntimeError(result['error'])
    return result

if __name__=='__main__':
    for lang in ['en','es']:
        for file in sorted((ROOT/lang).glob('*.wiki')):
            title=file.stem
            page=next(iter(request(lang,action='query',titles=title)['query']['pages'].values()))
            if 'missing' not in page:
                raise RuntimeError(('Existing page: review before publishing',lang,title))
            parsed=request(lang,action='parse',title=title,text=file.read_text(),prop='text|links|langlinks|categories')['parse']
            missing=[p['*'] for p in parsed['links'] if p['ns']==0 and 'exists' not in p]
            if missing or re.search(r'class="[^"]*\b(?:error|mw-ext-cite-error)\b',parsed['text']['*']):
                raise RuntimeError((lang,title,missing))
            print('Preview OK:',lang,title,flush=True)
