import pytest
from src_0888 import task_func

def test_task_func():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row_num = 50
    seed = 123

    df = task_func(T1, row_num, seed)

    assert df.shape == (row_num, sum(flattened_list))
    assert all(df.columns == [f'Col_{i+1}' for i in range(total_cols)])
    assert all(df.dtypes == np.int64)
    assert all(df.values >= 0)
    assert all(df.values <= 100)