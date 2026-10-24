
import json
import pandas as pd
from pathlib import Path


def validate_data(df, summary, output_folder):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    issues = []

    missing = df.isna().sum()
    for column, count in missing.items():
        if count > 0:
            issues.append(
                f"{column}: {count} missing value(s)"
            )

    duplicates = int(df.duplicated().sum())
    if duplicates > 0:
        issues.append(f"{duplicates} duplicate row(s) found")

    score_col = next(
        (c for c in df.columns if c in
         ["score", "marks", "grade", "total_score", "final_score"]),
        None
    )

    if score_col is not None:
        invalid_scores = (
            df[score_col].notna()
            & ((df[score_col] < 0) | (df[score_col] > 100))
        ).sum()

        if invalid_scores > 0:
            issues.append(
                f"{invalid_scores} score value(s) outside 0-100"
            )

    attendance_col = next(
        (c for c in df.columns if c in
         ["attendance", "attendance_percentage", "attendance_percent"]),
        None
    )

    if attendance_col is not None:
        invalid_attendance = (
            df[attendance_col].notna()
            & (
                (df[attendance_col] < 0)
                | (df[attendance_col] > 100)
            )
        ).sum()

        if invalid_attendance > 0:
            issues.append(
                f"{invalid_attendance} attendance value(s) outside 0-100"
            )

    summary_file = output_folder / "summary_after.json"
    with open(summary_file, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    report_file = output_folder / "cleaning_report.md"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("# Student Data Cleaning Report\n\n")
        file.write(f"- Original rows: {summary['original_rows']}\n")
        file.write(f"- Cleaned rows: {summary['cleaned_rows']}\n")
        file.write(
            f"- Duplicate rows removed: "
            f"{summary['duplicate_rows_removed']}\n"
        )
        file.write("\n## Missing Values After Cleaning\n\n")

        for column, count in df.isna().sum().items():
            file.write(f"- {column}: {count}\n")

        file.write("\n## Validation Findings\n\n")

        if issues:
            for issue in issues:
                file.write(f"- {issue}\n")
        else:
            file.write("No validation issues detected.\n")

    return issues
