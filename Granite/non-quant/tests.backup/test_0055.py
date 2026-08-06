import pytest
from src_0055 import task_func

def test_task_func():
    text = "This is a test. This is only a test. This is a test of the emergency broadcast system."
    expected_df = ... # Define the expected output DataFrame
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)

def test_task_func_empty_text():
    text = ""
    expected_df = ... # Define the expected output DataFrame for an empty text
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)

def test_task_func_single_sentence():
    text = "This is a test."
    expected_df = ... # Define the expected output DataFrame for a single sentence
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)