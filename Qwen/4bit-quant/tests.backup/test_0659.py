import pytest
from src_0659 import task_func
import pandas as pd

@pytest.fixture
def sample_texts():
    return [
        "Hello, world! This is a test.",
        "Another example, with different words.",
        "Testing, one, two, three."
    ]

def test_task_func_output(sample_texts):
    result_df = task_func(sample_texts)
    assert isinstance(result_df, pd.DataFrame), "The output should be a pandas DataFrame."

def test_task_func_columns(sample_texts):
    result_df = task_func(sample_texts)
    expected_columns = ['another', 'different', 'example', 'hello', 'is', 'one', 'test', 'three', 'two', 'world']
    assert all(col in result_df.columns for col in expected_columns), "DataFrame columns do not match expected values."

def test_task_func_values(sample_texts):
    result_df = task_func(sample_texts)
    # Check if the DataFrame has the correct shape (number of rows and columns)
    assert result_df.shape == (3, 10), "DataFrame shape does not match expected values."

def test_task_func_empty_input():
    result_df = task_func([])
    assert result_df.empty, "DataFrame should be empty for empty input."

def test_task_func_single_text():
    result_df = task_func(["This is a single text."])
    assert result_df.shape == (1, 3), "DataFrame shape does not match expected values for single text input."

def test_task_func_stopwords_removal(sample_texts):
    result_df = task_func(sample_texts)
    # Check if stopwords are removed
    assert 'is' not in result_df.columns, "Stopword 'is' should not be in the DataFrame columns."
    assert 'a' not in result_df.columns, "Stopword 'a' should not be in the DataFrame columns."
    assert 'this' not in result_df.columns, "Stopword 'this' should not be in the DataFrame columns."