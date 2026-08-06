import pandas as pd
import pytest
import string
from src_0936 import task_func

def test_empty_input():
    expected_df = pd.DataFrame({'Letter': [], 'Position': []})
    actual_df = task_func('')
    assert expected_df.equals(actual_df)

def test_non_alphabetic_input():
    with pytest.raises(ValueError) as exc_info:
        task_func('123')
    assert 'Input word must be in lowercase alphabetic characters only.' in str(exc_info.value)

def test_non_lowercase_input():
    with pytest.raises(ValueError) as exc_info:
        task_func('Abc')
    assert 'Input word must be in lowercase alphabetic characters only.' in str(exc_info.value)

def test_valid_input():
    expected_df = pd.DataFrame({'Letter': list('abc'), 'Position': [1, 2, 3]})
    actual_df = task_func('abc')
    assert expected_df.equals(actual_df)