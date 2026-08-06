import pandas as pd
from sklearn.cluster import DBSCAN
from src_0704 import task_func
import pytest

def test_task_func():
    data = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    cols = ['A', 'B']
    df = task_func(data, cols)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (6, 3)
    assert df.columns.tolist() == ['A', 'B', 'Cluster']
    assert df['Cluster'].dtype == int

def test_task_func_invalid_input():
    data = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    cols = ['A', 'B', 'C']
    with pytest.raises(ValueError):
        task_func(data, cols)