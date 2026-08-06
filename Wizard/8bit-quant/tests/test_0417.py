python
import pandas as pd
import seaborn as sns
import pytest

def task_func(data, column="c"):
    df = pd.DataFrame(data)
    if column in df.columns:
        df = df.drop(columns=column)

    df = df.select_dtypes(include=["number"])

    if df.empty:
        return None

    return sns.heatmap(df.corr())

def test_task_func():
    # Test case 1: Valid input data
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert isinstance(task_func(data), sns.matrix.HeatMap)

    # Test case 2: Invalid input data (empty list)
    data = []
    assert task_func(data) is None

    # Test case 3: Invalid input data (non-numeric column)
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert task_func(data, column="a") is None

    # Test case 4: Invalid input data (no numeric columns)
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert task_func(data, column="b") is None