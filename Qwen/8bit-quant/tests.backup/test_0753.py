import pytest
from src_0753 import task_func
import pandas as pd
import numpy as np

def test_task_func_data_not_dataframe():
    with pytest.raises(ValueError, match="data should be a DataFrame."):
        task_func([1, 2, 3], "target")

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="data should contain at least one row."):
        task_func(df, "target")

def test_task_func_target_column_not_in_dataframe():
    df = pd.DataFrame({"feature": [1, 2, 3]})
    with pytest.raises(ValueError, match="target_column should be in the provided DataFrame."):
        task_func(df, "target")

def test_task_func_non_numeric_data():
    df = pd.DataFrame({"feature": ["a", "b", "c"], "target": [1, 2, 3]})
    with pytest.raises(ValueError, match="data values should be numeric only."):
        task_func(df, "target")

def test_task_func_invalid_test_size():
    df = pd.DataFrame({"feature": [1, 2, 3], "target": [4, 5, 6]})
    with pytest.raises(ValueError, match="test_size should be between 0 and 1: 0 < test_size < 1"):
        task_func(df, "target", test_size=-0.1)
    with pytest.raises(ValueError, match="test_size should be between 0 and 1: 0 < test_size < 1"):
        task_func(df, "target", test_size=1.1)

def test_task_func_random_state_not_integer():
    df = pd.DataFrame({"feature": [1, 2, 3], "target": [4, 5, 6]})
    with pytest.raises(ValueError, match="random_state should be an integer."):
        task_func(df, "target", random_state="0")

def test_task_func_valid_input():
    df = pd.DataFrame({"feature": [1, 2, 3, 4, 5], "target": [2, 4, 6, 8, 10]})
    score = task_func(df, "target", test_size=0.2, random_state=0)
    assert isinstance(score, float)
    assert 0 <= score <= 1