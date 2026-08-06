import pytest
from src_0482 import task_func
import pandas as pd

def test_task_func():
    # Test with an empty list
    result = task_func([])
    assert result.empty
    assert list(result.columns) == ["Original String", "Randomized String"]

    # Test with a single string
    data_list = ["apple, banana, cherry"]
    result = task_func(data_list)
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Randomized String": ["banana, apple, cherry"]
    })
    assert result.equals(expected_df)

    # Test with multiple strings
    data_list = ["apple, banana, cherry", "dog, cat"]
    result = task_func(data_list)
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana, cherry", "dog, cat"],
        "Randomized String": ["banana, apple, cherry", "cat, dog"]
    })
    assert result.equals(expected_df)

    # Test with strings containing special characters
    data_list = ["!@# $%^ &*()", "123 456 789"]
    result = task_func(data_list)
    expected_df = pd.DataFrame({
        "Original String": ["!@# $%^ &*()", "123 456 789"],
        "Randomized String": ["$%^ !@# &*()", "456 123 789"]
    })
    assert result.equals(expected_df)

    # Test with a seed to ensure reproducibility
    data_list = ["apple, banana, cherry"]
    result1 = task_func(data_list, seed=42)
    result2 = task_func(data_list, seed=42)
    assert result1.equals(result2)

    # Test with different seed to ensure randomness
    data_list = ["apple, banana, cherry"]
    result1 = task_func(data_list, seed=42)
    result2 = task_func(data_list, seed=123)
    assert not result1.equals(result2)