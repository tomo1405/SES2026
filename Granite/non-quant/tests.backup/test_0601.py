import pytest
from src_0601 import task_func

def test_task_func():
    df = [['apple', 5], ['banana', 6], ['orange', 6], ['pear', 5]]
    letter = 'b'
    expected_statistics = {'mean': 5.5, 'median': 5.5, 'mode': 5}
    actual_statistics = task_func(df, letter)
    assert actual_statistics == expected_statistics

def test_task_func_with_empty_df():
    df = []
    letter = 'a'
    expected_statistics = {'mean': None, 'median': None, 'mode': None}
    actual_statistics = task_func(df, letter)
    assert actual_statistics == expected_statistics

def test_task_func_with_no_matching_words():
    df = [['apple', 5], ['banana', 6], ['orange', 6], ['pear', 5]]
    letter = 'z'
    expected_statistics = {'mean': None, 'median': None, 'mode': None}
    actual_statistics = task_func(df, letter)
    assert actual_statistics == expected_statistics