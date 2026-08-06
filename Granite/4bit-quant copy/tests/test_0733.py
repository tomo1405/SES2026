import re
import string
from nltk.stem import PorterStemmer
from collections import Counter
STEMMER = PorterStemmer()
def task_func(content):
    content = content.split(' ')[:-1]
    words = [word.strip(string.punctuation).lower() for word in re.split('\W+', ' '.join(content))]
    stemmed_words = [STEMMER.stem(word) for word in words]
    word_counts = Counter(stemmed_words)

    return dict(word_counts)
import pytest
def test_task_func():
    test_cases = [
        ("This is a test", {"this": 1, "is": 1, "a": 1, "test": 1}),
        ("This is another test", {"this": 1, "is": 1, "another": 1, "test": 1}),
        ("This is a different test", {"this": 1, "is": 1, "a": 1, "different": 1, "test": 1}),
    ]
    for test_input, expected_output in test_cases:
        actual_output = task_func(test_input)
        assert actual_output == expected_output, f"Failed for input '{test_input}'"