# F01 · What's inside The Ritual Kit · 10 slides · 1080x1350. Markers follow the published posts.
import os, re, sys
SC=os.path.dirname(os.path.abspath(__file__))
logo=open(f'{SC}/assets/noyau-logo-forest.svg').read().replace('fill="#2F4432"','fill="currentColor"').replace('width="799" height="235"','')
emblem=open(f'{SC}/assets/n-emblem-forest.svg').read().replace('fill="#2F4432"','fill="currentColor"').replace('width="279" height="283"','')
mont=open(f'{SC}/assets/fonts/montserrat.css').read().replace("FONTS/",f"{SC}/assets/fonts/")
CSS=f"""{mont}
@font-face{{font-family:'Sackers';font-weight:300;src:url('{SC}/assets/fonts/SackersGothic-Light.ttf')}}
@font-face{{font-family:'Sackers';font-weight:500;src:url('{SC}/assets/fonts/SackersGothic-Medium.ttf')}}
@font-face{{font-family:'Arabic Poetry';font-weight:500;src:local('Arabic Poetry')}}
@font-face{{font-family:'Cormorant Garamond';font-weight:600;src:url('{SC}/assets/fonts/CormorantGaramond-600-normal.woff2') format('woff2')}}
:root{{--forest:#2F4432;--cream:#F1EDE4;--dim:#C9CBBE;--olive:#B8B07A;--rule:rgba(241,237,228,.45)}}
*{{box-sizing:border-box}} body{{margin:0;width:1080px;height:1350px;overflow:hidden;font-family:'Montserrat',sans-serif;-webkit-font-smoothing:antialiased}}
.s{{position:relative;width:1080px;height:1350px;background:var(--forest);color:var(--cream);overflow:hidden}}
.eyebrow{{position:absolute;left:96px;top:112px;font:300 18px/1 'Sackers';letter-spacing:.42em;text-transform:uppercase;color:var(--olive)}}
.logo{{position:absolute;right:96px;top:96px;width:162px;color:var(--cream)}} .logo svg{{width:100%;height:auto;display:block}}
.counter{{position:absolute;left:0;right:0;bottom:84px;text-align:center;font:300 18px/1 'Sackers';letter-spacing:.4em;color:var(--olive)}}
.h1{{font:700 72px/1.16 'Montserrat';text-align:center;max-width:880px;margin:0 auto;color:var(--cream)}}
.h2{{font:300 32px/1.45 'Montserrat';text-align:center;max-width:760px;margin:22px auto 0;color:var(--cream)}}
.kick{{font:300 20px/1 'Sackers';letter-spacing:.42em;text-transform:uppercase;color:var(--olive);text-align:center;margin-bottom:30px}}
.emb{{position:absolute;left:-150px;top:120px;height:1120px;color:rgba(241,237,228,.07)}} .emb svg{{height:100%;width:auto;display:block}}
.center{{position:absolute;left:96px;right:96px;top:50%;transform:translateY(-50%)}}
/* item slides */
.t1{{position:absolute;left:96px;top:166px;font:600 60px/1.08 'Cormorant Garamond',serif;letter-spacing:.06em;text-transform:uppercase;color:var(--cream);max-width:640px}}
.t2{{position:absolute;left:96px;top:300px;font:italic 300 27px/1.4 'Montserrat';color:var(--dim)}}
.prod{{position:absolute;left:50%;top:380px;transform:translateX(-50%);height:640px;filter:drop-shadow(0 26px 34px rgba(0,0,0,.32))}}
.call{{position:absolute;font:500 17px/1.5 'Montserrat';letter-spacing:.2em;text-transform:uppercase;color:var(--cream);width:300px}}
.call b{{font-weight:700}}
.ln{{position:absolute;height:1px;background:var(--rule)}} .pt{{position:absolute;width:8px;height:8px;border-radius:50%;background:var(--cream);margin:-4px 0 0 -4px}}
.ph{{position:absolute;left:220px;top:380px;width:640px;height:640px;border:1px dashed rgba(241,237,228,.35);display:flex;align-items:center;justify-content:center;font:300 16px/1.8 'Sackers';letter-spacing:.3em;text-transform:uppercase;color:rgba(241,237,228,.55);text-align:center;padding:40px}}
"""
def page(inner): return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='s'>{inner}</div></body></html>"
def chrome(eyebrow,n,total=10): return f'<div class="eyebrow">{eyebrow}</div><div class="logo">{logo}</div><div class="counter">{n:02d} / {total:02d}</div>'
S={}
# 01 cover: photo on top (product untouched), forest panel with the title below
S[1]=f"""<img src="{SC}/plates/cover.jpg" style="position:absolute;left:0;top:0;width:1080px;height:930px;object-fit:cover">
<div style="position:absolute;left:0;top:930px;width:1080px;height:420px;background:var(--forest)"></div>
<div class="eyebrow" style="top:980px">The Ritual Kit</div>
<div style="position:absolute;left:96px;right:96px;top:1030px"><div class="h1" style="text-align:left;margin:0;font-size:64px;max-width:800px">What's inside The Ritual Kit.</div>
<div class="h2" style="text-align:left;margin:18px 0 0;font-size:28px">Eight pieces, one order, one bag.</div></div>
<div class="logo" style="top:980px;right:96px">{logo}</div>
<div class="counter" style="bottom:52px;text-align:right;right:96px;left:auto">01 / 10</div>"""
def item(n, idx, name, h1, h2, calls, photo=None, pts=None, ph_note=''):
    body=chrome(f'{idx:02d} &middot; {name}', n)
    body+=f'<div class="t1">{h1}</div><div class="t2">{h2}</div>'
    if photo: body+=f'<img class="prod" src="{photo}">'
    else: body+=f'<div class="ph">Photo needed<br>{ph_note}</div>'
    # callouts: (label_html, label_left, label_top, text_align, line x1,y1,x2,y2)
    for lab,lx,ly,al,x1,y1,x2,y2 in calls:
        body+=f'<div class="call" style="left:{lx}px;top:{ly}px;text-align:{al}">{lab}</div>'
        import math
        L=math.hypot(x2-x1,y2-y1); ang=math.degrees(math.atan2(y2-y1,x2-x1))
        body+=f'<div class="ln" style="left:{x1}px;top:{y1}px;width:{L:.0f}px;transform:rotate({ang:.2f}deg);transform-origin:0 0"></div><div class="pt" style="left:{x2}px;top:{y2}px"></div>'
    return body
bag=f"{SC}/plates/f01_bag.png" if os.path.exists(f"{SC}/plates/f01_bag.png") else None
S[2]=item(2,1,'The bag','Saffiano<br>leather bag','Genuine Saffiano leather',[
 ('<b>Water-resistant</b><br>&amp; scratch-proof',96,560,'left',300,585,420,620),
 ('Detachable dividers<br>+ interior lid zip',684,700,'right',684,725,560,700),
 ('Soft-structured<br>to hold every piece',96,920,'left',300,945,440,900)], photo=bag, ph_note='the green bag, front')
S[3]=item(3,2,'The brush','Thermal silicone<br>cleansing brush','Food-grade silicone',[
 ('Gentle warmth<br>&amp; vibration',96,560,'left',300,585,440,620),('<b>Boosts circulation</b><br>&amp; absorption',684,700,'right',684,725,600,700),('One-year<br>warranty',96,920,'left',300,945,470,900)], ph_note='the brush, front')
S[4]=item(4,3,'The headband set','Headband &amp;<br>wristbands set','Bamboo charcoal blend',[
 ('Keeps hair &amp;<br>sleeves dry',96,560,'left',300,585,440,620),('Soft, absorbent<br>weave',684,700,'right',684,725,600,700),('One headband,<br>two wristbands',96,920,'left',300,945,470,900)], ph_note='headband and wristbands')
S[5]=item(5,4,'The towels','Bamboo-cotton<br>face towels','Two in every kit',[
 ('Press,<br>never rub',96,560,'left',300,585,440,620),('<b>Embroidered</b><br>Noyau',684,700,'right',684,725,600,700),('Soft on skin,<br>quick to dry',96,920,'left',300,945,470,900)], ph_note='the two towels, folded')
S[6]=item(6,5,'The pads','Reusable makeup<br>removal pads','One bamboo-cotton, one pure cotton',[
 ('Wash &amp;<br>use again',96,560,'left',300,585,440,620),('Mesh wash bag<br>included',684,700,'right',684,725,600,700),('Two textures,<br>two jobs',96,920,'left',300,945,470,900)], ph_note='the two pads with the wash bag')
S[7]=item(7,6,'The jade roller','Jade roller','Natural jade',[
 ('Naturally cool<br>to the touch',96,560,'left',300,585,440,620),('<b>Depuffs</b> from the<br>centre outwards',684,700,'right',684,725,600,700),('Two ends:<br>face &amp; eyes',96,920,'left',300,945,470,900)], ph_note='the roller, upright')
S[8]=item(8,7,'The gua sha','Jade gua sha','Natural jade',[
 ('Contoured for<br>jaw, cheek &amp; brow',96,560,'left',300,585,440,620),('<b>Lifting</b><br>&amp; depuffing',684,700,'right',684,725,600,700),('Use with<br>a little oil',96,920,'left',300,945,470,900)], ph_note='the gua sha, flat')
S[9]=item(9,8,'The mask','Hot &amp; cold<br>compress mask','Facial steamer mask',[
 ('Warm before<br>cleansing',96,560,'left',300,585,440,620),('Cool after<br>rolling',684,700,'right',684,725,600,700),('One piece,<br>two temperatures',96,920,'left',300,945,470,900)], ph_note='the mask, front')
S[10]=f"""<div class="emb">{emblem}</div>{chrome('The Ritual Kit',10)}
<div class="center"><div class="kick">Sold complete</div><div class="h1">Eight pieces.<br>One order. One bag.</div>
<div class="h2">Forest Green or Beige. AED 1,028, one price everywhere.</div>
<div style="margin-top:54px;text-align:center;font:300 18px/1 'Sackers';letter-spacing:.4em;text-transform:uppercase;color:var(--cream)">noyauskin.com &middot; link in bio</div></div>"""
os.makedirs(f'{SC}/html',exist_ok=True)
for n,b in S.items(): open(f'{SC}/html/F01-{n:02d}.html','w').write(page(b))
print('wrote',len(S),'slides; bag photo:', bool(bag))
