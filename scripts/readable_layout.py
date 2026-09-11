"""Give snapshot files readable names and generate linked language indexes."""
import json
from pathlib import Path
import re
import shutil
import tempfile
import unicodedata
from urllib.parse import quote

LANGUAGE_NAMES = {'fr':'Français', 'en':'English', 'es':'Español', 'de':'Deutsch', 'nl':'Nederlands'}

def filenames(records):
    used=set()
    result={}
    for item in sorted(records, key=lambda p:(p['language'],p['pageid'])):
        name=unicodedata.normalize('NFC',item['title'])
        name=re.sub(r'[<>:"/\\|?*\x00-\x1f]', '-', name).strip(' .') or 'Page'
        while len(name.encode('utf-8'))>180:
            name=name[:-1]
        if name.split('.')[0].upper() in {'CON','PRN','AUX','NUL',*(f'COM{i}' for i in range(1,10)),*(f'LPT{i}' for i in range(1,10))}:
            name='Page - '+name
        candidate=name+'.wiki'
        while (item['language'],candidate.casefold()) in used:
            name+=' - '+str(item['pageid'])
            candidate=name+'.wiki'
        used.add((item['language'],candidate.casefold()))
        result[item['language'],item['pageid']]=item['language']+'/'+candidate
    return result

def _organize(root):
    root=Path(root)
    records=json.loads((root/'manifest.json').read_text())
    targets=filenames(records)
    # Read all originals before changing paths, including case-only renames.
    payloads=[(item,(root/item['file']).read_bytes()) for item in records]
    for item,_ in payloads:
        (root/item['file']).unlink()
    for item,content in payloads:
        item['file']=targets[item['language'],item['pageid']]
        (root/item['file']).write_bytes(content)
    (root/'manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    for lang,label in LANGUAGE_NAMES.items():
        lines=['# '+label,'','Articles et catégories du wiki. Chaque entrée donne accès au fichier et à la page publiée.','']
        for item in sorted((p for p in records if p['language']==lang),key=lambda p:p['title'].casefold()):
            title=item['title'].replace('\\','\\\\').replace('[','\\[').replace(']','\\]')
            lines.append('- ['+title+']('+quote(Path(item['file']).name,safe='')+') · [wiki]('+item['url']+')')
        (root/lang/'README.md').write_text('\n'.join(lines)+'\n')

def organize(root):
    root=Path(root).resolve()
    # Build a full replacement first. Keep the original recoverable until swap succeeds.
    workspace=Path(tempfile.mkdtemp(prefix='.wiki-layout-',dir=root.parent))
    staged=workspace/'replacement'
    backup=workspace/'original'
    try:
        shutil.copytree(root,staged)
        _organize(staged)
        from verify_snapshot import verify
        verify(staged)
        root.rename(backup)
        try:
            staged.rename(root)
        except BaseException:
            backup.rename(root)
            raise
    except BaseException:
        print('Layout staging retained for recovery:',workspace)
        raise
    else:
        shutil.rmtree(workspace)

if __name__=='__main__':
    import sys
    organize(sys.argv[1] if len(sys.argv)>1 else 'content')
