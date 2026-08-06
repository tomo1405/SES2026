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
    text = "This is a test sentence."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentence': 1}
    assert task_func(text) == expected_output

    # Test case 2
    text = "This is a test sentence. This is only a test."
    expected_output = {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2}
    assert task_func(text) == expected_output

    # Test case 3
    text = "The quick brown fox jumps over the lazy dog."
    expected_output = {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
    assert task_func(text) == expected_output

    # Test case 4
    text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected_output = {'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 2, 'over': 2, 'lazy': 2, 'dog': 2}
    assert task_func(text) == expected_output

    # Test case 5
    text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected_output = {'quick': 3, 'brown': 3, 'fox': 3, 'jumps': 3, 'over': 3, 'lazy': 3, 'dog': 3}
    assert task_func(text) == expected_output