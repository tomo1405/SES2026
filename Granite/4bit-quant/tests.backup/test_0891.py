import os
import random
import pandas as pd
import pytest

from src_0891 import task_func

def test_task_func():
    data_dir = "path/to/data"
    csv_files = ['file1.csv', 'file2.csv', 'file3.csv']
    seed = 42  # Set a fixed seed for reproducibility

    file, selected_rows = task_func(data_dir, csv_files, seed)

    assert isinstance(file, str)
    assert file in csv_files
    assert isinstance(selected_rows, pd.DataFrame)
    assert len(selected_rows) > 0
    assert selected_rows.shape[0] <= len(csv_files)

def test_task_func_empty_data():
    data_dir = "path/to/data"
    csv_files = ['file1.csv', 'file2.csv', 'file3.csv']
    seed = 42  # Set a fixed seed for reproducibility

    # Mock an empty DataFrame
    def mock_read_csv(*args, **kwargs):
        return pd.DataFrame()

    with pytest.raises(pd.errors.EmptyDataError):
        with patch('pandas.read_csv', side_effect=mock_read_csv):
            task_func(data_dir, csv_files, seed)