import pytest
from src_0287 import task_func

def test_task_func():
    test_directory = './test_files/'
    output_file = './output.csv'
    total_words = task_func(output_file, test_directory)
    assert total_words > 0

def test_task_func_with_invalid_directory():
    test_directory = './invalid_directory/'
    output_file = './output.csv'
    with pytest.raises(Exception):
        task_func(output_file, test_directory)