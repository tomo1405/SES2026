import pytest
from src_0836 import task_func

def test_task_func():
    n_rows = 10
    remove_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    random_seed = 42

    df = task_func(n_rows, remove_cols, columns, random_seed)

    assert df.shape == (n_rows, len(columns) - len(remove_cols))
    assert all(df.columns == columns)
    assert all(df.index == np.arange(n_rows))
    assert all(df.values == np.random.randint(0, 100, size=(n_rows, len(columns) - len(remove_cols))))