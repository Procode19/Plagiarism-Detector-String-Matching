# src/naive_match.py

def naive_string_matching(original_sentences, submitted_sentences):
    """
    Compare sentences using naive matching
    """

    matched_sentences = []

    for submitted in submitted_sentences:

        for original in original_sentences:

            # exact sentence match
            if submitted.strip() == original.strip():

                matched_sentences.append(submitted)

    return matched_sentences