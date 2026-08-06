import pytest
from src_0019 import task_func

def test_task_func_valid_file():
    file = 'test_data.csv'
    expected_split_files = ['split_0.csv', 'split_1.csv', 'split_2.csv', 'split_3.csv', 'split_4.csv']
    assert task_func(file) == expected_split_files

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