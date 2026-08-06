python
import re
import string
from nltk.stem import PorterStemmer
from collections import Counter
import pytest

STEMMER = PorterStemmer()

def task_func(content):
    content = content.split(' ')[:-1]
    words = [word.strip(string.punctuation).lower() for word in re.split('\W+', ' '.join(content))]
    stemmed_words = [STEMMER.stem(word) for word in words]
    word_counts = Counter(stemmed_words)

    return dict(word_counts)

def test_task_func():
    # Test case 1
    content = "The quick brown fox jumps over the lazy dog."
    expected_result = {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jump': 1, 'over': 1, 'lazy': 1, 'dog': 1}
    assert task_func(content) == expected_result

    # Test case 2
    content = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected_result = {'the': 4, 'quick': 2, 'brown': 2, 'fox': 2, 'jump': 2, 'over': 2, 'lazy': 2, 'dog': 2}
    assert task_func(content) == expected_result

    # Test case 3
    content = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected_result = {'the': 7, 'quick': 3, 'brown': 3, 'fox': 3, 'jump': 3, 'over': 3, 'lazy': 3, 'dog': 3}
    assert task_func(content) == expected_result

    # Test case 4
    content = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected_result = {'the': 11, 'quick': 4, 'brown': 4, 'fox': 4, 'jump': 4, 'over': 4, 'lazy': 4, 'dog': 4}
    assert task_func(content) == expected_result