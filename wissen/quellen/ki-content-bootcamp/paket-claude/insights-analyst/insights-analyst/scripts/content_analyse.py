#!/usr/bin/env python3
"""Content-Analyse für das KI-Content-Team (Insights-Analyst).

Liest Instagram-Statistik-Exporte (CSV oder Excel, z. B. aus der Meta Business Suite
unter Insights > Inhalte > Exportieren) und erstellt ohne weitere Fragen:

  bericht.md              Auswertung: Gewinner, Ausreißer, Muster, Trend, fällige Neuauflagen
  meine-beitraege.csv     Datenliste für das ganze KI-Team (maschinenlesbar)
  Meine Beiträge.md       dieselbe Liste als Tabelle zum Hochladen ins Projekt
  muster.md               kurze Zusammenfassung für Würfel, Hook-Sparring und Content-Tag
  *.png                   Grafiken (wenn matplotlib vorhanden ist)

Zweiter Modus: Ausreißer bei anderen Accounts (Wettbewerb), z. B. mit Daten aus vidIQ.

Aufruf:
  python content_analyse.py eigene EXPORT.csv [WEITERE.csv ...] [--alt "Meine Beiträge.md"] [--aus ordner] [--stichtag 2026-11-30]
  python content_analyse.py wettbewerb DATEN.csv [--aus ordner]

Nur Standard-Python plus pandas. matplotlib ist optional.
"""

import argparse
import os
import re
import sys
import unicodedata
from datetime import datetime, timedelta

try:
    import pandas as pd
except ImportError:  # pragma: no cover
    sys.exit("pandas fehlt. Installieren mit: pip install pandas")

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAT_PLOT = True
except Exception:  # pragma: no cover
    HAT_PLOT = False

# ---------------------------------------------------------------- Spalten erkennen

SYNONYME = {
    "datum": ["veroeffentlichungszeitpunkt", "veroeffentlichungsdatum", "veroeffentlicht", "publish time",
              "publish date", "publishing time", "datum", "date", "erstellt", "created", "timestamp", "zeitpunkt"],
    "format": ["beitragstyp", "post type", "beitragsart", "medientyp", "media type", "typ", "type", "format"],
    "text": ["beschreibung", "description", "caption", "bildunterschrift", "titel", "title", "text", "thema"],
    "link": ["permalink", "link", "url", "beitragslink"],
    "id": ["beitrags-id", "beitrags id", "post id", "media id", "id", "shortcode"],
    "reichweite": ["reichweite", "reach", "erreichte konten", "accounts reached", "erreichte personen"],
    "aufrufe": ["aufrufe", "views", "wiedergaben", "plays", "impressionen", "impressions", "playcount"],
    "likes": ["gefaellt mir", "gefaellt mir-angaben", "likes", "likecount", "reaktionen", "reactions"],
    "kommentare": ["kommentare", "comments", "commentcount"],
    "weiterleitungen": ["geteilte inhalte", "geteilt", "teilen", "shares", "weiterleitungen", "sends", "mal geteilt"],
    "speicherungen": ["gespeichert", "speicherungen", "saves", "saved"],
    "follows": ["follows", "neue follower", "follower gewonnen", "followers gained", "follower"],
    "profilbesuche": ["profilaufrufe", "profilbesuche", "profile visits", "profile views", "profile activity"],
    "dauer": ["dauer (sek.)", "dauer", "duration (sec)", "duration", "laenge", "durationseconds"],
    "wiedergabezeit": ["durchschnittliche wiedergabezeit", "average watch time", "avg watch time", "avgwatchtimems"],
    "angeschaut_prozent": ["durchschnittlich angeschaut", "avgwatchedpct", "watched percentage", "wiedergabe in prozent"],
    "ueberspringrate": ["ueberspringrate", "skip rate", "skiprate", "wegwisch-rate"],
    "hook_art": ["hook-art", "hook art", "hookart"],
    "thema_manuell": ["thema (manuell)"],
    "blickwinkel": ["blickwinkel", "angle"],
    "ziel": ["ziel", "goal"],
    "saeule": ["saeule", "pillar", "content-saeule"],
    # Wettbewerb
    "account": ["account", "handle", "username", "account username", "kontoname", "userposted"],
    "angepinnt": ["ispinned", "angepinnt", "pinned"],
}


def _norm(s):
    s = str(s).strip().lower()
    s = s.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.replace('"', "").replace("'", "").replace("„", "").replace("“", "")
    return re.sub(r"\s+", " ", s)


def spalten_zuordnen(df):
    """Ordnet die Spalten eines Exports den Standardnamen zu. Gibt dict standard -> original zurück."""
    zuordnung = {}
    normiert = {c: _norm(c) for c in df.columns}
    for standard, namen in SYNONYME.items():
        # exakte Treffer zuerst, dann Teiltreffer
        for n in namen:
            treffer = [c for c, nc in normiert.items() if nc == n and c not in zuordnung.values()]
            if treffer:
                zuordnung[standard] = treffer[0]
                break
        if standard in zuordnung:
            continue
        for n in namen:
            if len(n) < 4:
                continue
            treffer = [c for c, nc in normiert.items() if n in nc and c not in zuordnung.values()]
            if treffer:
                zuordnung[standard] = treffer[0]
                break
    return zuordnung


def _zahl(x):
    if pd.isna(x):
        return float("nan")
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x).strip().replace(" ", "").replace(" ", "")
    if s in ("", "-", "–", "n/a", "na", "none", "null"):
        return float("nan")
    s = s.replace("%", "")
    faktor = 1
    m = re.fullmatch(r"([\d.,]+)(k|tsd\.?|mio\.?|m)", s.lower())
    if m:
        s, faktor = m.group(1), (1000 if m.group(2)[0] in "kt" else 1000000)
    # 1.234,5 (deutsch) oder 1,234.5 (englisch)
    if "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "." in s and re.fullmatch(r"\d{1,3}(\.\d{3})+", s):
        s = s.replace(".", "")
    elif "," in s:
        teile = s.split(",")
        s = s.replace(",", "") if len(teile[-1]) == 3 and len(teile) > 1 else s.replace(",", ".")
    try:
        return float(s) * faktor
    except ValueError:
        return float("nan")


def datei_lesen(pfad, als_text=False):
    # als_text: alles als Text lesen (für die alte Liste, sonst wird aus "2.950" die Zahl 2,95)
    extra = {"dtype": str, "keep_default_na": False} if als_text else {}
    if pfad.lower().endswith((".xlsx", ".xls")):
        return pd.read_excel(pfad, **extra)
    for enc in ("utf-8-sig", "utf-16", "latin-1"):
        try:
            return pd.read_csv(pfad, sep=None, engine="python", encoding=enc, **extra)
        except Exception:
            continue
    sys.exit(f"Konnte {pfad} nicht lesen. Ist das eine CSV- oder Excel-Datei?")


def md_tabelle_lesen(pfad):
    """Liest eine Markdown-Tabelle (z. B. die alte 'Meine Beiträge.md')."""
    zeilen = [z.strip() for z in open(pfad, encoding="utf-8") if z.strip().startswith("|")]
    if len(zeilen) < 2:
        return pd.DataFrame()
    kopf = [c.strip() for c in zeilen[0].strip("|").split("|")]
    daten = []
    for z in zeilen[2:]:
        zellen = [c.strip() for c in z.strip("|").split("|")]
        if len(zellen) == len(kopf):
            daten.append(zellen)
    return pd.DataFrame(daten, columns=kopf)


def vereinheitlichen(df, quelle):
    z = spalten_zuordnen(df)
    out = pd.DataFrame()
    for standard, original in z.items():
        out[standard] = df[original]
    # Meta-Exporte haben manchmal eine zweite Kopfzeile (z. B. "Lifetime"): Zeilen ohne Zahlen raus
    zahlspalten = [c for c in ["reichweite", "aufrufe", "likes", "kommentare", "weiterleitungen",
                               "speicherungen", "follows", "profilbesuche", "dauer", "wiedergabezeit",
                               "angeschaut_prozent", "ueberspringrate"] if c in out]
    for c in zahlspalten:
        out[c] = out[c].map(_zahl)
    if zahlspalten:
        out = out[out[zahlspalten].notna().any(axis=1)].copy()
    if "datum" in out:
        out["datum"] = datum_lesen(out["datum"])
    out["quelle"] = os.path.basename(quelle)
    return out, z


def _zeit(werte, **kw):
    """pd.to_datetime mit Rückfall für ältere pandas-Versionen (ohne format='ISO8601'/'mixed')."""
    try:
        return pd.to_datetime(werte, errors="coerce", **kw)
    except (TypeError, ValueError):
        kw.pop("format", None)
        return pd.to_datetime(werte, errors="coerce", **kw)


def datum_lesen(serie):
    s = serie.astype(str).str.strip()
    iso = s.str.match(r"^\d{4}-\d{2}-\d{2}")
    erg = pd.Series(pd.NaT, index=s.index, dtype="datetime64[ns]")
    if iso.any():
        # Mit Zeitzone (z. B. vidIQ "...Z"): in deutsche Zeit umrechnen, sonst stimmen Uhrzeit und Wochentag nicht
        mit_tz = iso & s.str.contains(r"(?:Z|[+-]\d{2}:?\d{2})$")
        if mit_tz.any():
            erg[mit_tz] = _zeit(s[mit_tz], utc=True, format="ISO8601").dt.tz_convert("Europe/Berlin").dt.tz_localize(None)
        ohne_tz = iso & ~mit_tz
        if ohne_tz.any():
            erg[ohne_tz] = _zeit(s[ohne_tz], format="ISO8601")
    rest = ~iso & ~s.isin(["", "nan", "NaT", "None"])
    if rest.any():
        # Tag/Monat-Reihenfolge an der ganzen Spalte erkennen: deutsch 13.08.2026, US-englisch 08/13/2026
        teile = s[rest].str.extract(r"^(\d{1,2})[./-](\d{1,2})[./-]\d{2,4}")
        erster = pd.to_numeric(teile[0], errors="coerce")
        zweiter = pd.to_numeric(teile[1], errors="coerce")
        if (erster > 12).any():
            tag_zuerst = True
        elif (zweiter > 12).any():
            tag_zuerst = False
        else:
            tag_zuerst = not s[rest].str.contains("/").any()
            if not tag_zuerst:
                print("Hinweis: Datumsangaben mit / ohne eindeutigen Tag über 12 gefunden. "
                      "Gelesen als Monat/Tag/Jahr (englischer Export). Bitte Daten im Bericht kurz prüfen.")
        erg[rest] = _zeit(s[rest], dayfirst=tag_zuerst, format="mixed")
    return erg


FORMAT_MAP = [
    ("reel", "Reel"), ("video", "Reel"), ("clip", "Reel"),
    ("karussell", "Karussell"), ("carousel", "Karussell"), ("album", "Karussell"),
    ("bild", "Einzelbild"), ("image", "Einzelbild"), ("foto", "Einzelbild"), ("photo", "Einzelbild"),
    ("story", "Story"),
]


def format_normieren(x):
    s = _norm(x)
    for schluessel, name in FORMAT_MAP:
        if schluessel in s:
            return name
    return str(x).strip() if str(x).strip() and str(x) != "nan" else "unbekannt"


# ---------------------------------------------------------------- Rechnen

BASISNAME = "Reichweite"

QUOTEN = [("likes", "Likes/R"), ("kommentare", "Komm./R"), ("weiterleitungen", "Weiterl./R"),
          ("speicherungen", "Speich./R"), ("follows", "Follows/R"), ("profilbesuche", "Profil/R")]


def robust_z(werte):
    """Robuster z-Wert über Median und MAD. Unempfindlich gegen einzelne Ausreißer."""
    s = pd.Series(werte, dtype=float)
    med = s.median()
    mad = (s - med).abs().median()
    if not mad or pd.isna(mad):
        mad = s.std() / 1.4826 if s.std() else 1.0
    return (s - med) / (1.4826 * mad)


def auswerten(df, stichtag):
    df = df.copy()
    global BASISNAME
    nenner = "reichweite" if "reichweite" in df and df["reichweite"].notna().sum() >= max(1, len(df) // 2) else "aufrufe"
    BASISNAME = "Reichweite" if nenner == "reichweite" else "Aufrufe"
    df["_basis"] = df.get(nenner)
    for spalte, name in QUOTEN:
        if spalte in df and "_basis" in df:
            df[name] = df[spalte] / df["_basis"] * 100  # ungerundet rechnen, gerundet wird erst in der Ausgabe
    df["alter_tage"] = (stichtag - df["datum"]).dt.days if "datum" in df else 999
    df["bewertbar"] = df["alter_tage"] >= 7

    bewertet = df[df["bewertbar"]]
    signale = [n for _, n in QUOTEN if n in df and df[n].notna().any()]
    haupt = [s for s in ["Weiterl./R", "Speich./R"] if s in signale] or signale[:2]

    urteile, gruende, faktoren = [], [], []
    for idx, zeile in df.iterrows():
        if pd.isna(zeile["alter_tage"]):
            urteile.append("offen")
            gruende.append("Datum nicht erkannt")
            faktoren.append(float("nan"))
            continue
        if not zeile["bewertbar"]:
            urteile.append("zu früh")
            gruende.append(f"erst {int(zeile['alter_tage'])} Tage alt, in {7 - int(zeile['alter_tage'])} Tagen bewerten")
            faktoren.append(float("nan"))
            continue
        andere = bewertet.drop(index=idx, errors="ignore")
        if len(andere) < 2:
            urteile.append("offen")
            gruende.append("zu wenige Vergleichsbeiträge")
            faktoren.append(float("nan"))
            continue
        bester, bester_name = 0.0, ""
        unter_schnitt = False
        basis_faktor = float("nan")
        for s in haupt + ["_basis"]:
            schnitt = andere[s].mean()
            if pd.isna(zeile.get(s)) or not schnitt:
                continue
            f = zeile[s] / schnitt
            if s != "_basis" and f < 1:
                unter_schnitt = True
            if s == "_basis" and unter_schnitt:
                basis_faktor = f
                continue
            if f > bester:
                bester, bester_name = f, (BASISNAME if s == "_basis" else s)
        faktoren.append(round(bester, 2) if bester else float("nan"))
        if pd.isna(zeile.get("_basis")):
            urteile.append("offen")
            gruende.append(f"keine {BASISNAME} für diesen Beitrag im Export")
        elif bester < 1.7 and pd.notna(basis_faktor) and basis_faktor >= 2:
            # Regel aus signale.md: viel Reichweite, aber eine Quote unter dem Schnitt
            urteile.append("Thema gut, Umsetzung schwach")
            gruende.append(f"{BASISNAME} {_f(basis_faktor)}-fach, aber Quoten unter deinem Schnitt")
        elif bester >= 2:
            urteile.append("Gewinner")
            gruende.append(f"{bester_name} {_f(bester)}-fach über deinem Schnitt")
        elif bester >= 1.7:
            urteile.append("Gewinner auf Probe")
            gruende.append(f"{bester_name} {_f(bester)}-fach, in 2 Wochen nochmal prüfen")
        elif bester >= 0.8:
            urteile.append("solide")
            gruende.append("im Rahmen deines Schnitts")
        else:
            urteile.append("schwach")
            gruende.append(f"bestes Signal nur {_f(bester)}-fach deines Schnitts")
    df["urteil"] = urteile
    df["grund"] = gruende
    df["faktor"] = faktoren

    # Ausreißer: robust, getrennt nach Format, ab 4 bewertbaren Beiträgen pro Format
    df["ausreisser"] = ""
    for fmt, gruppe in df[df["bewertbar"]].groupby("format_n"):
        if len(gruppe) < 4:
            continue
        for s in ["_basis"] + haupt:
            if s not in gruppe or gruppe[s].notna().sum() < 4:
                continue
            werte = gruppe[s].clip(lower=0) + 1e-9
            z = robust_z(werte.map(lambda v: __import__("math").log10(v + 1)))
            name = BASISNAME if s == "_basis" else s
            for idx, zz in z.items():
                if zz >= 2:
                    df.at[idx, "ausreisser"] += f"{name} nach oben; "
                elif zz <= -2:
                    df.at[idx, "ausreisser"] += f"{name} nach unten; "
        if "ueberspringrate" in gruppe and gruppe["ueberspringrate"].notna().sum() >= 4:
            z = robust_z(gruppe["ueberspringrate"])
            for idx, zz in z.items():
                if zz <= -2:
                    df.at[idx, "ausreisser"] += "Überspringrate auffällig niedrig (starker Einstieg); "
                elif zz >= 2:
                    df.at[idx, "ausreisser"] += "Überspringrate auffällig hoch (Einstieg verliert); "
    df["ausreisser"] = df["ausreisser"].str.rstrip("; ")

    # Neuauflagen
    df["naechste_version"] = ""
    for idx, zeile in df.iterrows():
        if zeile["urteil"] == "Gewinner" and pd.notna(zeile.get("datum")):
            v2 = zeile["datum"] + timedelta(days=90)
            df.at[idx, "naechste_version"] = (
                "überfällig, so bald wie möglich" if v2 < stichtag else v2.strftime("%d.%m.%Y"))
    return df, nenner, signale, haupt


def muster_finden(df, haupt):
    """Gruppen, die sich deutlich vom eigenen Median abheben. Nur mit mindestens 2 Beiträgen."""
    b = df[df["bewertbar"]].copy()
    if len(b) < 6:
        return []
    ziel = haupt[0] if haupt else "_basis"
    gesamt_basis = b["_basis"].median()
    gesamt_ziel = b[ziel].median() if ziel in b else float("nan")
    b["wochentag"] = b["datum"].dt.day_name().map({
        "Monday": "Montag", "Tuesday": "Dienstag", "Wednesday": "Mittwoch", "Thursday": "Donnerstag",
        "Friday": "Freitag", "Saturday": "Samstag", "Sunday": "Sonntag"}) if "datum" in b else None
    b["uhrzeit"] = b["datum"].dt.hour.map(lambda h: "morgens (5 bis 11 Uhr)" if 5 <= h < 11 else
                                          "mittags (11 bis 15 Uhr)" if 11 <= h < 15 else
                                          "nachmittags (15 bis 19 Uhr)" if 15 <= h < 19 else "abends/nachts") if "datum" in b else None
    if "text" in b:
        erste = b["text"].fillna("").astype(str).str.split(r"[\n.!?]", n=1, regex=True).str[0]
        b["einstieg"] = erste.map(lambda t: "Frage im ersten Satz" if "?" in t[:200] else
                                  "Zahl im ersten Satz" if re.search(r"\d", t) else "Aussage im ersten Satz")
        b["caption_laenge"] = b["text"].fillna("").astype(str).str.len().map(
            lambda n: "kurze Caption (unter 300 Zeichen)" if n < 300 else
            "mittlere Caption (300 bis 1.000)" if n < 1000 else "lange Caption (über 1.000)")
    if "dauer" in b and b["dauer"].notna().sum() >= 4:
        b["laenge"] = b["dauer"].map(lambda d: "" if pd.isna(d) else "Reel unter 30 Sekunden" if d < 30 else
                                     "Reel 30 bis 60 Sekunden" if d <= 60 else "Reel über 60 Sekunden")
    ergebnisse = []
    for merkmal in ["format_n", "wochentag", "uhrzeit", "einstieg", "caption_laenge", "laenge", "hook_art", "blickwinkel", "saeule"]:
        if merkmal not in b or b[merkmal] is None:
            continue
        for wert, g in b.groupby(merkmal):
            if not str(wert).strip() or str(wert) == "nan" or len(g) < (3 if merkmal in ("wochentag", "uhrzeit") else 2):
                continue
            if merkmal == "format_n" and b["format_n"].nunique() < 2:
                continue
            fb = g["_basis"].median() / gesamt_basis if gesamt_basis else float("nan")
            fz = g[ziel].median() / gesamt_ziel if ziel in g and gesamt_ziel else float("nan")
            staerke = max(abs((fb or 1) - 1), abs((fz if pd.notna(fz) else 1) - 1))
            skip = round(g["ueberspringrate"].median(), 1) if "ueberspringrate" in g and g["ueberspringrate"].notna().any() else None
            if staerke >= 0.3:
                ergebnisse.append({
                    "merkmal": wert, "n": len(g), "reichweite_faktor": round(fb, 2) if pd.notna(fb) else None,
                    "ziel_faktor": round(fz, 2) if pd.notna(fz) else None, "ziel": ziel,
                    "sicherheit": "Muster" if len(g) >= 5 else "Tendenz", "skip": skip,
                })
    ergebnisse.sort(key=lambda e: -max(abs((e["reichweite_faktor"] or 1) - 1), abs((e["ziel_faktor"] or 1) - 1)))
    return ergebnisse[:8]


def trend_pruefen(df, stichtag):
    if "datum" not in df or df["datum"].isna().all():
        return None
    # Nur bewertbare Beiträge: ganz frische Beiträge haben ihre Reichweite noch nicht und täuschen sonst einen Einbruch vor
    d = df[df["bewertbar"]].dropna(subset=["datum"]).copy()
    d["woche"] = d["datum"].dt.to_period("W").dt.start_time
    woche = d.groupby("woche")["_basis"].median()
    if len(woche) < 6:
        return {"status": "zu wenig Daten", "woche": woche}
    letzte3 = woche.iloc[-3:]
    basis = woche.iloc[-15:-3].median()
    if not basis:
        return {"status": "zu wenig Daten", "woche": woche}
    verhaeltnis = letzte3.median() / basis
    if (letzte3 < 0.7 * basis).all():
        status = "Einbruch"
    elif verhaeltnis >= 1.3:
        status = "Aufwärtstrend"
    elif verhaeltnis < 0.7:
        status = "deutlich unter Schnitt, aber noch kein Einbruch (nicht alle 3 Wochen klar darunter), beobachten"
    elif verhaeltnis <= 0.85:
        status = "leicht unter Schnitt, normale Schwankung"
    else:
        status = "stabil"
    return {"status": status, "verhaeltnis": round(verhaeltnis, 2), "basis": basis,
            "letzte3": letzte3, "woche": woche}


# ---------------------------------------------------------------- Ausgabe

def _p(x, nachkomma=1):
    if x is None or pd.isna(x):
        return ""
    return f"{x:,.{nachkomma}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _f(x):
    return _p(x, 1)


def _ganz(x):
    if x is None or pd.isna(x):
        return ""
    return f"{int(round(x)):,}".replace(",", ".")


def _titel(zeile, n=60):
    for s in ["thema_manuell", "text"]:
        t = zeile.get(s)
        if isinstance(t, str) and t.strip():
            t = re.sub(r"\s+", " ", t.strip())
            return (t[:n] + "…") if len(t) > n else t
    return zeile.get("link", "") or "ohne Titel"


def grafiken(df, trend, aus, haupt):
    if not HAT_PLOT:
        return []
    dateien = []
    farbe_haupt, farbe_grau, farbe_gold = "#2B4A38", "#9AA79B", "#C9A227"
    if trend and "woche" in trend and len(trend["woche"]) >= 2:
        fig, ax = plt.subplots(figsize=(8, 3.6))
        w = trend["woche"]
        ax.plot(w.index, w.values, color=farbe_haupt, linewidth=2, marker="o", markersize=3)
        if trend.get("basis"):
            ax.axhline(trend["basis"], color=farbe_grau, linestyle="--", linewidth=1, label="dein Schnitt")
            ax.legend(frameon=False)
        ax.set_title(f"{BASISNAME} pro Beitrag, Median je Woche", loc="left", fontsize=11)
        ax.spines[["top", "right"]].set_visible(False)
        fig.autofmt_xdate()
        p = os.path.join(aus, "reichweite_verlauf.png")
        fig.tight_layout(); fig.savefig(p, dpi=160); plt.close(fig)
        dateien.append(p)
    if haupt and haupt[0] in df:
        b = df[df["bewertbar"] & df[haupt[0]].notna()]
        if len(b) >= 3:
            fig, ax = plt.subplots(figsize=(8, 4.2))
            farben = [farbe_gold if u == "Gewinner" else farbe_haupt if "Probe" in u else farbe_grau for u in b["urteil"]]
            ax.scatter(b["_basis"], b[haupt[0]], c=farben, s=40)
            ax.set_xscale("log")
            ax.set_xlabel(f"{BASISNAME} (log)"); ax.set_ylabel(f"{haupt[0]} in %")
            ax.set_title(f"Jeder Punkt ein Beitrag. Gold = Gewinner", loc="left", fontsize=11)
            ax.spines[["top", "right"]].set_visible(False)
            for _, z in b.nlargest(3, haupt[0]).iterrows():
                ax.annotate(_titel(z, 28), (z["_basis"], z[haupt[0]]), fontsize=7, xytext=(4, 4), textcoords="offset points")
            p = os.path.join(aus, "gewinner_karte.png")
            fig.tight_layout(); fig.savefig(p, dpi=160); plt.close(fig)
            dateien.append(p)
    return dateien


LISTEN_SPALTEN = ["Datum", "Thema", "Blickwinkel", "Format", "Ziel", "Hook-Art", "Reichweite", "Weiterl./R",
                  "Speich./R", "Profil/R", "Gewinner", "Nächste Version", "Link"]


def _schluessel_df(z):
    link = z.get("link")
    if isinstance(link, str) and link.strip():
        return link.strip()
    datum = z["datum"].strftime("%d.%m.%Y") if pd.notna(z.get("datum")) else ""
    return f"{datum}|{_titel(z, 70)[:25]}"


def handspalten_uebernehmen(df, alt):
    """Hook-Art und Blickwinkel aus der alten Liste in die Daten holen, damit die Muster sie auswerten können."""
    if alt is None or not len(alt):
        return df
    df = df.copy()
    alt_map = {}
    for _, r in alt.iterrows():
        k = str(r.get("Link", "")).strip() or f"{r.get('Datum', '')}|{str(r.get('Thema', ''))[:25]}"
        alt_map[k] = r
    for spalte, alt_spalte in [("hook_art", "Hook-Art"), ("blickwinkel", "Blickwinkel"), ("ziel", "Ziel")]:
        if spalte not in df:
            df[spalte] = ""
        for idx, z in df.iterrows():
            vorhanden = z.get(spalte)
            if isinstance(vorhanden, str) and vorhanden.strip():
                continue
            a = alt_map.get(_schluessel_df(z))
            if a is not None and str(a.get(alt_spalte, "")).strip():
                df.at[idx, spalte] = str(a[alt_spalte]).strip()
    return df


def liste_bauen(df, alt):
    zeilen = []
    for _, z in df.sort_values("datum", ascending=False).iterrows():
        gewinner = {"Gewinner": "ja", "Gewinner auf Probe": "auf Probe", "zu früh": "offen", "offen": "offen"}.get(z["urteil"], "nein")
        zeilen.append({
            "Datum": z["datum"].strftime("%d.%m.%Y") if pd.notna(z.get("datum")) else "",
            "Thema": _titel(z, 70), "Blickwinkel": z.get("blickwinkel", "") if isinstance(z.get("blickwinkel"), str) else "",
            "Format": z.get("format_n", ""), "Ziel": z.get("ziel", "") if isinstance(z.get("ziel"), str) else "",
            "Hook-Art": z.get("hook_art", "") if isinstance(z.get("hook_art"), str) else "",
            "Reichweite": _ganz(z.get("_basis")), "Weiterl./R": _p(z.get("Weiterl./R"), 2),
            "Speich./R": _p(z.get("Speich./R"), 2), "Profil/R": _p(z.get("Profil/R"), 2),
            "Gewinner": gewinner, "Nächste Version": z.get("naechste_version", ""),
            "Link": z.get("link", "") if isinstance(z.get("link"), str) else "",
        })
    neu = pd.DataFrame(zeilen, columns=LISTEN_SPALTEN)
    if alt is not None and len(alt):
        # handgepflegte Spalten aus der alten Liste übernehmen, alte Zeilen ohne neue Daten behalten
        alt = alt.copy()
        for c in LISTEN_SPALTEN:
            if c not in alt:
                alt[c] = ""
        schluessel = lambda r: (str(r.get("Link", "")).strip() or f"{r.get('Datum','')}|{str(r.get('Thema',''))[:25]}")
        alt_map = {schluessel(r): r for _, r in alt.iterrows()}
        for i, r in neu.iterrows():
            a = alt_map.pop(schluessel(r), None)
            if a is not None:
                for c in ["Blickwinkel", "Ziel", "Hook-Art"]:
                    if not str(r[c]).strip() and str(a.get(c, "")).strip():
                        neu.at[i, c] = a[c]
                if str(a.get("Nächste Version", "")).startswith("erledigt"):
                    neu.at[i, "Nächste Version"] = a["Nächste Version"]
        if alt_map:
            neu = pd.concat([neu, pd.DataFrame(list(alt_map.values()))[LISTEN_SPALTEN]], ignore_index=True)
    return neu


def md_tabelle(df):
    kopf = "| " + " | ".join(df.columns) + " |\n| " + " | ".join("---" for _ in df.columns) + " |\n"
    zeilen = "".join("| " + " | ".join("" if (not isinstance(v, str) and pd.isna(v)) else str(v).replace("|", "/").replace("\n", " ")
                                       for v in r) + " |\n" for r in df.values)
    return kopf + zeilen


def bericht_schreiben(df, nenner, signale, haupt, muster, trend, zuordnung, aus, grafikdateien, stichtag):
    b = df[df["bewertbar"]]
    L = []
    L.append(f"# Content-Auswertung vom {stichtag.strftime('%d.%m.%Y')}\n")
    zeitraum = ""
    if df["datum"].notna().any():
        zeitraum = f"{df['datum'].min().strftime('%d.%m.%Y')} bis {df['datum'].max().strftime('%d.%m.%Y')}"
    L.append(f"{len(df)} Beiträge ({zeitraum}), davon {len(b)} bewertbar (älter als 7 Tage). "
             f"Quoten gerechnet pro {'Reichweite' if nenner == 'reichweite' else 'Aufrufe (keine Reichweite im Export)'}.\n")
    ohne_basis = int(df["_basis"].isna().sum())
    if ohne_basis:
        L.append(f"Bei {ohne_basis} Beiträgen fehlt die {BASISNAME} im Export. Sie bleiben „offen“ und zählen nicht in die Schnitte.\n")
    fehlend = [n for n in ["reichweite", "weiterleitungen", "speicherungen", "profilbesuche"] if n not in zuordnung]
    if fehlend:
        L.append(f"Nicht im Export gefunden: {', '.join(fehlend)}. Mehr Spalten im Export ergeben eine genauere Auswertung.\n")

    gew = df[df["urteil"] == "Gewinner"].sort_values("faktor", ascending=False)
    L.append("## Das lief richtig gut\n")
    if len(gew):
        for _, z in gew.head(5).iterrows():
            L.append(f"- **{_titel(z)}** ({z.get('format_n','')}, {z['datum'].strftime('%d.%m.') if pd.notna(z.get('datum')) else ''}): {z['grund']}. {BASISNAME} {_ganz(z['_basis'])}.")
    else:
        # nur Beiträge zeigen, die wirklich mindestens im eigenen Schnitt liegen
        top = b[b["faktor"] >= 1].sort_values("faktor", ascending=False).head(3)
        for _, z in top.iterrows():
            L.append(f"- **{_titel(z)}**: {z['grund']}, {BASISNAME} {_ganz(z['_basis'])}.")
        L.append("- Noch kein klarer Gewinner (doppelt so gut wie dein Schnitt). Das ist am Anfang normal.")
    L.append("")

    ausr = df[df["ausreisser"] != ""]
    L.append("## Ausreißer (automatisch gefunden)\n")
    if len(ausr):
        for _, z in ausr.iterrows():
            L.append(f"- **{_titel(z)}** ({z.get('format_n','')}): {z['ausreisser']}.")
        L.append("\nAusreißer nach oben sind Kandidaten zum Nachbauen, Ausreißer nach unten zeigen, was du lassen kannst.")
    else:
        L.append("Keine statistischen Ausreißer. Ab etwa 4 bewertbaren Beiträgen pro Format wird gesucht.")
    L.append("")

    L.append("## Muster in deinen Zahlen\n")
    if muster:
        for m in muster:
            teile = []
            if m["reichweite_faktor"]:
                teile.append(f"{BASISNAME} {_f(m['reichweite_faktor'])}-fach")
            if m["ziel_faktor"]:
                teile.append(f"{m['ziel']} {_f(m['ziel_faktor'])}-fach")
            if m.get("skip") is not None:
                teile.append(f"Überspringrate {_f(m['skip'])} %")
            L.append(f"- **{m['merkmal']}** ({m['n']} Beiträge, {m['sicherheit']}): {', '.join(teile)} im Vergleich zu deinem Median.")
        L.append("\n„Tendenz“ heißt: unter 5 Beiträgen, noch kein sicheres Muster.")
    else:
        L.append("Noch keine belastbaren Muster. Ab etwa 6 bewertbaren Beiträgen wird gesucht.")
    L.append("")

    L.append("## Trend\n")
    if trend and trend["status"] != "zu wenig Daten":
        L.append(f"Status: **{trend['status']}**. Die letzten 3 Wochen liegen bei {_p(trend['verhaeltnis'] * 100, 0)} % "
                 f"deiner üblichen {BASISNAME} pro Beitrag (Median der Wochen davor: {_ganz(trend['basis'])}).")
        if trend["status"] == "Einbruch":
            L.append("\n**Echter Einbruch nach Faustregel (3 Wochen am Stück klar unter Schnitt). Jetzt den Notfallplan starten, nichts löschen.**")
    else:
        L.append("Für einen Trend braucht es Beiträge aus mindestens 6 Wochen.")
    L.append("")

    if "ueberspringrate" in df and df["ueberspringrate"].notna().sum() >= 4:
        L.append("## Einstiege, die halten (niedrigste Überspringrate)\n")
        s = df[df["ueberspringrate"].notna()].sort_values("ueberspringrate")
        for _, z in s.head(5).iterrows():
            L.append(f"- {_f(z['ueberspringrate'])} % · „{_titel(z, 80)}“ ({_ganz(z['_basis'])} {BASISNAME})")
        L.append("\nUnter etwa 45 % ist stark, um 60 % hat der Einstieg nicht gezogen (Faustregel aus dem Kurs). Am Ende:")
        for _, z in s.tail(3).iterrows():
            L.append(f"- {_f(z['ueberspringrate'])} % · „{_titel(z, 80)}“")
        L.append("")

    faellig = df[df["naechste_version"] != ""]
    L.append("## Fällige Neuauflagen\n")
    if len(faellig):
        for _, z in faellig.sort_values("datum").iterrows():
            L.append(f"- **{_titel(z)}**: Version 2 {z['naechste_version']}.")
    else:
        L.append("Noch keine. Gewinner bekommen automatisch ein Datum (etwa 3 Monate nach dem Original).")
    L.append("")

    L.append("## Alle Beiträge\n")
    tab = []
    for _, z in df.sort_values("datum", ascending=False).iterrows():
        tab.append([z["datum"].strftime("%d.%m.%y") if pd.notna(z.get("datum")) else "", _titel(z, 45), z.get("format_n", ""),
                    _ganz(z["_basis"]), *[_p(z.get(s), 2) for s in signale[:4]],
                    *([_f(z.get("ueberspringrate"))] if "ueberspringrate" in df else []), z["urteil"]])
    L.append(md_tabelle(pd.DataFrame(tab, columns=["Datum", "Beitrag", "Format", BASISNAME, *signale[:4],
                                                   *(["Überspr. %"] if "ueberspringrate" in df else []), "Urteil"])))
    L.append("\nRechnung: Quote = Signal geteilt durch Reichweite mal 100. Gewinner = Weiterleitungen, Speicherungen oder Reichweite "
             "etwa doppelt so hoch wie der Schnitt deiner übrigen bewertbaren Beiträge. Faustregel, kein Gesetz.\n")
    if grafikdateien:
        L.append("Grafiken: " + ", ".join(os.path.basename(g) for g in grafikdateien))
    open(os.path.join(aus, "bericht.md"), "w", encoding="utf-8").write("\n".join(L))


def muster_datei(df, muster, haupt, aus):
    gew = df[df["urteil"] == "Gewinner"]
    L = ["# Muster (für Würfel, Hook-Sparring und Content-Tag)\n",
         f"Stand: {datetime.now().strftime('%d.%m.%Y')}. Erzeugt vom Insights-Analyst. Nicht von Hand ändern.\n",
         "## Was bei mir funktioniert"]
    for m in muster:
        if (m["reichweite_faktor"] or 0) > 1 or (m["ziel_faktor"] or 0) > 1:
            L.append(f"- {m['merkmal']} ({m['sicherheit']}, {m['n']} Beiträge)")
    L.append("\n## Was bei mir schwächer läuft")
    for m in muster:
        if (m["reichweite_faktor"] or 2) < 1 and (m["ziel_faktor"] or 2) < 1:
            L.append(f"- {m['merkmal']} ({m['sicherheit']}, {m['n']} Beiträge)")
    L.append("\n## Meine stärksten Einstiege (erste Sätze der Gewinner)")
    for _, z in gew.sort_values("faktor", ascending=False).head(8).iterrows():
        t = str(z.get("text", "") or "")
        erster = re.split(r"(?<=[.!?])\s|\n", t.strip(), maxsplit=1)[0][:140] if t.strip() else _titel(z)
        L.append(f"- „{erster}“ ({z.get('format_n','')}, {z['grund']})")
    if "ueberspringrate" in df and df["ueberspringrate"].notna().sum() >= 4:
        L.append("\n## Einstiege mit der niedrigsten Überspringrate")
        for _, z in df[df["ueberspringrate"].notna()].sort_values("ueberspringrate").head(5).iterrows():
            L.append(f"- „{_titel(z, 120)}“ ({_f(z['ueberspringrate'])} %)")
    open(os.path.join(aus, "muster.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")


def modus_eigene(args):
    teile, zuordnung = [], {}
    for pfad in args.dateien:
        df, z = vereinheitlichen(datei_lesen(pfad), pfad)
        teile.append(df)
        zuordnung.update(z)
    df = pd.concat(teile, ignore_index=True)
    if "link" in df:
        # nur echte Links abgleichen: Zeilen ohne Link dürfen nicht zu einer einzigen zusammenfallen
        doppelt = df["link"].notna() & (df["link"].astype(str).str.strip() != "") & df.duplicated(subset=["link"], keep="last")
        df = df[~doppelt].copy()
    if "datum" not in df or df["datum"].isna().all():
        sys.exit("Keine Datumsspalte erkannt. Bitte den Export mit Veröffentlichungsdatum nutzen.")
    if "reichweite" not in df and "aufrufe" not in df:
        sys.exit("Weder Reichweite noch Aufrufe erkannt. Gefundene Spalten: " + ", ".join(zuordnung.values()))
    df["format_n"] = df["format"].map(format_normieren) if "format" in df else "unbekannt"
    stichtag = pd.Timestamp(args.stichtag) if args.stichtag else df["datum"].max().normalize() + pd.Timedelta(days=1)
    df, nenner, signale, haupt = auswerten(df, stichtag)
    alt = None
    if args.alt and os.path.exists(args.alt):
        alt = md_tabelle_lesen(args.alt) if args.alt.endswith(".md") else datei_lesen(args.alt, als_text=True)
        df = handspalten_uebernehmen(df, alt)
    elif args.alt:
        print(f"Hinweis: --alt {args.alt} nicht gefunden. Handgepflegte Spalten werden nicht übernommen.")
    muster = muster_finden(df, haupt)
    trend = trend_pruefen(df, stichtag)
    os.makedirs(args.aus, exist_ok=True)
    liste = liste_bauen(df, alt)
    liste.to_csv(os.path.join(args.aus, "meine-beitraege.csv"), index=False, encoding="utf-8")
    kopf = ("# Meine Beiträge\n\nErzeugt vom Insights-Analyst. Spalten Blickwinkel, Ziel und Hook-Art darfst du von Hand ergänzen, "
            "sie bleiben bei der nächsten Auswertung erhalten.\n\n")
    open(os.path.join(args.aus, "Meine Beiträge.md"), "w", encoding="utf-8").write(kopf + md_tabelle(liste))
    g = grafiken(df, trend, args.aus, haupt)
    bericht_schreiben(df, nenner, signale, haupt, muster, trend, zuordnung, args.aus, g, stichtag)
    muster_datei(df, muster, haupt, args.aus)
    print(f"Fertig: {len(df)} Beiträge ausgewertet. Erkannte Spalten: "
          + ", ".join(f"{k}={v}" for k, v in zuordnung.items()))
    print("Gewinner:", int((df["urteil"] == "Gewinner").sum()), "| Ausreißer:", int((df["ausreisser"] != "").sum()),
          "| Trend:", trend["status"] if trend else "keine Daten")
    print("Dateien in:", os.path.abspath(args.aus))


def modus_wettbewerb(args):
    teile = []
    for pfad in args.dateien:
        df, z = vereinheitlichen(datei_lesen(pfad), pfad)
        teile.append(df)
    df = pd.concat(teile, ignore_index=True)
    if "account" not in df:
        df["account"] = "unbekannt"
    if "angepinnt" in df:
        # angepinnte Reels sind meist alte Hits und verzerren den Schnitt des Accounts
        gepinnt = df["angepinnt"].astype(str).str.strip().str.lower().isin(["true", "1", "ja", "yes", "wahr"])
        if gepinnt.any():
            print(f"Hinweis: {int(gepinnt.sum())} angepinnte Reels nicht mitgerechnet.")
        df = df[~gepinnt].copy()
    basis = "aufrufe" if "aufrufe" in df and df["aufrufe"].notna().any() else "reichweite" if "reichweite" in df else None
    if not basis:
        sys.exit("Keine Spalte mit Aufrufen gefunden.")
    df["median_account"] = df.groupby("account")[basis].transform("median")
    df["faktor"] = (df[basis] / df["median_account"]).round(1)
    if "kommentare" in df:
        df["komm_pro_1000"] = (df["kommentare"] / df[basis] * 1000).round(1)
    top = df[df["faktor"] >= 3].sort_values("faktor", ascending=False)
    if len(top) < 3:
        top = df.sort_values("faktor", ascending=False).head(5)
    os.makedirs(args.aus, exist_ok=True)
    L = ["# Ausreißer bei anderen Accounts\n",
         "Faktor = Aufrufe geteilt durch den Median desselben Accounts. Ab 3-fach ist ein Beitrag ein echter Ausreißer: "
         "Das Thema oder der Einstieg hat mehr Menschen erreicht als sonst bei diesem Account.\n"]
    for acc, g in df.groupby("account"):
        L.append(f"- {acc}: {len(g)} Beiträge, Median {_ganz(g[basis].median())} Aufrufe")
    L.append("\n## Die stärksten Ausreißer\n")
    for _, z in top.iterrows():
        zusatz = f", {_p(z['komm_pro_1000'], 1)} Kommentare pro 1.000 Aufrufe" if "komm_pro_1000" in z and pd.notna(z.get("komm_pro_1000")) else ""
        markierung = ("" if z["faktor"] >= 3 else " (gut gelaufen, aber kein echter Ausreißer)" if z["faktor"] >= 2
                      else " (kein echter Ausreißer, nur der stärkste vorhandene)")
        L.append(f"- **{_f(z['faktor'])}-fach**{markierung} · {z['account']} · {_ganz(z[basis])} Aufrufe{zusatz}: {_titel(z, 90)} {z.get('link','') if isinstance(z.get('link'), str) else ''}")
    if "komm_pro_1000" in df and df["komm_pro_1000"].notna().any():
        L.append("\n## Kommentar-Magneten (die meisten Kommentare pro 1.000 Aufrufe)\n")
        L.append("Hohe Werte heißen fast immer: Kommentar-Keyword mit Freebie. Gut, um zu sehen, welche Angebote Leute haben wollen.\n")
        for _, z in df.sort_values("komm_pro_1000", ascending=False).head(5).iterrows():
            L.append(f"- {_p(z['komm_pro_1000'], 1)} · {z['account']}: {_titel(z, 90)}")
    L.append("\nNächster Schritt: Für jeden Ausreißer Thema, Einstieg und Aufbau herausziehen und mit dem Content-Würfel "
             "in deinem Thema und deinem Tonfall umsetzen. Nie kopieren.")
    open(os.path.join(args.aus, "wettbewerb.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"Fertig: {len(df)} Beiträge von {df['account'].nunique()} Accounts, {len(top)} Ausreißer. Datei: {os.path.join(args.aus, 'wettbewerb.md')}")


def main():
    p = argparse.ArgumentParser(description="Content-Analyse für das KI-Content-Team")
    p.add_argument("modus", choices=["eigene", "wettbewerb"])
    p.add_argument("dateien", nargs="+")
    p.add_argument("--alt", help="bisherige 'Meine Beiträge.md' oder meine-beitraege.csv")
    p.add_argument("--aus", default="auswertung")
    p.add_argument("--stichtag", help="Datum der Auswertung, Standard: Tag nach dem neuesten Beitrag")
    args = p.parse_args()
    modus_eigene(args) if args.modus == "eigene" else modus_wettbewerb(args)


if __name__ == "__main__":
    main()
