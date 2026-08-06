import pytest
from src_0601 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Test with a simple DataFrame
    data = {'Word': ['apple', 'banana', 'apricot', 'cherry', 'avocado']}
    df = pd.DataFrame(data)
    letter = 'a'
    result = task_func(df, letter)
    expected = {
        'mean': 6.5,
        'median': 6.0,
        'mode': 6
    }
    assert result == expected

def test_task_func_no_matches():
    # Test with no matches
    data = {'Word': ['kiwi', 'mango', 'pear']}
    df = pd.DataFrame(data)
    letter = 'z'
    result = task_func(df, letter)
    expected = {
        'mean': np.nan,
        'median': np.nan,
        'mode': np.nan
    }
    assert result == expected

def test_task_func_single_match():
    # Test with a single match
    data = {'Word': ['grape']}
    df = pd.DataFrame(data)
    letter = 'g'
    result = task_func(df, letter)
    expected = {
        'mean': 5.0,
        'median': 5.0,
        'mode': 5
    }
    assert result == expected

def test_task_func_multiple_modes():
    # Test with multiple modes
    data = {'Word': ['apple', 'apricot', 'apex']}
    df = pd.DataFrame(data)
    letter = 'a'
    result = task_func(df, letter)
    expected = {
        'mean': 6.333333333333333,
        'median': 6.0,
        'mode': 6
    }
    assert result == expected

def test_task_func_empty_dataframe():
    # Test with an empty DataFrame
    df = pd.DataFrame(columns=['Word'])
    letter = 'b'
    result = task_func(df, letter)
    expected = {
        'mean': np.nan,
        'median': np.nan,
        'mode': np.nan
    }
    assert result == expected