import re

import pandas as pd
from src_0484 import task_func


def test_task_func_no_pattern():
    df = pd.DataFrame({'text': ['hello world', 'foo bar']})
    result = task_func(df, 'text', '')
    assert result.equals(df)

def test_task_func_no_matches():
    df = pd.DataFrame({'text': ['hello world', 'foo bar']})
    result = task_func(df, 'text', r'\d+')
    assert result.equals(df)

def test_task_func_single_match():
    df = pd.DataFrame({'text': ['hello world 123', 'foo bar']})
    expected_df = pd.DataFrame({'text': ['hello world 321', 'foo bar']})
    result = task_func(df, 'text', r'\d+')
    assert result.equals(expected_df)

def test_task_func_multiple_matches():
    df = pd.DataFrame({'text': ['hello 123 world 456', 'foo 789 bar']})
    expected_df = pd.DataFrame({'text': ['hello 456 world 123', 'foo 789 bar']})
    result = task_func(df, 'text', r'\d+')
    assert result.equals(expected_df)

def test_task_func_case_insensitive():
    df = pd.DataFrame({'text': ['Hello World', 'Foo Bar']})
    expected_df = pd.DataFrame({'text': ['Hello World', 'Foo Bar']})
    result = task_func(df, 'text', r'world', flags=re.IGNORECASE)
    assert result.equals(expected_df)

def test_task_func_with_special_characters():
    df = pd.DataFrame({'text': ['hello @world#', 'foo $bar!']})
    expected_df = pd.DataFrame({'text': ['hello $#world@', 'foo $bar!']})
    result = task_func(df, 'text', r'\w+')
    assert result.equals(expected_df)