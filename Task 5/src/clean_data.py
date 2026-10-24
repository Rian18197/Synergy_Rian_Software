
import pandas as pd
import json
from pathlib import Path


def normalize_column(name):
    name = str(name).strip().lower()
    for char in [" ", "-", ".", "/", "\\", "(", ")", "[", "]"]:
        name = name.replace(char, "_")
    while "__" in name:
        name = name.replace("__", "_")
    return name.strip("_")


def find_column(df, possible_names):
    columns = {normalize_column(c): c for c in df.columns}

    for name in possible_names:
        key = normalize_column(name)
        if key in columns:
            return columns[key]

    for column in df.columns:
        key = normalize_column(column)
        for name in possible_names:
            if normalize_column(name) in key:
                return column

    return None


def parse_number(value):
    if pd.isna(value):
        return None

    if isinstance(value, (int, float)):
        return float(value)

    text = str(value).strip()
    text = text.replace(",", "").replace("%", "")

    number = ""
    decimal_found = False
    sign_allowed = True

    for char in text:
        if char.isdigit():
            number += char
            sign_allowed = False
        elif char == "." and not decimal_found:
            number += char
            decimal_found = True
            sign_allowed = False
        elif char in ["-", "+"] and sign_allowed:
            number += char
            sign_allowed = False
        elif number:
            break

    try:
        return float(number) if number not in ["", "+", "-", "."] else None
    except ValueError:
        return None


def clean_data(input_file, output_folder):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_file, encoding="utf-8-sig")
    original_rows = len(df)

    df.columns = [normalize_column(c) for c in df.columns]
    df = df.drop_duplicates()

    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].astype("string").str.strip()
            df[column] = df[column].replace("", pd.NA)

    name_col = find_column(df, ["name", "student_name", "student"])
    if name_col is not None:
        df[name_col] = df[name_col].astype("string").str.strip()

    score_col = find_column(
        df, ["score", "marks", "grade", "total_score", "final_score"]
    )
    if score_col is not None:
        df[score_col] = df[score_col].apply(parse_number)

    attendance_col = find_column(
        df, ["attendance", "attendance_percentage", "attendance_percent"]
    )
    if attendance_col is not None:
        df[attendance_col] = df[attendance_col].apply(parse_number)

    cleaned_file = output_folder / "cleaned_students.csv"
    df.to_csv(cleaned_file, index=False)

    summary = {
        "original_rows": original_rows,
        "cleaned_rows": len(df),
        "duplicate_rows_removed": original_rows - len(df),
        "missing_values_by_column": {
            str(k): int(v) for k, v in df.isna().sum().items()
        },
        "columns": list(df.columns)
    }

    return df, summary
