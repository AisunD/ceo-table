P="/home/user/ceo-table/content/entwuerfe/ueber-mich/fotos/"
import sys

H2=lambda s,size=64: f'<h2 style="font-size:{size}px">{s}</h2>'
S=[
 ("f15.jpg","50% 14%",.30,"b",'<h2 style="font-size:96px">Mein Sohn war <em>fünf</em>.</h2><p>Der Zahnarzt, sofort: Eiter. Antibiotika. Zahn ziehen. Lachgas oder Vollnarkose. Zahnspange.</p>'),
 ("f09.jpg","50% 10%",.36,"b",'<h2>Ich war ganz schön geschockt.</h2><p>Und doch hab ich gespürt: Das kann nicht die <em>einzige</em> Lösung sein.</p>'),
 ("f13.jpg","50% 58%",.38,"t",'<h2>Ich hab mir eine innerwise-Kollegin dazugeholt.</h2><p>Wir haben auf die energetischen Ursachen geguckt. Und was wir da <em>gefunden</em> haben, war mir vorher überhaupt nicht klar.</p>'),
 ("f04.jpg","50% 15%",.40,"b",'<h2>Bauchweh vor der Klassenarbeit? Da fragst du sofort: Was ist los, mein Schatz?</h2><p>Beim Zahn fragen wir meistens nur: Wann ist der <em>Termin</em>? Komisch eigentlich, oder?</p>'),
 ("f06.jpg","50% 15%",.40,"b",'<h2>Unter seinem Zahn hatte er MEINE Beziehungsthemen gespeichert.</h2><p>Streit und Ärger, als fremdes Feld. Das haben wir energetisch geklärt. <em>Am nächsten Tag:</em> kein Schmerz, keine Entzündung, kein Eiter mehr da. So genial!</p>'),
 ("f07.jpg","50% 12%",.36,"b",'<h2>Ich weiß nicht, wie lange es anhält.</h2><p>Bei uns war es so. Ich kann nicht ausschließen, dass ich mit meinem Sohn wieder zum Zahnarzt gehe. Aber ich guck immer, was <em>HINTER</em> den Symptomen liegt.</p>'),
 ("f14.jpg","50% 15%",.38,"b",'<h2>Was ist bei euch zu Hause gerade eng?</h2><p>Spür mal rein, ja? Zusätzlich zum Zahnarzt. Schreib die erste Antwort auf. Da gibt es nichts <em>falsch</em> zu machen.</p><p class="s" style="font-size:32px;font-style:normal;font-weight:500">Energetische Arbeit ersetzt keine ärztliche Hilfe. Bei Warnzeichen oder wenn dein Bauchgefühl Alarm schlägt, gehört dein Kind abgeklärt.</p>'),
 ("f02.jpg","50% 45%",.50,"t",'<h2>Nicht alles, was dein Kind trägt, gehört zu ihm.</h2><p>Manchmal trägt es etwas von uns mit. Das darfst du anschauen, ganz ohne <em>Schuld</em>.</p>'),
 ("f12.jpg","55% 25%",.34,"b",'<h2>Ich bin Aisun.</h2><p>Diplom-Psychologin, ehemalige Psychotherapeutin. Mama von zwei Jungs, heute 12 und 6. Ich zeig dir, wie du dich und dein Kind selbst <em>wahrnimmst</em> und testest.</p>'),
 ("f05.jpg","50% 18%",.34,"b",'<h2>Kommentiere</h2><div class="kw">ZÄHNE</div><p>Dann schick ich dir mein <em>Arbeitsblatt</em>, mit dem ich selbst gearbeitet habe. Damit schaust du hinter die Themen deiner Zähne. Oder hinter die deines Kindes.</p>'),
]
css="""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden;background:#1A1A1A}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ov{position:absolute;inset:0}
.brand{position:absolute;top:70px;right:64px;text-align:right;font-family:'Bodoni Moda',serif;color:#FBFAF0;letter-spacing:.18em;font-size:24px;font-weight:600;text-shadow:0 1px 8px rgba(0,0,0,.6)}
.brand i{display:block;font-family:'Dancing Script',cursive;letter-spacing:0;font-size:26px;font-style:normal}
.n{position:absolute;top:74px;left:64px;color:#FBFAF0;font:600 24px Raleway;letter-spacing:.1em;text-shadow:0 1px 8px rgba(0,0,0,.6)}
.tx{position:absolute;left:64px;right:64px;color:#FBFAF0;text-shadow:0 2px 14px rgba(0,0,0,.65);display:grid;gap:26px}
.tx.b{bottom:140px}.tx.t{top:175px}
.tx p{font:500 40px/1.32 Raleway}.tx p.h{font:600 42px/1.3 Raleway}
.tx h2{font:700 64px/1.1 'Bodoni Moda',serif;font-variation-settings:'opsz' 11}
.tx h2.m{font-size:76px;text-align:center}
.tx em{color:#C6A764;font-style:italic;font-variation-settings:'opsz' 11;font-kerning:normal;padding-left:.04em}
.tx ul{list-style:none;display:grid;gap:4px}.tx li{font:700 70px/1.1 'Bodoni Moda',serif;font-variation-settings:'opsz' 11}
.q{font:700 130px/1.0 'Bodoni Moda',serif;font-variation-settings:'opsz' 11}
.yr{font:700 190px/1 'Bodoni Moda',serif;color:#C6A764;font-variation-settings:'opsz' 11}
.s{font:500 italic 34px Raleway;opacity:.95}
.kw{justify-self:start;background:linear-gradient(115deg,#a88a4c,#C6A764 30%,#efe2bf 50%,#C6A764 70%,#9d7f43);color:#1A1A1A;font:700 62px Raleway;letter-spacing:.1em;padding:20px 52px;border-radius:999px;text-shadow:none}
.bg{transform:scale(1.03)}.tx h2{font-kerning:normal;text-rendering:optimizeLegibility;letter-spacing:-.005em}
.sw{position:absolute;bottom:64px;right:64px;color:#FBFAF0;font:600 26px Raleway;letter-spacing:.14em;text-shadow:0 1px 8px rgba(0,0,0,.6)}"""
head='<!doctype html><html lang="de"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..800;1,6..96,400..800&family=Raleway:ital,wght@0,500;0,600;0,700;1,500&family=Dancing+Script:wght@500..700&display=swap" rel="stylesheet"><style>'+css+'</style></head><body>'
for i,(f,pos,dk,anc,html) in enumerate(S,1):
    grad = "linear-gradient(0deg,rgba(26,26,26,.88) 0%,rgba(26,26,26,.70) 40%,rgba(26,26,26,0) 78%)" if anc=="b" else "linear-gradient(180deg,rgba(26,26,26,.88) 0%,rgba(26,26,26,.64) 42%,rgba(26,26,26,0) 78%)"
    d=head+f'<img class="bg" src="file://{P}{f}" style="object-position:{pos}"><div class="ov" style="background:rgba(26,26,26,{dk})"></div><div class="ov" style="background:{grad}"></div><div class="ov" style="background:linear-gradient(180deg,rgba(0,0,0,.40) 0%,rgba(0,0,0,0) 20%)"></div><div class="brand">AISUN DODENHOFF<i>Unheilbar gibt´s nicht</i></div><div class="n">{i}/10</div><div class="tx {anc}">{html}</div>'+('<div class="sw">WEITER →</div>' if i<10 else '')+'</body></html>'
    open(f'/tmp/claude-0/-home-user-ceo-table/98fccc0b-51e2-52b4-9177-97ef7eb9be37/scratchpad/zs{i:02d}.html','w').write(d)
