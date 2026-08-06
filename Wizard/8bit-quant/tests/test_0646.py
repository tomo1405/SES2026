python
import os
import pandas as pd
import pytest

from src_0646 import task_func

def test_task_func_valid_filename():
    # Test with a valid filename
    filename = 'test.csv'
    with open(filename, 'w') as file:
        file.write('col1,col2\n1,2\n3,4')
    df = task_func(filename)
    assert df.shape == (2, 2)
    os.remove(filename)

def test_task_func_invalid_filename():
    # Test with an invalid filename
    with pytest.raises(FileNotFoundError):
        task_func('invalid.csv')

def test_task_func_empty_file():
    # Test with an empty file
    filename = 'empty.csv'
    with open(filename, 'w') as file:
        pass
    df = task_func(filename)
    assert df.shape == (0, 0)
    os.remove(filename)