import pytest
from src_0733 import task_func

def test_task_func():
    content = "This is a test sentence. It contains words and punctuation."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'it': 1, 'contain': 1, 'word': 1, 'punctuat': 1}
    actual_output = task_func(content)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_with_empty_string():
    content = ""
    expected_output = {}
    actual_output = task_func(content)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_with_whitespace_string():
    content = "    "
    expected_output = {}
    actual_output = task_func(content)
    assert actual_output == expected_output, "Task function returned incorrect output"