import pandas as pd
from pathlib import Path

# =========================
# Paths
# =========================
input_file = Path("/home/thant_syn/exp/polar/myPolar_master.csv")
output_dir = Path("/home/thant_syn/exp/polar/processed")

output_dir.mkdir(parents=True, exist_ok=True)

# =========================
# Read CSV
# =========================
df = pd.read_csv(input_file, encoding="utf-8")

df = df.dropna(subset=["text"])
df["text"] = df["text"].astype(str).str.strip()


# =========================
# Task 1
# Polarization Detection
# =========================
task1 = df[["id", "text", "polarization"]].copy()

task1 = task1.dropna(subset=["polarization"])

task1.to_csv(
    output_dir / "task1_polarization.txt",
    sep="|",
    index=False,
    header=True,
    encoding="utf-8"
)


# =========================
# Task 2
# Polarization Type
# =========================
task2_columns = [
    "political",
    "racial/ethnic",
    "religious",
    "gender/sexual",
    "other"
]

task2 = df[["id", "text"] + task2_columns].copy()

# Convert all Task 2 labels to 0/1
for col in task2_columns:
    task2[col] = task2[col].apply(
        lambda x: "" if pd.isna(x) else str(int(float(x)))
    )

task2.to_csv(
    output_dir / "task2_polarization_type.txt",
    sep="|",
    index=False,
    header=True,
    encoding="utf-8"
)


# =========================
# Task 3
# Polarization Manifestation
# =========================
task3_columns = [
    "stereotype",
    "vilification",
    "dehumanization",
    "extreme_language",
    "lack_of_empathy",
    "invalidation"
]

task3 = df[["id", "text"] + task3_columns].copy()

for col in task3_columns:
    task3[col] = task3[col].apply(
        lambda x: "" if pd.isna(x) else str(int(float(x)))
    )

task3.to_csv(
    output_dir / "task3_polarization_manifestation.txt",
    sep="|",
    index=False,
    header=True,
    encoding="utf-8"
)


print("Done!")
print(f"Original rows : {len(df)}")
print(f"Task 1 rows   : {len(task1)}")
print(f"Task 2 rows   : {len(task2)}")
print(f"Task 3 rows   : {len(task3)}")
