# Fotos für den Stations-Check

- `images/*.jpg` sind die Fotos, die das Tool anzeigt: verkleinert (max. 1400 px), richtig gedreht, mit einfachen Dateinamen ohne Leerzeichen und Umlaute.
- `images/original/` enthält deine Original-Fotos unverändert.

## Neues Foto hinzufügen oder austauschen

1. Foto in `images/original/` hochladen (Name egal).
2. Claude Bescheid geben. Das Foto wird dann verkleinert, umbenannt und im passenden Schritt eingetragen.

Austauschen geht auch selbst: eine Datei in `images/` mit **genau gleichem Namen** überschreiben.

## Welches Foto in welchem Schritt

| Schritt | Fotos |
|---|---|
| Start | `stationsname` |
| Welche LED-Panels leuchten? | `led-panel-vorne-an`, `led-panel-oben-an`, `station-aus` |
| Vorderes Panel in WBK-Grün? | `led-panel-vorne-an` |
| Notaus gedrückt? / lösen | `notaus-gedrueckt`, `notaus-geloest` |
| Hauptschalter aus? / einschalten | `hauptschalter-aus`, `hauptschalter-an` |
| Grüner Knopf / Kontroll-LED | `station-eingeschaltet` |
| Monitor-LED | `monitor-aus`, `monitor-an` |
| Batterieanzeige | `station-laedt`, `batterie-modus` |
| Netz- oder Batteriebetrieb, Batteriespannung | `station-laedt`, `batterie-modus` |
| Netzkabel anschließen | `kein-stecker-station`, `stecker-station`, `stecker-steckdose` |
| Normales Bild / Touch / Anmelden | `anmelden-kennwort` |
| Docker-Abfrage nach dem Anmelden | `docker-bestaetigen` |
| NUC-PC an? / einschalten | `nuc-aus`, `nuc-an` |
| RFID-Reader | `rfid-erkennt-poltopf`, `rfid-nur-gruen` |
| Smart-Light | `smartlight-gruen`, `smartlight-aus` |
| Docker gestartet? | `docker-taskleiste`, `docker-laeuft` |
| Docker als Administrator | `docker-admin-ausfuehren`, `docker-bestaetigen` |
| Docker Start-Pfeil | `docker-angehalten-start` |
| PC neu starten | `pc-neustart-windows` (Windows-Stationen), `linux-power` + `linux-neustart` (nur Linux-Stationen, siehe `LINUX_STATIONS` in config.js) |
| IO-Link-Master | `io-link-master-strom` |
| Ergebnis „einsatzbereit" (MES öffnen) | `browser-verknuepfung`, `adresse-mes`, `arbeitsstation-zuordnen` |

Noch nicht verwendet: `docker-laeuft-2`, `nur-eine-smart-led`, `switch-strom`.

Noch ohne Foto: Fernbedienung für die LED-Panels, HDMI-Kabel am NUC-PC, Stromkabel hinten am Monitor, Stromkabel am NUC-PC, Kabel hinten am Monitor (Touch).
