import pytest
from src_0592 import task_func

def test_task_func():
    hours = 10
    file_path, ax = task_func(hours)
    assert file_path == 'custom_data.csv'
    assert ax is not None

def test_task_func_with_invalid_file_path():
    hours = 10
    with pytest.raises(ValueError):
        task_func(hours, file_path='invalid_file_path.csv')

def test_task_func_with_invalid_hours():
    with pytest.raises(ValueError):
        task_func(-1)