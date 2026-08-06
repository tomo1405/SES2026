python
import pytest
from src_0925 import task_func

def test_task_func_valid_file():
    file_path = 'data/test_data.csv'
    column_name = 'text'
    expected_df = pd.read_csv(file_path)
    expected_df[column_name] = expected_df[column_name].replace({'\n': '<br>'}, regex=True)
    actual_df = task_func(file_path, column_name)
    assert actual_df.equals(expected_df)

def test_task_func_invalid_file():
    file_path = 'data/invalid_file.csv'
    column_name = 'text'
    with pytest.raises(SystemExit):
        task_func(file_path, column_name)

def test_task_func_invalid_column():
    file_path = 'data/test_data.csv'
    column_name = 'invalid_column'
    expected_df = pd.read_csv(file_path)
    actual_df = task_func(file_path, column_name)
    assert actual_df.equals(expected_df)