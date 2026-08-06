import pytest
from src_0598 import task_func
import pandas as pd

@pytest.fixture
def sample_data():
    return [
        {'Name': 'Alice'},
        {'Name': 'Bob'},
        {'Name': 'Charlie'},
        {'Name': 'David'},
        {'Name': 'alice'},
        {'Name': 'bob'},
        {'Name': 'charlie'},
        {'Name': 'david'}
    ]

def test_task_func_with_uppercase_letter(sample_data):
    result = task_func(sample_data, 'A')
    expected = pd.Series([2], index=['Alice'], name='Name')
    pd.testing.assert_series_equal(result, expected)

def test_task_func_with_lowercase_letter(sample_data):
    result = task_func(sample_data, 'b')
    expected = pd.Series([2], index=['Bob'], name='Name')
    pd.testing.assert_series_equal(result, expected)

def test_task_func_with_no_matching_names(sample_data):
    result = task_func(sample_data, 'z')
    expected = pd.Series([], dtype=int, name='Name')
    pd.testing.assert_series_equal(result, expected)

def test_task_func_with_empty_data():
    result = task_func([], 'a')
    expected = pd.Series([], dtype=int, name='Name')
    pd.testing.assert_series_equal(result, expected)

def test_task_func_with_all_matching_names(sample_data):
    result = task_func(sample_data, '')
    expected = pd.Series([2] * 4, index=['Alice', 'Bob', 'Charlie', 'David'], name='Name')
    pd.testing.assert_series_equal(result, expected)