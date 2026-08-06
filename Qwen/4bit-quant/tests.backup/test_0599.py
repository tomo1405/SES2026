import pytest
from src_0599 import task_func
import pandas as pd

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame(columns=['Word'])
    letter = 'a'
    result = task_func(df, letter)
    assert result == {}

def test_task_func_with_no_matching_words():
    data = {'Word': ['banana', 'cherry', 'date']}
    df = pd.DataFrame(data)
    letter = 'z'
    result = task_func(df, letter)
    assert result == {}

def test_task_func_with_one_word():
    data = {'Word': ['apple']}
    df = pd.DataFrame(data)
    letter = 'a'
    result = task_func(df, letter)
    assert result == {5: 1}

def test_task_func_with_multiple_words():
    data = {'Word': ['apple', 'apricot', 'banana', 'apex']}
    df = pd.DataFrame(data)
    letter = 'a'
    result = task_func(df, letter)
    assert result == {5: 2, 7: 1}

def test_task_func_with_different_letter():
    data = {'Word': ['orange', 'grape', 'plum']}
    df = pd.DataFrame(data)
    letter = 'g'
    result = task_func(df, letter)
    assert result == {5: 1}

def test_task_func_with_case_sensitive_match():
    data = {'Word': ['Apple', 'apple', 'apricot']}
    df = pd.DataFrame(data)
    letter = 'A'
    result = task_func(df, letter)
    assert result == {5: 1}

def test_task_func_with_non_string_data():
    data = {'Word': [123, 'abc', 'abcd']}
    df = pd.DataFrame(data)
    letter = 'a'
    result = task_func(df, letter)
    assert result == {3: 1}