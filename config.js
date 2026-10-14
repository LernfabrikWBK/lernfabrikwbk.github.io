// =============================================================
//  EINSTELLUNGEN – nur diese Datei musst du anpassen
// =============================================================

// 1) Supabase-Zugang (Supabase → Project Settings → API / API Keys)
//    Solange hier nichts steht, speichert das Tool nur auf dem jeweiligen Handy.
window.CONFIG = {
  SUPABASE_URL: "https://wbmbvaqertnvfhdrsvbl.supabase.co",
  SUPABASE_KEY: "sb_publishable__tCuvT5v0UrCYIEpgUJN0w_hOAxaOqe",   // öffentlicher Key (NIE den secret / service_role Key eintragen!)

  // 2) Namen der Stationen
  //    ACHTUNG: Der QR-Code enthält den Namen (z. B. ?s=pressen-3).
  //    Einen Namen hier ändern = der gedruckte QR-Code dieser Station passt nicht mehr.
  //    Neue Stationen einfach dazuschreiben, Reihenfolge ist egal.
  STATIONS: [
    "Pressen 1", "Pressen 2", "Pressen 3", "Pressen 4",
    "Schrauben 1", "Schrauben 2",
    "Fügen 1", "Fügen 2",
    "Demontagewagen", "Motorprüfstand", "Automatische Pressestation"
  ],

  // 3) Stationen, deren PC mit Linux statt Windows läuft (zeigt dort die passenden Fotos)
  LINUX_STATIONS: ["Pressen 1"],

  // 4) Docker nach dem Anmelden: Kommt eine Abfrage (Admin/Bestätigung) oder startet Docker still von selbst?
  //    Stationen, die in keiner Liste stehen, bekommen eine Auswahl ("Abfrage kam" / "startete ohne Abfrage" / "nichts passiert").
  DOCKER_MIT_ABFRAGE:  ["Pressen 1", "Pressen 2", "Fügen 1"],
  DOCKER_OHNE_ABFRAGE: ["Pressen 3", "Pressen 4", "Fügen 2", "Schrauben 1", "Schrauben 2"]
};
