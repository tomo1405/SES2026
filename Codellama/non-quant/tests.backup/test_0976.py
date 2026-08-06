import pytest
from src_0976 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    rows = 5
    columns = ["A", "B", "C", "D", "E"]
    seed = 0
    expected_columns = sorted(list(set(columns)))
    expected_data = np.random.rand(rows, len(expected_columns))
    np.random.shuffle(expected_columns)
    expected_df = pd.DataFrame(expected_data, columns=expected_columns)

    actual_df = task_func(rows, columns, seed)

    assert actual_df.columns.tolist() == expected_df.columns.tolist()
    assert np.allclose(actual_df.values, expected_df.values)