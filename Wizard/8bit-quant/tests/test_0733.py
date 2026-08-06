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
    expected_output = {'the': 2, 'qui': 1, 'bro': 1, 'fox': 1, 'jump': 1, 'over': 1, 'lazi': 1, 'dog': 1}
    assert task_func(content) == expected_output

    # Test case 2
    content = "The quick brown fox jumps over the lazy dog. The dog is not amused."
    expected_output = {'the': 3, 'qui': 1, 'bro': 1, 'fox': 1, 'jump': 1, 'over': 1, 'lazi': 1, 'dog': 2, 'not': 1, 'amus': 1}
    assert task_func(content) == expected_output

    # Test case 3
    content = "The quick brown fox jumps over the lazy dog. The dog is not amused. The quick brown fox jumps over the lazy dog."
    expected_output = {'the': 5, 'qui': 2, 'bro': 2, 'fox': 2, 'jump': 2, 'over': 2, 'lazi': 2, 'dog': 3, 'not': 1, 'amus': 1}
    assert task_func(content) == expected_output

    # Test case 4
    content = "The quick brown fox jumps over the lazy dog. The dog is not amused. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected_output = {'the': 7, 'qui': 3, 'bro': 3, 'fox': 3, 'jump': 3, 'over': 3, 'lazi': 3, 'dog': 4, 'not': 2, 'amus': 1}
    assert task_func(content) == expected_output