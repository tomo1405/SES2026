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
    expected_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

    # Test case 1: Test with valid data
    actual_df = task_func(data_dir, csv_files)
    assert actual_df.equals(expected_df)

    # Test case 2: Test with invalid data
    with pytest.raises(FileNotFoundError):
        task_func('invalid_data', csv_files)