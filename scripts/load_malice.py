#!/usr/bin/env python3
"""Load, filter, and summarize the MALICE dataset.

Works on the bundled 30-row sample (data/sample/malice_sample.csv) and, once you have been granted
access, on the full corpus (see ACCESS.md).

Examples
--------
    python scripts/load_malice.py --path data/sample/malice_sample.csv --stats
    python scripts/load_malice.py --path data/sample/malice_sample.csv --type code-mixed
    python scripts/load_malice.py --path data/sample/malice_sample.csv --language Yoruba --limit 5
"""
from __future__ import annotations

import argparse
import sys

try:
    import pandas as pd
except ImportError:
    sys.exit("pandas is required: pip install -r requirements.txt")

EXPECTED_COLUMNS = ["seed_prompt", "malice_prompt", "type", "languages"]


def load_malice(path: str) -> "pd.DataFrame":
    """Load a MALICE CSV into a DataFrame, validating the expected schema."""
    df = pd.read_csv(path)
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(
            f"{path} is missing expected column(s): {missing}. "
            f"Found columns: {list(df.columns)}"
        )
    return df


def filter_df(df, ptype=None, language=None):
    if ptype:
        df = df[df["type"] == ptype]
    if language:
        df = df[df["languages"].str.contains(language, case=False, na=False)]
    return df


def print_stats(df) -> None:
    print(f"rows: {len(df):,}")
    print("\nby type:")
    for t, n in df["type"].value_counts().items():
        print(f"  {t:<16} {n:,}")
    print(f"\nunique seed prompts: {df['seed_prompt'].nunique():,}")
    print(f"unique language assignments: {df['languages'].nunique():,}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Load / filter / summarize the MALICE dataset.")
    ap.add_argument("--path", required=True, help="Path to a MALICE CSV file.")
    ap.add_argument("--type", choices=["code-mixed", "transliteration"], help="Filter by track.")
    ap.add_argument("--language", help="Substring match on the languages column (e.g. Yoruba).")
    ap.add_argument("--limit", type=int, default=10, help="Max rows to print (default 10).")
    ap.add_argument("--stats", action="store_true", help="Print summary statistics and exit.")
    args = ap.parse_args()

    df = load_malice(args.path)
    df = filter_df(df, args.type, args.language)

    if args.stats:
        print_stats(df)
        return

    print(f"Showing up to {args.limit} of {len(df):,} matching rows:\n")
    for _, row in df.head(args.limit).iterrows():
        print(f"[{row['type']}] {row['languages']}")
        print(f"  seed:   {row['seed_prompt'][:160]}")
        print(f"  malice: {row['malice_prompt'][:160]}")
        print()


if __name__ == "__main__":
    main()
