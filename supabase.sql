-- =============================================================
--  Stations-Check: Tabelle für die Prüf-Ergebnisse
--  In Supabase: SQL Editor → New query → alles einfügen → Run
-- =============================================================

create table if not exists public.runs (
  id            bigint generated always as identity primary key,
  created_at    timestamptz not null default now(),
  station       text        not null,
  ts            bigint      not null,
  end_node      text        not null,
  kind          text        not null check (kind in ('ok','tech','dorian')),
  tech_note     boolean     not null default false,
  findings      jsonb       not null default '[]'::jsonb,
  unresolved    text,
  path          jsonb       not null default '[]'::jsonb,
  duration_sec  integer
);

-- Zugriff für die Webseite erlauben (nötig, falls neue Tabellen nicht automatisch freigegeben werden)
grant usage on schema public to anon, authenticated;
grant select, insert on public.runs to anon, authenticated;

-- Zugriffsschutz einschalten
alter table public.runs enable row level security;

-- Jeder darf ein neues Ergebnis eintragen (QR-Code scannen, ohne Login)
drop policy if exists "runs_insert_public" on public.runs;
create policy "runs_insert_public" on public.runs
  for insert to anon, authenticated
  with check (true);

-- Jeder darf die Ergebnisse lesen (für den Reiter "Auswertung")
drop policy if exists "runs_select_public" on public.runs;
create policy "runs_select_public" on public.runs
  for select to anon, authenticated
  using (true);

-- Ändern oder Löschen ist von außen NICHT erlaubt (keine Policy = verboten).
-- Einträge löschen kannst du selbst im Supabase Table Editor.
