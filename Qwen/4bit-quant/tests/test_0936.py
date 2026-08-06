import pandas as pd
import pytest
from src_0936 import task_func


def test_task_func_empty_input():
    result = task_func('')
    assert result.equals(pd.DataFrame({'Letter': [], 'Position': []}))

def test_task_func_non_alphabetic_input():
    with pytest.raises(ValueError, match="Input word must be in lowercase alphabetic characters only."):
        task_func('123')

def test_task_func_uppercase_input():
    with pytest.raises(ValueError, match="Input word must be in lowercase alphabetic characters only."):
        task_func('HELLO')

def test_task_func_valid_input():
    result = task_func('hello')
    expected_df = pd.DataFrame({'Letter': ['h', 'e', 'l', 'l', 'o'], 'Position': [8, 5, 12, 12, 15]})
    assert result.equals(expected_df)

def test_task_func_single_letter():
    result = task_func('a')
    expected_df = pd.DataFrame({'Letter': ['a'], 'Position': [1]})
    assert result.equals(expected_df)