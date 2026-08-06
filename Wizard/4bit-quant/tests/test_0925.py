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
    # Test case 1: file exists, column exists
    file_path = 'data.csv'
    column_name = 'text'
    expected_df = pd.DataFrame({'id': [1, 2, 3], 'text': ['This is a\ntest', 'Another\ntest', 'Last\ntest']})
    actual_df = task_func(file_path, column_name)
    assert actual_df.equals(expected_df)

    # Test case 2: file exists, column does not exist
    file_path = 'data.csv'
    column_name = 'title'
    expected_df = pd.DataFrame({'id': [1, 2, 3], 'text': ['This is a\ntest', 'Another\ntest', 'Last\ntest']})
    actual_df = task_func(file_path, column_name)
    assert actual_df.equals(expected_df)

    # Test case 3: file does not exist
    file_path = 'nonexistent.csv'
    column_name = 'text'
    with pytest.raises(SystemExit):
        task_func(file_path, column_name)