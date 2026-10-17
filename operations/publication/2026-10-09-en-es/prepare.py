"""Read-only preview and revision capture; refuses stale French source revisions."""
import hashlib
import json
import re
from check import request
from publish import ROOT,page
if __name__=='__main__':
    if (ROOT/'publication.json').exists(): raise SystemExit('Batch already prepared')
    items=json.loads((ROOT/'seed.json').read_text())
    (ROOT/'before').mkdir(exist_ok=True)
    planned={(p['language'],p['title']) for p in items}
    for index,item in enumerate(items):
        rev,actual=page(item['language'],item['title'])
        if rev!=item['base_revision']: raise SystemExit('Source revision changed: '+item['title'])
        text=(ROOT/item['file']).read_text()
        parsed=request(item['language'],action='parse',title=item['title'],text=text,prop='text|links|langlinks')['parse']
        missing={p['*'] for p in parsed['links'] if p['ns']==0 and 'exists' not in p and (item['language'],p['*']) not in planned}
        old=request(item['language'],action='parse',title=item['title'],text=actual,prop='links')['parse'] if actual else {'links':[]}
        old_missing={p['*'] for p in old['links'] if p['ns']==0 and 'exists' not in p}
        if missing-old_missing or re.search(r'class="[^"]*\b(?:error|mw-ext-cite-error)\b',parsed['text']['*']):
            raise SystemExit(('Preview failed',item['title'],missing-old_missing))
        (ROOT/'before'/(str(index)+'.wiki')).write_text(actual)
        item['sha256']=hashlib.sha256(text.encode()).hexdigest()
        print('Prepared:',item['language'],item['title'],rev,flush=True)
    (ROOT/'publication.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
