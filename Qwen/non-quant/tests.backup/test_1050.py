import pytest
from src_1050 import task_func
import pandas as pd

def test_task_func_empty_input():
    input_string = ""
    expected_df = pd.DataFrame(columns=["Text"])
    result_df = task_func(input_string)
    assert result_df.equals(expected_df)

def test_task_func_single_line():
    input_string = "Hello, World!"
    expected_df = pd.DataFrame({"Text": ["Hello, World!"]})
    result_df = task_func(input_string)
    assert result_df.equals(expected_df)

def test_task_func_multiple_lines():
    input_string = "Line 1\nLine 2\nLine 3"
    expected_df = pd.DataFrame({"Text": ["Line 1", "Line 2", "Line 3"]})
    result_df = task_func(input_string)
    assert result_df.equals(expected_df)

def test_task_func_with_tabs():
    input_string = "Line 1\twith\ttabs\nLine 2"
    expected_df = pd.DataFrame({"Text": ["Line 1 with tabs", "Line 2"]})
    result_df = task_func(input_string)
    assert result_df.equals(expected_df)

def test_task_func_with_newlines_and_tabs():
    input_string = "Line 1\\nwith\\ntabs\nLine 2"
    expected_df = pd.DataFrame({"Text": ["Line 1\nwith\ntabs", "Line 2"]})
    result_df = task_func(input_string)
    assert result_df.equals(expected_df)

def test_task_func_with_empty_lines():
    input_string = "\nLine 1\n\nLine 2\n"
    expected_df = pd.DataFrame({"Text": ["Line 1", "Line 2"]})
    result_df = task_func(input_string)
    assert result_df.equals(expected_df)