# src/report.py

def generate_report(results, final_score):
    """
    Generate plagiarism report
    """

    report_path = "outputs/report.txt"

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "=" * 50 + "\n"
        )

        file.write(
            "PLAGIARISM DETECTION REPORT\n"
        )

        file.write(
            "=" * 50 + "\n\n"
        )

        for i, result in enumerate(results, 1):

            file.write(
                f"Match {i}\n"
            )

            file.write(
                f"Original Sentence:\n"
            )

            file.write(
                f"{result['original']}\n\n"
            )

            file.write(
                "Submitted Sentence:\n"
            )

            file.write(
                f"{result['submitted']}\n\n"
            )

            file.write(
                f"Similarity: "
                f"{result['similarity']}%\n"
            )

            file.write(
                f"KMP Match: "
                f"{result['kmp']}\n"
            )

            file.write(
                f"Rabin-Karp Match: "
                f"{result['rk']}\n"
            )

            file.write(
                "-" * 50 + "\n"
            )

        file.write("\n")

        file.write(
            "=" * 50 + "\n"
        )

        file.write(
            f"Overall Plagiarism "
            f"Percentage: "
            f"{final_score}%\n"
        )

        file.write(
            "=" * 50 + "\n"
        )

    print(
        "\nReport generated successfully!"
    )

    print(
        f"Saved at: {report_path}"
    )