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
    # Test case 1: Valid input data
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    ax = task_func(data)
    assert isinstance(ax, sns.matrix.ClusterGrid)

    # Test case 2: Invalid input data (no numeric columns)
    data = {'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']}
    with pytest.raises(ValueError):
        task_func(data)