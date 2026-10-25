import json,html
F="/home/user/ceo-table/content/entwuerfe/ueber-mich/fotos/"
def L(t,side,y,gold=False): return {"t":t,"s":side,"y":y,"g":gold}
S=[
 {"img":"f15.jpg","pos":"50% 0%","tb":1,"title":"Das bin ich","hook":"Und nein, ich bin keine typische Heilerin.","labels":[
   L("Jungs-Mama (12 & 6)","l",470),L("Jahrgang 1980","l",590),L("Glücklich liiert","l",710),L("Hilfsbereit & unkompliziert","l",830),
   L("Diplom-Psychologin,<br>ehemalige Psychotherapeutin","r",450),L("Mentorin für energetische<br>Selbstheilung","r",615),L("Generatorin 4/6","r",745),L("Wohne in Berlin,<br>geboren in Heidenheim","r",830)]},
 {"img":"f10.jpg","pos":"50% 60%","title":"Dinge, die ich liebe","labels":[
   L("Laufen, jeden Morgen","l",430),L("Meine Familie","l",580),L("Eisbaden","l",730),L("Sauna im eigenen Garten","l",880),
   L("Frauen begleiten, die ihre<br>eigene Heilerin werden","r",430),L("Rohkakao","r",600),L("Reisen (hier: Ägypten)","r",750),L("Abwechslung","r",900)]},
 {"img":"f09.jpg","pos":"50% 30%","dark":0.55,"title":"Meine tiefsten Täler","labels":[
   L("Meine Schwester starb<br>2023 an Krebs","l",560),L("1 Fehlgeburt 2023","l",760),L("Sexueller Missbrauch","l",960),
   L("22 Jahre Colitis Ulcerosa","r",560),L("2x geschieden","r",760),L("Meine Tochter starb<br>2011 bei der Geburt","r",960)]},
 {"img":"f14.jpg","pos":"50% 25%","title":"Was daraus wurde","list":["22 Jahre Colitis. Schulmedizinisch: unheilbar.","<b>Ich habe meine Colitis geheilt.</b>","Ich habe gelernt, meinem Körper wieder zuzuhören.","Seitdem glaube ich nicht mehr an „unheilbar“."]},
 {"img":"f01.jpg","pos":"60% 40%","title":"Mein Weg","list":["Diplom-Psychologin","Knapp 20 Jahre Unternehmensberaterin, u. a. Auswahl von Führungskräften für die Deutsche Bahn","2011 Approbation in Verhaltenstherapie. Ehemalige Psychotherapeutin, heute nicht mehr im Gesundheitssystem","2016 innerwise · 2018 Guide · 2024 Mentorin","Über 1.000 Menschen begleitet","Seit 2 Jahren Kurs im Heilen: über 60 Frauen, viele sind heute selbst Coach"]},
 {"img":"f13.jpg","pos":"50% 45%","title":"Random Facts","labels":[
   L("19x umgezogen: Aachen, Würzburg,<br>Frankfurt, St. Petersburg, Berlin","l",400),L("Ich liebe Gedichte: Hilde<br>Domin, Hesse, Rilke","l",600),L("Wir schlafen zu viert<br>im Familienbett","l",800),L("Ich habe ein Buch<br>geschrieben","l",1000),
   L("Seit 9.9.2024:<br>0,0 Alkohol","r",400,True),L("Super unordentlich","r",600),L("Mega spontan, emotional<br>& unkonventionell","r",780),L("3 Geschwister","r",960)]},
 {"img":"f11.jpg","pos":"62% 40%","title":"Was du hier findest","list":["Energetische Selbstheilung, erklärt von einer Psychologin","<b>Effektive Alternativen zur klassischen Schulmedizin</b>, so wie ich sie für mich und meine Familie nutze","Klartext statt Räucherstäbchen","Wie du deinem Körper wieder zuhörst","Für Coaches, Heilpraktikerinnen und Ärztinnen: wie du bei deinen Klientinnen tiefer ansetzt"]},
 {"img":"f12.jpg","pos":"55% 40%","dark":0.45,"money":"Der wichtigste Experte für deinen Körper<br><em>bist du selbst.</em>"},
 {"img":"f07.jpg","pos":"50% 30%","title":"Wo du anfangen kannst","steps":[("Neugierig?","Der Heilungskompass, kostenlos","KOMPASS"),("Selbst lernen?","Kurs im Heilen als Selbstlernkurs, jederzeit","kursimheilen"),("Andere begleiten?","Die Coach-Ausbildung, ca. 1 Jahr","COACH")]},
 {"img":"f04.jpg","pos":"50% 30%","title":"Und wer bist du?","cta":"Schreib mir in die Kommentare, wo du gerade stehst:<br><b>KOMPASS</b>, <b>kursimheilen</b> oder <b>COACH</b>.<br><br>Ich schick dir per DM, was zu dir passt."},
]
css="""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden;background:#1A1A1A}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ov{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.15) 35%,rgba(0,0,0,.15) 60%,rgba(0,0,0,.6) 100%)}
.brand{position:absolute;top:44px;right:56px;text-align:right;font-family:'Bodoni Moda',serif;color:#FBFAF0;letter-spacing:.18em;font-size:22px}
.brand i{display:block;font-family:'Dancing Script',cursive;letter-spacing:0;font-size:24px;opacity:.9}
.n{position:absolute;top:48px;left:60px;color:#FBFAF0;font:600 22px Raleway;letter-spacing:.1em;opacity:.8}
.ti{position:absolute;top:120px;left:60px;right:60px;color:#FBFAF0}
.ti small{display:block;font:500 34px 'Bodoni Moda',serif;letter-spacing:.2em}
.ti h1{font:500 104px/1 'Dancing Script',cursive;margin-top:-6px;text-shadow:0 2px 14px rgba(0,0,0,.45)}
.hook{font:500 44px/1.2 'Bodoni Moda',serif;margin-top:18px;text-shadow:0 2px 12px rgba(0,0,0,.6);font-variation-settings:'opsz' 11}
.lab{position:absolute;width:440px;color:#FBFAF0;font:500 30px/1.25 'Bodoni Moda',serif;font-variation-settings:'opsz' 11}.lab span{display:inline-block;background:rgba(26,26,26,.55);padding:10px 16px;border-radius:14px}
.lab.l{left:50px}.lab.r{right:50px;text-align:right}
.lab.g{color:#C6A764;font-weight:600}
.lab svg{display:block;margin-top:8px;width:90px;height:44px}.lab.r svg{margin-left:auto;transform:scaleX(-1)}
.box{position:absolute;left:60px;right:60px;bottom:90px;background:rgba(26,26,26,.72);border-radius:28px;padding:34px 38px;color:#FBFAF0}
.box ul{list-style:none;display:grid;gap:16px;font:500 33px/1.32 Raleway}
.box li{padding-left:34px;position:relative}.box li:before{content:"";position:absolute;left:0;top:20px;width:20px;height:2px;background:#C6A764}
.box b{color:#C6A764;font-weight:700}
.money{position:absolute;left:70px;right:70px;top:50%;transform:translateY(-50%);text-align:center;color:#FBFAF0;font:500 76px/1.15 'Bodoni Moda',serif;text-shadow:0 2px 18px rgba(0,0,0,.6);font-variation-settings:'opsz' 11}
.money em{color:#C6A764;display:block}
.step{display:grid;grid-template-columns:1fr auto;gap:18px;align-items:center;padding:20px 0;border-top:1px solid rgba(198,167,100,.4)}.step:first-child{border-top:0}
.step h3{font:600 36px 'Bodoni Moda',serif}.step p{font:500 28px Raleway;opacity:.92}
.kw{background:linear-gradient(115deg,#a88a4c,#C6A764 30%,#efe2bf 50%,#C6A764 70%,#9d7f43);color:#1A1A1A;font:700 24px Raleway;letter-spacing:.08em;padding:12px 18px;border-radius:999px;white-space:nowrap}
.cta{font:500 38px/1.4 Raleway;text-align:center}.cta b{color:#C6A764}
.swipe{position:absolute;bottom:34px;right:56px;color:#FBFAF0;font:600 22px Raleway;letter-spacing:.14em;opacity:.85}"""
arrow='<svg viewBox="0 0 90 44"><path d="M5 5 C 20 38, 55 40, 82 30" fill="none" stroke="#FBFAF0" stroke-width="3" stroke-linecap="round"/><path d="M70 22 L84 30 L70 38" fill="none" stroke="#FBFAF0" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
head='<!doctype html><html lang="de"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..700;1,6..96,400..700&family=Raleway:wght@500;600;700&family=Dancing+Script:wght@500;600&display=swap" rel="stylesheet"><style>'+css+'</style></head><body>'
for i,s in enumerate(S,1):
    o=f'<img class="bg" src="{F}{s["img"]}" style="object-position:{s["pos"]}"><div class="ov" style="background-color:rgba(0,0,0,{s.get("dark",0.1)})"></div>'
    o+=f'<div class="n">{i}/10</div><div class="brand">AISUN DODENHOFF<i>Unheilbar gibt\'s nicht</i></div>'
    if "title" in s:
        o+=(f'<div class="ti" style="top:auto;bottom:90px;background:rgba(26,26,26,.6);border-radius:28px;padding:26px 34px">' if s.get('tb') else '<div class="ti">')+f'<small>AISUN</small><h1>{s["title"]}</h1>'+(f'<p class="hook">{s["hook"]}</p>' if s.get("hook") else '')+'</div>'
    for l in s.get("labels",[]):
        o+=f'<div class="lab {l["s"]}{" g" if l["g"] else ""}" style="top:{l["y"]}px"><span>{l["t"]}</span>{arrow}</div>'
    if "list" in s: o+='<div class="box"><ul>'+"".join(f"<li>{x}</li>" for x in s["list"])+'</ul></div>'
    if "money" in s: o+=f'<div class="money">{s["money"]}</div>'
    if "steps" in s: o+='<div class="box">'+"".join(f'<div class="step"><div><h3>{a}</h3><p>{b}</p></div><span class="kw">{c}</span></div>' for a,b,c in s["steps"])+'</div>'
    if "cta" in s: o+=f'<div class="box"><p class="cta">{s["cta"]}</p></div>'
    if i<10: o+='<div class="swipe">SWIPE →</div>'
    open(f"s{i:02d}.html","w").write(head+o+"</body></html>")
