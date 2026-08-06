import pytest
from src_0348 import task_func
import pandas as pd

def test_task_func_no_matches():
    data = {'id': [1, 2, 3], 'text': ['no hex here', 'nor here', 'or here']}
    df = pd.DataFrame(data)
    result = task_func(df, 'text')
    assert result.empty

def test_task_func_single_match():
    data = {'id': [1, 2, 3], 'text': ['aabbccddeeff00112233445566778899', 'no hex here', 'nor here']}
    df = pd.DataFrame(data)
    result = task_func(df, 'text')
    expected = pd.Series([1], index=['aabbccddeeff00112233445566778899'])
    pd.testing.assert_series_equal(result, expected)

def test_task_func_multiple_matches():
    data = {'id': [1, 2, 3], 'text': ['aabbccddeeff00112233445566778899', 'aabbccddeeff00112233445566778899', 'aabbccddeeff00112233445566778899']}
    df = pd.DataFrame(data)
    result = task_func(df, 'text')
    expected = pd.Series([3], index=['aabbccddeeff00112233445566778899'])
    pd.testing.assert_series_equal(result, expected)

def test_task_func_mixed_matches():
    data = {'id': [1, 2, 3], 'text': ['aabbccddeeff00112233445566778899', '1234567890abcdef1234567890abcdef', 'no hex here']}
    df = pd.DataFrame(data)
    result = task_func(df, 'text')
    expected = pd.Series([1, 1], index=['aabbccddeeff00112233445566778899', '1234567890abcdef1234567890abcdef'])
    pd.testing.assert_series_equal(result, expected)

def test_task_func_empty_string():
    data = {'id': [1, 2, 3], 'text': ['', '', '']}
    df = pd.DataFrame(data)
    result = task_func(df, 'text')
    assert result.empty

def test_task_func_non_string_column():
    data = {'id': [1, 2, 3], 'text': [123456, 789012, 345678]}
    df = pd.DataFrame(data)
    with pytest.raises(AttributeError):
        task_func(df, 'text')