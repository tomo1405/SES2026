import pandas as pd
from src_0839 import task_func


def test_task_func():
    # Test case 1: Empty input
    text_series = pd.Series([])
    expected_output = pd.Series([])
    assert task_func(text_series).equals(expected_output)

    # Test case 2: Single word
    text_series = pd.Series(['hello'])
    expected_output = pd.Series(['hello'])
    assert task_func(text_series).equals(expected_output)

    # Test case 3: Multiple words
    text_series = pd.Series(['hello world', 'goodbye'])
    expected_output = pd.Series(['hello world', 'goodbye'])
    assert task_func(text_series).equals(expected_output)

    # Test case 4: Non-alphanumeric characters
    text_series = pd.Series(['hello world!', 'goodbye?'])
    expected_output = pd.Series(['hello world', 'goodbye'])
    assert task_func(text_series).equals(expected_output)

    # Test case 5: Stemming
    text_series = pd.Series(['hello', 'hello'])
    expected_output = pd.Series(['hello', 'hello'])
    assert task_func(text_series).equals(expected_output)