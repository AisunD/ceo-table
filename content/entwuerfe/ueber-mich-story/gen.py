import sys
P="/home/user/ceo-table/content/entwuerfe/ueber-mich/fotos/"
# (foto, bg-pos, overlay, anker, html)
S=[
 ("f05.jpg","50% 18%",.30,"b",'<div class="q">„Darm<br>entfernen.“</div><p>Das war die Empfehlung.<br>Nach über 20 Jahren Colitis ulcerosa.</p><p class="h">Ich habe <em>Stopp</em> gesagt.</p>'),
 ("f04.jpg","50% 15%",.45,"b",'<h2>Nicht, weil ich naiv war.</h2><p>Ich bin Diplom-Psychologin und ausgebildete Psychologische Psychotherapeutin.<br>Ich habe in Kliniken gearbeitet.<br>Ich kannte das System von innen.</p><p class="h"><em>Genau deshalb.</em></p>'),
 ("f09.jpg","50% 10%",.42,"b",'<ul><li>Cortison.</li><li>Medikamente.</li><li>Darmspiegelungen.</li><li>Schübe.</li></ul><p>Über 20 Jahre lang.</p><h2>Schulmedizinisch: <em>unheilbar.</em></h2>'),
 ("f08.jpg","50% 12%",.45,"b",'<p>Ich war in zwei Welten zu Hause: in Kliniken und Praxen. Und als Unternehmensberaterin im <span style="white-space:nowrap">Top-Management</span>, unter anderem bei der Deutschen Bahn.</p><p class="h">In beiden sah ich dasselbe:</p><h2>Die eigentlichen Ursachen bleiben fast immer <em>unsichtbar.</em></h2>'),
 ("f02.jpg","50% 45%",.50,"t",'<p>In der Therapie wurde ein Symptom behandelt.<br>In der Beratung eine Struktur optimiert.</p><h2>Aber <em>warum</em> ist das überhaupt entstanden?</h2><p>Was will das System eigentlich sagen?<br>Ich habe diese Frage gestellt.</p>'),
 ("f06.jpg","50% 15%",.45,"b",'<div class="yr">2016.</div><p>Ich lerne Uwe Albrecht und innerwise kennen.</p><p class="h">In wenigen Tagen erlebe ich eine Tiefe, die ich in Jahren psychotherapeutischer Ausbildung nicht gesehen hatte.</p>'),
 ("f14.jpg","50% 15%",.45,"b",'<p>Ich habe energetisch gearbeitet.<br>Nicht von heute auf morgen,<br>mit Hilfe anderer energetischer Coaches.</p><h2>Und ich habe meine Colitis <em>geheilt.</em></h2><p>Heute habe ich keine Beschwerden mehr.</p><p class="s">Meine Geschichte. Keine Anleitung.</p>'),
 ("f07.jpg","50% 12%",.32,"b",'<p>Deshalb löse ich deine Probleme nicht für dich.</p><h2>Ich zeige dir, wie du wieder Zugang findest:</h2><p>zu deiner eigenen Wahrnehmung.<br>Und zu deiner Entscheidungsfähigkeit.</p>'),
 ("f12.jpg","55% 25%",.34,"b",'<h2 class="m">Du brauchst nicht noch eine Expertin.</h2><h2 class="m"><em>Werde die Expertin für dich selbst.</em></h2>'),
 ("f15.jpg","50% 14%",.40,"b",'<p>Wie diese Heilung wirklich passiert ist, erzähle ich in einem Interview.</p><p class="h">Kommentiere</p><div class="kw">INTERVIEW</div><p>und ich schick es dir.</p>'),
]
css="""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden;background:#1A1A1A}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ov{position:absolute;inset:0}
.brand{position:absolute;top:44px;right:56px;text-align:right;font-family:'Bodoni Moda',serif;color:#FBFAF0;letter-spacing:.18em;font-size:24px;font-weight:600;text-shadow:0 1px 8px rgba(0,0,0,.6)}
.brand i{display:block;font-family:'Dancing Script',cursive;letter-spacing:0;font-size:26px;font-style:normal}
.n{position:absolute;top:48px;left:60px;color:#FBFAF0;font:600 24px Raleway;letter-spacing:.1em;text-shadow:0 1px 8px rgba(0,0,0,.6)}
.tx{position:absolute;left:64px;right:64px;color:#FBFAF0;text-shadow:0 2px 14px rgba(0,0,0,.65);display:grid;gap:26px}
.tx.b{bottom:110px}.tx.t{top:130px}
.tx p{font:500 40px/1.32 Raleway}.tx p.h{font:600 42px/1.3 Raleway}
.tx h2{font:700 64px/1.1 'Bodoni Moda',serif;font-variation-settings:'opsz' 11}
.tx h2.m{font-size:76px;text-align:center}
.tx em{color:#C6A764;font-style:italic;font-variation-settings:'opsz' 11;font-kerning:normal;padding-left:.04em}
.tx ul{list-style:none;display:grid;gap:4px}.tx li{font:700 70px/1.1 'Bodoni Moda',serif;font-variation-settings:'opsz' 11}
.q{font:700 130px/1.0 'Bodoni Moda',serif;font-variation-settings:'opsz' 11}
.yr{font:700 190px/1 'Bodoni Moda',serif;color:#C6A764;font-variation-settings:'opsz' 11}
.s{font:500 italic 34px Raleway;opacity:.95}
.kw{justify-self:start;background:linear-gradient(115deg,#a88a4c,#C6A764 30%,#efe2bf 50%,#C6A764 70%,#9d7f43);color:#1A1A1A;font:700 62px Raleway;letter-spacing:.1em;padding:20px 52px;border-radius:999px;text-shadow:none}
.sw{position:absolute;bottom:40px;right:56px;color:#FBFAF0;font:600 26px Raleway;letter-spacing:.14em;text-shadow:0 1px 8px rgba(0,0,0,.6)}"""
head='<!doctype html><html lang="de"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..800;1,6..96,400..800&family=Raleway:ital,wght@0,500;0,600;0,700;1,500&family=Dancing+Script:wght@500..700&display=swap" rel="stylesheet"><style>'+css+'</style></head><body>'
for i,(f,pos,dk,anc,html) in enumerate(S,1):
    grad = "linear-gradient(0deg,rgba(26,26,26,.78) 0%,rgba(26,26,26,.55) 38%,rgba(26,26,26,0) 70%)" if anc=="b" else "linear-gradient(180deg,rgba(26,26,26,.78) 0%,rgba(26,26,26,.5) 40%,rgba(26,26,26,0) 72%)"
    d=head+f'<img class="bg" src="file://{P}{f}" style="object-position:{pos}"><div class="ov" style="background:rgba(115,1,58,{dk})"></div><div class="ov" style="background:rgba(0,0,0,.16)"></div><div class="ov" style="background:{grad}"></div><div class="brand">AISUN DODENHOFF<i>Unheilbar gibt´s nicht</i></div><div class="n">{i}/10</div><div class="tx {anc}">{html}</div>'+('<div class="sw">WEITER →</div>' if i<10 else '')+'</body></html>'
    open(f'/tmp/claude-0/-home-user-ceo-table/98fccc0b-51e2-52b4-9177-97ef7eb9be37/scratchpad/us{i:02d}.html','w').write(d)
