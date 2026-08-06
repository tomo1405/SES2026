import pytest
from src_0735 import task_func

def test_task_func():
    content = "This is a test sentence. It contains words and punctuation."
    expected_output = {'DT': 2, 'NN': 2, 'VBZ': 1, '.': 1}
    actual_output = task_func(content)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_empty_string():
    content = ""
    expected_output = {}
    actual_output = task_func(content)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_single_word():
    content = "Test"
    expected_output = {'NN': 1}
    actual_output = task_func(content)
    assert actual_output == expected_output, "Output does not match expected output"