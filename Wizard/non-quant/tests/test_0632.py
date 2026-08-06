python
import csv
import os
import pytest

from src_0632 import task_func

def test_task_func():
    # Test case 1: Test with default output directory
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    filename = 'test.csv'
    file_path = task_func(df, filename)
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)
    os.remove(file_path)

    # Test case 2: Test with custom output directory
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    filename = 'test.csv'
    output_dir = './custom_output'
    file_path = task_func(df, filename, output_dir)
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)
    assert os.path.abspath(file_path).startswith(os.path.abspath(output_dir))
    os.remove(file_path)