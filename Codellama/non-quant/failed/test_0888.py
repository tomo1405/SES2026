import pytest
from src_0888 import task_func

def test_task_func():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row_num = 50
    seed = 123

    df = task_func(T1, row_num, seed)

    assert df.shape == (row_num, 9)
    assert df.columns.tolist() == ['Col_1', 'Col_2', 'Col_3', 'Col_4', 'Col_5', 'Col_6', 'Col_7', 'Col_8', 'Col_9']
    assert df.dtypes.tolist() == [np.int64, np.int64, np.int64, np.int64, np.int64, np.int64, np.int64, np.int64, np.int64]
    assert df.sum().tolist() == [10, 10, 10, 10, 10, 10, 10, 10, 10]