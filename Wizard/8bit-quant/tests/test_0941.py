python
import re
import pytest
from nltk import word_tokenize
from collections import Counter

def task_func(input_str):
    cleaned_str = re.sub('[^A-Za-z0-9 ]+', '', input_str)
    words = word_tokenize(cleaned_str)
    freq_dict = Counter(words)

    return freq_dict

def test_task_func():
    # Test case 1
    input_str = "This is a test string."
    expected_output = {'This': 1, 'is': 1, 'a': 1, 'test': 1, 'string.': 1}
    assert task_func(input_str) == expected_output

    # Test case 2
    input_str = "This is a test string. This is only a test."
    expected_output = {'This': 2, 'is': 2, 'a': 2, 'test': 2, 'string.': 1, 'only': 1}
    assert task_func(input_str) == expected_output

    # Test case 3
    input_str = "This is a test string. This is only a test. This is only a test."
    expected_output = {'This': 3, 'is': 3, 'a': 3, 'test': 3, 'string.': 1, 'only': 1}
    assert task_func(input_str) == expected_output

    # Test case 4
    input_str = "This is a test string. This is only a test. This is only a test. This is only a test."
    expected_output = {'This': 4, 'is': 4, 'a': 4, 'test': 4, 'string.': 1, 'only': 1}
    assert task_func(input_str) == expected_output

    # Test case 5
    input_str = "This is a test string. This is only a test. This is only a test. This is only a test. This is only a test."
    expected_output = {'This': 5, 'is': 5, 'a': 5, 'test': 5, 'string.': 1, 'only': 1}
    assert task_func(input_str) == expected_output