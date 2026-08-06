import pytest
from src_0484 import task_func
import pandas as pd

def test_task_func_no_pattern():
    df = pd.DataFrame({'text': ['hello world', 'foo bar baz']})
    result = task_func(df, 'text', '')
    assert result.equals(df)

def test_task_func_no_matches():
    df = pd.DataFrame({'text': ['hello world', 'foo bar baz']})
    result = task_func(df, 'text', r'\d+')
    assert result.equals(df)

def test_task_func_single_match():
    df = pd.DataFrame({'text': ['hello 123 world', 'foo 456 bar baz']})
    result = task_func(df, 'text', r'\d+')
    expected_df = pd.DataFrame({'text': ['hello 123 world', 'foo 456 bar baz']})
    assert result.equals(expected_df)

def test_task_func_multiple_matches():
    df = pd.DataFrame({'text': ['hello 123 world 456', 'foo 789 bar 012 baz']})
    result = task_func(df, 'text', r'\d+')
    expected_df = pd.DataFrame({'text': ['hello 456 world 123', 'foo 012 bar 789 baz']})
    assert result.equals(expected_df)

def test_task_func_case_insensitive():
    df = pd.DataFrame({'text': ['Hello World', 'Foo Bar Baz']})
    result = task_func(df, 'text', r'(?i)world')
    expected_df = pd.DataFrame({'text': ['Hello World', 'Foo Bar Baz']})
    assert result.equals(expected_df)

def test_task_func_non_string_column():
    df = pd.DataFrame({'numbers': [123, 456], 'text': ['hello world', 'foo bar baz']})
    with pytest.raises(AttributeError):
        task_func(df, 'numbers', r'\d+')

def test_task_func_nonexistent_column():
    df = pd.DataFrame({'text': ['hello world', 'foo bar baz']})
    with pytest.raises(KeyError):
        task_func(df, 'nonexistent', r'\d+')