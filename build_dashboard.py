#!/usr/bin/env python3
"""
Bonbeach CC — Dashboard Builder
================================
Takes players_data.json (produced by fetch_playhq_data.py) and injects it into
the dashboard template, producing a single self-contained HTML file you can
open in any browser or upload anywhere.

Run this AFTER fetch_playhq_data.py has produced players_data.json.
"""

import json

DATA_FILE = "players_data.json"
TEMPLATE_FILE = "dashboard_template.html"
OUTPUT_FILE = "Bonbeach-CC-Milestone-Dashboard-LIVE.html"
# Also written so GitHub Pages (serving from the repo root) shows the
# dashboard at the site's base URL without needing the exact filename.
PAGES_OUTPUT_FILE = "index.html"

def main():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        players_json = f.read()
        json.loads(players_json)  # sanity check it's valid JSON before we embed it

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    if "__PLAYERS_JSON__" not in html:
        raise SystemExit("ERROR: dashboard_template.html is missing the __PLAYERS_JSON__ placeholder.")

    html = html.replace("__PLAYERS_JSON__", players_json)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    with open(PAGES_OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Done! Open {OUTPUT_FILE} (or {PAGES_OUTPUT_FILE}) in your browser.")

if __name__ == "__main__":
    main()
