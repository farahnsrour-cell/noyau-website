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
S['S2']=page('', """
<img class="plate" src="../plates/s2.jpg" style="left:72px;top:72px;width:936px;height:660px">
<div class="copy" style="top:800px"><div class="eyebrow"><span class="sw" style="background:#2F4432"></span><span class="sw" style="background:#E4D7C4"></span>Choose yours</div>
<div class="line">Forest Green or Light Beige.</div>
<div class="sub">The same eight pieces, the same order, in the colour you will keep on the vanity.</div></div>""")
S['S3']=page('', """
<img class="plate" src="../plates/s3.jpg" style="left:72px;top:72px;width:936px;height:674px">
<div class="copy" style="top:820px"><div class="eyebrow">Wherever the evening is</div>
<div class="line">A ritual that travels.</div></div>""")
S['S4']=page('dark', """
<img src="../plates/s4_mirror.png" style="position:absolute;left:50%;top:84px;height:870px;transform:translateX(-50%);filter:drop-shadow(0 30px 40px rgba(0,0,0,.28))">
<div class="copy" style="top:1004px"><div class="eyebrow" style="font-size:17px;letter-spacing:.26em">Bamboo &middot; light ring &middot; 5&times; compact &middot; sold separately</div>
<div class="line" style="font-size:96px">The mirror.</div></div>""")
S['S5']=page('', """
<img class="plate" src="../plates/s5.jpg" style="left:150px;top:72px;width:780px;height:930px">
<div class="copy" style="top:1046px"><div class="eyebrow">Gifting</div>
<div class="line" style="font-size:80px">A ritual, given.</div></div>""")
pieces=["The bag","The brush","The headband and wristbands","Two towels","Two pads","The jade roller","The gua sha","The mask"]
S['S6']=page('dark', f"""
<div style="position:absolute;left:62px;top:30px;font:600 640px/1 'Cormorant Garamond';color:var(--on-dark);letter-spacing:-.02em">8</div>
<div class="copy" style="top:712px"><div class="eyebrow" style="color:var(--on-dark);font-size:22px">Eight pieces. One order. One bag.</div>
<div style="margin-top:34px;columns:2;column-gap:48px;max-width:900px">{''.join(f'<div style="font:500 17px/2.2 Hanken Grotesk;letter-spacing:.22em;text-transform:uppercase;color:var(--on-dark-dim);border-bottom:1px solid rgba(241,237,228,.18)">{p}</div>' for p in pieces)}</div></div>""")
S['S7']=page('dark photo', """
<img class="plate" src="../plates/s7.jpg" style="left:0;top:0;width:1080px;height:1350px">
<div class="grad" style="top:0;height:560px;background:linear-gradient(rgba(20,28,22,.72),rgba(20,28,22,0))"></div>
<div class="grad" style="bottom:0;height:340px;background:linear-gradient(rgba(20,28,22,0),rgba(20,28,22,.62))"></div>
<div class="copy" style="top:92px"><div class="eyebrow">The evening, kept together</div>
<div class="line" style="font-size:96px;color:var(--on-dark)">A ritual, shared.</div></div>""")
S['S8']=page('', f"""
<img class="plate" src="../plates/s8.jpg" style="left:0;top:0;width:820px;height:1350px">
<div style="position:absolute;left:820px;top:0;width:260px;height:1350px">
<div style="position:absolute;right:48px;top:72px;width:150px;color:var(--forest)">{LOGO.replace('<svg ','<svg style="width:150px;height:auto;display:block" ')}</div>
<div style="position:absolute;left:0;top:0;width:260px;height:1350px;display:flex;align-items:center;justify-content:center"><div style="transform:rotate(-90deg);white-space:nowrap;font:500 17px/1 'Hanken Grotesk';letter-spacing:.3em;text-transform:uppercase;color:var(--olive-deep)">Bamboo &middot; engraved &middot; 5&times; compact</div></div>
<div style="position:absolute;left:36px;right:36px;bottom:84px"><div style="font:500 46px/1.05 'Cormorant Garamond';color:var(--forest)">The details.</div><div style="margin-top:14px;font:500 13px/1.6 'Hanken Grotesk';letter-spacing:.26em;text-transform:uppercase;color:var(--muted)">Sold separately</div></div>
</div>""").replace(foot(),'')  # editorial page has its own marks
S['S9']=page('dark', """
<div class="copy" style="top:120px"><div class="eyebrow">The house rule</div>
<div class="line" style="font-size:128px;line-height:1.02;margin-top:28px;max-width:960px">Sold complete.<br>One price, everywhere.</div>
<div class="sub" style="font-size:24px;margin-top:48px;max-width:640px">The kit is never sold in pieces, and never on sale. One price, at noyauskin.com and nowhere else.</div></div>""")
S['S10']=page('', """
<div style="position:absolute;left:72px;top:72px;width:456px;height:1000px"><img class="plate" src="../plates/s10_home.jpg" style="left:0;top:0;width:456px;height:1000px"><div class="tag">Home</div></div>
<div style="position:absolute;left:552px;top:72px;width:456px;height:1000px"><img class="plate" src="../plates/s10_away.jpg" style="left:0;top:0;width:456px;height:1000px"><div class="tag">Away</div></div>
<div class="copy" style="top:1116px"><div class="eyebrow">The same bag, the same order</div>
<div class="line" style="font-size:58px">A familiar ritual, wherever you stay.</div></div>""")
os.makedirs('html',exist_ok=True)
for k,v in S.items(): open(f'html/{k}.html','w').write(v)
print('wrote',list(S))
