import os
import re
import pandas as pd
import pytest

def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    matched_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.match(pattern, file):
                matched_paths.append(os.path.join(root, file))

    df = pd.DataFrame(matched_paths, columns=['File Path'])
    df.to_csv(output_csv, index=False)

    return df

def test_task_func():
    # Test case 1: Test if the function returns a DataFrame with the correct columns
    df = task_func(pattern='.*', directory='test_directory', output_csv='test_output.csv')
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['File Path']

    # Test case 2: Test if the function correctly matches files based on the pattern
    df = task_func(pattern='^test_.*\.csv$', directory='test_directory', output_csv='test_output.csv')
    assert len(df) > 0
    assert all(df['File Path'].str.match('^test_.*\.csv$'))

    # Test case 3: Test if the function correctly writes the DataFrame to a CSV file
    df = task_func(pattern='.*', directory='test_directory', output_csv='test_output.csv')
    assert os.path.exists('test_output.csv')
    os.remove('test_output.csv')