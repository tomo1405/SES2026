import pytest
from src_1050 import task_func
import pandas as pd

def test_task_func_empty_string():
    input_string = ""
    expected_output = pd.DataFrame(columns=["Text"])
    assert task_func(input_string).equals(expected_output)

def test_task_func_single_line():
    input_string = "Hello, World!"
    expected_output = pd.DataFrame({"Text": ["Hello, World!"]})
    assert task_func(input_string).equals(expected_output)

def test_task_func_multiple_lines():
    input_string = "Line 1\nLine 2\nLine 3"
    expected_output = pd.DataFrame({"Text": ["Line 1", "Line 2", "Line 3"]})
    assert task_func(input_string).equals(expected_output)

def test_task_func_with_tabs():
    input_string = "Line\t1\nLine\t2\nLine\t3"
    expected_output = pd.DataFrame({"Text": ["Line 1", "Line 2", "Line 3"]})
    assert task_func(input_string).equals(expected_output)

def test_task_func_with_newlines_and_tabs():
    input_string = "Line\\n1\\tLine\\n2\\tLine\\n3"
    expected_output = pd.DataFrame({"Text": ["Line 1", "Line 2", "Line 3"]})
    assert task_func(input_string).equals(expected_output)

def test_task_func_with_empty_lines():
    input_string = "\nLine 1\n\nLine 2\n\n\nLine 3\n"
    expected_output = pd.DataFrame({"Text": ["Line 1", "Line 2", "Line 3"]})
    assert task_func(input_string).equals(expected_output)