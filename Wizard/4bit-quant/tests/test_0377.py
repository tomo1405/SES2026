python
import nltk
import re
from collections import Counter
import pytest

# Constants
STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(text):
    words = re.split(r'\W+', text.lower())
    words = [word for word in words if word not in STOPWORDS and word != '']
    word_freq = dict(Counter(words))

    return word_freq

def test_task_func():
    # Test case 1
    text = "The quick brown fox jumps over the lazy dog."
    expected_result = {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
    assert task_func(text) == expected_result

    # Test case 2
    text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected_result = {'the': 4, 'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 2, 'over': 2, 'lazy': 2, 'dog': 2}
    assert task_func(text) == expected_result

    # Test case 3
    text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected_result = {'the': 7, 'quick': 3, 'brown': 3, 'fox': 3, 'jumps': 3, 'over': 3, 'lazy': 3, 'dog': 3}
    assert task_func(text) == expected_result

    # Test case 4
    text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected_result = {'the': 11, 'quick': 4, 'brown': 4, 'fox': 4, 'jumps': 4, 'over': 4, 'lazy': 4, 'dog': 4}
    assert task_func(text) == expected_result

    # Test case 5
    text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected_result = {'the': 16, 'quick': 5, 'brown': 5, 'fox': 5, 'jumps': 5, 'over': 5, 'lazy': 5, 'dog': 5}
    assert task_func(text) == expected_result