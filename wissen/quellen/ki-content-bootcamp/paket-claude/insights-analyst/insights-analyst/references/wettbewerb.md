# Ausreißer bei anderen Accounts

## Warum das funktioniert

Ein Beitrag, der bei einem Account dreimal so gut läuft wie dessen eigener Schnitt, hat ein Thema oder einen Einstieg getroffen, das gerade viele Menschen interessiert. Die Größe des Accounts spielt dabei keine Rolle, weil jeder Account nur mit sich selbst verglichen wird. Das ist das beste Signal für Themen, die auch bei der Person funktionieren könnten.

## Welche Accounts

- 3 bis 5 Accounts aus derselben Zielgruppe oder einem Nachbarthema, ruhig auch kleinere.
- Stehen im Business-Gehirn unter "Accounts, von denen ich lerne". Fehlen sie, frag einmal danach.
- Zusätzlich mit vidIQ: `vidiq_instagram_tiktok_outlier_search` mit den Säulen der Person als Suchbegriffe. So tauchen auch Accounts auf, die die Person noch nicht kennt.

## Rechnen

Faktor = Aufrufe eines Beitrags geteilt durch den Median aller Beiträge desselben Accounts.
- ab 3-fach: echter Ausreißer
- 2- bis 3-fach: gut gelaufen
- Kommentare pro 1.000 Aufrufe zeigen zusätzlich, wo ein Kommentar-Keyword mit Freebie gezogen hat. Das verrät, welche Angebote die Zielgruppe haben will.

Mit vidIQ: `vidiq_ig_profile_reels` liefert höchstens 12 Reels pro Account, angepinnte zuerst, und kostet vidIQ-Credits pro Account. Schreib angepinnte Reels mit der Spalte angepinnt = ja mit, das Skript lässt sie beim Schnitt weg. Aufrufe wie "14,3K" oder "1,2 Mio." darfst du so übernehmen.

Das Skript macht das: `python scripts/content_analyse.py wettbewerb <datei> --aus auswertung`. Die Datei braucht mindestens die Spalten account und views (oder Aufrufe), gern auch link, caption, comments.

## Auswerten

Für die drei stärksten Ausreißer (mit vidIQ über `vidiq_watch_shortform_content`, sonst aus Caption und Titelbild):
1. **Thema:** Welche Frage beantwortet der Beitrag?
2. **Einstieg:** Welche Hook-Art? Was steht im Bild?
3. **Aufbau:** Liste, Geschichte, Anleitung, Meinung?
4. **Handlungsaufforderung:** Keyword, Speichern, Teilen?

## Übersetzen, nie kopieren

Pro Ausreißer ein Wurf im Format des Content-Würfels, mit:
- einem Thema aus den Säulen der Person, das dieselbe Frage oder dasselbe Gefühl anspricht
- einem anderen Blickwinkel oder einer eigenen Geschichte
- dem Hinweis "(Muster von [Account], nicht kopieren)"

Fremde Sätze, Titelbilder und Grafiken werden nie übernommen. Musik nur lizenzfrei.
