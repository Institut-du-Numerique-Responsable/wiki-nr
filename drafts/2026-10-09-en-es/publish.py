"""Publish the reviewed batch on the wiki server; uses native revision conflict protection."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
from check import request

ROOT=Path(__file__).resolve().parent

def page(lang,title):
    p=next(iter(request(lang,action='query',titles=title,prop='revisions',rvprop='ids|content',rvslots='main')['query']['pages'].values()))
    if 'missing' in p:
        return 0,''
    r=p['revisions'][0]
    return r['revid'],r['slots']['main']['*']

def same(actual,expected):
    return actual==expected or actual==expected.rstrip('\n')

def command(item,dry=False):
    args=['sudo','-n','-u','www-data2','env','SERVER_NAME=wiki.isit-europe.org',
          'HTTP_HOST='+item['language']+'.wiki.isit-europe.org','/usr/bin/php',
          str(ROOT/'safe-edit.php'),'--wiki='+item['language']+'_wiki','--base='+str(item['base_revision'])]
    if dry: args.append('--dry-run')
    return args+[item['title']]

if __name__=='__main__':
    if os.geteuid()!=0: raise SystemExit('Run this reviewed batch with sudo on the wiki server')
    manifest=json.loads((ROOT/'publication.json').read_text())
    pending=[]
    for item in manifest:
        text=(ROOT/item['file']).read_text()
        if hashlib.sha256(text.encode()).hexdigest()!=item['sha256']:
            raise SystemExit('Draft changed: '+item['title'])
        rev,actual=page(item['language'],item['title'])
        if same(actual,text): continue
        if rev!=item['base_revision']: raise SystemExit('Revision conflict: '+item['title'])
        subprocess.run(command(item,True),check=True)
        pending.append((item,text))
    for item,text in pending:
        subprocess.run(command(item),input=text.encode(),check=True)
        rev,actual=page(item['language'],item['title'])
        if not same(actual,text): raise SystemExit('Saved content differs: '+item['title'])
        print('Published and checked:',item['language'],item['title'],rev,flush=True)
    print('All batch contents are published and checked.')
