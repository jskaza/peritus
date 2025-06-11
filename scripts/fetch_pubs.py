#!/usr/bin/env python3
"""
Sync Google Scholar → publications.toml
  fields: title, pub_year, author, journal, volume, abstract, url
Install: pip install scholarly tomli-w requests-cache tqdm
"""
import argparse
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import quote_plus

import requests_cache
import tomli_w
from scholarly import ProxyGenerator, scholarly
from tqdm import tqdm

def scholar_search_url(title: str) -> str:
    """Guaranteed fallback: Google Scholar search for the full title."""
    return f"https://scholar.google.com/scholar?q={quote_plus(title)}"

def build_toml(scholar_id: str, limit: int = None) -> dict:
    # 1) Cache HTML pages for 1 day
    requests_cache.install_cache('scholarly_cache', expire_after=86400)

    # 2) Try to set up free proxies (optional, fallback to no proxy if it fails)
    try:
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        print("✅ Successfully configured free proxies")
    except Exception as e:
        print(f"⚠️  Failed to configure proxies, continuing without them: {e}")
        # Continue without proxies - this should still work for reasonable request rates

    # 3) Fetch author + publication stubs
    try:
        # Try the new API first (returns dict directly)
        author_data = scholarly.search_author_id(scholar_id)
        if isinstance(author_data, dict):
            author = scholarly.fill(author_data, sections=["publications"])
        else:
            # Fallback to old API (returns iterator)
            author = scholarly.fill(next(author_data), sections=["publications"])
    except Exception as e:
        print(f"❌ Failed to fetch author data: {e}")
        raise

    toml_data = {
        "metadata": {
            "last_updated": datetime.now().isoformat(),
            "source": "Google Scholar",
            "scholar_id": scholar_id,
            "note": "Publications automatically fetched from Google Scholar profile"
        },
        "publication": []
    }

    pubs = author["publications"]
    if limit:
        pubs = pubs[:limit]

    for stub in tqdm(pubs, desc="Fetching publication data", unit="paper"):
        try:
            pub = scholarly.fill(stub)          # one API call per paper
        except Exception as e:
            tqdm.write(f"⚠️  Failed to fill stub: {e}")
            continue

        bib = pub.get("bib", {})
        title    = bib.get("title", "")
        year     = bib.get("pub_year") or bib.get("year")
        authors  = [a.strip() for a in bib.get("author", "").split(" and ")]
        journal  = (bib.get("journal") or bib.get("booktitle")
                    or bib.get("venue") or bib.get("conference"))
        volume   = bib.get("volume")
        abstract = bib.get("abstract")

        url = (
            pub.get("pub_url")
            or pub.get("eprint_url")
            or scholar_search_url(title)
        )

        entry = {
            "title":    title,
            "pub_year": int(year) if str(year).isdigit() else year,
            "author":   authors,
            "journal":  journal,
            "volume":   volume,
            "abstract": abstract,
            "url":      url,
        }

        # drop any None-valued fields
        entry = {k: v for k, v in entry.items() if v is not None}
        toml_data["publication"].append(entry)

        time.sleep(1)   # throttle requests

    return toml_data


def main() -> None:
    ap = argparse.ArgumentParser(description="Sync Google Scholar → TOML")
    ap.add_argument("--scholar-id",
                    default="dAAMOqgAAAAJ",
                    help="Your Google Scholar author ID")
    ap.add_argument("--out",
                    default=Path(__file__).parent.parent / "data" / "publications.toml",
                    type=Path,
                    help="Output TOML file path")
    ap.add_argument("--limit",
                    type=int,
                    default=None,
                    help="Max number of publications to fetch")
    args = ap.parse_args()

    data = build_toml(args.scholar_id, limit=args.limit)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "wb") as fh:
        tomli_w.dump(data, fh)

    print(f"✅  Wrote {len(data['publication'])} entries → {args.out}")
    print(f"📅  Last updated: {data['metadata']['last_updated']}")
    print(f"🎓  Source: {data['metadata']['source']}")


if __name__ == "__main__":
    main()