import pytest
from src_0925 import task_func

def test_task_func_valid_file_path():
    file_path = 'test_data.csv'
    column_name = 'name'
    df = pd.DataFrame({'name': ['John Doe', 'Jane Doe']})
    df.to_csv(file_path, index=False)

    result = task_func(file_path, column_name)

    assert result.equals(df)

def test_task_func_invalid_file_path():
    file_path = 'invalid_file.csv'
    column_name = 'name'

    with pytest.raises(SystemExit) as e:
        task_func(file_path, column_name)

    assert e.type == SystemExit
    assert e.value.code == 1

def test_task_func_invalid_column_name():
    file_path = 'test_data.csv'
    column_name = 'invalid_column'
    df = pd.DataFrame({'name': ['John Doe', 'Jane Doe']})
    df.to_csv(file_path, index=False)

    result = task_func(file_path, column_name)

    assert result.equals(df)
    assert 'Column' in result.columns
    assert 'invalid_column' not in result.columns