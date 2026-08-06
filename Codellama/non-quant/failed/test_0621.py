import pytest
from src_0621 import task_func

def test_task_func():
    L = [(1, 2), (3, 4)]
    df = task_func(L)
    assert df.shape == (1 * 2, 3 * 4)
    assert df.dtypes == np.int64
    assert np.all(df >= RANGE[0])
    assert np.all(df <= RANGE[1])