import json, html, re
from pathlib import Path
from urllib.parse import quote

root = Path('outputs/frontiers/dist')
data = json.loads(Path('work/page-data.json').read_text(encoding='utf-8'))
home = (root / 'index.html').read_text(encoding='utf-8')
header = re.search(r'<header>[\s\S]*?</header>', home).group()
footer = re.search(r'<footer>[\s\S]*?</footer>', home).group()
routes = {'#home':'index.html', '#about':'about.html', '#programmes':'services.html', '#contact':'contact.html'}
def route_links(text):
    for old,new in routes.items(): text = text.replace(f'href="{old}"', f'href="{new}"')
    return text
header, footer = route_links(header), route_links(footer)
def escape(value): return html.escape(value)
def p(value, cls=''): return f'<p class="{cls}">{escape(value)}</p>'
def image(name, alt, eager=False):
    return f'<img src="assets/{name}.png" alt="{escape(alt)}" loading="{"eager" if eager else "lazy"}">'
def button(label, url, cls='dark'): return f'<a class="button {cls}" href="{escape(url)}">{escape(label)}</a>'
def enquiry(name): return 'contact.html?interest='+quote(name)+'#enquiry'
def benefits(values): return '<ul class="benefits">'+''.join(f'<li>{escape(v)}</li>' for v in values)+'</ul>'
def heading(label,title,center=False):
    return f'<div class="page-section-heading{" centered" if center else ""}">{p(label,"eyebrow")}<h2>{title}</h2></div>'
def hero(label,title,description,photo=None):
    bg = image(photo,'',True) if photo else '<span class="watermark" aria-hidden="true">FEI</span>'
    return f'<section class="page-hero {"photo-hero" if photo else ""}">{bg}<div class="wrap">{p(label,"eyebrow line")}<h1>{title}</h1>{p(description,"intro")}</div></section>'
def save(name,title,content):
    h = header.replace('class="active"','')
    h = h.replace(f'<a href="{name}.html">',f'<a class="active" aria-current="page" href="{name}.html">')
    page = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{escape(title)} — Frontiers Executive Institute"><title>{escape(title)} — Frontiers Executive Institute</title><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="pages.css"></head><body class="{name}-page"><a class="skip" href="#main">Skip to content</a>{h}<main id="main">{content}</main>{footer}<script src="app.js"></script></body></html>'
    page = page.replace('src="app.js"', 'src="app.js?v=2"')
    (root / (name+'.html')).write_text(page,encoding='utf-8')

a = data['about']
about = hero(a[8],escape(a[9])+'<br>'+escape(a[10])+'<br><em>'+escape(a[11])+'</em>',a[12],'container')
about += '<section class="wrap origin page-section"><div class="origin-photo">'+image('image-leadership-panel-discussion','Leadership panel discussion')+'<div class="experience"><strong>2009</strong><span>Founded</span></div></div><div class="origin-copy">'+heading(a[15],escape(a[16])+'<br>'+escape(a[17]))+''.join(p(v) for v in a[18:21])+'</div></section>'
about += '<section class="journey page-section"><div class="wrap">'+heading(a[21],escape(a[22]))+'<ol class="timeline">'
for i in range(23,35,2): about += f'<li><h3>{escape(a[i])}</h3>{p(a[i+1])}</li>'
about += '</ol></div></section><section class="values page-section wrap">'+heading(a[35],escape(a[36]),True)+'<div class="value-grid">'
for i in range(37,49,3): about += f'<article class="value {"value-dark" if i==37 else ""}"><span class="value-index">{a[i]}</span><h3>{escape(a[i+1])}</h3>{p(a[i+2])}</article>'
about += '</div></section><section class="leadership page-section"><div class="wrap">'+heading(a[49],escape(a[50]))+'<div class="team-grid">'
team_assets = ['image-prof-adaeze-nwosu-okeke','image-emeka-jideoku','image-dr-fatima-al-rashid','image-oluwaseun-adeyemo']
for i,name in zip(range(51,63,3),team_assets): about += '<article class="team-person">'+image(name,a[i])+f'<div><h3>{escape(a[i])}</h3>{p(a[i+1],"role")}{p(a[i+2])}</div></article>'
about += '</div></div></section><section class="partner page-section"><div class="wrap"><h2>'+escape(a[64])+'<br>'+escape(a[65])+'</h2>'+p(a[66])+'<div class="actions">'+button(a[67],'services.html','red')+button(a[68],'contact.html','outline')+'</div></div></section>'
save('about','About Us',about)

s = data['services']
services = hero(s[9],escape(s[10])+'<br><em>'+escape(s[11])+'</em>',s[12])
services += '<section class="wrap service-catalogue page-section">'
service_starts = [14,27,41,54,67,80]
service_assets = ['image-executive-leadership-programme','image-emerging-leaders-accelerator','image-ngo-leadership-masterclass','image-social-enterprise-growth-lab','image-organisational-leadership-design','image-executive-keynotes-retreats']
programme_names = []
for n,(i,asset) in enumerate(zip(service_starts,service_assets)):
    name = s[i+2]; programme_names.append(name)
    services += f'<article class="service-detail" id="programme-{n+1}"><div class="service-photo">'+image(asset,name)
    if n in (0,2): services += '<span class="featured">Featured Programme</span>'
    services += '</div><div class="service-copy"><div class="service-meta"><span class="category">'+escape(s[i])+'</span><span>'+escape(s[i+1])+'</span></div><h2>'+escape(name)+'</h2>'+p(s[i+3])+benefits([s[i+5],s[i+7],s[i+9],s[i+11]])+button(s[i+12],enquiry(name))+'</div></article>'
services += '</section><section class="plans page-section"><div class="wrap">'+heading(s[93],escape(s[94])+'<br>'+escape(s[95]),True)+'<div class="plan-grid">'
for n,i in enumerate([96,108,120]):
    services += f'<article class="plan {"popular" if n==1 else ""}">{p(s[i],"eyebrow")}<h3>{escape(s[i+1])}</h3>{p(s[i+2])}'+benefits([s[i+4],s[i+6],s[i+8],s[i+10]])+button(s[i+11],enquiry(s[i+1]),'red' if n==1 else 'outline ink')+'</article>'
services += '</div></div></section>'
save('services','Programmes & Services',services)

c = data['contact']
contact = hero(c[9],escape(c[10])+'<br><em>'+escape(c[11])+'</em>',c[12])
contact += '<section class="wrap contact-content page-section"><aside class="contact-direct"><h2>'+escape(c[13])+'</h2><dl>'
for label,value in [(c[15],c[16]),(c[18],c[19]),(c[21],c[22]),(c[24],c[25])]:
    valuehtml = '<a href="mailto:'+escape(value)+'">'+escape(value)+'</a>' if label=='Email' else escape(value)
    contact += f'<div><dt>{escape(label)}</dt><dd>{valuehtml}</dd></div>'
contact += '</dl></aside><div class="enquiry-panel" id="enquiry"><h2>'+escape(c[26])+'</h2>'+p(c[27],'form-intro')+'<form id="enquiry-form"><div class="form-row"><div class="field"><label for="full-name">Full Name <span aria-hidden="true">*</span></label><input id="full-name" name="name" autocomplete="name" placeholder="Dr. Amina Koité" required maxlength="120"></div><div class="field"><label for="email">Email Address <span aria-hidden="true">*</span></label><input id="email" name="email" type="email" autocomplete="email" placeholder="amina@example.org" required maxlength="254"></div></div><div class="field"><label for="organisation">Organisation</label><input id="organisation" name="organisation" autocomplete="organization" placeholder="Sahel Education Trust" maxlength="160"></div><div class="field"><label for="interest">Area of Interest</label><select id="interest" name="interest"><option value="">Select a programme area</option>'
for value in programme_names+['Open Cohort Enrolment','Organisational Cohort','Fully Bespoke Design','General Enquiry']: contact += f'<option>{escape(value)}</option>'
contact += '</select></div><div class="field"><label for="message">Message</label><textarea id="message" name="message" rows="6" maxlength="5000" placeholder="'+escape(c[37])+'"></textarea></div><button type="submit" class="button dark">'+escape(c[38])+'</button><p class="form-help">Submitting opens an email draft in your email app. Review and send it there to complete your enquiry.</p><p class="form-status" id="form-status" role="status" aria-live="polite"></p>'+p(c[39],'privacy')+'</form></div></section><section class="offices page-section"><div class="wrap"><h2>'+escape(c[40])+'</h2><div class="office-grid">'
for i in [41,44,47]: contact += '<article>'+p(c[i],'eyebrow')+'<h3>'+escape(c[i+1])+'</h3>'+p(c[i+2])+'</article>'
contact += '</div></div></section>'
save('contact','Contact Us',contact)

# Wire the existing home surface to the new pages without changing its layout.
home = route_links(home)
home = home.replace('href="#ngo"','href="services.html#programme-3"')
home = home.replace('href="mailto:info@frontiersexec.org?subject=Programme%20Information"','href="services.html"')
home = home.replace('href="mailto:info@frontiersexec.org?subject=About%20Frontiers%20Executive%20Institute"','href="about.html"')
home = home.replace('<a class="active" href="index.html">','<a class="active" aria-current="page" href="index.html">')
home = home.replace('href="mailto:info@frontiersexec.org?subject=Executive%20Training%20Enquiry"','href="services.html#programme-1"')
home = home.replace('href="mailto:info@frontiersexec.org?subject=Leadership%20Keynotes%20Enquiry"','href="services.html#programme-6"')
home = home.replace('href="mailto:info@frontiersexec.org?subject=NGO%20Capacity%20Building%20Enquiry"','href="contact.html?interest=NGO%20Leadership%20Masterclass#enquiry"')
(root / 'index.html').write_text(home,encoding='utf-8')
print('Created about.html, services.html and contact.html; updated home navigation.')
