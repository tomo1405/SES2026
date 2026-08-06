import os
import pandas as pd
import numpy as np
import pytest
from src_0410 import task_func

@pytest.mark.parametrize("excel_file_path, file_name, column_name, expected_output", [
    ("path/to/excel/files", "file1.xlsx", "column1", {'mean': 10, 'median': 10, 'std_dev': 0}),
    ("path/to/excel/files", "file2.xlsx", "column2", {'mean': 20, 'median': 20, 'std_dev': 5}),
    ("path/to/excel/files", "file3.xlsx", "column3", {'mean': 30, 'median': 30, 'std_dev': 10}),
])
def test_task_func(excel_file_path, file_name, column_name, expected_output):
    actual_output = task_func(excel_file_path, file_name, column_name)
    assert actual_output == expected_output