import re
from collections import Counter
def task_func(input_str):
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str).lower()
    freq_dict = Counter(cleaned_str)
    return freq_dict
import pytest

def test_task_func():
    input_str = "Hello, World! 123"
    expected_output = Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, '1': 1, '2': 1, '3': 1})
    actual_output = task_func(input_str)
    assert actual_output == expected_output, "Task function output does not match expected output"

def test_task_func_with_empty_string():
    input_str = ""
    expected_output = Counter({})
    actual_output = task_func(input_str)
    assert actual_output == expected_output, "Task function output does not match expected output"

def test_task_func_with_non_string_input():
    input_str = 123
    with pytest.raises(TypeError):
        task_func(input_str)