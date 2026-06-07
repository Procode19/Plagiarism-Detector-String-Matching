# src/preprocess.py

import re


def clean_text(text):
    """
    Clean text
    """

    text = text.lower()

    # remove punctuation except period
    text = re.sub(r'[^a-zA-Z0-9\s.]', '', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def sentence_tokenization(text):
    """
    Convert paragraph into sentences
    """

    sentences = text.split('.')

    cleaned_sentences = []

    for sentence in sentences:

        sentence = sentence.strip()

        if sentence:
            cleaned_sentences.append(sentence)

    return cleaned_sentences