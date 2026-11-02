# Monatsauswertung Oktober 2026 (Insta-Ines, Stand 2.11.2026)

**Für den Monats-Rückblick (5 Zeilen)**
1. Instagram (Reels, 28.9.-28.10.): 200.583 Aufrufe, Teilen 0,53 % und Speichern 0,26 % pro Aufruf. Teilen liegt unter Sebis Messlatte von 1 %. Erster Monat mit Messwert, also noch kein Trend.
2. Newsletter: 27 Einzelmails, 17.573 Versände, Öffnungen 30,1 %, Klicks 1,3 %, Abmeldungen 1,2 %. Die Verkaufsmails an die 2.500er-Liste kosten 1,0 bis 1,7 % Abmeldungen je Mail (zusammen 83 allein bei Downsell 1 und 2).
3. Klick-Befund: Hausarzt Email 1, DARE Day Email 2 und Hausarzt Email 2 haben je genau 1 Klick. Das Tracking funktioniert technisch (siehe unten). Die Mails haben nur einen Button, und der wurde kaum geklickt.
4. Brücke: Welches Keyword oder welcher Post Kontakte brachte, lässt sich nicht sagen. ManyChat-Zahlen und Meta-Export fehlen. Verkäufe: nicht in diesem Bericht (ThriveCart-Export bei Franzi).
5. Größte Lücke: Meta-Business-Suite-Export (Karussells, Stories, einzelne Posts) und ManyChat-Export der Keyword-Map.

## Newsletter, Massenversand ab 500 Empfängern
Vergleich untereinander, eindeutige Werte. Öffnungen sind durch Apple-Mail-Datenschutz überhöht (Schätzung), Klicks und Abmeldungen zählen mehr.

| Mail (Datum) | versendet | Öffn. % | Klicks % | Abm. % |
|---|---|---|---|---|
| Podcast Folge 7 (5.10.) | 828 | 32,4 | 1,69 | 0,12 |
| Podcast Folge 8 (19.10.) | 804 | 28,2 | 1,37 | 0,50 |
| DARE Day Email 1 (17.10.) | 803 | 28,3 | 1,00 | 0,12 |
| DARE Day Email 2 (28.10.) | 552 | 30,6 | 0,18 | 0,72 |
| Hausarzt Email 1, alle außer KIH+MM+Ausbildung (26.10.) | 522 | 27,0 | 0,19 | 0,77 |
| Heilraum ext Launch 1 / 2 (5.10. / 8.10.) | 2.604 / 2.591 | 28,0 / 27,5 | 0,65 / 0,50 | 1,15 / 0,96 |
| Downsell KIH Selfstudy 1 / 2 (9.10. / 11.10.) | 2.560 / 2.546 | 31,1 / 27,1 | 0,86 / 1,30 | 1,72 / 1,53 |
| KIH Open Cart 2, alle außer Käufer+Warteliste+Workshop (4.10.) | 2.404 | 26,1 | 0,29 | 1,62 |

Kleine Segmente: Hausarzt nur Kundinnen (je 47): Öffnungen 47 % / 40 %, je 1 Klick. KIH-Workshop-Teilnehmer (ca. 190): Open Cart 3 hatte 17,4 % Klicks, Open Cart 4 und 7 hatten 0. Umfrage an KIH-Nicht-Käufer (175): 51 % Öffnungen, 8,6 % Klicks.
Lesart: Podcast und DARE Email 1 holen die meisten Klicks bei den wenigsten Abmeldungen. Die drei Mails mit 1 Klick liegen mit 0,18 bis 0,19 % am unteren Ende. Kleine Zahlen: Ein Klick mehr oder weniger verschiebt bei 47 Empfängerinnen 2 Prozentpunkte.

## Klick-Befund (nur gelesen, nichts geändert)
- **Tracking funktioniert:** tracklinks steht auf "all". Der Button-Link ist in allen drei Mails als verfolgt registriert (`tracked` = 1) und hat genau den einen Klick. Öffnungen werden gezählt. Andere Mails derselben Zeit zählen Klicks (Podcast 11, DARE Email 1 mit 8).
- **Ziele:** Hausarzt Email 1 führt zu `aisundodenhoff.com/kurs-im-heilen-selfstudy/`, Hausarzt Email 2 zu `aisundodenhoff.com/goldene-dienstage/`, DARE Email 2 zu `aisundodenhoff.com/dare-day-berlin-november-2026/`. Keine der drei Mails verlinkt direkt auf ThriveCart. In den Linklisten stehen noch ersetzte Altlinks (`tracked` = 2, 0 Klicks), darunter die ThriveCart-Adresse `.../hausarzt/` und ein claude.ai-Artifact-Link in Email 2. Das sind Reste vom Bearbeiten, die Mails wurden nach den Änderungen versendet.
- **Fehler gefunden:** Der Button in Hausarzt Email 1 trägt `utm_source=instagram&utm_medium=social`. Klicks aus dem Newsletter erscheinen in der Website-Statistik als Instagram. Das verfälscht die Brücke.
- **DARE Email 2:** Die zwei Video-Vorschaubilder (Vimeo) haben 0 Klicks bei 169 Öffnungen.
- **Nicht klärbar mit meinen Zugriffen:** Ob die Buttons auf den drei Seiten (Selfstudy, Goldene Dienstage) zum ThriveCart-Checkout führen und ob dort Bestellungen aus dem Newsletter ankommen. Auch nicht, ob 1 Klick die Wahrheit ist oder ob Leute die Seite direkt aufrufen (Datenschutz-Blocker auf Mail-Ebene, Direktaufruf). Beides sind Annahmen, keine Befunde.

## Instagram-Konto (Edits, nur Reels, 163 Reels)
Follower 15.389 (davon ca. 3.000 gekauft, Schätzung). Pro Aufruf: Likes 4,0 %, Kommentare 0,18 %, Speichern 0,26 %, Teilen 0,53 %. Top-Reels: Hausarzt-Boot (2x), Podcast-Ausschnitt, Gelenke, Frauenarzt-Tipp. Karussells und Stories fehlen im Export, einen Vormonat zum Vergleichen gibt es nicht.

## Drei Empfehlungen
1. **Frieda, diese Woche:** In ActiveCampaign eine Testmail an eine eigene Adresse schicken, den Button klicken und prüfen, ob der Klick in `get_campaign_links` ankommt. Dann auf den Seiten Selfstudy und Goldene Dienstage prüfen, wohin der Bestellbutton führt, und ob ThriveCart die Quelle zeigt. UTM in der Hausarzt-Vorlage auf `newsletter` / `email` ändern.
2. **Conny mit Karla:** Verkaufsmails mit Button und Videolink-Vorschau haben weniger Klicks als Podcast und DARE Email 1 (Annahme: zu wenig klare Handlung, nicht geprüft). November-Test: Link schon im oberen Drittel und als Button, Videos als eigener Button. Verkaufsmails an die große Liste auf höchstens eine pro Woche begrenzen, solange 1,0 bis 1,7 % abmelden.
3. **Aisun oder Nina, Anfang November:** Meta-Export (90 Tage, CSV) und ManyChat-Export der Keyword-Map ablegen. Danach nennt Ines Gewinner, schwächsten Post und Keywords mit Kontakten. Romy und Sina bis dahin: Teilen-Rate (Ziel über 1 %) als Ziel in die Reel-Hooks aufnehmen und im November vier Reels mit Teilen-Auslöser testen.

## Datenlage
- Vorhanden: Konto-Insights PDF (Reels), ActiveCampaign Kampagnen 1.-31.10., Kontaktzahl: 2.206 aktive Kontakte am 2.11. (Startwert, Aufruf mit Status "aktiv", nicht je Liste).
- Fehlt: Meta-Business-Suite-Export (Aisun), ManyChat-Auswertung (Aisun/Nina), ThriveCart-Verkäufe pro Quelle (Franzi), Vormonatswerte als Vergleich.
- Katalog (`instagram-katalog-2026-10.csv`) ist ein Archiv 2024 bis 2025, keine Oktoberposts.
