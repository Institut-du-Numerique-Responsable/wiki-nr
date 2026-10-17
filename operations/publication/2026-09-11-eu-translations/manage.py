import sys
mode=sys.argv[1]
if mode=='publish':
    raise SystemExit('Archived batch: publishing is disabled in this repository copy. Prepare a new reviewed batch with atomic edit-conflict protection.')
if not __debug__:
    raise SystemExit('Run without Python optimization; validation requires assertions.')
sys.argv[1]='library'
import base
sys.argv[1]=mode
import json,re,hashlib,os,subprocess
root=base.ROOT
(root/"preview").mkdir(exist_ok=True)
if mode=='prepare':
    assert not (root/'manifest.json').exists()
    for directory in ['before','after','preview']: (root/directory).mkdir(exist_ok=True)
    manifest=[]
    for name,item in json.loads((root/'articles.json').read_text()).items():
        titles={lang:item.get(lang+'_title',name) for lang in ['es','de']}
        for lang in ['es','de']:
            title=titles[lang]; rev,old=base.page(lang,title)
            cats=re.findall(r'\[\[(?:Category|Catégorie):[^\]]+\]\]',old)
            if not cats: cats=['[[Category:Inteligencia Artificial]]' if lang=='es' else '[[Category:Künstliche Intelligenz]]']
            links=re.findall(r'\[\[nl:[^\]]+\]\]',old)
            other='de' if lang=='es' else 'es'
            links.append('[['+other+':'+titles[other]+']]')
            fr_title='AI Act' if name=='AI Act' else 'Codes de conduite et de bonnes pratiques IA'
            links.extend(['[[fr:'+fr_title+']]','[[en:'+name+']]'])
            text=item[lang].rstrip()+'\n\n'+'\n'.join(cats+links)+'\n'
            stem=str(len(manifest))
            (root/'before'/(stem+'.wiki')).write_text(old)
            (root/'after'/(stem+'.wiki')).write_text(text)
            manifest.append(dict(lang=lang,title=title,stem=stem,base_revid=rev,sha256=hashlib.sha256(text.encode()).hexdigest()))
    (root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print('Prepared',len(manifest))
else:
    manifest=json.loads((root/'manifest.json').read_text())
    planned={(i['lang'],i['title']) for i in manifest}
    for item in manifest:
        lang,title,stem=item['lang'],item['title'],item['stem']
        text=(root/'after'/(stem+'.wiki')).read_text()
        assert hashlib.sha256(text.encode()).hexdigest()==item['sha256']
        rev,actual=base.page(lang,title)
        if mode=='publish':
            assert os.geteuid()==0
            assert rev==item['base_revid'] or base.same(actual,text),(lang,title,'Concurrent edit')
            if not base.same(actual,text):
                subprocess.run(['sudo','-n','-u','www-data2','env','SERVER_NAME=wiki.isit-europe.org','HTTP_HOST='+lang+'.wiki.isit-europe.org','/usr/bin/php','/applis/wiki/www/maintenance/run.php','edit','--wiki='+lang+'_wiki','--nocreate' if item['base_revid'] else '--createonly','--summary=Document EU digital regulation and practical responsible IT implications with official sources',title],input=text.encode(),check=True)
            rev,actual=base.page(lang,title)
        if mode in ['publish','verify-live']: assert base.same(actual,text),(lang,title,'Saved content differs')
        parsed=base.request(lang,action='parse',title=title,text=text,prop='text|links|langlinks|externallinks')['parse']
        missing={x['*'] for x in parsed['links'] if x['ns']==0 and 'exists' not in x}
        if mode!='verify-live': missing={t for t in missing if (lang,t) not in planned}
        assert not missing,(lang,title,missing)
        assert not re.search(r'class="[^"]*\b(?:error|mw-ext-cite-error)\b',parsed['text']['*'])
        assert parsed['langlinks'],(lang,title,'No language links')
        (root/'preview'/(stem+'.html')).write_text(parsed['text']['*'])
        print(mode,lang,title,rev,flush=True)
