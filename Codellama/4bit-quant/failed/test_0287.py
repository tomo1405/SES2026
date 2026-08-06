import pytest
from src_0287 import task_func

def test_task_func():
    output_file = 'output.csv'
    test_directory = 'test_directory'
    total_words = task_func(output_file, test_directory)
    assert total_words == 10

def test_task_func_invalid_output_file():
    output_file = 'invalid_output_file.csv'
    test_directory = 'test_directory'
    with pytest.raises(Exception):
        task_func(output_file, test_directory)

def test_task_func_invalid_test_directory():
    output_file = 'output.csv'
    test_directory = 'invalid_test_directory'
    with pytest.raises(Exception):
        task_func(output_file, test_directory)