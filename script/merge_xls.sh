#!/bin/bash

python3 - <<'PY'
import pandas as pd
from pathlib import Path

input_dir = Path("/home/thant_syn/exp/polar/data/")
output_file = Path("myPolar_master.xlsx")

dfs = []

for file in sorted(input_dir.glob("*.xls")):
    print(f"Reading: {file.name}")

    df = pd.read_excel(file, engine="xlrd")

    df["annotator"] = file.stem
    df["source_file"] = file.name

    dfs.append(df)

merged = pd.concat(dfs, ignore_index=True)

merged.to_excel(output_file, index=False, engine="openpyxl")

print("\nDone!")
print(f"Files merged: {len(dfs)}")
print(f"Total rows: {len(merged)}")
print(f"Output: {output_file}")
PY
