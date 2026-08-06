import pytest
from src_0183 import task_func

def test_task_func():
    df = ...  # provide a sample input dataframe
    expected_output = ...  # provide the expected output for the given input dataframe
    actual_output = task_func(df)
    assert actual_output == expected_output, "Output does not match the expected output"

def test_task_func_with_empty_input():
    df = ...  # provide an empty input dataframe
    expected_output = []
    actual_output = task_func(df)
    assert actual_output == expected_output, "Output does not match the expected output"

def test_task_func_with_no_interesting_articles():
    df = ...  # provide a sample input dataframe with no interesting articles
    expected_output = []
    actual_output = task_func(df)
    assert actual_output == expected_output, "Output does not match the expected output"