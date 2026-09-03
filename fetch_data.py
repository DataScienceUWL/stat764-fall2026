#!/usr/bin/env python3
"""Download the capstone datasets that are too large to ship in this repo.

The four course datasets are already in course/data/ and need nothing. This is
for the curated capstone list.

    python fetch_data.py --list           what is available
    python fetch_data.py --check          are the sources still up? (no download)
    python fetch_data.py oulad beijing    download these into course/data/external/
"""
import argparse
import pathlib
import sys
import urllib.error
import urllib.request

DEST = pathlib.Path(__file__).parent / "course" / "data" / "external"

# tier: 1 = recommended starting points, 2 = viable with more wrangling
SOURCES = {
    "loans": dict(
        tier=1, name="OpenIntro loans_full_schema", fmt="csv",
        note="10,000 Lending Club loans, documented schema. Replaces the retired "
             "Lending Club release. Clean starting point.",
        url="https://www.openintro.org/data/csv/loans_full_schema.csv"),
    "chicago_food": dict(
        tier=1, name="Chicago Food Inspections", fmt="csv",
        note="~290k inspections. Grouped (restaurants recur) AND temporal — both "
             "traps from Meeting 4 in one file. Large download.",
        url="https://data.cityofchicago.org/api/views/4ijn-s7e5/rows.csv?accessType=DOWNLOAD"),
    "oulad": dict(
        tier=1, name="Open University Learning Analytics", fmt="zip",
        note="Multi-table student data; requires joins. Grouped by student, and "
             "the outcome is defined by you.",
        manual="https://analyse.kmi.open.ac.uk/open-dataset",
        url=None),
    "beijing": dict(
        tier=2, name="Beijing PM2.5 (UCI 381)", fmt="csv",
        note="Hourly air quality. Temporal structure; missingness is real.",
        url="https://archive.ics.uci.edu/static/public/381/data.csv"),
    "scorecard": dict(
        tier=2, name="College Scorecard (most recent cohorts)", fmt="zip",
        note="Institution-level. Wide, many missing, policy-relevant. The old "
             "direct download 404s as of 2026-09-03; take the file from the "
             "landing page, or use the API (needs a free data.gov key).",
        manual="https://collegescorecard.ed.gov/data/",
        url=None),
    "faa_strikes": dict(
        tier=2, name="FAA Wildlife Strikes", fmt="zip",
        note="Ships as Microsoft Access. Converting it is either a lesson or a "
             "detour — decide before assigning. Download is behind a form.",
        manual="https://wildlife.faa.gov/home",
        url=None),
}


def check(key, spec, timeout=45):
    if not spec.get("url"):
        return None, f"manual download: {spec['manual']}"
    req = urllib.request.Request(spec["url"], method="GET",
                                 headers={"User-Agent": "STAT764/1.0",
                                          "Range": "bytes=0-2047"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            size = r.headers.get("Content-Range") or r.headers.get("Content-Length") or "?"
            return True, f"{r.status}  {r.headers.get('Content-Type','?').split(';')[0]}  {size}"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, f"{type(e).__name__}: {str(e)[:60]}"


def download(key, spec):
    DEST.mkdir(parents=True, exist_ok=True)
    out = DEST / f"{key}.{spec['fmt']}"
    print(f"  {spec['name']} -> {out.relative_to(DEST.parent.parent.parent)}")
    req = urllib.request.Request(spec["url"], headers={"User-Agent": "STAT764/1.0"})
    with urllib.request.urlopen(req, timeout=600) as r, open(out, "wb") as f:
        while chunk := r.read(1 << 20):
            f.write(chunk)
    print(f"    {out.stat().st_size / 1e6:.1f} MB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("keys", nargs="*")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    if a.list or not (a.keys or a.check):
        for tier in (1, 2):
            print(f"\nTier {tier}")
            for k, s in SOURCES.items():
                if s["tier"] == tier:
                    how = "manual" if not s.get("url") else "auto"
                    print(f"  {k:<14} {s['name']}  [{how}]")
                    print(f"  {'':<14} {s['note']}")
        print("\nDownload with:  python fetch_data.py <key> [<key> ...]")
        return

    if a.check:
        print(f"{'key':<14}{'status':<9}{'detail'}")
        bad = 0
        for k, s in SOURCES.items():
            ok, detail = check(k, s)
            label = {True: "auto", False: "BROKEN", None: "manual"}[ok]
            bad += ok is False
            print(f"{k:<14}{label:<9}{detail}")
        print("\n'manual' is expected — those sources sit behind a form or a "
              "landing page.\n'BROKEN' means the direct URL stopped working and "
              "needs fixing.")
        sys.exit(1 if bad else 0)

    for k in a.keys:
        if k not in SOURCES:
            sys.exit(f"unknown dataset '{k}' — run --list")
        spec = SOURCES[k]
        if not spec.get("url"):
            print(f"  {spec['name']}: manual download only.")
            print(f"    Get it from {spec['manual']} and put it in "
                  f"{DEST.relative_to(DEST.parent.parent.parent)}/")
            continue
        download(k, spec)


if __name__ == "__main__":
    main()
