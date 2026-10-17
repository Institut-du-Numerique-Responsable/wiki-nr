import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unicodedata
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
TITLES = {'fr': 'Cybersécurité', 'en': 'Cybersecurity', 'es': 'Ciberseguridad', 'de': 'Cybersicherheit', 'nl': 'Cyberbeveiliging'}
HUBS = {'fr': 'Numérique Responsable', 'en': 'Sustainable IT', 'es': 'TI Responsable', 'de': 'Verantwortungsvolle Digitalisierung', 'nl': 'Duurzame IT'}

def request(lang, **params):
    data = urllib.parse.urlencode(dict(params, format='json')).encode()
    with urllib.request.urlopen('https://' + lang + '.wiki.isit-europe.org/api.php', data=data, timeout=60) as response:
        result = json.load(response)
    if 'error' in result:
        raise RuntimeError(result['error'])
    return result

def page(lang, title):
    result = next(iter(request(lang, action='query', titles=title, prop='revisions', rvprop='ids|content', rvslots='main')['query']['pages'].values()))
    if 'missing' in result:
        return 0, ''
    rev = result['revisions'][0]
    return rev['revid'], rev['slots']['main']['*']

def same(actual, expected):
    return actual == expected or actual == expected.rstrip('\n')

def split(text):
    found = re.search(r'\[\[(?:Category|Catégorie|Kategorie|Categoría|Categorie):', text)
    return (text[:found.start()].rstrip(), text[found.start():]) if found else (text.rstrip(), '')

