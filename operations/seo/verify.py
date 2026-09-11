"""Read-only checks of public SEO metadata, crawl rules and sitemap XML."""
import datetime,gzip,json,re,urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

class Head(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.meta=[]
    def handle_starttag(self,tag,attrs):
        if tag=='link':self.links.append(dict(attrs))
        if tag=='meta':self.meta.append(dict(attrs))

def fetch(url):
    with urllib.request.urlopen(url,timeout=60) as r:return r.read(),dict(r.headers)

def verify():
    report=[];ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for lang,title in [('fr','Accueil'),('en','Sustainable_IT'),('de','Green_IT'),('es','TI_Responsable'),('nl','Duurzame_IT')]:
        host='https://'+lang+'.wiki.isit-europe.org';url=host+'/nr/'+title
        html,_=fetch(url);head=Head();head.feed(html.decode())
        if not any(l.get('rel')=='canonical' and l.get('href')==url for l in head.links):raise RuntimeError(('canonical',lang))
        if not any(l.get('hreflang')==lang and l.get('href')==url for l in head.links):raise RuntimeError(('self language',lang))
        if any('noindex' in m.get('content','') for m in head.meta if m.get('name')=='robots'):raise RuntimeError(('noindex',lang))
        robots,_=fetch(host+'/robots.txt');robots=robots.decode()
        lines=[l.strip() for l in robots.splitlines() if l.strip() and not l.startswith('#')]
        first_rule=next(i for i,l in enumerate(lines) if l.startswith(('Allow:','Disallow:')))
        if any(l.startswith('User-agent:') for l in lines[first_rule:]):raise RuntimeError(('separate crawler group',lang))
        for rule in ['Disallow: /api.php','Disallow: /*?action=','Disallow: /*&action=']:
            if rule not in lines:raise RuntimeError(('missing rule',lang,rule))
        sitemap=re.search(r'Sitemap: (\S+)',robots)[1]
        xml,headers=fetch(sitemap);index=ET.fromstring(xml);count=0
        for loc in index.findall('.//s:loc',ns):
            if not loc.text.startswith(host+'/sitemap/'):raise RuntimeError(('wrong sitemap host',lang))
            data,_=fetch(loc.text)
            if data[:2]==b'\x1f\x8b':data=gzip.decompress(data)
            count+=len(ET.fromstring(data).findall('s:url',ns))
        if count==0:raise RuntimeError(('empty sitemap',lang))
        report.append(dict(language=lang,checked_page=url,sitemap=sitemap,urls=count,
            sitemap_dates=[e.text for e in index.findall('.//s:lastmod',ns)],cache_control=headers.get('Cache-Control',headers.get('cache-control'))))
    return dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),sites=report)

if __name__=='__main__':print(json.dumps(verify(),indent=2,ensure_ascii=False))
