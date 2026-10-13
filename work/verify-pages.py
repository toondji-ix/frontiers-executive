from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

root = Path('outputs/frontiers/dist')
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.path=path; self.refs=[]; self.ids=set(); self.images=0
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        for attribute in ('href','src'):
            if attribute in attrs: self.refs.append(attrs[attribute])
        if tag=='img': self.images+=1

pages={}
for path in root.glob('*.html'):
    page=Page(path); page.feed(path.read_text(encoding='utf-8-sig')); pages[path.name]=page
failures=[]
for name,page in pages.items():
    for ref in page.refs:
        url=urlsplit(ref)
        if url.scheme or url.netloc: continue
        target=unquote(url.path) or name
        file=root/target
        if not file.is_file() or file.stat().st_size==0: failures.append(f'{name}: missing {target}')
        if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids: failures.append(f'{name}: missing anchor {target}#{url.fragment}')
    print(f'{name}: {page.images} images; local routes and resources checked')
if failures: raise SystemExit('\n'.join(failures))
print('PASS: all local routes, image files, script/style files and anchors resolve.')
