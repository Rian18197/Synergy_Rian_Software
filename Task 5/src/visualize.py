
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def visualize_data(df, output_folder):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    plot_notes = []

    score_col = next(
        (c for c in df.columns if c in
         ["score", "marks", "grade", "total_score", "final_score"]),
        None
    )

    domain_col = next(
        (c for c in df.columns if c in
         ["domain", "department", "subject", "course"]),
        None
    )

    attendance_col = next(
        (c for c in df.columns if c in
         ["attendance", "attendance_percentage", "attendance_percent"]),
        None
    )

    status_col = next(
        (c for c in df.columns if c in
         ["submission_status", "status", "assignment_status",
          "submission", "submitted"]),
        None
    )

    if domain_col is not None and score_col is not None:
        data = df[[domain_col, score_col]].dropna()
        averages = data.groupby(domain_col)[score_col].mean()

        if not averages.empty:
            averages.plot(kind="bar")
            plt.title("Average Score by Domain")
            plt.xlabel("Domain")
            plt.ylabel("Average Score")
            plt.tight_layout()
            plt.savefig(
                output_folder / "domain_average_score.png"
            )
            plt.close()
            plot_notes.append("Created average score by domain graph.")
    else:
        plot_notes.append(
            "Domain average graph skipped: domain or score column missing."
        )

    if attendance_col is not None and score_col is not None:
        data = df[[attendance_col, score_col]].dropna()

        if not data.empty:
            plt.scatter(data[attendance_col], data[score_col])
            plt.title("Attendance vs Score")
            plt.xlabel("Attendance")
            plt.ylabel("Score")
            plt.tight_layout()
            plt.savefig(
                output_folder / "attendance_vs_score.png"
            )
            plt.close()
            plot_notes.append("Created attendance vs score graph.")
    else:
        plot_notes.append(
            "Attendance graph skipped: attendance or score column missing."
        )

    if status_col is not None:
        counts = df[status_col].fillna("Missing").astype(str).value_counts()

        if not counts.empty:
            counts.plot(kind="bar")
            plt.title("Submission Status Count")
            plt.xlabel("Submission Status")
            plt.ylabel("Number of Students")
            plt.tight_layout()
            plt.savefig(
                output_folder / "submission_status_count.png"
            )
            plt.close()
            plot_notes.append("Created submission status graph.")
    else:
        plot_notes.append(
            "Submission graph skipped: status column missing."
        )

    with open(
        output_folder / "plot_summary.md",
        "w",
        encoding="utf-8"
    ) as file:
        file.write("# Plot Summary\n\n")

        for note in plot_notes:
            file.write(f"- {note}\n")
