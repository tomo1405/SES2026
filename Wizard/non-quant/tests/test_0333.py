python
import re
from collections import Counter
from nltk.corpus import stopwords
import pytest

def task_func(text: str) -> dict:
    words = re.findall(r'\b\w+\b', text)
    non_stopwords = [word for word in words if word.lower() not in set(stopwords.words('english'))]
    count = dict(Counter(non_stopwords))

    return count

def test_task_func():
    # Test case 1
    text = "This is a test sentence."
    expected_result = {'test': 1, 'sentence': 1}
    assert task_func(text) == expected_result

    # Test case 2
    text = "This is a test sentence. This is another test sentence."
    expected_result = {'test': 2, 'sentence': 2}
    assert task_func(text) == expected_result

    # Test case 3
    text = "This is a test sentence. This is another test sentence. This is yet another test sentence."
    expected_result = {'test': 3, 'sentence': 3}
    assert task_func(text) == expected_result

    # Test case 4
    text = "This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence."
    expected_result = {'test': 4, 'sentence': 4}
    assert task_func(text) == expected_result

    # Test case 5
    text = "This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence. This is another test sentence."
    expected_result = {'test': 5, 'sentence': 5}
    assert task_func(text) == expected_result

    # Test case 6
    text = "This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence. This is another test sentence. This is yet another test sentence."
    expected_result = {'test': 6, 'sentence': 6}
    assert task_func(text) == expected_result

    # Test case 7
    text = "This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence."
    expected_result = {'test': 7, 'sentence': 7}
    assert task_func(text) == expected_result

    # Test case 8
    text = "This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence. This is another test sentence."
    expected_result = {'test': 8, 'sentence': 8}
    assert task_func(text) == expected_result

    # Test case 9
    text = "This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence. This is another test sentence. This is yet another test sentence."
    expected_result = {'test': 9, 'sentence': 9}
    assert task_func(text) == expected_result

    # Test case 10
    text = "This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence. This is another test sentence. This is yet another test sentence. This is a test sentence."
    expected_result = {'test': 10, 'sentence': 10}
    assert task_func(text) == expected_result