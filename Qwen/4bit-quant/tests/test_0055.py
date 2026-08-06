import pytest
from src_0055 import task_func
import pandas as pd

def test_task_func():
    # Test with a simple text
    text = "This is the first sentence. This is the second sentence."
    df = task_func(text)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (2, 6), "The DataFrame should have 2 rows and 6 columns"
    
    # Check if the column names are correct
    expected_columns = ['this', 'is', 'the', 'first', 'second', 'sentence']
    assert list(df.columns) == expected_columns, "Column names do not match expected output"
    
    # Check if the DataFrame contains non-zero values
    assert df.values.sum() > 0, "The DataFrame should contain non-zero values"

def test_task_func_empty_text():
    # Test with empty text
    text = ""
    df = task_func(text)
    
    # Check if the DataFrame is empty
    assert df.empty, "The DataFrame should be empty for an empty input text"

def test_task_func_single_sentence():
    # Test with a single sentence
    text = "Single sentence without any punctuation"
    df = task_func(text)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (1, 4), "The DataFrame should have 1 row and 4 columns"
    
    # Check if the column names are correct
    expected_columns = ['single', 'sentence', 'without', 'punctuation']
    assert list(df.columns) == expected_columns, "Column names do not match expected output"
    
    # Check if the DataFrame contains non-zero values
    assert df.values.sum() > 0, "The DataFrame should contain non-zero values"

def test_task_func_multiple_punctuations():
    # Test with multiple punctuations
    text = "First sentence... Second sentence!!!"
    df = task_func(text)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (2, 3), "The DataFrame should have 2 rows and 3 columns"
    
    # Check if the column names are correct
    expected_columns = ['first', 'sentence', 'second']
    assert list(df.columns) == expected_columns, "Column names do not match expected output"
    
    # Check if the DataFrame contains non-zero values
    assert df.values.sum() > 0, "The DataFrame should contain non-zero values"