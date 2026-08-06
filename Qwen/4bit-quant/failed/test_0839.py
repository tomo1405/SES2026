import pytest
from src_0839 import task_func
import pandas as pd

@pytest.fixture
def sample_series():
    return pd.Series(["Hello, World!", "This is a test.", "Python is great!"])

def test_task_func(sample_series):
    # Expected output after stemming and removing non-alphanumeric characters
    expected_output = pd.Series(["hello world", "this is a test", "python is great"])
    
    # Call the function with the sample series
    result = task_func(sample_series)
    
    # Assert that the result matches the expected output
    assert result.equals(expected_output)

def test_task_func_empty_string(sample_series):
    # Add an empty string to the series
    sample_series = sample_series.append(pd.Series([""]))
    
    # Expected output with an empty string
    expected_output = pd.Series(["hello world", "this is a test", "python is great", ""])
    
    # Call the function with the updated series
    result = task_func(sample_series)
    
    # Assert that the result matches the expected output
    assert result.equals(expected_output)

def test_task_func_single_character(sample_series):
    # Add a single character to the series
    sample_series = sample_series.append(pd.Series(["a"]))
    
    # Expected output with a single character
    expected_output = pd.Series(["hello world", "this is a test", "python is great", "a"])
    
    # Call the function with the updated series
    result = task_func(sample_series)
    
    # Assert that the result matches the expected output
    assert result.equals(expected_output)