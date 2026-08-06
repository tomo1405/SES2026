import pandas as pd
import pytest
from src_0936 import task_func


def test_task_func_empty_string():
    result = task_func("")
    assert result.equals(pd.DataFrame({'Letter': [], 'Position': []}))

def test_task_func_single_letter():
    result = task_func("a")
    expected_df = pd.DataFrame({'Letter': ['a'], 'Position': [1]})
    assert result.equals(expected_df)

def test_task_func_multiple_letters():
    result = task_func("abc")
    expected_df = pd.DataFrame({'Letter': ['a', 'b', 'c'], 'Position': [1, 2, 3]})
    assert result.equals(expected_df)

def test_task_func_uppercase_input():
    with pytest.raises(ValueError, match="Input word must be in lowercase alphabetic characters only."):
        task_func("Abc")

def test_task_func_non_alphabetic_input():
    with pytest.raises(ValueError, match="Input word must be in lowercase alphabetic characters only."):
        task_func("abc123")

def test_task_func_special_characters():
    with pytest.raises(ValueError, match="Input word must be in lowercase alphabetic characters only."):
        task_func("abc!")

def test_task_func_long_word():
    result = task_func("zyxwvutsrqponmlkjihgfedcba")
    expected_positions = list(range(26, 0, -1))
    expected_df = pd.DataFrame({'Letter': list("zyxwvutsrqponmlkjihgfedcba"), 'Position': expected_positions})
    assert result.equals(expected_df)