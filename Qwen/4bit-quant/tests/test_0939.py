import pytest
from src_0939 import task_func
import pandas as pd

def test_task_func_with_valid_text():
    # Test with a DataFrame containing valid text
    input_df = pd.DataFrame({'text': ['Hello, World!', 'Python 3.8']})
    expected_output = pd.DataFrame({
        'clean_text': ['HelloWorld', 'Python38'],
        'text_length': [10, 8]
    })
    result = task_func(input_df)
    assert result.equals(expected_output)

def test_task_func_with_empty_string():
    # Test with a DataFrame containing an empty string
    input_df = pd.DataFrame({'text': ['']})
    expected_output = pd.DataFrame({
        'clean_text': [''],
        'text_length': [0]
    })
    result = task_func(input_df)
    assert result.equals(expected_output)

def test_task_func_with_null_values():
    # Test with a DataFrame containing null values
    input_df = pd.DataFrame({'text': [None, pd.NA]})
    expected_output = pd.DataFrame({
        'clean_text': ['', ''],
        'text_length': [0, 0]
    })
    result = task_func(input_df)
    assert result.equals(expected_output)

def test_task_func_with_special_characters():
    # Test with a DataFrame containing special characters
    input_df = pd.DataFrame({'text': ['!@#$%^&*()', '1234567890']})
    expected_output = pd.DataFrame({
        'clean_text': ['', '1234567890'],
        'text_length': [0, 10]
    })
    result = task_func(input_df)
    assert result.equals(expected_output)