import pytest
from src_1086 import task_func

def test_task_func():
    text = "This is a sample text for testing."
    expected_output = ([('a', 1), ('is', 1), ('sample', 1), ('text', 1), ('testing.', 1), ('for', 1)], <matplotlib.axes._subplots.AxesSubplot object at 0x7f8e1d1d1c10>)
    actual_output = task_func(text)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_empty():
    text = ""
    expected_output = ([], <matplotlib.axes._subplots.AxesSubplot object at 0x7f8e1d1d1c10>)
    actual_output = task_func(text)
    assert actual_output == expected_output, "Output does not match expected output"