import re
from nltk import word_tokenize
from collections import Counter
def task_func(input_str):
    cleaned_str = re.sub('[^A-Za-z0-9 ]+', '', input_str)
    words = word_tokenize(cleaned_str)
    freq_dict = Counter(words)

    return freq_dict
import pytest

def test_task_func():
    input_str = "This is a test string"
    expected_output = Counter({'this': 1, 'is': 1, 'a': 1, 'test': 1, 'string': 1})
    actual_output = task_func(input_str)
    assert actual_output == expected_output

def test_task_func_with_special_characters():
    input_str = "This!@# is a $%& test string"
    expected_output = Counter({'this': 1, 'is': 1, 'a': 1, 'test': 1, 'string': 1})
    actual_output = task_func(input_str)
    assert actual_output == expected_output

def test_task_func_with_numbers():
    input_str = "This is a test 123 string"
    expected_output = Counter({'this': 1, 'is': 1, 'a': 1, 'test': 1, '123': 1, 'string': 1})
    actual_output = task_func(input_str)
    assert actual_output == expected_output