import pandas as pd
import pytest
from src_0928 import task_func

def test_task_func():
    file_path = 'path/to/test/file.csv'
    column_name = 'test_column'
    expected_df = pd.DataFrame({
        'test_column': [1, 2, 3]
    })
    actual_df = task_func(file_path, column_name)
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_with_null_values():
    file_path = 'path/to/test/file_with_nulls.csv'
    column_name = 'test_column'
    expected_df = pd.DataFrame({
        'test_column': [0, 1, 2]
    })
    actual_df = task_func(file_path, column_name)
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_with_invalid_file_path():
    file_path = 'path/to/invalid/file.csv'
    column_name = 'test_column'
    with pytest.raises(FileNotFoundError):
        task_func(file_path, column_name)