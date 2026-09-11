"""Install narrow SEO fixes after backing up the current server configuration."""
from pathlib import Path
import datetime
import os
import shutil
import subprocess

assert os.geteuid() == 0, 'Run with sudo'
root = Path('/applis/wiki/www')
backup = Path('/home/ggallon/wiki-seo-20260911/backups') / datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
backup.mkdir(parents=True)
settings = root / 'LocalSettings.php'
original = settings.read_text()
anchor = '\t// liens de langue -> hreflang, que MediaWiki n emet pas de lui-meme'
assert original.count(anchor) == 1, 'Inspect the current hook before changing it'
snippet = '''\t// SEO: include this language in the alternate-language cluster.
\tif ( $title->getNamespace() === NS_MAIN && $title->exists() ) {
\t\t$out->addLink( [
\t\t\t'rel' => 'alternate',
\t\t\t'hreflang' => $conf->get( 'LanguageCode' ),
\t\t\t'href' => $title->getFullURL(),
\t\t] );
\t}

'''
assert '// SEO: include this language' not in original, 'Already installed'
shutil.copy2(settings, backup / settings.name)
candidate = settings.with_name('LocalSettings.seo-candidate.php')
shutil.copy2(settings,candidate)
candidate.write_text(original.replace(anchor,snippet+anchor))
subprocess.run(['/usr/bin/php','-l',str(candidate)],check=True)
os.chown(candidate,settings.stat().st_uid,settings.stat().st_gid)
os.replace(candidate,settings)

for lang in ['fr','en','es','de','nl']:
    path = root / ('robots_' + lang + '.txt')
    old = path.read_text()
    shutil.copy2(path,backup / path.name)
    # Apply the existing public-content exclusions to every named crawler.
    agents = list(dict.fromkeys(line for line in old.splitlines() if line.lower().startswith('user-agent:')))
    first = old.split('User-agent: *',1)[1].split('User-agent:',1)[0]
    rules = [line for line in first.splitlines() if line.startswith(('Disallow:','Allow:','Sitemap:'))]
    for key in ['action','oldid','diff','printable','curid','redirect']:
        rules.append('Disallow: /*&' + key + '=')
    path.write_text('# Public articles remain crawlable; service URLs are excluded for all crawlers.\n' + '\n'.join(agents) + '\n\n' + '\n'.join(dict.fromkeys(rules)) + '\n')

cron = Path('/etc/cron.d/wiki-sitemap')
shutil.copy2(cron,backup / 'wiki-sitemap.cron')
runner = Path('/usr/local/bin/wiki-refresh-sitemaps')
if runner.exists():
    shutil.copy2(runner,backup / runner.name)
shutil.copy2(Path(__file__).with_name('refresh-sitemaps.sh'),runner)
runner.chmod(0o755)
cron.write_text('SHELL=/bin/bash\nPATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin\n# Refresh each hour; flock prevents overlapping runs.\n17 * * * * www-data2 /usr/local/bin/wiki-refresh-sitemaps\n')
cron.chmod(0o644)
print('Configuration installed. Backups:',backup)
subprocess.run(['sudo','-n','-u','www-data2',str(runner)],check=True)
