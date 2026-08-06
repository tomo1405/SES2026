import pytest
from src_0951 import task_func

def test_task_func():
    rows = 3
    columns = 2
    seed = 0
    U, s, Vh = task_func(rows, columns, seed)

    assert U.shape == (rows, rows)
    assert s.shape == (rows,)
    assert Vh.shape == (columns, columns)

    assert np.allclose(U @ np.diag(s) @ Vh, matrix)