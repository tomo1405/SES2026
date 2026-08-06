python
import re
import pandas as pd
import pytest

STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]

def task_func(text):
    sentences = re.split(r"\.\s*", text)
    sentence_counts = {}

    for i, sentence in enumerate(sentences):
        if sentence.strip() == "":
            continue
        words = re.split(r"\s+", sentence.lower())
        words = [word for word in words if word not in STOPWORDS]
        sentence_counts[f"Sentence {i+1}"] = len(words)

    sentence_counts = pd.Series(sentence_counts)
    return sentence_counts

def test_task_func():
    text = "This is the first sentence. This is the second sentence. This is the third sentence."
    expected_result = pd.Series({"Sentence 1": 4, "Sentence 2": 5, "Sentence 3": 4})
    assert task_func(text) == expected_result