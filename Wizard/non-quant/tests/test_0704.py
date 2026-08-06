python
import pandas as pd
from sklearn.cluster import DBSCAN
import pytest

def task_func(data, cols):
    df = pd.DataFrame(data, columns=cols)
    dbscan = DBSCAN(eps=3, min_samples=2)
    df['Cluster'] = dbscan.fit_predict(df)
    return df

def test_task_func():
    data = [[1, 2], [2, 3], [2, 4], [8, 7]]
    cols = ['A', 'B']
    df = task_func(data, cols)
    assert df.shape == (4, 3)
    assert df['Cluster'].tolist() == [0, 0, 0, 1]