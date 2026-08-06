import pytest
from src_0950 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    rows = 5
    columns = 3
    seed = 123
    expected_matrix = np.array([[0.5488135, 0.71518934, 0.60276335],
                               [0.4236548, 0.8300264, 0.89177364],
                               [0.9492429, 0.97910626, 0.30548734],
                               [0.5689483, 0.5311472, 0.99406426],
                               [0.9396925, 0.7883327, 0.95755196]])
    expected_df = pd.DataFrame(expected_matrix)
    result_df = task_func(rows, columns, seed)
    np.testing.assert_array_equal(result_df.values, expected_df.values)

def test_task_func_no_seed():
    rows = 5
    columns = 3
    result_df = task_func(rows, columns)
    assert result_df.shape == (rows, columns)

def test_task_func_invalid_input():
    rows = 0
    columns = 3
    with pytest.raises(ValueError):
        task_func(rows, columns)

if __name__ == '__main__':
    pytest.main()