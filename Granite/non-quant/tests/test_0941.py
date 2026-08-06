from typing import Counter

from src_0941 import task_func


def test_task_func():
    input_str = "This is a test string."
    expected_output = Counter({'This': 1, 'is': 1, 'a': 1, 'test': 1, 'string.': 1})
    actual_output = task_func(input_str)
    assert actual_output == expected_output, "task_func() returned an incorrect output"