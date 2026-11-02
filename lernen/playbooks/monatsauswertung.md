# Playbook: Monatsauswertung (Insta-Ines)

> Erste Fassung 2.11.2026. Liefert den Baustein "Ines' Monatszahlen in 5 Zeilen" für `monats-rueckblick.md`. Kein zweites System: Instagram-Gewinner folgen `gewinner-recycling.md`, Sebastians Rückblick bleibt `monats-rueckblick.md`.

**Auslöser:** Anfang des Monats, vor dem Monats-Rückblick. **Ausgabe:** `daten/berichte/JJJJ-MM-monatsauswertung.md`, maximal eine Bildschirmseite.
**Regeln:** Nur Kennzahlen, aus denen sich eine Entscheidung ableiten lässt. Nichts erfinden, Schätzungen kennzeichnen. In ActiveCampaign nur lesen, nie senden oder ändern. Keine Kontaktnamen oder E-Mail-Adressen in Dateien.

## Teil A: Instagram
1. **Aisun legt ab (genau diese zwei):**
   - Konto-Insights-PDF aus Edits für die letzten 30 Tage → `daten/instagram/konto-insights-JJJJ-MM-TT-bis-MM-TT.pdf` (Ines legt die Zahlen als `konto-insights-JJJJ-MM.md` ab).
   - Meta-Business-Suite-Export: Insights → Inhalte → Instagram → 30 Tage (am Monatsanfang 90 Tage, um 7-Tage-Reife zu sichern) → Exportieren (CSV) → `daten/instagram/meta-export-JJJJ-MM.csv`. Enthält Reels, Karussells, Stories; Edits liefert nur Reels.
2. **Rechnen:** Quoten immer pro Aufruf bzw. Reichweite, nie pro Follower (ca. 3.000 gekaufte Follower, Riga; Follower-Quoten nur mit Vorbehalt). Teilen, Speichern, Kommentare je Aufruf; Vergleich mit dem Vormonat und mit dem eigenen Schnitt.
3. **Gewinner und Schwächster** nach `gewinner-recycling.md` (Sebis Skript, ab 2-fach eigener Schnitt, erst nach 7 Tagen). Ein Monat mit weniger als 10 auswertbaren Posts: "kein Trend" schreiben.
4. **Fehlt der Meta-Export:** Post-Ebene weglassen und genau das als Datenlücke benennen. Der Katalog (`instagram-katalog-*.csv`) ist ein Archiv und ersetzt ihn nicht.

## Teil B: Newsletter (ActiveCampaign, nur lesen)
1. `run_campaign_performance_report` (module campaigns, explore all_campaigns_performance, Filter campaign_type = single, Datum 1. bis Monatsletzter): versendet, eindeutige Öffnungen in %, eindeutige Klicks in %, Abmeldungen in %. Pro Kampagne auch Klick-zu-Öffnung.
2. Segment je Mail aus dem Kampagnennamen. Nur wenn nötig: ein `list_campaigns` (status complete, ldate DESC) für Segment-ID und Versanddatum.
3. **Vergleichen: die Mails untereinander**, getrennt nach Größe (Massenversand ab 500 Empfängern / kleine Segmente). Keine Branchenwerte. Öffnungen sind durch Apple-Mail-Datenschutz verzerrt (Schätzung): Klicks und Abmeldungen zählen mehr.
4. **Klick-Check, wenn eine Mail auffällig wenige Klicks hat:** `get_campaign_links` und `get_campaign_messages` (include_text). Prüfen: Ist der Button-Link registriert (`tracked` = 1)? Wohin führt er? Sind UTM-Parameter richtig (Newsletter = `utm_source=newsletter&utm_medium=email`)? Verweist ein Link auf eine alte, ersetzte Adresse? Bleibt es unklar, bekommt Frieda einen konkreten Prüfauftrag.
5. Kontaktzahl: ein einziger Aufruf `list_contacts` mit status 1 und limit 1, `meta.total` notieren (Startwert für den Folgemonat). Keine Auswertungen über Listen.

## Teil C: Brücke
1. ManyChat-Zahlen kommen von Aisun oder Nina (Export der Keyword-Map: Kommentare, DMs, Anmeldungen je Keyword). Fehlen sie, steht "fehlt" im Bericht, keine Schätzung.
2. Zusammenführen: Welches Keyword (Liste `wissen/projekte/instagram/manychat-keywords.md`) und welcher Post brachten Kontakte? Welche Mail brachte Klicks auf die Verkaufsseite? Verkäufe nur aus ThriveCart-Export (Franzi), nie aus Ines' Annahmen.
3. Daraus: was die nächsten 4 Wochen ändern (Format, Keyword, Segment, Mailfrequenz).

## Aufbau des Berichts
1. Oben 5 Zeilen (Übernahme in den Monats-Rückblick): Instagram, Newsletter, Brücke, auffälligster Befund, wichtigste Datenlücke.
2. Tabelle Newsletter (Massenversand), eine Zeile Instagram-Konto, Klick-Befund falls vorhanden.
3. Drei konkrete Empfehlungen mit Zuständiger (Tina, Romy, Greta, Conny, Frieda, Karla, Sina).
4. Datenlage: was fehlt und wer es liefert.

## Danach
Sebastian übernimmt die 5 Zeilen in `lernen/rueckblicke/JJJJ-MM.md`. Erkenntnisse, die sich zweimal bestätigt haben, kommen in `lernen/gelernt.md` unter "Was wirkt".
