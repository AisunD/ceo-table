# KI-Content-Bootcamp (Sebastian Clauß): Auswertung Teil 2, die acht Skills (Claude-Paket)

Social-Sina, 28.10.2026. Baut auf `auswertung-teil-1.md` auf.
Status: **Auswertung, keine Regel.** Nichts davon gilt, bis Aisun entscheidet. Bei Widerspruch gilt unser Stand.
Quelle: `paket-claude/` (aus Aisuns Drive-Ordner „Content Bootcamp Sebiforce“). Jede ZIP liegt entpackt in einem eigenen Ordner (`<skill>/<skill>/SKILL.md` + `references/`). Dazu `Projekt-Anweisung-Claude.txt` und `Meine Beiträge.md` (leere Tabellenvorlage). Die Datei `references/meine-beitraege.md` liegt in sieben Skills, alle sieben Kopien sind identisch.
Gelesen: alle 8 SKILL.md, alle Referenzen, das Skript `content_analyse.py` (802 Zeilen, nur gelesen, nicht ausgeführt).

---

## 0. Was das Paket als Ganzes ist

Acht Skills für ein Claude-Projekt „Mein Content-Team“. Alle lesen zuerst ein „Business-Gehirn“ und die drei Datendateien `Meine Beiträge.md`, `muster.md`, `wettbewerb.md`, die der Insights-Analyst per Skript erzeugt. Drei Prinzipien in jedem Skill:
- **Partner, nicht Ghostwriter:** nur Gliederungen und Varianten, höchstens der erste Satz ist ausformuliert, alles andere sind Platzhalter in eckigen Klammern.
- **Loop-Stufe:** Entwurf intern gegen eine 6-Punkte-Checkliste prüfen, höchstens 3 Durchläufe, dann eine Zeile „Loop-Check: x von 6 erfüllt“ und ehrlich sagen, was offen blieb.
- **Von dir aus melden:** vor jeder Aufgabe prüfen, ob die Zahlen älter als 30 Tage sind, ein Gewinner als Version 2 fällig ist, ein Einbruch läuft oder ein Ausreißer noch nicht verwertet wurde. Höchstens zwei Zeilen.

Feste Stilregeln aller Skills: keine Gedankenstriche, kurze Sätze wie gesprochen, kein Wut-Köder, positiv formuliert, Musik nur lizenzfrei, Kundinnen nur als „Kundin S.“.

---

## 1. Die Skills einzeln (was, Auslöser, braucht, liefert)

**1. business-gehirn**
- Was: Interview mit 14 Fragen (eine pro Nachricht, einmal nachhaken), daraus eine Datei mit 12 Abschnitten: Angebot, Zielkundin mit 3 wörtlichen Sätzen, 2 bis 4 Säulen, „Mein Satz“, Tonfall mit 2 Beispielsätzen, „Das sage ich nie“ (Floskeln, Privates), Formate, Vorlagen, Lead-Wort, beste Beiträge, Geschichten und Zahlen, Vorbild-Accounts. Lücken bleiben „(noch offen)“.
- Auslöser: „Bau mein Business-Gehirn“, „richte mein KI-Team ein“. Braucht: nur die Antworten. Liefert: `business-gehirn.md` plus 3 Stichpunkte, was fehlt.

**2. insights-analyst**
- Was: liest Meta-Export (CSV/Excel), vidIQ-Daten oder Screenshots, rechnet per Skript, meldet zuerst das Gute, dann Ausreißer, Muster, Trend, genau 3 nächste Schritte. Modi: Vollanalyse, Wettbewerb (Ausreißer bei 3 bis 5 fremden Accounts), Notfall (14-Tage-Plan), Screenshots.
- Auslöser: Export-Datei, „was lief gut“, „Ausreißer“, „Notfallplan“, „was läuft bei anderen“. Braucht: 90-Tage-Export, optional vidIQ (Abo, Credits, nur Reels). Liefert: `bericht.md`, `Meine Beiträge.md`, `meine-beitraege.csv`, `muster.md`, `wettbewerb.md`, zwei Grafiken.
- **Was das Skript rechnet:**
  - Nenner: Reichweite, wenn mindestens die Hälfte der Zeilen sie hat, sonst Aufrufe. Quoten = Signal / Nenner × 100 für Likes, Kommentare, Weiterleitungen, Speicherungen, Follows, Profilbesuche.
  - Bewertbar erst ab 7 Tagen. Hauptsignale: Weiterl./R und Speich./R (sonst die ersten zwei vorhandenen).
  - Urteil je Beitrag gegen den **Mittelwert der übrigen bewertbaren Beiträge** (mindestens 2): bestes Signal ≥ 2,0-fach „Gewinner“, 1,7 bis 2,0 „Gewinner auf Probe“, 0,8 bis 1,7 „solide“, unter 0,8 „schwach“. Reichweite ≥ 2-fach, aber eine Quote unter Schnitt: „Thema gut, Umsetzung schwach“.
  - Ausreißer: je Format ab 4 bewertbaren Beiträgen, robuster z-Wert (Median und MAD auf log10-Werten), |z| ≥ 2 nach oben oder unten; dasselbe für die Überspringrate (niedrig = starker Einstieg).
  - Muster: ab 6 bewertbaren Beiträgen, Gruppen ab 2 (Wochentag, Uhrzeit ab 3) nach Format, Wochentag, Tageszeit, Einstieg (Frage, Zahl, Aussage im ersten Caption-Satz), Caption-Länge, Reel-Länge, Hook-Art, Blickwinkel, Säule. Zählt, wenn der Gruppen-Median mindestens 30 % vom Gesamt-Median abweicht. Ab 5 Beiträgen „Muster“, darunter „Tendenz“. Höchstens 8.
  - Trend: Median je Woche, mindestens 6 Wochen. Vergleich der letzten 3 Wochen mit dem Median der Wochen davor (bis zu 12): alle 3 unter 70 % = „Einbruch“, Median ≥ 130 % = „Aufwärtstrend“, unter 70 % = „deutlich unter Schnitt“, bis 85 % = „normale Schwankung“, sonst „stabil“.
  - Neuauflage: jeder Gewinner bekommt Datum + 90 Tage, sonst „überfällig“.
  - Wettbewerb: Faktor = Aufrufe / Median desselben Accounts, ab 3 „echter Ausreißer“, 2 bis 3 „gut gelaufen“; angepinnte Reels raus; Kommentare pro 1.000 Aufrufe als „Kommentar-Magnet“.
  - Faustregel im Bericht: Überspringrate unter 45 % stark, um 60 % schwach (Sebis Erfahrung).
- **Erwartete Export-Spalten** (deutsch oder englisch, erkennt Synonyme, CSV mit beliebigem Trenner oder xlsx): Pflicht ist ein Datum (Veröffentlichungszeitpunkt/Publish time/date) und Reichweite oder Aufrufe (Reach/Views/Plays/Impressionen). Optional: Beitragstyp, Beschreibung/Caption, Permalink, Gefällt mir, Kommentare, Geteilt/Shares, Gespeichert/Saves, Follows, Profilaufrufe, Dauer, durchschnittliche Wiedergabezeit, angeschaut %, Überspringrate, dazu von Hand Hook-Art, Blickwinkel, Ziel, Säule. Wettbewerb: account und views (Aufrufe), optional link, caption, comments, angepinnt.
- Unser Katalog `daten/instagram/instagram-katalog-2026-10.csv` würde erkannt (views, likes, comments, saved, shared, follower, date, typ, caption), aber ohne Reichweite rechnet es pro Aufruf.

**3. themenspeicher**
- Was: macht aus DMs, Kommentaren, Sprachnotizen eine Themenliste. Jedes Thema als Frage im Wortlaut der Zielgruppe, je eine Säule, E (evergreen) oder T (Trend), Nachfrage gezählt („4x gefragt“), Abgleich mit Gewinnern, Hook-Kandidaten (wörtlich, höchstens 12 Wörter). Modus B: „30 Themen in 30 Minuten“ in 5 Schritten. Heikles (Erkrankungen, Medikamente) wird mit „(fachlich absichern)“ markiert, nicht aussortiert.
- Auslöser: „Sortier mir das“. Braucht: Rohmaterial, Säulen. Liefert: Liste nach Säulen, Evergreen-Anteil (Ziel ≥ 70 %), Datei „Themenspeicher“.

**4. content-wuerfel**
- Was: 3 Würfe aus Thema (Frage der Zielkundin) + Blickwinkel (12) + Tonfall (5) + Format + Vorlage, je mit Gliederung, nur Folie 1 ausformuliert. Ab 3 Würfen Mix Wissen, Emotion, Unterhaltung, mindestens ein persönlicher Blickwinkel, einer auf eigenem Muster, einer darf ein „Ausreißer-Nachbau“ sein. 100K-Test.
- Auslöser: „Würfel mir …“, „was poste ich“. Braucht: Business-Gehirn, optional Meine Beiträge, muster.md, wettbewerb.md. Liefert: Würfe plus Zeile für „Meine Beiträge“.

**5. hook-sparring**
- Was: Modus A 10 erste Sätze aus mindestens 6 der 18 Hook-Arten plus „Zitat der Zielgruppe“, Top 3 mit Begründung, Text im Bild (Reel, 2 bis 4 Wörter) oder Folie 2 (Karussell), Testvorschlag. Modus B: eigenen Hook prüfen (was trägt, was schwach ist, 3 bessere Varianten). Regeln: höchstens 10 Wörter gesprochen, 8 auf der Titelfolie, kein Anlauf, nichts verraten, kein Angebot im Hook, für Fremde mindestens 3 Storytelling-Hooks.
- Auslöser: „Hooks für …“, „Prüf meinen Hook“. Liefert: Varianten, nie den fertigen Satz.

**6. beitrags-bauplan**
- Was: Gerüst für Karussell (Mehrwert 7 Folien, Trigger 4 Folien, 4 Vorlagen Fehler/Schritte/Geschichte/Irrglaube, Foto-Dump), Reel (4 Vorlagen plus Geschichte, Kopfnicker, Selbstversuch, B-Roll), Einzelbeitrag, Caption (Satz 1 mit Suchbegriff), Stories (Verkaufsabfolge mit Keyword statt Link-Sticker), Broadcast-Kanal. Pflicht: ein Ziel von vier, eine Handlung mit „weil/damit“, Reichweite und Verkauf nie im selben Beitrag, Drei-Signale-Check (bleiben, liken, weiterleiten).
- Auslöser: „Bauplan für …“. Liefert: Gliederung mit Platzhaltern plus Caption-Gerüst.

**7. recycling**
- Was: schlägt selbst fällige Gewinner vor, prüft Gewinner-Status mit Zahl. Varianten: A Version 2 (bleibt Aufbau, Kernaussage, Länge, Format; neu Titelbild, erster Satz mit anderer Hook-Art, Caption, Zahlen; nach 3 Monaten, Version 3 nach 6), B anderes Format, C ganze Kette aus einem großen Stück (bis 11 Feed-Beiträge, 5 Stories, 1 Newsletter), D Evergreen-Rotation. Kein Gewinner: ehrlich abraten.
- Auslöser: „Was kann ich recyceln?“, „Version 2“, „mach daraus ein Karussell“.

**8. content-tag**
- Was: wöchentlicher Produktionstermin in 4 Nachrichten: Rahmen (Anzahl, Wochen, Zeit), Wochenplan (80 % bewährt, 20 % neu; mindestens Hälfte Reichweite; Lead-Beitrag Mi bis Fr, bei 3 pro Woche jede zweite Woche), Würfe, dann Gliederungen plus je 3 erste Sätze, Batching-Reihenfolge, Zeilen für „Meine Beiträge“. Zeitbudget 10 bis 15 Minuten pro Beitrag, sonst Plan kürzen.
- Auslöser: „Starte meinen Content-Tag“, „plan meine Woche“.

**Projekt-Anweisung:** Router (welcher Satz welchen Skill auslöst) plus die Grundregeln oben. Ersetzt bei uns `CLAUDE.md` und die Agentinnen-Tabelle.

---

## 2. Abgleich und 3. Empfehlung je Skill

| Skill | Bei uns schon | Besser als unser Stand? | Widerspruch zu uns | Empfehlung |
|---|---|---|---|---|
| business-gehirn | `wissen/` (ueber-aisun, zielgruppe, positionierung, angebote, stimme, regeln), Skills `aisun-stimme`, `aisun-instagram-content`, `manychat-keywords.md` | Nein, unser Stand ist tiefer. Neu sind nur zwei Prüffragen: „3 wörtliche Sätze der Zielkundin“ und „Vorbild-Accounts“ | „Kundin S.“ mit Zustimmung erlaubt; bei uns keine Kundinnendaten im Ordner | **Weglassen.** Teil: prüfen, ob `zielgruppe.md` wörtliche Sätze der Zielgruppe hat (anonym, ohne Gesundheitsdaten); Vorbild-Accounts gehören in `wissen/vorbilder/` |
| insights-analyst | Ines (Wochenbericht, Saves/Shares), `katalog-auswertung.md`, `daten/instagram/` | **Ja, deutlich.** Ines hat keine Gewinner-Regel, keine Ausreißer-Statistik, keinen Trend, keinen Notfallplan, kein Werkzeug | Überspringrate-Schwellen und Mosseri-Belege sind Sebis Zahlen; vidIQ kostet und gibt Daten an Dritte | **Teile übernehmen → Ines.** Gewinner-Regel, Ausreißer, Trend, Notfall-14-Tage-Plan (als Abschnitt in `wochen-content.md`), monatlicher 90-Tage-Export. Skript als Werkzeug für Ines erst nach Aisuns OK und Probelauf auf einem echten Export. Kein vidIQ. Keine eigene `Meine Beiträge.md`: Gewinner, Faktor und Version-2-Datum gehören als Felder in die Cockpit-Collection `content` |
| themenspeicher | Säulen nur im Entwurf `content-strategie-2026-10-19.md`; kein Ort für gesammelte Fragen | Ja, als Methode (Frage im Wortlaut, Nachfrage zählen, E/T) | DM-Material von Kundinnen enthält Gesundheitsdaten: darf nicht im Ordner landen | **Teile übernehmen → Sina.** Nur anonymisierte Fragen ohne Personenbezug und ohne Krankheitsdetails einzelner Menschen. Ablage als Status `idee` im Cockpit-Tab Content, keine eigene Themenspeicher-Datei. Säulen erst, wenn Aisun die Strategie entschieden hat |
| content-wuerfel | Sinas Briefing (Ziel, Persona, Keyword, Hook-Winkel), Formel | Teilweise: 12 Blickwinkel und Tonfall-Mix fehlen bei uns als Liste | Formate „Einzelbeitrag“, Listen-Mehrwert-Karussell, „nur Folie 1 ausformuliert“ (bei uns schreibt das Team Entwürfe); Checkliste verbietet Angst- und Druckwörter | **Teile übernehmen → Sina-Briefing:** Feld „Blickwinkel (1 bis 12)“ und „Tonfall“, Regel „kein Blickwinkel doppelt im Monat“. Würfel-Ritual weglassen |
| hook-sparring | Sina/Formel (mindestens 10 Hooks, 3 Winkel), Playbook (15 Hooks), Tina/Romy | Teilweise: 18 Hook-Arten als Pflichtmix, „Zitat der Zielgruppe“, Text im Bild 2 bis 4 Wörter, Modus „Hook prüfen“ | Checklistenpunkt „positiv, kein Angstwort, nie ‚hör sofort auf‘“ widerspricht Aisuns Entscheidung 19.10. (provokante Hooks erlaubt, „Tu das NICHT“) | **Teile übernehmen → Sina/Tina/Romy:** von den 10 Hooks mindestens 6 verschiedene Hook-Arten, mit Art in Klammern. Positiv-Regel weglassen, unser Stand gilt |
| beitrags-bauplan | Karussell-Formel (8 Funktionen), `reel-und-caption-regeln.md`, Romy, Tina, Playbook | Für Karussells nein (Formel ist strenger). Neu: Drei-Signale-Check, Reel-Vorlagen, Story-Verkaufsabfolge, Broadcast-Rhythmus | Trigger-Karussell 4 Folien und Mehrwert als Liste gegen Formel; Caption Satz 1 = Suchbegriff gegen Caption-Regel (Zweithook); Story „Kundenstimme als Screenshot“ gegen HWG § 11 und `regeln.md` | **Teile übernehmen:** Drei-Signale-Check als Zusatz zum Gate (Sina), Reel-Vorlagen und B-Roll-Muster → Romy, Story-Abfolge ohne Kundenstimme → Tina. Karussell-Baupläne weglassen |
| recycling | Strategie-Entwurf „Sieger nach 8 bis 12 Wochen neu“, Katalog-Hebel „Sieger variieren“ | Ja: klare Bleibt/Neu-Trennung, Datum für Version 2/3, Kette nur für Gewinner | Frauenarzt-Sieger wird nicht neu gepostet (Entscheidung 19.10.); Evergreen-Rotation „jeden Tag die nächsten Nummern“ passt nicht zu unserem Mo-bis-Fr-Plan mit neuen Themen | **Übernehmen → Playbook `wochen-content.md`** (Abschnitt „Gewinner neu auflegen“) und Karla (Termine Version 2/3). Evergreen-Rotation weglassen |
| content-tag | Playbook `wochen-content.md` (sehr dünn), Karla, Rhythmus-Entscheidung Mo bis Fr 12 Uhr | Ja als Ablauf (Rahmen, Plan mit Warum-Spalte, Würfe, Batching, Zeitbudget) | 3 Posts pro Woche als Standard, Lead nur Mi bis Fr, 80/20 ohne Gewinnerliste nicht machbar | **Teile übernehmen → `wochen-content.md`:** Ablauf und Batching; 80/20 erst, wenn die Gewinnerliste steht; unser Rhythmus bleibt |
| Projekt-Anweisung | `CLAUDE.md`, Agentinnen | Nein | Zweites Steuerungssystem | **Weglassen.** Teil: die vier „Von dir aus melden“-Signale als Prüfpunkt für Ines bzw. Sebastians Sitzungsstart |

**Querschnitt, was wir nicht übernehmen:**
- „Keine Gedankenstriche“ ist Sebis Stil. Für Aisun entscheidet `wissen/stimme.md`; ihre eigenen Captions nutzen Striche. Keine neue Regel.
- „Partner, nicht Ghostwriter“: unser Tisch schreibt Entwürfe in Aisuns Stimme. Gleich ist der Kern: Erlebnisse und Zahlen nur von Aisun, sonst eine Frage an sie (steht schon bei Sina).
- Sebis Kursbelege (Mosseri, seine Reels mit 29.000 Aufrufen, 45 %/60 % Überspringrate) sind keine Zahlen für Aisuns Gesundheitsnische.

**Querschnitt, was wir übernehmen könnten:** die **Loop-Stufe** als Form für Sinas Gate. Unser Gate ist strenger (10 Fragen, Note ab 8). Neu wäre nur: höchstens 3 Überarbeitungsrunden, dann ehrlich sagen, welcher Punkt offen bleibt, statt endlos zu schleifen.

**Ohne Parallelsystem heißt konkret:** kein Business-Gehirn neben `wissen/`, keine `Meine Beiträge.md` neben dem Cockpit, kein Themenspeicher als eigene Datei, keine acht Skills im Repo. Alles geht als Werkzeug zu Sina, Ines, Romy, Tina, Karla und in `wochen-content.md`.

**Größte Lücke bleibt die gleiche wie in Teil 1:** Ohne monatlichen Meta-Export mit Reichweite, Geteilt, Gespeichert, Profilaufrufe und Karussells läuft weder Gewinner-Regel noch Skript. Unser Katalog hat keine Reichweite und keine Karussell-Daten.

---

## 4. Sicherheit

- **Skript `content_analyse.py`:** keine Netzwerkzugriffe (kein requests, urllib, socket, http), kein subprocess, kein os.system, kein eval/exec, kein Pickle, keine Umgebungsvariablen. Löscht nichts. Liest nur die übergebenen Dateien, schreibt nur in den Ausgabeordner (`--aus`, Standard `auswertung`) und überschreibt dort gleichnamige Dateien (`bericht.md`, `muster.md`, `Meine Beiträge.md`, `meine-beitraege.csv`, `wettbewerb.md`, PNGs). Abhängigkeiten: pandas, optional matplotlib, für Excel zusätzlich openpyxl. Unbedenklich.
- **Datenweitergabe:** nur über vidIQ (externer, kostenpflichtiger Dienst; Konto- und Statistikdaten gehen an vidIQ, Abfragen kosten Credits). Wir nutzen es nicht.
- **Skill-Texte:** keine versteckten Anweisungen gefunden. Sie verlangen nur Dateien im Claude-Projekt und Code-Ausführung.
- **Datenschutz-Risiko liegt im Inhalt, nicht im Code:** Themenspeicher und Hook-Sparring arbeiten mit DMs und Kundinnen-Sätzen. Bei Aisun sind das oft Gesundheitsdaten. Nur anonymisiert und ohne Krankheitsdetails einzelner Personen in den Ordner (`wissen/regeln.md`).
