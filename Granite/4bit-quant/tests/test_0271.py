import re
from collections import Counter
def task_func(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    return dict(Counter(words))
import pytest

def test_task_func():
    sentence = "This is a test sentence"
    expected_output = {'This': 1, 'is': 1, 'a': 1, 'test': 1, 'sentence': 1}
    actual_output = task_func(sentence)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_empty_sentence():
    sentence = ""
    expected_output = {}
    actual_output = task_func(sentence)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_non_string_input():
    with pytest.raises(TypeError):
        task_func(123)