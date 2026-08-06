import pytest
from src_0735 import task_func

def test_task_func():
    content = "This is a test sentence. It contains words and their corresponding parts of speech."
    expected_output = {'DT': 2, 'NN': 2, 'VBZ': 1, 'IN': 1, 'DT': 1, 'JJ': 1, 'NNS': 1, '.': 1}
    actual_output = task_func(content)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_empty_string():
    content = ""
    expected_output = {}
    actual_output = task_func(content)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_single_word():
    content = "word"
    expected_output = {}
    actual_output = task_func(content)
    assert actual_output == expected_output, "Output does not match expected output"