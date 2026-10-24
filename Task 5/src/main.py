
import sys
import json
from pathlib import Path

from clean_data import clean_data
from validate_data import validate_data
from visualize import visualize_data


def main():
    if len(sys.argv) < 2:
        print(
            'Usage: python main.py "messy_students.csv"'
        )
        return

    input_file = Path(sys.argv[1])

    if not input_file.exists():
        print("Error: CSV file not found.")
        print("Check the file path and try again.")
        return

    output_folder = Path("output")
    output_folder.mkdir(parents=True, exist_ok=True)

    try:
        import pandas as pd

        original_df = pd.read_csv(
            input_file, encoding="utf-8-sig"
        )

        summary_before = {
            "total_rows": len(original_df),
            "total_columns": len(original_df.columns),
            "missing_values_by_column": {
                str(k): int(v)
                for k, v in original_df.isna().sum().items()
            }
        }

        with open(
            output_folder / "summary_before.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(summary_before, file, indent=4)

        df, summary_after = clean_data(
            input_file, output_folder
        )

        validate_data(df, summary_after, output_folder)

        visualize_data(df, output_folder)

        print("Task 5 completed successfully!")
        print("Check the output folder for your files.")

    except Exception as error:
        print("An error occurred:", error)


if __name__ == "__main__":
    main()
