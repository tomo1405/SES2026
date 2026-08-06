import pytest
from src_1050 import task_func
import pandas as pd

def test_task_func_with_empty_string():
    input_string = ""
    expected_output = pd.DataFrame(columns=["Text"])
    assert task_func(input_string).equals(expected_output)

def test_task_func_with_single_line():
    input_string = "This is a test"
    expected_output = pd.DataFrame({"Text": ["This is a test"]})
    assert task_func(input_string).equals(expected_output)

def test_task_func_with_multiple_lines():
    input_string = "Line 1\nLine 2\nLine 3"
    expected_output = pd.DataFrame({"Text": ["Line 1", "Line 2", "Line 3"]})
    assert task_func(input_string).equals(expected_output)

def test_task_func_with_trailing_newlines():
    input_string = "\nLine 1\nLine 2\n\n"
    expected_output = pd.DataFrame({"Text": ["Line 1", "Line 2"]})
    assert task_func(input_string).equals(expected_output)

def test_task_func_with_tabs():
    input_string = "Line\twith\ttabs"
    expected_output = pd.DataFrame({"Text": ["Line with tabs"]})
    assert task_func(input_string).equals(expected_output)

def test_task_func_with_escaped_newlines_and_tabs():
    input_string = "Line\\nwith\\ttabs"
    expected_output = pd.DataFrame({"Text": ["Line\nwith tabs"]})
    assert task_func(input_string).equals(expected_output)