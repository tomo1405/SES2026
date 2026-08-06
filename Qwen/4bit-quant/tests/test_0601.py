import pandas as pd
import pytest
from src_0601 import task_func


def test_task_func_with_empty_dataframe():
    df = pd.DataFrame({'Word': []})
    letter = 'a'
    result = task_func(df, letter)
    assert result == {'mean': np.nan, 'median': np.nan, 'mode': np.nan}

def test_task_func_with_no_matching_words():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry']})
    letter = 'z'
    result = task_func(df, letter)
    assert result == {'mean': np.nan, 'median': np.nan, 'mode': np.nan}

def test_task_func_with_single_word():
    df = pd.DataFrame({'Word': ['apple']})
    letter = 'a'
    result = task_func(df, letter)
    assert result == {'mean': 5.0, 'median': 5.0, 'mode': 5}

def test_task_func_with_multiple_words():
    df = pd.DataFrame({'Word': ['apple', 'apricot', 'banana', 'avocado']})
    letter = 'a'
    result = task_func(df, letter)
    assert result == {'mean': 6.25, 'median': 6.0, 'mode': 5}

def test_task_func_with_repeated_words():
    df = pd.DataFrame({'Word': ['apple', 'apple', 'banana', 'avocado']})
    letter = 'a'
    result = task_func(df, letter)
    assert result == {'mean': 6.0, 'median': 6.0, 'mode': 5}

def test_task_func_with_case_sensitive_matching():
    df = pd.DataFrame({'Word': ['Apple', 'apricot', 'Banana', 'Avocado']})
    letter = 'a'
    result = task_func(df, letter)
    assert result == {'mean': 6.25, 'median': 6.0, 'mode': 5}

def test_task_func_with_non_string_data():
    df = pd.DataFrame({'Word': [123, 'apple', 'banana', 'cherry']})
    letter = 'a'
    with pytest.raises(AttributeError):
        task_func(df, letter)

def test_task_func_with_non_dataframe_input():
    df = [1, 2, 3]
    letter = 'a'
    with pytest.raises(TypeError):
        task_func(df, letter)