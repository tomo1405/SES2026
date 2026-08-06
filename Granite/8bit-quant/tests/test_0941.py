from typing import Counter

from src_0941 import task_func


def test_task_func():
    input_str = "This is a test string."
    expected_output = Counter({'This': 1, 'is': 1, 'a': 1, 'test': 1, 'string.': 1})
    actual_output = task_func(input_str)
    assert actual_output == expected_output, "Task function output does not match expected output."

def test_task_func_with_empty_string():
    input_str = ""
    expected_output = Counter()
    actual_output = task_func(input_str)
    assert actual_output == expected_output, "Task function output does not match expected output."

def test_task_func_with_non_alphabetic_characters():
    input_str = "12345!@#$%^&*()_+"
    expected_output = Counter({'12345': 1, '!@#$%^&*()_+': 1})
    actual_output = task_func(input_str)
    assert actual_output == expected_output, "Task function output does not match expected output."