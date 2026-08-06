import pytest
from src_0599 import task_func
import pandas as pd

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame(columns=['Word'])
    letter = 'a'
    result = task_func(df, letter)
    assert result == {}

def test_task_func_with_no_matching_words():
    df = pd.DataFrame({'Word': ['banana', 'cherry', 'date']})
    letter = 'z'
    result = task_func(df, letter)
    assert result == {}

def test_task_func_with_single_word():
    df = pd.DataFrame({'Word': ['apple']})
    letter = 'a'
    result = task_func(df, letter)
    assert result == {5: 1}

def test_task_func_with_multiple_words():
    df = pd.DataFrame({'Word': ['apple', 'apricot', 'banana', 'avocado', 'almond']})
    letter = 'a'
    result = task_func(df, letter)
    assert result == {5: 2, 7: 1, 6: 1}

def test_task_func_with_case_sensitive_matching():
    df = pd.DataFrame({'Word': ['Apple', 'apple', 'Banana', 'banana']})
    letter = 'A'
    result = task_func(df, letter)
    assert result == {5: 1}
    letter = 'a'
    result = task_func(df, letter)
    assert result == {5: 1}

def test_task_func_with_special_characters():
    df = pd.DataFrame({'Word': ['@apple', '#banana', '$cherry']})
    letter = '@'
    result = task_func(df, letter)
    assert result == {6: 1}
    letter = '#'
    result = task_func(df, letter)
    assert result == {7: 1}