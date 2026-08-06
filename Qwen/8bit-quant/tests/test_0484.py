import pytest
from src_0484 import task_func
import pandas as pd

def test_task_func_no_pattern():
    df = pd.DataFrame({'text': ['hello world', 'foo bar']})
    result = task_func(df, 'text', '')
    assert result.equals(df)

def test_task_func_no_matches():
    df = pd.DataFrame({'text': ['hello world', 'foo bar']})
    pattern = r'\d+'
    result = task_func(df, 'text', pattern)
    assert result.equals(df)

def test_task_func_single_word_match():
    df = pd.DataFrame({'text': ['hello 123 world', 'foo 456 bar']})
    pattern = r'\d+'
    expected_df = pd.DataFrame({'text': ['hello 456 world', 'foo 123 bar']})
    result = task_func(df, 'text', pattern)
    assert result.equals(expected_df)

def test_task_func_multiple_matches():
    df = pd.DataFrame({'text': ['hello 123 world 456', 'foo 789 bar 012']})
    pattern = r'\d+'
    expected_df = pd.DataFrame({'text': ['hello 012 world 789', 'foo 456 bar 123']})
    result = task_func(df, 'text', pattern)
    assert result.equals(expected_df)

def test_task_func_case_insensitive():
    df = pd.DataFrame({'text': ['Hello 123 World', 'Foo 456 Bar']})
    pattern = r'\b\w{3}\b'
    expected_df = pd.DataFrame({'text': ['Hello Bar World', 'Foo World Bar']})
    result = task_func(df, 'text', pattern)
    assert result.equals(expected_df)