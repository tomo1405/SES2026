import re
import pandas as pd
from src_1050 import task_func
def test_task_func():
    input_string = "Hello, world!\\nThis is a test.\\n\\n\\tWith tabs."
    expected_output = pd.DataFrame(["Hello, world!", "This is a test.", "With tabs."], columns=["Text"])
    actual_output = task_func(input_string)
    assert actual_output.equals(expected_output)
def test_task_func_empty_string():
    input_string = ""
    expected_output = pd.DataFrame(columns=["Text"])
    actual_output = task_func(input_string)
    assert actual_output.equals(expected_output)
def test_task_func_no_tabs():
    input_string = "Hello, world!\\nThis is a test.\\n\\nNo tabs here."
    expected_output = pd.DataFrame(["Hello, world!", "This is a test.", "No tabs here."], columns=["Text"])
    actual_output = task_func(input_string)
    assert actual_output.equals(expected_output)