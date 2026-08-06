python
import re
from collections import Counter
import pytest

def task_func(input_str):
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str).lower()
    freq_dict = Counter(cleaned_str)
    return freq_dict

def test_task_func():
    # Test case 1
    input_str = "Hello, World!"
    expected_output = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    assert task_func(input_str) == expected_output

    # Test case 2
    input_str = "The quick brown fox jumps over the lazy dog."
    expected_output = {'t': 2, 'h': 2, 'e': 3, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}
    assert task_func(input_str) == expected_output

    # Test case 3
    input_str = "1234567890"
    expected_output = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '0': 1}
    assert task_func(input_str) == expected_output