import pandas as pd
import numpy as np
from random import choice
from src_0194 import task_func
import pytest

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

def test_task_func():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == columns
    for col in df.columns:
        data_type = df[col].dtype
        if data_type == np.object_:
            assert all(isinstance(val, str) for val in df[col])
        elif data_type == np.int64:
            assert all(isinstance(val, int) for val in df[col])
        elif data_type == np.float64:
            assert all(isinstance(val, float) for val in df[col])
        elif data_type == np.ndarray:
            assert all(isinstance(val, list) for val in df[col])
        elif data_type == np.void:
            assert all(isinstance(val, tuple) for val in df[col])
        elif data_type == np.record:
            assert all(isinstance(val, dict) for val in df[col])
        elif data_type == np.object_:
            assert all(isinstance(val, set) for val in df[col])

if __name__ == "__main__":
    pytest.main()