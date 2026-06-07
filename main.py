# main.py

from src.file_handler import read_file
from src.preprocess import clean_text
from src.preprocess import sentence_tokenization
from src.naive_match import naive_string_matching
from src.kmp import kmp_search
from src.rabin_karp import rabin_karp_search
from src.similarity import calculate_similarity
from src.report import generate_report


def print_header():

    print("\n" + "=" * 60)
    print("      PLAGIARISM DETECTION SYSTEM")
    print("=" * 60)


def main():

    print_header()

    original_path = "documents/original.txt"
    submitted_path = "documents/submitted.txt"

    # Read Files
    original_text = read_file(
        original_path
    )

    submitted_text = read_file(
        submitted_path
    )

    # Clean Text
    cleaned_original = clean_text(
        original_text
    )

    cleaned_submitted = clean_text(
        submitted_text
    )

    # Sentence Tokenization
    original_sentences = (
        sentence_tokenization(
            cleaned_original
        )
    )

    submitted_sentences = (
        sentence_tokenization(
            cleaned_submitted
        )
    )

    print("\nOriginal Sentences:")
    print("-" * 60)

    for sentence in original_sentences:
        print("•", sentence)

    print("\nSubmitted Sentences:")
    print("-" * 60)

    for sentence in submitted_sentences:
        print("•", sentence)

    # Exact Match
    matched_content = (
        naive_string_matching(
            original_sentences,
            submitted_sentences
        )
    )

    print("\nExact Matches:")
    print("-" * 60)

    if matched_content:

        for match in matched_content:
            print("✓", match)

    else:
        print("No Exact Match Found")

    print("\nSimilarity Analysis")
    print("=" * 60)

    plagiarism_scores = []
    results = []

    for submitted in submitted_sentences:

        for original in (
            original_sentences
        ):

            similarity = (
                calculate_similarity(
                    original,
                    submitted
                )
            )

            if similarity >= 50:

                words = (
                    submitted.split()
                )

                if len(words) >= 2:

                    pattern = (
                        " ".join(
                            words[:2]
                        )
                    )

                    # KMP
                    kmp_found = (
                        kmp_search(
                            original,
                            pattern
                        )
                    )

                    # Rabin-Karp
                    rk_found = (
                        rabin_karp_search(
                            original,
                            pattern
                        )
                    )

                    print("\n✓ Match Found")
                    print("-" * 60)

                    print(
                        "Original:"
                    )
                    print(original)

                    print(
                        "\nSubmitted:"
                    )
                    print(submitted)

                    print(
                        f"\nSimilarity:"
                        f" {similarity}%"
                    )

                    print(
                        f"KMP Match:"
                        f" {kmp_found}"
                    )

                    print(
                        f"Rabin-Karp "
                        f"Match:"
                        f" {rk_found}"
                    )

                plagiarism_scores.append(
                    similarity
                )

                results.append({
                    "original":
                    original,

                    "submitted":
                    submitted,

                    "similarity":
                    similarity,

                    "kmp":
                    kmp_found,

                    "rk":
                    rk_found
                })

    # Final Percentage
    if plagiarism_scores:

        final_score = round(
            sum(
                plagiarism_scores
            )
            /
            len(
                plagiarism_scores
            ),
            2
        )

    else:
        final_score = 0

    print("\n" + "=" * 60)

    print(
        "OVERALL "
        "PLAGIARISM "
        "PERCENTAGE"
    )

    print("=" * 60)

    print(
        f"{final_score}%"
    )

    print("=" * 60)

    # Generate report
    generate_report(
        results,
        final_score
    )


if __name__ == "__main__":
    main()