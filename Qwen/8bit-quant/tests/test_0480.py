import pytest
from src_0480 import task_func
import pandas as pd

def test_task_func_with_empty_list():
    result = task_func([])
    expected_columns = ["Original String", "Modified String"]
    assert result.equals(pd.DataFrame(columns=expected_columns))

def test_task_func_with_single_empty_string():
    result = task_func([""])
    expected_df = pd.DataFrame({
        "Original String": [""],
        "Modified String": [""]
    })
    assert result.equals(expected_df)

def test_task_func_with_single_string_no_commas():
    result = task_func(["hello"], seed=0)
    expected_df = pd.DataFrame({
        "Original String": ["hello"],
        "Modified String": ["hello"]
    })
    assert result.equals(expected_df)

def test_task_func_with_single_string_with_commas():
    result = task_func(["a, b, c"], seed=0)
    expected_df = pd.DataFrame({
        "Original String": ["a, b, c"],
        "Modified String": ["a, b, c"]
    })
    assert result.equals(expected_df)

def test_task_func_with_multiple_strings():
    result = task_func(["apple, banana", "cherry"], seed=0)
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana", "cherry"],
        "Modified String": ["apple, banana", "cherry"]
    })
    assert result.equals(expected_df)

def test_task_func_with_random_replacement():
    result = task_func(["apple, banana, cherry"], seed=42)
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["apple, banana, xkcdj"]
    })
    assert result.equals(expected_df)

def test_task_func_with_whitespace():
    result = task_func(["  apple ,  banana  "], seed=0)
    expected_df = pd.DataFrame({
        "Original String": ["  apple ,  banana  "],
        "Modified String": ["  apple ,  banana  "]
    })
    assert result.equals(expected_df)