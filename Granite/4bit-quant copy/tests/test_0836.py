import pytest
from src_0836 import task_func

def test_task_func():
    n_rows = 10
    remove_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    random_seed = 42
    df = task_func(n_rows, remove_cols, columns, random_seed)
    assert df.shape == (n_rows, len(columns) - len(remove_cols))
    assert df.columns.tolist() == list(columns)[len(remove_cols):]

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(-1, [0, 1])