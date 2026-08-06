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
    data_dir = "path/to/data"
    csv_files = ["file1.csv", "file2.csv"]
    expected_df = pd.DataFrame() # Replace this with the expected DataFrame

    actual_df = task_func(data_dir, csv_files)

    assert actual_df.equals(expected_df)