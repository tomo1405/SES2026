import pandas as pd
from collections import Counter
from src_0887 import task_func
import pytest

def test_task_func():
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [20, 25, 30],
            'Score': [80, 90, 100]}
    df, avg_scores, most_common_age = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(avg_scores, pd.Series)
    assert isinstance(most_common_age, int) or most_common_age is None
    assert df.shape == (3, 3)
    assert list(df.columns) == ['Name', 'Age', 'Score']
    assert list(avg_scores.index) == ['Alice', 'Bob', 'Charlie']
    assert avg_scores['Alice'] == 80
    assert avg_scores['Bob'] == 90
    assert avg_scores['Charlie'] == 100
    assert most_common_age == 20

def test_task_func_invalid_data():
    data = {'Name': ['Alice', 'Bob'],
            'Age': [20, 25],
            'Score': [80, 90]}
    with pytest.raises(ValueError):
        task_func(data)