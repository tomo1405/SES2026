import pandas as pd
from sklearn.cluster import DBSCAN
from src_0704 import task_func

def test_task_func():
    data = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    cols = ['Col1', 'Col2']
    df = task_func(data, cols)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (6, 3)
    assert df.columns.tolist() == ['Col1', 'Col2', 'Cluster']
    assert df['Cluster'].nunique() == 2

def test_task_func_with_no_data():
    data = []
    cols = ['Col1', 'Col2']
    df = task_func(data, cols)
    assert df.empty

def test_task_func_with_one_data_point():
    data = [[1, 2]]
    cols = ['Col1', 'Col2']
    df = task_func(data, cols)
    assert df.shape == (1, 3)

def test_task_func_with_one_column():
    data = [[1], [2], [3], [4], [5], [6]]
    cols = ['Col1']
    df = task_func(data, cols)
    assert df.shape == (6, 2)
    assert df.columns.tolist() == ['Col1', 'Cluster']