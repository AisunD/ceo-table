F="/home/user/ceo-table/content/entwuerfe/ueber-mich/fotos/"
def L(t,side,y,size=44,rot=0,x=None): return dict(t=t,s=side,y=y,size=size,rot=rot,x=x)
S=[
 dict(img="f08.jpg",pos="50% 0%",dark=.28,title="Das bin ich",trot=0,tbottom=True,hook="Und nein, ich bin keine typische Heilerin.",labels=[
   L("Jungs-Mama<br>(12 &amp; 6)","l",190,40,0),L("Hundemama","l",340,40,0),L("Jahrgang 1980","l",450,40,0),L("Glücklich liiert","l",560,40,-2),L("Hilfsbereit &amp;<br>unkompliziert","l",670,40,0),
   L("Diplom-Psychologin,<br>ehemalige Psycho-<br>therapeutin","r",170,42,0),L("Mentorin für<br>energetische<br>Selbstheilung","r",430,40,0),L("Generatorin 4/6","r",640,40,2),L("Berlin · Heidenheim","r",750,40,0)]),
 dict(img="f10.jpg",pos="50% 60%",dark=.30,title="Dinge, die ich liebe",trot=0,labels=[
   L("Laufen,<br>jeden Morgen","l",330,44,0),L("Meine Familie","l",520,48,-2),L("Sauna im<br>eigenen Garten","l",680,44,0),
   L("Frauen begleiten,<br>die ihre eigene<br>Heilerin werden","r",300,44,0),L("Rohkakao","r",560,44,0),L("Reisen (hier: Ägypten)","r",700,40,2),L("Abwechslung","r",880,44,0)]),
 dict(img="f09.jpg",pos="50% 30%",dark=.45,title="Meine tiefsten Täler",trot=0,tsize=104,labels=[
   L("Meine Schwester<br>starb 2023<br>an Krebs","l",380,40,0),L("1 Fehlgeburt<br>2023","l",640,40,0),L("Sexueller<br>Missbrauch","l",860,40,0),
   L("22 Jahre<br>Colitis Ulcerosa","r",380,40,0),L("2x geschieden","r",640,40,0),L("Meine Tochter<br>starb 2011<br>bei der Geburt","r",840,40,0)]),
 dict(img="f14.jpg",pos="50% 15%",dark=.38,title="Was daraus wurde",trot=0,tsize=110,text=["22 Jahre Colitis. Schulmedizinisch: unheilbar.","<big>Ich habe meine Colitis geheilt.</big>","Ich habe gelernt, meinem Körper wieder zuzuhören.","Seitdem glaube ich nicht mehr an „unheilbar“."]),
 dict(img="f01.jpg",pos="60% 35%",dark=.40,title="Mein Weg",trot=0,text=["Diplom-Psychologin · 2011 Approbation · ehemalige Psychotherapeutin","Knapp 20 Jahre Unternehmensberaterin (u. a. Deutsche Bahn)","2016 innerwise · 2018 Guide · 2024 Mentorin","<big>Über 1.000 Menschen begleitet</big>","Kurs im Heilen: über 60 Frauen, 13 sind heute selbst Coach"]),
 dict(img="f13.jpg",pos="50% 45%",dark=.30,title="Random Facts",trot=0,labels=[
   L("19x umgezogen:<br><small>Aachen, Würzburg,<br>Frankfurt, St. Petersburg,<br>Berlin</small>","l",330,42,0),L("Ich liebe Gedichte:<br><small>Hilde Domin, Hesse, Rilke</small>","l",620,40,0),L("Familienbett<br>zu viert","l",820,40,-2),L("Ich habe ein<br>Buch geschrieben","l",1020,40,0),
   L("Seit 9.9.2024:<br>0,0 Alkohol","r",270,48,0),L("Super unordentlich","r",420,40,2),L("Mega spontan,<br>emotional &amp;<br>unkonventionell","r",960,40,0),L("3 Geschwister","r",1140,40,0)]),
 dict(img="f11.jpg",pos="72% 25%",dark=.42,warm=True,title="Was du hier findest",trot=0,tsize=104,text=["Energetische Selbstheilung, erklärt von einer Psychologin","<big>Effektive Alternativen zur klassischen Schulmedizin</big><br>so wie ich sie für mich und meine Familie nutze","Klartext statt Räucherstäbchen","Wie du deinem Körper wieder zuhörst","Für Coaches, Heilpraktikerinnen und Ärztinnen: wie du tiefer ansetzt"]),
 dict(img="f12.jpg",pos="55% 50%",dark=.40,warm=True,money=True),
 dict(img="f07.jpg",pos="50% 35%",dark=.38,title="Wo du anfangen kannst",trot=0,tsize=88,steps=[("Neugierig?","Der Heilungskompass, kostenlos","KOMPASS"),("Selbst lernen?","Kurs im Heilen als Selbstlernkurs","KURSIMHEILEN"),("Andere begleiten?","Die Coach-Ausbildung, ca. 1 Jahr","COACH")]),
 dict(img="f04.jpg",pos="50% 35%",dark=.38,title="Und wer bist du?",trot=0,cta=True),
]
css="""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden;background:#1A1A1A}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ov{position:absolute;inset:0}
.grad{position:absolute;left:0;right:0;bottom:0;height:55%;background:linear-gradient(180deg,rgba(26,26,26,0),rgba(26,26,26,.5))}
.gradt{position:absolute;left:0;right:0;top:0;height:34%;background:linear-gradient(0deg,rgba(26,26,26,0),rgba(26,26,26,.55))}
.sh{text-shadow:0 2px 12px rgba(0,0,0,.55),0 0 2px rgba(0,0,0,.6)}
.brand{position:absolute;top:44px;right:56px;text-align:right;font-family:'Bodoni Moda',serif;color:#FBFAF0;letter-spacing:.18em;font-size:24px;font-weight:600}
.brand i{display:block;font-family:'Dancing Script',cursive;letter-spacing:0;font-size:26px;color:#FBFAF0;font-style:normal}
.n{position:absolute;top:48px;left:60px;color:#FBFAF0;font:600 24px Raleway;letter-spacing:.1em}
.ti{position:absolute;top:96px;left:60px;right:60px;color:#FBFAF0}
.ti small{display:block;font:600 34px 'Bodoni Moda',serif;letter-spacing:.22em}
.ti h1{font:600 120px/1 'Dancing Script',cursive;transform-origin:left center}
.hook{font:700 50px/1.2 'Bodoni Moda',serif;margin-top:12px;font-variation-settings:'opsz' 11}
.lab{position:absolute;color:#FBFAF0;font-family:'Bodoni Moda',serif;font-weight:700;line-height:1.15;font-variation-settings:'opsz' 11}
.lab small{font-size:.85em;font-weight:700}
.lab{max-width:430px}.lab.l{left:44px;transform-origin:left center}.lab.r{right:56px;text-align:right;transform-origin:right center}
.txt{position:absolute;left:64px;right:64px;bottom:70px;color:#FBFAF0;display:grid;gap:20px;font:500 40px/1.3 Raleway;text-shadow:0 2px 16px rgba(0,0,0,.7)}
.txt p{padding-left:34px;position:relative}.txt p:before{content:"";position:absolute;left:0;top:24px;width:20px;height:2px;background:rgba(251,250,240,.6)}
.txt big{font:700 50px/1.2 'Bodoni Moda',serif;font-variation-settings:'opsz' 11}
.money{position:absolute;left:70px;right:70px;top:150px;text-align:center;color:#FBFAF0;font:700 78px/1.15 'Bodoni Moda',serif;font-variation-settings:'opsz' 11}
.money .a{display:block}.money .b{display:block;color:#C6A764;font-style:italic;font-size:88px;margin-top:16px}
.steps{position:absolute;left:64px;right:64px;bottom:96px;color:#FBFAF0;display:grid;gap:30px;text-shadow:0 2px 16px rgba(0,0,0,.7)}
.step{display:grid;grid-template-columns:1fr auto;gap:20px;align-items:center}
.step h3{font:700 50px 'Bodoni Moda',serif;font-variation-settings:'opsz' 11}.step p{font:500 34px Raleway}
.kw{width:300px;text-align:center;background:linear-gradient(115deg,#a88a4c,#C6A764 30%,#efe2bf 50%,#C6A764 70%,#9d7f43);color:#1A1A1A;font:700 28px Raleway;letter-spacing:.08em;padding:16px 24px;border-radius:999px;white-space:nowrap;text-shadow:none}
.cta{position:absolute;left:70px;right:70px;bottom:110px;color:#FBFAF0;text-align:center;font:500 42px/1.4 Raleway;text-shadow:0 2px 16px rgba(0,0,0,.7)}
.cta b{font-weight:700;letter-spacing:.06em;border-bottom:3px solid #C6A764;padding-bottom:2px}
.swipe{position:absolute;bottom:36px;right:56px;color:#FBFAF0;font:600 24px Raleway;letter-spacing:.14em}
svg.ar{position:absolute;inset:0;width:1080px;height:1350px;pointer-events:none}"""
head='<!doctype html><html lang="de"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..800;1,6..96,400..800&family=Raleway:wght@500;600;700&family=Dancing+Script:wght@500..700&display=swap" rel="stylesheet"><style>'+css+'</style></head><body>'
import math
def arrow(x1,y1,x2,y2):
    mx,my=(x1+x2)/2,(y1+y2)/2; dx,dy=x2-x1,y2-y1; cx,cy=mx-dy*.25,my+dx*.25
    ang=math.atan2(y2-cy,x2-cx); a1,a2=ang+2.6,ang-2.6
    p=f'M{x1} {y1} Q{cx:.0f} {cy:.0f} {x2} {y2}'
    h=f'M{x2+18*math.cos(a1):.0f} {y2+18*math.sin(a1):.0f} L{x2} {y2} L{x2+18*math.cos(a2):.0f} {y2+18*math.sin(a2):.0f}'
    st='fill="none" stroke="#FBFAF0" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" style="filter:drop-shadow(0 1px 3px rgba(0,0,0,.6))"'
    return f'<path d="{p}" {st}/><path d="{h}" {st}/>'
for i,s in enumerate(S,1):
    o=f'<img class="bg" src="{F}{s["img"]}" style="object-position:{s["pos"]};{s.get("imgst","")}"><div class="ov" style="background:rgba({'34,24,16' if s.get('warm') else '26,26,26'},{s["dark"]})"></div><div class="gradt"></div><div class="grad"></div>'
    o+=f'<div class="n sh">{i}/10</div><div class="brand sh">AISUN DODENHOFF<i>Unheilbar gibt\'s nicht</i></div>'
    if "title" in s:
        st='top:auto;bottom:90px' if s.get("tbottom") else ''
        o+=f'<div class="ti sh" style="{st}"><h1 style="transform:rotate({s["trot"]}deg);font-size:{s.get("tsize",140)}px">{s["title"]}</h1>'+(f'<p class="hook">{s["hook"]}</p>' if s.get("hook") else '')+'</div>'
    for l in s.get("labels",[]):
        o+=f'<div class="lab sh {l["s"]}" style="top:{l["y"]}px;font-size:{l["size"]}px;transform:rotate({l["rot"]}deg)">{l["t"]}</div>'
    if s.get("arrows"): o+='<svg class="ar" viewBox="0 0 1080 1350">'+"".join(arrow(*a) for a in s["arrows"])+'</svg>'
    if "text" in s: o+='<div class="txt">'+"".join(f"<p>{x}</p>" for x in s["text"])+'</div>'
    if s.get("money"): o+='<div class="money sh"><span class="a">Der wichtigste Experte für deinen Körper</span><span class="b">bist du selbst.</span></div>'
    if "steps" in s: o+='<div class="steps">'+"".join(f'<div class="step"><div><h3>{a}</h3><p>{b}</p></div><span class="kw">{c}</span></div>' for a,b,c in s["steps"])+'</div>'
    if s.get("cta"): o+='<div class="cta">Schreib mir in die Kommentare,<br>wo du gerade stehst:<br><b>KOMPASS</b> · <b>KURSIMHEILEN</b> · <b>COACH</b><br><br>Ich schick dir per DM, was zu dir passt.</div>'
    if i<10: o+='<div class="swipe sh">SWIPE →</div>'
    open(f"s{i:02d}.html","w").write(head+o+"</body></html>")
