import pytest
from src_0838 import task_func

def test_task_func():
    n_rows = 10
    scale_cols = [0, 2, 4]
    columns = ['A', 'B', 'C', 'D', 'E']
    random_seed = 42
    
    df = task_func(n_rows, scale_cols, columns, random_seed)
    
    assert df.shape == (n_rows, len(columns))
    assert df.columns.tolist() == columns
    assert df.dtypes.tolist() == [np.int64] * len(columns)
    assert df.iloc[:, scale_cols].apply(lambda x: x.mean()).tolist() == [0] * len(scale_cols)
    assert df.iloc[:, scale_cols].apply(lambda x: x.std()).tolist() == [1] * len(scale_cols)