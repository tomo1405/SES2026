import pytest
from src_0185 import task_func
import pandas as pd

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame(columns=['text'])
    result = task_func(df, 'text')
    assert result.empty, "The result should be an empty DataFrame"

def test_task_func_with_single_row():
    df = pd.DataFrame({'text': ['This is a test.']})
    expected_columns = ['test']
    result = task_func(df, 'text')
    assert list(result.columns) == expected_columns, "The result should have the correct column names"
    assert result.iloc[0][0] == 1, "The first row should have the correct token count"

def test_task_func_with_multiple_rows():
    df = pd.DataFrame({'text': ['This is a test.', 'Another test example.']})
    expected_columns = ['another', 'example', 'test']
    result = task_func(df, 'text')
    assert list(result.columns) == expected_columns, "The result should have the correct column names"
    assert result.iloc[0]['test'] == 1, "The first row should have the correct token count for 'test'"
    assert result.iloc[1]['example'] == 1, "The second row should have the correct token count for 'example'"

def test_task_func_with_stopwords():
    df = pd.DataFrame({'text': ['This is a test with stopwords.']})
    expected_columns = ['test', 'with', 'stopwords']
    result = task_func(df, 'text')
    assert list(result.columns) == expected_columns, "The result should have the correct column names"
    assert result.iloc[0]['test'] == 1, "The first row should have the correct token count for 'test'"

def test_task_func_with_numbers():
    df = pd.DataFrame({'text': ['This is a test with numbers 123.']})
    expected_columns = ['test', 'with', 'numbers']
    result = task_func(df, 'text')
    assert list(result.columns) == expected_columns, "The result should have the correct column names"
    assert result.iloc[0]['test'] == 1, "The first row should have the correct token count for 'test'"

def test_task_func_with_special_characters():
    df = pd.DataFrame({'text': ['This is a test with special characters!@#']})
    expected_columns = ['test', 'with', 'special', 'characters']
    result = task_func(df, 'text')
    assert list(result.columns) == expected_columns, "The result should have the correct column names"
    assert result.iloc[0]['test'] == 1, "The first row should have the correct token count for 'test'"