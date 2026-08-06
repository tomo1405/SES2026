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
    content = "This is a test sentence. It contains some words."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'contain': 1, 'some': 1, 'word': 1}
    assert task_func(content) == expected_output

    # Test case 2
    content = "This is a test sentence. It contains some words. And some more words."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'contain': 1, 'some': 2, 'word': 2}
    assert task_func(content) == expected_output

    # Test case 3
    content = "This is a test sentence. It contains some words. And some more words. And some more words."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'contain': 1, 'some': 3, 'word': 3}
    assert task_func(content) == expected_output

    # Test case 4
    content = "This is a test sentence. It contains some words. And some more words. And some more words. And some more words."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'contain': 1, 'some': 4, 'word': 4}
    assert task_func(content) == expected_output

    # Test case 5
    content = "This is a test sentence. It contains some words. And some more words. And some more words. And some more words. And some more words."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'contain': 1, 'some': 5, 'word': 5}
    assert task_func(content) == expected_output

    # Test case 6
    content = "This is a test sentence. It contains some words. And some more words. And some more words. And some more words. And some more words. And some more words."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'contain': 1, 'some': 6, 'word': 6}
    assert task_func(content) == expected_output

    # Test case 7
    content = "This is a test sentence. It contains some words. And some more words. And some more words. And some more words. And some more words. And some more words. And some more words."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'contain': 1, 'some': 7, 'word': 7}
    assert task_func(content) == expected_output

    # Test case 8
    content = "This is a test sentence. It contains some words. And some more words. And some more words. And some more words. And some more words. And some more words. And some more words. And some more words."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'contain': 1, 'some': 8, 'word': 8}
    assert task_func(content) == expected_output

    # Test case 9
    content = "This is a test sentence. It contains some words. And some more words. And some more words. And some more words. And some more words. And some more words. And some more words. And some more words. And some more words."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'contain': 1, 'some': 9, 'word': 9}
    assert task_func(content) == expected_output

    # Test case 10
    content = "This is a test sentence. It contains some words. And some more words. And some more words. And some more words. And some more words. And some more words. And some more words. And some more words. And some more words. And some more words."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'contain': 1, 'some': 10, 'word': 10}
    assert task_func(content) == expected_output