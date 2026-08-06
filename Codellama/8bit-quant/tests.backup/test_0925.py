import pytest
from src_0925 import task_func
import pandas as pd

def test_task_func_valid_file_path():
    file_path = 'test_data.csv'
    column_name = 'name'
    df = pd.DataFrame({'name': ['John', 'Jane', 'Jim']})
    df.to_csv(file_path, index=False)

    result = task_func(file_path, column_name)

    assert result.equals(df)

def test_task_func_invalid_file_path():
    file_path = 'invalid_file.csv'
    column_name = 'name'

    with pytest.raises(SystemExit):
        task_func(file_path, column_name)

def test_task_func_column_does_not_exist():
    file_path = 'test_data.csv'
    column_name = 'invalid_column'
    df = pd.DataFrame({'name': ['John', 'Jane', 'Jim']})
    df.to_csv(file_path, index=False)

    result = task_func(file_path, column_name)

    assert result.equals(df)
    assert result['invalid_column'].isnull().all()