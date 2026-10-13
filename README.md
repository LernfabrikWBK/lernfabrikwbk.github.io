# Stations-Check Lernfabrik

Schritt-für-Schritt-Prüfung einer Lernfabrik-Station: QR-Code an der Station scannen, Fragen mit Ja/Nein beantworten, am Ende steht fest, ob die Station einsatzbereit ist oder wer geholt werden muss. Jede Prüfung wird gespeichert, der Reiter **Auswertung** zeigt die häufigsten Ursachen.

## Dateien

| Datei | Wofür |
|---|---|
| `index.html` | Das Tool selbst (Ablauf, Auswertung) |
| `config.js` | **Einstellungen:** Supabase-Zugang und Stationsnamen |
| `qr.html` | Erzeugt druckfertige QR-Codes für alle Stationen |
| `supabase.sql` | Legt die Datenbank-Tabelle an (einmalig in Supabase ausführen) |
| `images/` | Fotos für die einzelnen Schritte (Namen siehe `images/LIESMICH.md`) |

## Links (nach dem Einrichten)

- Tool: `https://sazexlucifer1.github.io/KIT_LF_Anleitung/`
- Direkt eine Station (Nummer = Position in config.js, z. B. 3 = Pressen 3): `https://sazexlucifer1.github.io/KIT_LF_Anleitung/?s=3`
- Auswertung: `https://sazexlucifer1.github.io/KIT_LF_Anleitung/#auswertung`
- QR-Codes drucken: `https://sazexlucifer1.github.io/KIT_LF_Anleitung/qr.html`

## Wie die Auswertung zählt

Gezählt wird nur, was sicher ist:

- **Direkt gesehen:** z. B. „Ist der NUC-PC an?" → Nein ergibt „NUC-PC war aus".
- **Nachweislich geholfen:** Eine Handlung (z. B. HDMI-Kabel einstecken) zählt nur, wenn die nächste Kontrollfrage danach positiv ist. Sonst wird sie verworfen.
- **Ungelöst:** Endet die Prüfung beim Techniker oder bei Dorian, wird der Grund separat gezählt.

Den Ablauf selbst ändert man in `index.html` im Block `const FLOW={ ... }`.
