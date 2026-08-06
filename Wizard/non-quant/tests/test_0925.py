python
import pandas as pd
import os
import sys
import pytest

def task_func(file_path: str, column_name: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        print(f'File does not exist: {file_path}')
        sys.exit(1)

    df = pd.read_csv(file_path)
    
    # Check if the column exists
    if column_name in df.columns:
        df[column_name] = df[column_name].replace({'\n': '<br>'}, regex=True)
    else:
        print(f"Column '{column_name}' does not exist in the DataFrame. No changes were made.")

    return df

def test_task_func():
    # Test case 1: Valid file path and column name
    df = task_func('data.csv', 'column_name')
    assert df.shape == (10, 2)
    assert df['column_name'][0] == 'value1<br>value2'

    # Test case 2: Invalid file path
    with pytest.raises(SystemExit):
        task_func('invalid_file.csv', 'column_name')

    # Test case 3: Column name does not exist
    df = task_func('data.csv', 'invalid_column_name')
    assert df.shape == (10, 1)
    assert df.columns.tolist() == ['column_name']