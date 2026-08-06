python
import pandas as pd
from statistics import mean
import pytest

def task_func(df: pd.DataFrame) -> dict:

    if 'Name' not in df.columns or 'Score' not in df.columns:
        raise ValueError('The DataFram should have the columns "Name" and "Score".')

    grouped = df.groupby('Name')
    result_dict = {}
    for name, group in grouped:
        avg_score = mean(group['Score'])
        result_dict[name] = iter([(name, avg_score)])

    return result_dict

def test_task_func():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [80, 70, 90]})
    result = task_func(df)
    assert result == {'Alice': [('Alice', 80.0)], 'Bob': [('Bob', 70.0)], 'Charlie': [('Charlie', 90.0)]}

    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [80, 70, 90], 'Extra': ['A', 'B', 'C']})
    with pytest.raises(ValueError):
        task_func(df)