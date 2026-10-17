# Coach-Selbstcheck (Arbeitstitel)

Bezahltes Mini-Produkt (27–37 €) für Aisun Dodenhoff. Zielgruppe: Heilpraktiker, Ärzte (offen für energetische Methoden), Coaches und angehende Coaches, Therapeuten. Zweck: Warteliste/Lead-Qualifizierung für die große Coach-Ausbildung. Ursprünglich als Freebie geplant, am 07.07.2026 bewusst zu Low-Ticket-Produkt umentschieden.

## Was das Tool ist

Eine einzelne HTML-Datei ([coach-selbstcheck.html](coach-selbstcheck.html)), die Aisuns echten Vorbereitungs-Prozess vor energetischen Sitzungen digital abbildet – in 3 Phasen:

1. **Morgenroutine** – 6 Testfragen mit Arm-/Fingerlängentest (Ja/Nein-Kalibrierung → Ich bin ich → Name → überall-ich → ein Energiefeld → reine Quelle). Bei "Nein" je ein Soforthilfe-Tipp; bei "reine Quelle = Nein" Verweis auf Workshop "Make me an Instrument".
2. **Es schaut** – innerwise-Konzept der 3 Blick-Ebenen (Illusion → Mensch → Es schaut), als Einstimmung vor dem Rad. CSS-radial-gradient als Grafik.
3. **Coach-Selbstcheck-Rad** – 12 Segmente × 12 Ringe (innen→außen: 4 grün, 5 gelb, 2 dunkelgelb, 1 rot), Zentrum: Herz "LIEBE". Ring antippen = Einschätzung. Auswertung: alles grün = Arbeitserlaubnis; gelb = hinschauen; ein rot = Arbeitsverbot. Pro Kategorie Erklärtext + ggf. Produktlink.

Jede Phase ist überspringbar; Navigation über Fortschritts-Pills oben (abgeschlossene Phasen mit ✓).

Nach Red-Team-Analyse (07.07.2026) ergänzt: Pain-Point-Block auf der Startseite (dunkler Beere-Block, "Kennst du das?"-Hook in Aisuns Stimme – kann später durch Video ersetzt werden), Morgenroutine mit klickbaren Schritt-Punkten (grün/rot je nach Antwort), Starre-Warnung am Rad (wenn Ja/Nein-Kalibrierung fehlschlug), Rad-Anleitung auf "testen statt denken" umgestellt, "Erfahre mehr"-Aufklapper pro Bereich (Erklärtext + Link immer zugänglich), Auswertung mit Datum + Anerkennungstext, Check-Historie via localStorage (letzte 7 als Ampel-Icons, "Willkommen zurück"-Hinweis am Start), "Bis morgen früh"-Ritual-Framing, Footer mit Disclaimer + persönliche-Nutzung-Lizenzzeile.

## Lizenz

Das Rad und "Es schaut" sind innerwise®-Tools von Uwe Albrecht. Aisun ist innerwise-zertifiziert und hat die Erlaubnis, sie anzubieten (mit Uwe Albrecht abgesprochen). Lizenzhinweis steht im Footer.

## Die 12 Kategorien (Reihenfolge im Rad, im Uhrzeigersinn ab oben)

Präsenz der Originalseele, Achtsamkeit, Integrität, Bedarf & Notwendigkeit, Stille, Dankbarkeit, Freude, Namaste, Anmut, Quellen, Ladung, Identität.

Verlinkte Produkte (Werteleiter):
- Quellen + Morgenroutine Schritt 6 → Workshop "Make me an Instrument" (49 €): https://aisundodenhoff.thrivecart.com/workshop-makemeaninstrument/
- Präsenz der Originalseele → Workshop UrSeele: https://aisundodenhoff.thrivecart.com/workshop-urseele/
- Integrität → https://innerwise.com/integrity (8 Prinzipien)
- Dankbarkeit → DARE-Day Berlin, nächster Termin 10./11. April 2027 (von Aisun bestätigt; DARE-Day-Unterseite zeigt evtl. noch alten Termin): https://aisundodenhoff.com/dare-day-berlin/
- Namaste → Kurs im Heilen Selfstudy (699 €, Voraussetzung für Ausbildung): https://aisundodenhoff.com/kurs-im-heilen-selfstudy/
- Abschluss-CTA → große Coach-Ausbildung (Platzhalter-Link auf aisundodenhoff.com)

## Technik

- Alles in einer HTML-Datei, kein Server, kein CDN, DSGVO-konform (keine Datenübertragung, aktuell auch kein localStorage)
- Fotos aus `Fotos/` (DSCF-Serie, Aisun bei energetischer Arbeit) werden per PowerShell-Skript verkleinert und als base64 eingebettet. Workflow: Template mit `%%IMG_*%%`-Platzhaltern im Scratchpad → perl-Replace → fertige Datei hier im Ordner
- Brand: Farben aus dem aisun-brand-design-Skill (Gold #C6A764, Beere #73013A etc.)
- Schriften: freie Marken-Pendants (Bodoni Moda = Serif/Headlines, Raleway 400/600/700 = Fließtext, Dancing Script = Script-Akzente) als Latin-woff2 base64 in die Datei eingebettet (@font-face, ~242 KB) → sehen auf jedem Gerät gleich aus. Schrift-System über CSS-Tokens `--fs-h1/h2/h3/body/small/micro/script` (statt vorher ~14 Einzelgrößen), alle Größen +10%.
- Rad ist per JS generiertes SVG (ringPath-Funktion), Kategorien/Texte im `categories`-Array, Morgenroutine im `routineSteps`-Array
- Build: Scratchpad-Skripte `resize.ps1` (Fotos), `buildfonts.pl` (fonts-embed.css aus Google-Fonts-Latin), `gen.pl` (setzt %%FONTS%% + %%IMG_*%% ins Template → fertige Datei). Bei Bedarf neu erzeugen.

## Offene Punkte

- [x] Armlängentest-Link: eingebaut → Heilungskompass (0€, PDF+Video): https://aisundodenhoff.com/heilungskompass/
- [x] Abschluss-CTA verlinkt auf https://aisundodenhoff.com/grosse-coach-ausbildung/ (Seite wird laut Aisun bald auf Warteliste umgestellt – Link bleibt gleich)
- [ ] Vimeo-Videos pro Kategorie (geplant, noch nicht produziert; aktuell nur Texte)
- [ ] Verkauf über ThriveCart einrichten (Auslieferung der HTML-Datei)
- [ ] Produkt-Mockups in Canva erstellen (Vorlage "Kopie von Mockup-Vorlagen Share", DAG1Q8ITtRY, 56 Seiten; Zugriff via Canva-MCP vorhanden)
- [ ] Feinschliff Design + Aisuns Feedback zur ersten Version

## Dateien

- `coach-selbstcheck.html` – das Tool (fertig generiert, mit eingebetteten Bildern)
- `verkaufsstruktur.md` – Preis (37€), Namensvorschläge ("Die Arbeitserlaubnis"), ThriveCart-Funnel, Sales-Page-Gliederung
- `email-serie.md` – 10 ausformulierte Mails (ActiveCampaign, Tag coach-selbstcheck-käuferin), 2 Testimonial-Mails mit Platzhaltern + Interview-Fragen, AC-Setup-Anleitung
- `design-varianten.html` – erste Design-Exploration (A/B/C), vor dem Konzept-Pivot entstanden
- `Fotos/` – Original-Fotos (6000×4000, z.T. EXIF-rotiert)
- Bildaufbereitung: `resize.ps1` + Template liegen im Session-Scratchpad, bei Bedarf neu erzeugen

## Arbeitsweise mit Aisun

Erst Fragen klären, dann bauen – nicht vorpreschen. Feedback kam explizit. Details und alle inhaltlichen Rohnotizen (12 Kategorien, Morgenroutine-Wortlaut, "Es schaut") liegen im Claude-Memory dieses Projekts.
