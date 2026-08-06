import pytest
from src_0704 import task_func
import pandas as pd
from sklearn.cluster import DBSCAN

def test_task_func():
    data = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    cols = ['a', 'b']
    df = pd.DataFrame(data, columns=cols)
    dbscan = DBSCAN(eps=3, min_samples=2)
    df['Cluster'] = dbscan.fit_predict(df)
    expected_result = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, 10], 'Cluster': [0, 0, 1, 1, 2]})
    assert df.equals(expected_result)