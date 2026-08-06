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
    # Test case 1: File does not exist
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        task_func('path/to/nonexistent/file.csv', 'column_name')
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code != 0

    # Test case 2: Column exists
    df = pd.DataFrame({'column_name': ['value1\n', 'value2\n', 'value3\n']})
    df_expected = pd.DataFrame({'column_name': ['value1<br>', 'value2<br>', 'value3<br>']})
    df_actual = task_func(df, 'column_name')
    assert df_actual.equals(df_expected)

    # Test case 3: Column does not exist
    df = pd.DataFrame({'other_column': ['value1', 'value2', 'value3']})
    df_expected = pd.DataFrame({'other_column': ['value1', 'value2', 'value3']})
    df_actual = task_func(df, 'column_name')
    assert df_actual.equals(df_expected)