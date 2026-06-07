# src/similarity.py

def calculate_similarity(original, submitted):
    """
    Calculate percentage similarity
    """

    original_words = set(original.split())
    submitted_words = set(submitted.split())

    common_words = original_words.intersection(submitted_words)

    similarity = (
        len(common_words)
        / max(len(original_words), len(submitted_words))
    ) * 100

    return round(similarity, 2)
