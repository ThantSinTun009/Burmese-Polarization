#!/bin/bash

python3 - <<'PY'
import pandas as pd
from pathlib import Path

input_dir = Path("/home/thant_syn/exp/polar/data/")
output_file = Path("/home/thant_syn/exp/polar/myPolar_master.csv")

dfs = []

for file in sorted(input_dir.glob("*.csv")):
    print(f"Reading: {file.name}")

    df = pd.read_csv(file, encoding="utf-8")

    # Add annotator and source file information
    df["annotator"] = file.stem
    df["source_file"] = file.name

    dfs.append(df)

if not dfs:
    print("ERROR: No CSV files found!")
    exit(1)

merged = pd.concat(dfs, ignore_index=True)

# Save merged CSV
merged.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("\nDone!")
print(f"Files merged: {len(dfs)}")
print(f"Total rows: {len(merged)}")
print(f"Output: {output_file}")
PY
