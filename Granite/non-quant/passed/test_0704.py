import pandas as pd
from sklearn.cluster import DBSCAN
import pytest

def task_func(data, cols):
    df = pd.DataFrame(data, columns=cols)
    dbscan = DBSCAN(eps=3, min_samples=2)
    df['Cluster'] = dbscan.fit_predict(df)
    return df

def test_task_func():
    data = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    cols = ['X', 'Y']
    expected_result = pd.DataFrame(data, columns=cols)
    expected_result['Cluster'] = [0, 0, 0, 0, 0, 0]
    result = task_func(data, cols)
    assert result.equals(expected_result)