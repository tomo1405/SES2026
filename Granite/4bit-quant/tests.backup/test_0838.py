import pytest
from src_0838 import task_func

def test_task_func():
    n_rows = 100
    scale_cols = [0, 2, 4]
    columns = ['A', 'B', 'C', 'D', 'E']
    random_seed = 42
    df = task_func(n_rows, scale_cols, columns, random_seed)
    
    assert df.shape == (n_rows, len(columns))
    for i in scale_cols:
        assert df[columns[i]].mean() == pytest.approx(0.0)
        assert df[columns[i]].std() == pytest.approx(1.0)