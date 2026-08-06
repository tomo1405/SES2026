import re
import pandas as pd
from src_1050 import task_func
def test_task_func():
    input_string = "Hello\nWorld\nPython\n"
    expected_output = pd.DataFrame(["Hello", "World", "Python"], columns=["Text"])
    actual_output = task_func(input_string)
    assert actual_output.equals(expected_output)
def test_task_func_with_tabs():
    input_string = "Hello\tWorld\tPython\t"
    expected_output = pd.DataFrame(["Hello World Python"], columns=["Text"])
    actual_output = task_func(input_string)
    assert actual_output.equals(expected_output)
def test_task_func_with_empty_lines():
    input_string = "Hello\n\nWorld\nPython\n\n"
    expected_output = pd.DataFrame(["Hello", "World", "Python"], columns=["Text"])
    actual_output = task_func(input_string)
    assert actual_output.equals(expected_output)