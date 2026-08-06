import pytest
from src_0839 import task_func
import pandas as pd

def test_task_func():
    # Test with a single text entry
    text_series = pd.Series(["Hello, world!"])
    expected_result = pd.Series(["hello world"])
    result = task_func(text_series)
    assert result.equals(expected_result)

    # Test with multiple text entries
    text_series = pd.Series(["Hello, world!", "This is a test."])
    expected_result = pd.Series(["hello world", "this is a test"])
    result = task_func(text_series)
    assert result.equals(expected_result)

    # Test with an empty text entry
    text_series = pd.Series([""])
    expected_result = pd.Series([""])
    result = task_func(text_series)
    assert result.equals(expected_result)

    # Test with a text entry containing non-alphanumeric characters
    text_series = pd.Series(["Hello!@#"])
    expected_result = pd.Series(["hello"])
    result = task_func(text_series)
    assert result.equals(expected_result)