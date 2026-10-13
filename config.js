// =============================================================
//  EINSTELLUNGEN – nur diese Datei musst du anpassen
// =============================================================

// 1) Supabase-Zugang (Supabase → Project Settings → API / API Keys)
//    Solange hier nichts steht, speichert das Tool nur auf dem jeweiligen Handy.
window.CONFIG = {
  SUPABASE_URL: "",        // z. B. "https://abcdefgh.supabase.co"
  SUPABASE_KEY: "",        // der "anon public" bzw. "publishable" Key (NICHT den service_role / secret Key!)

  // 2) Namen der Stationen (Reihenfolge = Nummer im QR-Code-Link, ?s=1 ist die erste)
  STATIONS: [
    "Pressen 1", "Pressen 2", "Pressen 3", "Pressen 4",
    "Schrauben 1", "Schrauben 2",
    "Fügen 1", "Fügen 2",
    "Demontagewagen", "Motorprüfstand", "Automatische Pressestation"
  ],

  // 3) Stationen, deren PC mit Linux statt Windows läuft (zeigt dort die passenden Fotos)
  LINUX_STATIONS: ["Pressen 1"]
};
