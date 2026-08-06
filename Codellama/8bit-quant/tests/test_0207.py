import pytest
from src_0207 import task_func

def test_task_func_valid_file():
    file_name = 'test_data.csv'
    json_file_name = task_func(file_name)
    assert json_file_name == 'test_data.json'

def test_task_func_invalid_file():
    file_name = 'invalid_file.csv'
    with pytest.raises(FileNotFoundError):
        task_func(file_name)