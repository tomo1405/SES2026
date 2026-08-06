python
import pandas as pd
import os
import pytest

def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    merged_df = pd.DataFrame()

    for file in csv_files:
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)
        merged_df = pd.concat([merged_df, df], ignore_index=True)

    return merged_df

def test_task_func():
    data_dir = 'data'
    csv_files = ['file1.csv', 'file2.csv']

    # Test case 1: Test with valid data directory and csv files
    merged_df = task_func(data_dir, csv_files)
    assert isinstance(merged_df, pd.DataFrame)
    assert len(merged_df) == 2

    # Test case 2: Test with invalid data directory
    with pytest.raises(FileNotFoundError):
        task_func('invalid_data_dir', csv_files)

    # Test case 3: Test with invalid csv files
    with pytest.raises(FileNotFoundError):
        task_func(data_dir, ['invalid_file1.csv', 'invalid_file2.csv'])