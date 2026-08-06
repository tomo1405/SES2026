import pytest
from src_0417 import task_func
import pandas as pd
import seaborn as sns

def test_task_func_with_valid_data():
    data = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "b": 5, "c": 6},
        {"a": 7, "b": 8, "c": 9}
    ]
    column = "c"
    expected_result = sns.heatmap(pd.DataFrame(data).drop(columns=column).select_dtypes(include=["number"]).corr())
    result = task_func(data, column)
    assert result == expected_result

def test_task_func_with_invalid_data():
    data = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "b": 5, "c": 6},
        {"a": 7, "b": 8, "c": 9}
    ]
    column = "d"
    expected_result = None
    result = task_func(data, column)
    assert result == expected_result

def test_task_func_with_empty_data():
    data = []
    column = "c"
    expected_result = None
    result = task_func(data, column)
    assert result == expected_result