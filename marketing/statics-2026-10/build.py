import os
LOGO=open('logo.svg').read()
FONTS=open('fonts/local.css').read().replace("url('fonts/","url('../fonts/")
CSS=f"""{FONTS}
:root{{--cream:#F1EDE4;--cream2:#EAE5D9;--beige:#E4D7C4;--forest:#2F4432;--ink:#333;--muted:#6F6F65;--rule:#DADACF;--olive:#B1B17F;--olive-deep:#7D7D55;--on-dark:#F1EDE4;--on-dark-dim:#C2C7B6}}
*{{box-sizing:border-box}} body{{margin:0;width:1080px;height:1350px;overflow:hidden;font-family:'Hanken Grotesk',sans-serif;-webkit-font-smoothing:antialiased}}
.page{{position:relative;width:1080px;height:1350px;background:var(--cream);color:var(--forest)}}
.page.dark{{background:var(--forest);color:var(--on-dark)}}
.eyebrow{{font:500 19px/1.4 'Hanken Grotesk';letter-spacing:.3em;text-transform:uppercase;color:var(--olive-deep);display:flex;align-items:center;gap:14px}}
.dark .eyebrow{{color:var(--on-dark-dim)}}
.line{{font:500 84px/1.06 'Cormorant Garamond',serif;letter-spacing:-.005em;margin-top:18px;text-wrap:balance;max-width:936px}}
.sub{{font:400 22px/1.6 'Hanken Grotesk';color:var(--muted);margin-top:22px;max-width:760px}} .dark .sub{{color:var(--on-dark-dim)}}
.copy{{position:absolute;left:72px;right:72px}}
.plate{{position:absolute;object-fit:cover;display:block}}
.foot{{position:absolute;left:72px;right:72px;bottom:60px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--rule);padding-top:24px}}
.dark .foot,.photo .foot{{border-color:rgba(241,237,228,.28)}}
.foot svg{{height:24px;width:auto;display:block}}
.site{{font:500 15px/1 'Hanken Grotesk';letter-spacing:.28em;text-transform:uppercase;color:var(--muted)}} .dark .site,.photo .site{{color:var(--on-dark-dim)}}
.sw{{width:14px;height:14px;border-radius:50%;display:inline-block;border:1px solid rgba(0,0,0,.08)}}
.grad{{position:absolute;left:0;right:0}}
.tag{{position:absolute;top:22px;left:22px;background:var(--cream);color:var(--forest);font:500 15px/1 'Hanken Grotesk';letter-spacing:.3em;text-transform:uppercase;padding:10px 14px 9px 16px}}
"""
def foot(): return f'<div class="foot">{LOGO}<div class="site">noyauskin.com</div></div>'
def page(cls, inner): return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='page {cls}'>{inner}{foot()}</div></body></html>"

S={}
S['S1']=page('', """
<img class="plate" src="../plates/s1.jpg" style="left:150px;top:72px;width:780px;height:930px">
<div class="copy" style="top:1046px"><div class="eyebrow">The Ritual Kit</div>
<div class="line" style="font-size:66px">A complete skincare ritual, in one place.</div></div>""")
S['S2']=page('dark photo', """
<img class="plate" src="../plates/s7.jpg" style="left:0;top:0;width:1080px;height:1350px">
<div class="grad" style="top:0;height:560px;background:linear-gradient(rgba(20,28,22,.72),rgba(20,28,22,0))"></div>
<div class="grad" style="bottom:0;height:340px;background:linear-gradient(rgba(20,28,22,0),rgba(20,28,22,.62))"></div>
<div class="copy" style="top:92px"><div class="eyebrow">The evening, kept together</div>
<div class="line" style="font-size:96px;color:var(--on-dark)">A ritual, shared.</div></div>""")
S['S3']=page('', """
<img class="plate" src="../plates/s2.jpg" style="left:72px;top:72px;width:936px;height:660px">
<div class="copy" style="top:800px"><div class="eyebrow"><span class="sw" style="background:#2F4432"></span><span class="sw" style="background:#E4D7C4"></span>Choose yours</div>
<div class="line">Forest Green or Light Beige.</div>
<div class="sub">The same eight pieces, the same order, in the colour you will keep on the vanity.</div></div>""")
S['S4']=page('dark', """
<img src="../plates/s4_mirror.png" style="position:absolute;left:50%;top:84px;height:870px;transform:translateX(-50%);filter:drop-shadow(0 30px 40px rgba(0,0,0,.28))">
<div class="copy" style="top:1004px"><div class="eyebrow" style="font-size:17px;letter-spacing:.26em">Bamboo &middot; light ring &middot; 5&times; compact &middot; sold separately</div>
<div class="line" style="font-size:96px">The mirror.</div></div>""")
S['S5']=page('', f"""
<img class="plate" src="../plates/s8.jpg" style="left:0;top:0;width:820px;height:1350px">
<div style="position:absolute;left:820px;top:0;width:260px;height:1350px">
<div style="position:absolute;right:48px;top:72px;width:150px;color:var(--forest)">{LOGO.replace('<svg ','<svg style="width:150px;height:auto;display:block" ')}</div>
<div style="position:absolute;left:0;top:0;width:260px;height:1350px;display:flex;align-items:center;justify-content:center"><div style="transform:rotate(-90deg);white-space:nowrap;font:500 17px/1 'Hanken Grotesk';letter-spacing:.3em;text-transform:uppercase;color:var(--olive-deep)">Bamboo &middot; engraved &middot; 5&times; compact</div></div>
<div style="position:absolute;left:36px;right:36px;bottom:84px"><div style="font:500 46px/1.05 'Cormorant Garamond';color:var(--forest)">The details.</div><div style="margin-top:14px;font:500 13px/1.6 'Hanken Grotesk';letter-spacing:.26em;text-transform:uppercase;color:var(--muted)">Sold separately</div></div>
</div>""").replace(foot(),'')
S['S6']=page('', """
<img class="plate" src="../plates/s3.jpg" style="left:72px;top:72px;width:936px;height:674px">
<div class="copy" style="top:820px"><div class="eyebrow">Wherever the evening is</div>
<div class="line">A ritual that travels.</div></div>""")
S['S7']=page('', """
<div style="position:absolute;left:72px;top:72px;width:456px;height:1000px"><img class="plate" src="../plates/s10_home.jpg" style="left:0;top:0;width:456px;height:1000px"><div class="tag">Home</div></div>
<div style="position:absolute;left:552px;top:72px;width:456px;height:1000px"><img class="plate" src="../plates/s10_away.jpg" style="left:0;top:0;width:456px;height:1000px"><div class="tag">Away</div></div>
<div class="copy" style="top:1116px"><div class="eyebrow">The same bag, the same order</div>
<div class="line" style="font-size:58px">A familiar ritual, wherever you stay.</div></div>""")
S['S8']=page('dark', """
<div class="copy" style="top:112px"><div class="eyebrow">Made to be kept</div>
<div class="line" style="font-size:98px;line-height:1.04;margin-top:24px;max-width:900px">Built to a standard, not to a season.</div></div>
<img class="plate" src="../plates/s8_saffiano.jpg" style="left:160px;top:480px;width:760px;height:422px">
<div class="copy" style="top:956px"><div class="sub" style="margin-top:0;max-width:700px">Saffiano leather, natural jade, food-grade silicone, bamboo-cotton. Chosen for how they behave against skin, in water, and over years.</div></div>""")
dots=''.join('<span style="width:26px;height:26px;border-radius:50%;background:var(--forest);display:inline-block"></span>' for _ in range(22))
dots+='<span style="width:26px;height:26px;border-radius:50%;display:inline-block;border:1.5px solid var(--forest);background:linear-gradient(90deg,var(--forest) 40%,transparent 40%)"></span>'
S['I1']=page('', f"""
<div class="copy" style="top:120px"><div class="eyebrow">On average, women spend</div>
<div style="display:flex;align-items:baseline;gap:26px;margin-top:6px"><div style="font:600 340px/1 'Cormorant Garamond';color:var(--forest);letter-spacing:-.03em;font-variant-numeric:tabular-nums">22.4</div><div style="font:italic 500 88px/1 'Cormorant Garamond';color:var(--forest)">minutes</div></div>
<div class="line" style="font-size:56px;margin-top:10px">on their skincare routines, every day.</div></div>
<div class="copy" style="top:760px"><div style="display:flex;justify-content:space-between;align-items:center">{dots}</div>
<div class="eyebrow" style="margin-top:22px;font-size:14px;letter-spacing:.26em;color:var(--muted)">One dot, one minute</div></div>
<div class="copy" style="top:960px"><div style="font:italic 500 42px/1.3 'Cormorant Garamond';color:var(--forest);max-width:900px">Twenty-two minutes, every day. Worth keeping well.</div></div>""")
def row(top,pct,num,text,extra=''):
    return f"""<div class="copy" style="top:{top}px"><div style="display:flex;align-items:flex-start;gap:36px"><div style="font:600 150px/0.95 'Cormorant Garamond';color:var(--on-dark);letter-spacing:-.03em;font-variant-numeric:tabular-nums;min-width:300px">{num}</div><div style="font:400 24px/1.5 'Hanken Grotesk';color:var(--on-dark-dim);max-width:560px;padding-top:22px">{text}{extra}</div></div>
<div style="margin-top:22px;height:4px;border-radius:2px;background:rgba(241,237,228,.18);position:relative"><div style="position:absolute;left:0;top:0;height:4px;width:{pct}%;border-radius:2px;background:var(--on-dark)"></div></div></div>"""
five=''.join(f'<span style="width:12px;height:12px;border-radius:50%;display:inline-block;margin-right:6px;{"background:var(--on-dark)" if i==0 else "border:1.5px solid var(--on-dark-dim)"}"></span>' for i in range(5))
S['I2']=page('dark', f"""
<div class="copy" style="top:104px"><div class="eyebrow">A recent UK study shows that</div></div>
{row(176,60,'60%','of women neglect a consistent skincare routine, and nearly 1 in 5 go to bed without washing their face.','<div style="margin-top:14px;display:flex;align-items:center;gap:10px;font:500 13px/1 Hanken Grotesk;letter-spacing:.26em;text-transform:uppercase;color:var(--on-dark-dim)"><span>'+five+'</span>1 in 5</div>')}
{row(486,69,'69%','say skincare ingredients are important to them.')}
<div class="copy" style="top:740px"><div class="eyebrow" style="font-size:15px">Yet only</div></div>
{row(776,21,'21%','are fully aware of what is in their skincare products.')}
<div class="copy" style="top:1086px"><div style="font:italic 500 40px/1.3 'Cormorant Garamond';color:var(--on-dark);max-width:800px">The ritual that works is the one you keep.</div></div>""")
import os
os.makedirs('html',exist_ok=True)
import shutil; shutil.rmtree('html'); os.makedirs('html')
for k,v in S.items(): open(f'html/{k}.html','w').write(v)
print('wrote',list(S))
