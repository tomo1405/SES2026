import pytest
from src_0889 import task_func
import pandas as pd
import os

def test_task_func():
    data_dir = "path/to/data/dir"
    csv_files = ["file1.csv", "file2.csv"]
    expected_df = pd.DataFrame({"column1": [1, 2, 3], "column2": [4, 5, 6]})

    merged_df = task_func(data_dir, csv_files)

    assert merged_df.equals(expected_df)