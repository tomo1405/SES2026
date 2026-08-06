python
import pandas as pd
import seaborn as sns
import pytest

def task_func(data):
    df = pd.DataFrame(data)
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        raise ValueError("No numeric columns present")

    df_cumsum = numeric_df.cumsum()
    ax = sns.heatmap(df_cumsum)
    return ax

def test_task_func():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': ['a', 'b', 'c']}
    ax = task_func(data)
    assert isinstance(ax, sns.matrix.ClusterGrid)

def test_task_func_no_numeric_columns():
    data = {'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f'], 'C': ['g', 'h', 'i']}
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_empty_dataframe():
    data = {}
    with pytest.raises(ValueError):
        task_func(data)