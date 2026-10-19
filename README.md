# Stations-Check Lernfabrik

Schritt-für-Schritt-Prüfung einer Lernfabrik-Station: QR-Code an der Station scannen, Fragen mit Ja/Nein beantworten, am Ende steht fest, ob die Station einsatzbereit ist oder wer geholt werden muss. Jede Prüfung wird gespeichert, der Reiter **Auswertung** zeigt die häufigsten Ursachen.

## Dateien

| Datei | Wofür |
|---|---|
| `index.html` | Das Tool selbst (Ablauf, Auswertung) |
| `config.js` | **Einstellungen:** Supabase-Zugang und Stationsnamen |
| `qr.html` | Erzeugt druckfertige QR-Codes für alle Stationen (im Browser) |
| `qr-codes/` | Fertige QR-Codes: `QR-Codes_Stationen.pdf` zum Drucken (A4, 6 pro Seite), ein PNG pro Station und `erzeugen.py` zum Neu-Erstellen |
| `supabase.sql` | Legt die Datenbank-Tabelle an (einmalig in Supabase ausführen) |
| `docs/Anleitung_MES.pdf` | MES-Benutzerdokumentation (Grundlage für den MES-Guide) |
| `images/` | Fotos für die einzelnen Schritte (Namen siehe `images/LIESMICH.md`) |

## Aufbau: Werkstatt und Live-Seite

- **Werkstatt:** `SazexLucifer1/KIT_LF_Anleitung`. Hier werden Änderungen gemacht.
- **Live-Seite:** `LernfabrikWBK/lernfabrikwbk.github.io` (Fork). GitHub Pages läuft hier.
- Änderungen übernehmen: im Live-Repo **Sync fork → Update branch** klicken.

## Links

- Tool: `https://lernfabrikwbk.github.io/`
- Direkt eine Station: `https://lernfabrikwbk.github.io/?s=pressen-3` (Stationsname klein, Umlaute als ae/oe/ue, Leerzeichen als `-`)
- Auswertung: `https://lernfabrikwbk.github.io/#auswertung`
- MES-Guide (Stationen laufen schon): `https://lernfabrikwbk.github.io/?m=mes`
- QR-Codes drucken: `https://lernfabrikwbk.github.io/qr.html`

## Wie die Auswertung zählt

Gezählt wird nur, was sicher ist:

- **Direkt gesehen:** z. B. „Ist der NUC-PC an?" → Nein ergibt „NUC-PC war aus".
- **Nachweislich geholfen:** Eine Handlung (z. B. HDMI-Kabel einstecken) zählt nur, wenn die nächste Kontrollfrage danach positiv ist. Sonst wird sie verworfen.
- **Ungelöst:** Endet die Prüfung beim Techniker oder bei Dorian, wird der Grund separat gezählt.

Den Ablauf selbst ändert man in `index.html` im Block `const FLOW={ ... }`.

## QR-Codes

Die QR-Codes enthalten den **Stationsnamen**, nicht die Position in der Liste, z. B. `?s=fuegen-1`.
Sie bleiben gültig, solange sich die Adresse `lernfabrikwbk.github.io` und der Name der Station in `config.js` nicht ändern.
Neue Stationen können jederzeit ergänzt werden, die gedruckten Codes funktionieren weiter.
