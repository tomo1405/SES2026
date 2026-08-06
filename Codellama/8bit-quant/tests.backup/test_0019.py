import pytest
from src_0019 import task_func

def test_task_func_valid_file():
    file = 'test_data.csv'
    assert task_func(file) == ['split_0', 'split_1', 'split_2', 'split_3', 'split_4']

def test_task_func_invalid_file():
    file = 'test_data.txt'
    assert task_func(file) == []

def test_task_func_invalid_extension():
    file = 'test_data.csv.txt'
    assert task_func(file) == []

def test_task_func_exception():
    file = 'test_data.csv'
    with pytest.raises(Exception):
        task_func(file)