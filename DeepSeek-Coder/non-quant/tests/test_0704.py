import pytest
from src_0704 import task_func
import pandas as pd
from sklearn.cluster import DBSCAN

def test_task_func():
    data = [[1, 2], [2, 3], [3, 4], [10, 11], [12, 13]]
    cols = ['col1', 'col2']
    result = task_func(data, cols)
    assert isinstance(result, pd.DataFrame)
    assert 'Cluster' in result.columns
    assert len(result) == len(data)
    assert result['Cluster'].isin([-1, 0, 1]).all()