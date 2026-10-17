"""Read-only public MediaWiki API helper for the German enrichment batch."""
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

