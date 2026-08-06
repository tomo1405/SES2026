import pytest
from src_0704 import task_func
import pandas as pd
from sklearn.cluster import DBSCAN

def test_task_func():
    data = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    cols = ['x', 'y']
    df = pd.DataFrame(data, columns=cols)
    dbscan = DBSCAN(eps=3, min_samples=2)
    df['Cluster'] = dbscan.fit_predict(df)
    assert df.equals(task_func(data, cols))