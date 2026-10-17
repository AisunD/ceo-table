# Ergebnis-Zusammenfassung: Coach-Selbstcheck

Stand dieser Sitzung · Projekt „Coach-Selbstcheck" (Arbeitstitel), Produktname-Favorit **„Die Arbeitserlaubnis"**

---

## 1. Die wichtigsten Entscheidungen

| Thema | Entscheidung |
|---|---|
| **Produktart** | Bezahltes Mini-Produkt statt kostenlosem Freebie (bessere Vorqualifizierung für die Ausbildung) |
| **Preis** | Empfehlung **37 €** (optional 27 € Einführungspreis für die erste Welle) |
| **Produktname** | Favorit **„Die Arbeitserlaubnis – Dein täglicher Coach-Selbstcheck"**; „Heute Arbeitsverbot?" als Hook-Zeile. Noch kurz mit Uwe Albrecht wegen innerwise-Lizenz abstimmen |
| **Interaktion Rad** | Diskrete Ringe antippen (wie Original) |
| **Verkauf/Auslieferung** | **ThriveCart** (E-Mail wird beim Kauf automatisch erfasst) |
| **Video-Hosting** | **Vimeo** (später; aktuell nur Texte) |
| **E-Mail-Tool** | **ActiveCampaign** |
| **Zielgruppe** | Heilpraktiker, Ärzte (offen für energetische Methoden), Coaches, angehende Coaches, Therapeuten – NICHT die klassische Selbstanwenderin |
| **Zweck** | Lead-Qualifizierung + Warteliste für die große Coach-Ausbildung |

---

## 2. Das Tool (coach-selbstcheck.html)

Eine einzelne, eigenständige HTML-Datei (ca. 746 KB) – kein Server, kein Login, offline lauffähig, DSGVO-konform (Daten bleiben lokal im Browser). Aufbau in 3 Phasen, jede überspringbar:

**Startseite:** Foto, Pain-Point-Block („Kennst du das?"), klickbarer „Über mich"-Block (→ aisundodenhoff.com/ueber-mich/), 3 klickbare Phasen-Karten (rosé-gold), Start-Button. Pain- und Über-mich-Block erscheinen nur beim ersten Besuch; ab dem zweiten Besuch „Schön, dass du wieder da bist" mit Direkt-Buttons.

**Phase 1 – Morgenroutine:** 7 Testschritte mit Arm-/Fingerlängentest (Ja/Nein-Kalibrierung in 2 Schritten → Ich bin ich → Name → überall-ich → ein Energiefeld → reine Quelle). Klickbare Schritt-Punkte (grün/rot), bei „Ja" automatisches Weitergehen mit Klangschale, bei „Nein" bleibt der ausführliche Soforthilfe-Tipp stehen. Verweise: Heilungskompass (0 €) als Voraussetzung, „Make me an Instrument" bei unreiner Quelle, Kurs im Heilen bei Energiefeld, innerwise-Heilkarten.

**Phase 2 – „Es schaut":** Interaktive Grafik der 3 Blick-Ebenen (Illusion außen, blass auslaufend / Mensch / goldene Mitte). Pulsierende, klickbare Mitte → „ins ES SCHAUT gehen" + weiter. Anleitungstext nur noch einmal (im Kasten unten).

**Phase 3 – Das Rad:** 12 Segmente × 12 Ringe (innen→außen: 4 grün, 5 gelb, 2 dunkelgelb, 1 rot), Zentrum Herz „LIEBE". Ring antippen = Einschätzung (mit leisem Ton), Gras-Effekt beim Hovern. Beschriftungen vergrößert, anklickbar (→ volle Erklärung + Link). Priorität im Info-Kasten: kritischster Bereich (am weitesten außen / rot) zuerst. Starre-Warnung, falls Ja/Nein-Kalibrierung fehlschlug.

**Auswertung:** Datum + Anerkennungstext; alles grün = **Arbeitserlaubnis**, gelb = hinschauen, ein rot = **Arbeitsverbot**. Pro nicht-grünem Bereich: Erklärtext, Produktlink und **„Geklärt & nachgetestet"-Button** (setzt Bereich live auf grün, Ergebnis aktualisiert sich). Klär-Hinweis („Jetzt bist du dran…" + Heilkarten). Check-Historie (localStorage, letzte 7 als Ampel-Icons), „Bis morgen früh"-Ritual, Abschluss-CTA zur Ausbildung.

### Design / Technik
- **Schriften** als freie Marken-Pendants eingebettet (Bodoni Moda = Headlines, Raleway = Fließtext, Dancing Script = Script-Akzente) → auf jedem Gerät gleich.
- **Schrift-System** über feste CSS-Tokens (h1/h2/h3/body/small/micro/script statt ~14 Einzelgrößen), alle Größen +10 %.
- Farben nach Brand-Board (Gold #C6A764, Beere #73013A, Creme #FBFAF0 …).
- Leise Web-Audio-Töne (Klangschale bei Ja/Klären, dezentes Brummen bei Nein).
- **Titel-Regel:** immer „Diplom-Psychologin & Expertin für energetische Selbstheilung" – nie „Psychotherapeutin".

### Eingebaute Links (Werteleiter)
- Heilungskompass 0 € (Armlängentest): https://aisundodenhoff.com/heilungskompass/
- Workshop „Make me an Instrument" 49 €: https://aisundodenhoff.thrivecart.com/workshop-makemeaninstrument/
- Workshop UrSeele: https://aisundodenhoff.thrivecart.com/workshop-urseele/
- Integrität (8 Prinzipien): https://innerwise.com/integrity
- DARE-Day Berlin — **7. November 2026 (1 Tag, 250 €)**: https://aisundodenhoff.com/dare-day-berlin-november-2026/ · **10./11. April 2027 (2 Tage, 500 €)**: https://aisundodenhoff.com/dare-day-berlin/
- Kurs im Heilen Selfstudy 699 €: https://aisundodenhoff.com/kurs-im-heilen-selfstudy/
- Große Coach-Ausbildung (Warteliste): https://aisundodenhoff.com/grosse-coach-ausbildung/

---

## 3. Verkaufsstruktur (Details in verkaufsstruktur.md)

- **Funnel:** Instagram/Liste → Sales Page → ThriveCart-Checkout (E-Mail-Erfassung) → Sofort-Download + Tag `coach-selbstcheck-käuferin` → E-Mail-Serie → Warteliste Ausbildung.
- **Order-Bump** im Checkout: „Make me an Instrument" (49 € → 39 €).
- **Widerrufs-Checkbox** für digitale Produkte im Checkout aktivieren.
- **Sales Page:** 10 Abschnitte ausgearbeitet (Hook/Pain → Wende → Produkt-Demo → Wert-Stapel → für wen → über Aisun → Preis-Anker → FAQ → CTA → P.S. mit Ausbildungs-Teaser).

---

## 4. E-Mail-Serie (Volltexte in email-serie.md)

10 Mails über ~3,5 Wochen (ActiveCampaign, Trigger = Kauf-Tag), in tiefer E-Mail-Stimme. Bogen: Nutzung festigen (Mail 0–2) → Vertiefung mit Mehrwert + sanften Brücken zu Workshop & Kurs (Mail 3–5) → Ausbildung + Warteliste (Mail 6–8) → Feedback/Testimonial-Frage (Mail 9). **Zwei Testimonial-Mails** (Tag 8 und Tag 16) mit zwei verschiedenen Archetypen – als Platzhalter mit Struktur angelegt; echte Aussagen müssen von Teilnehmerinnen kommen (5 Interview-Fragen + Einverständnis-Hinweis in Anhang A). ActiveCampaign-Setup in Anhang B.

---

## 5. Veröffentlichen & Testen

- **Lokal ansehen:** Datei per Doppelklick öffnen oder `file:///…/coach-selbstcheck.html` im Browser.
- **Verschickbarer Link entsteht erst durch Upload** auf die Website (WP Dateimanager → `wp-content/uploads/[ORDNER]/coach-selbstcheck.html`). Ordnername im WP Dateimanager nachschauen; bei jeder Änderung Datei dort neu hochladen (überschreiben).
- **Zum Testen:** einzeln an vertraute Coaches (nicht in offenen Gruppen – die Datei ist das ganze Produkt). Am Handy testen lassen. 3 Testfragen: (1) War klar, wo klicken? (2) Wie fühlt sich das Rad an? (3) War es das Geld wert?
- Optional später: automatischer FTP-Upload einrichten (spart manuelles Hochladen).

---

## 6. Offene To-dos

- [ ] Produktname final + kurze Abstimmung mit Uwe Albrecht (Lizenz-Zusatzname)
- [ ] Einführungspreis 27 € ja/nein
- [ ] Vimeo-Videos pro Kategorie (ersetzen später die Texte / Pain-Block-Video)
- [ ] ThriveCart einrichten + mit ActiveCampaign verbinden (Tag, Order-Bump, Widerruf)
- [ ] Testimonial-Interviews führen (Mail 4 + 7) inkl. schriftlichem Einverständnis
- [ ] Eigene Geschichte für Mail 2 ergänzen
- [ ] Produkt-Mockups in Canva (Vorlage „Mockup-Vorlagen Share")
- [ ] FAQ-Bereich der Ausbildungsseite: alte 2026-Termine entfernen
- [ ] Aktuelle Tool-Version auf WordPress hochladen

---

## 7. Projektdateien

- `coach-selbstcheck.html` – das fertige Tool
- `verkaufsstruktur.md` – Preis, Name, Funnel, Sales-Page-Gliederung
- `email-serie.md` – 10 E-Mails + Interview-Fragen + AC-Setup
- `ergebnis-coach-selbstcheck.md` – diese Zusammenfassung
- `design-varianten.html` – erste Design-Exploration (vor dem Konzept-Pivot)
- `CLAUDE.md` – Projektdokumentation für künftige Sitzungen
- `Fotos/` – Original-Fotos
