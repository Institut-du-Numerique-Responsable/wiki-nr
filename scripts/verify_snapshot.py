"""Check exported files against their manifest; no network or credentials needed."""
import hashlib
import json
from pathlib import Path
import sys

def verify(root):
    root=Path(root).resolve()
    records=json.loads((root/'manifest.json').read_text())
    seen=set()
    for item in records:
        relative=Path(item['file'])
        assert not relative.is_absolute() and '..' not in relative.parts, item['file']
        assert relative.parts[0]==item['language'], item['file']
        assert item['file'] not in seen, item['file']
        seen.add(item['file'])
        content=(root/relative).read_bytes()
        content.decode('utf-8')
        assert hashlib.sha256(content).hexdigest()==item['sha256'], item['file']
        assert item['revision']>0 and item['pageid']>0
    assert seen=={str(p.relative_to(root)) for p in root.glob('*/*.wiki')}
    assert {i['language'] for i in records}=={'fr','en','es','de','nl'}
    print('Verified',len(records),'pages across five languages')

if __name__=='__main__':
    verify(sys.argv[1] if len(sys.argv)>1 else 'content')
