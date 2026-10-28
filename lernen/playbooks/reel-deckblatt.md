# Playbook: Reel-Deckblatt aus Canva-Vorlage

> Erste Fassung 28.10.2026 (Hausarzt-Reels 1, 2, 7, 9, 10). Sebastian verbessert sie nach jedem Lauf.

**Vorlage:** Canva „Reels, Stories & Highlights“ (DAGey79SZLY), Seite 2. Foto von Aisun, drei Felder: Gold (oben), Rosé (schräg, fett), Beere (unten), darunter www.aisundodenhoff.com. Original nie ändern.

1. **Texte** (drei Zeilen Gold / Rosé / Beere) aus dem Content-Eintrag (`cover_text`). Aisun gibt Texte frei, Petra nur bei Reibung mit Medizin.
2. **Kopie:** `copy-design` mit `page_numbers: [2]`. Titel: „Deckblatt <Kampagne> Reel NN“.
3. **Texte tauschen:** Elemente heißen in jeder Kopie gleich: Gold `LBW6LnChlGq8pj90`, Rosé `LB4bF3WnLqr8HYDz`, Beere `LBwkXFpXwKzM4958` (Locator = `<page_id>-<element_id>`).
   - Gold: 108 px bis ca. 10 Zeichen, 90 bis 14, 80 bis 21.
   - Rosé: 89 px bis ca. 12 Zeichen, bei langen Wörtern 64.
   - Beere: 100 px bis ca. 14 Zeichen, 70 bei 22.
   - Unterlängen im Gold-Feld werden vom Rosé-Feld überdeckt: dann Gold kleiner und Rosé ca. 15–30 px tiefer. Achtung: `position_element` setzt beim gedrehten Rosé-Feld rund 85 px tiefer als angegeben, also Ziel minus 85 eintragen.
4. **Vorschau prüfen** (Thumbnail), dann **Greta** auf alle Deckblätter zusammen, erst danach speichern (`commit`).
5. **Export** als PNG und in den Asset-Speicher des Content-Boards, `cover_id` eintragen. Solange `export-download.canva.com` in der Cloud-Umgebung gesperrt ist: `canva_id` und `canva_link` eintragen, Aisun speichert über „In Canva öffnen“.
6. Ab dem sechsten Deckblatt einer Serie eine zweite Pose einmischen (Greta, 28.10.).
