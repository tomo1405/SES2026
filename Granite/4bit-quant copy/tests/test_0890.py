import os
import pandas as pd
import numpy as np
from src_0890 import task_func
import pytest

def test_task_func():
    data_dir = "path/to/data"
    csv_file = "data.csv"
    expected_df = pd.DataFrame()
    actual_df = task_func(data_dir, csv_file)
    assert actual_df.equals(expected_df)

def test_task_func_with_numeric_columns():
    data_dir = "path/to/data"
    csv_file = "data.csv"
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, 5],
        'C': [1, 2, 3, 4, 5]
    })
    expected_df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [3, 2, 3, 4, 5],
        'C': [1, 2, 3, 4, 5]
    })
    actual_df = task_func(data_dir, csv_file)
    assert actual_df.equals(expected_df)