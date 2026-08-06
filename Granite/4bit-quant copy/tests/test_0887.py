import pandas as pd
from collections import Counter
from src_0887 import task_func
import pytest

def test_task_func():
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'Score': [80, 90, 100]}
    df, avg_scores, most_common_age = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(avg_scores, pd.Series)
    assert most_common_age == 35

def test_task_func_with_missing_keys():
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35]}
    with pytest.raises(ValueError):
        task_func(data)