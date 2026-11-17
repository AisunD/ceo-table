import math
P="/home/user/ceo-table/content/entwuerfe/toxisch-karussell/fotos/"
BE="#73013A";GO="#C6A764";CR="#FBFAF0";SA="#EADCC1";DK="#1A1A1A";RO="#D17A81"
def person(x,y,s,fill,stroke,sw=5):
    return (f'<circle cx="{x}" cy="{y}" r="{34*s:.0f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
            f'<rect x="{x-48*s:.0f}" y="{y+40*s:.0f}" width="{96*s:.0f}" height="{120*s:.0f}" rx="{44*s:.0f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
def pill(cx,cy,txt,fill,color,w=None,size=34,stroke=None):
    w=w or (len(txt)*size*.56+54); h=size*1.75
    st=f' stroke="{stroke}" stroke-width="3"' if stroke else ''
    return f'<rect x="{cx-w/2:.0f}" y="{cy-h/2:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{h/2:.0f}" fill="{fill}"{st}/><text x="{cx}" y="{cy+size*.36:.0f}" text-anchor="middle" font-family="Raleway" font-weight="600" font-size="{size}" fill="{color}">{txt}</text>'
def arrow(x1,y1,x2,y2,c,w=6):
    a=math.atan2(y2-y1,x2-x1);h=18
    p1=(x2-h*math.cos(a-.5),y2-h*math.sin(a-.5));p2=(x2-h*math.cos(a+.5),y2-h*math.sin(a+.5))
    return f'<line x1="{x1}" y1="{y1}" x2="{x2-6*math.cos(a):.0f}" y2="{y2-6*math.sin(a):.0f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/><polygon points="{x2},{y2} {p1[0]:.0f},{p1[1]:.0f} {p2[0]:.0f},{p2[1]:.0f}" fill="{c}"/>'
def G(n):
    s=''
    if n==1:
        s+='<g transform="translate(0,-70)">'
        s+=f'<rect x="170" y="130" width="740" height="240" rx="40" fill="{BE}" stroke="{GO}" stroke-width="8"/><text x="540" y="290" text-anchor="middle" font-family="Bodoni Moda" font-weight="700" font-size="96" fill="{CR}" letter-spacing="4">KONTROLLE</text>'
        s+=pill(540,480,'Sorge ist die Maske',GO,DK,size=40)+pill(540,590,'Dahinter: Kontrolle',BE,CR,size=40)+'</g>'
    if n==2:
        s+=f'<rect x="290" y="50" width="30" height="580" rx="10" fill="{BE}"/><rect x="760" y="50" width="30" height="580" rx="10" fill="{BE}"/>'
        s+=person(540,190,1.7,SA,GO)
        s+=pill(150,200,'Druck',BE,CR,size=38)+pill(915,200,'Schuld',BE,CR,size=38)
        for y in (300,470): s+=arrow(110,y,270,y,BE)+arrow(970,y,810,y,BE)
        s+=pill(540,620,'Erklären müssen',BE,CR,size=38)
    if n==3:
        s+=f'<circle cx="390" cy="330" r="190" fill="none" stroke="{GO}" stroke-width="6"/><circle cx="690" cy="330" r="190" fill="none" stroke="{BE}" stroke-width="6"/>'
        s+=person(300,270,1.1,SA,GO)+person(780,270,1.1,"#E7B7BB",BE)
        s+='<path d="M540 365 C500 330 480 300 505 280 C525 262 540 280 540 292 C540 280 555 262 575 280 C600 300 580 330 540 365Z" fill="'+GO+'"/>'
        s+=pill(540,90,'Nähe',BE,CR,size=40)+pill(540,610,'und trotzdem frei',GO,DK,size=40)
    if n==4:
        cx,cy=620,350
        rs=(70,120,170,220,270)
        for k,r in enumerate(rs): s+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GO if k==3 else BE}" stroke-width="{10 if k==3 else 3}"/>'
        s+=person(cx,cy-40,0.8,SA,GO,4)
        s+=person(110,300,1.0,"#E7B7BB",BE,4)
        s+=arrow(190,370,cx-rs[3]+6,350,GO,7)
        s+=f'<circle cx="{cx-rs[3]}" cy="350" r="14" fill="{GO}"/>'
    if n==5:
        s+=person(210,260,1.8,SA,GO)+person(860,260,1.5,"#E7B7BB",BE)
        for k in range(14):
            a=k/14*2*math.pi; s+=f'<circle cx="{860+135*math.cos(a):.0f}" cy="{330+135*math.sin(a):.0f}" r="8" fill="none" stroke="{BE}" stroke-width="3"/>'
        s+=f'<rect x="770" y="330" width="44" height="80" rx="9" fill="{BE}"/><rect x="776" y="340" width="32" height="56" rx="4" fill="{CR}"/>'+arrow(340,330,690,360,GO)
        s+=pill(510,215,'Wo bist du?',CR,BE,size=36,stroke=GO)
        s+=pill(210,560,'Ich',GO,DK,size=36)+pill(860,560,'Partner',BE,CR,size=36)+pill(540,660,'Kontrolliere ich auch?',GO,DK,size=40)
    if n==6:
        s+=f'<rect x="548" y="70" width="10" height="560" rx="5" fill="{GO}"/>'
        s+=person(260,300,1.8,"#E7B7BB",BE)+person(830,300,1.8,SA,GO)
        for (x,y) in ((400,210),(450,320),(380,430),(480,500),(430,160)): s+=f'<circle cx="{x}" cy="{y}" r="11" fill="{BE}"/>'
        s+=pill(553,40,'Meine Grenze',GO,DK,size=38)+pill(260,610,'Er',BE,CR,size=36)+pill(830,610,'Ich',GO,DK,size=36)
    return f'<svg viewBox="0 0 1080 700" width="1080" height="700" xmlns="http://www.w3.org/2000/svg">{s}</svg>'
# slides: photo or graphic
# ('p',foto,cx_in_2000scale,headline,small,panel)  panel: 'c' creme, 'b' beere
# ('g',n,headline,small)
S=[
 ('p','p06',1180,'„Wo bist du? Mit wem? Warum so spät?“','Drei Fragen. Klingt nach Sorge. Und du fängst an, dich zu <em>erklären</em>.','b'),
 ('p','p11',1000,'Kontrolle fühlt sich oft an wie <em>Liebe</em>.','Deshalb merkst du sie so spät. Meistens zuerst an dir selbst.','c'),
 ('p','p07',1170,'Du warst nur kurz mit einer Freundin essen.','Auf dem Heimweg hast du schon Sätze gebaut. Wer dabei war. Warum es länger ging. Dass es nett war, aber nicht <em>zu</em> nett.','c'),
 ('p','p01',1250,'Du merkst nur: Ich rechtfertige mich. Ich werde <em>enger</em>.','Kein Streit, kein lautes Wort. Und trotzdem ist da was eng.','c'),
 ('g',1,'Kontrolle versteckt sich oft hinter <em>Sorge</em>.',''),
 ('p','p04',1160,'Sorge sieht so liebevoll aus.','Darum traust du dich kaum, sie <em>infrage</em> zu stellen.','c'),
 ('g',4,'Und wie <em>tief</em> kommt er dabei in dich hinein?','Manche Kontrolle merkst du sofort. Manche erst nach Jahren.'),
 ('p','p05',1250,'Spür mal <em>rein</em>.','Wie fühlt sich dein Abend an, nachdem er gefragt hat? Eng oder weit?','c'),
 ('g',2,'<em>Fremd</em> fühlt sich an wie Druck, Schuld und Erklären müssen.',''),
 ('g',3,'<em>Eigen</em> fühlt sich an wie Freiheit, auch in Nähe.','Er darf fragen. Du darfst antworten. Und es bleibt weit in dir.'),
 ('p','p10',1050,'Und jetzt ehrlich hinschauen: Wo <em>kontrollierst</em> du selbst?','','c'),
 ('g',5,'Der kurze Blick auf sein Handy.','Die Frage, die du „nur so“ stellst.'),
 ('p','p17',1150,'Und die meisten merken es <em>nicht</em>.','Weder wenn sie kontrolliert werden. Noch wenn sie selbst kontrollieren.','c'),
 ('p','p13',1160,'Liebe will wissen, wie es dir geht. Kontrolle will wissen, wo du <em>warst</em>.','','b'),
 ('p','p09',1100,'Wie tief kontrolliert dich jemand? Und wie tief kontrollierst du?','Das Arbeitsblatt zeigt es dir.<br>Kommentiere <b class="kw">TOXISCH</b>','b'),
]
css="""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:Raleway,sans-serif;position:relative;background:#FBFAF0}
.brand{position:absolute;top:70px;right:64px;font:700 26px 'Bodoni Moda',serif;letter-spacing:.18em;z-index:5}
.n{position:absolute;top:74px;left:64px;font:600 24px Raleway;letter-spacing:.1em;z-index:5}
.ph{position:absolute;left:0;top:0;width:1080px;height:830px;background-size:cover;background-repeat:no-repeat}
.pan{position:absolute;left:0;right:0;top:830px;bottom:0;padding:44px 64px 0}
.pan h2{font:700 62px/1.1 'Bodoni Moda',serif;font-variation-settings:'opsz' 11;font-kerning:normal;text-rendering:optimizeLegibility;letter-spacing:-.005em;text-wrap:balance}.w{margin-right:-.09em}.pan h2.big{font-size:76px}.pan p{text-wrap:balance}
.pan p{font:500 38px/1.35 Raleway;margin-top:22px}
.c{background:#FBFAF0;color:#73013A}.c p{color:#1A1A1A}.c em{color:#73013A;font-style:italic}
.b{background:#73013A;color:#FBFAF0}.b em{color:#C6A764;font-style:italic}.b p{color:#FBFAF0}
.kw{display:inline-block;background:linear-gradient(115deg,#a88a4c,#C6A764 30%,#efe2bf 50%,#C6A764 70%,#9d7f43);color:#1A1A1A;padding:2px 22px;border-radius:999px;letter-spacing:.08em}
.gs{background:#FBFAF0}.gs h2{position:absolute;left:64px;right:64px;top:150px;font:700 62px/1.1 'Bodoni Moda',serif;color:#73013A;font-variation-settings:'opsz' 11;font-kerning:normal;text-rendering:optimizeLegibility;letter-spacing:-.005em;text-wrap:balance}
.gs em{font-style:italic;color:#73013A;text-decoration:underline;text-decoration-color:#C6A764;text-decoration-thickness:6px;text-underline-offset:8px}
.gs .svg{position:absolute;left:0;top:380px}
.gs p{position:absolute;left:64px;right:64px;bottom:160px;text-wrap:balance;font:500 38px/1.35 Raleway;color:#1A1A1A}
.sw{position:absolute;bottom:64px;right:64px;font:600 26px Raleway;letter-spacing:.14em;z-index:5}"""
head='<!doctype html><html lang="de"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..800;1,6..96,400..800&family=Raleway:ital,wght@0,500;0,600;0,700;1,500&display=swap" rel="stylesheet"><style>'+css+'</style></head><body>'
D='/tmp/claude-0/-home-user-ceo-table/98fccc0b-51e2-52b4-9177-97ef7eb9be37/scratchpad/ts'
import re
fix=lambda x: re.sub(r'(?<![A-Za-z>])W(?=[a-zäöü])','<span class="w">W</span>',x)
tot=len(S)
for i,s in enumerate(S,1):
    sw='<div class="sw" style="color:%s">WEITER →</div>'
    if s[0]=='p':
        _,f,cx,h,sm,pn=s
        # crop window 2033 wide in 2400 image; cx in 2000-scale -> *1.2
        x0=max(0,min(2400-2033,cx*1.2-1016));pos=-x0*1080/2033
        bg=f"background-image:url(file://{P}{f}.jpg);background-size:{2400*1080/2033:.0f}px auto;background-position:{pos:.0f}px 0"
        dark=pn=='b'
        body=f'<div class="ph" style="{bg}"></div><div class="pan {pn}"><h2{' class="big"' if not sm else ''}>{fix(h)}</h2>'+(f'<p>{sm}</p>' if sm else '')+'</div>'
        body+='<div class="brand" style="color:#73013A">AISUN DODENHOFF</div><div class="n" style="color:#73013A">%d/%d</div>'%(i,tot)
        body+=(sw%('#FBFAF0' if dark else '#73013A') if i<tot else '')
    else:
        _,n,h,sm=s
        body=f'<div class="gs"><h2>{fix(h)}</h2><div class="svg">{G(n)}</div>'+(f'<p>{sm}</p>' if sm else '')+'</div><div class="brand" style="color:#73013A">AISUN DODENHOFF</div><div class="n" style="color:#73013A">%d/%d</div>'%(i,tot)+(sw%'#73013A')
    open(f'{D}{i:02d}.html','w').write(head+body+'</body></html>')
