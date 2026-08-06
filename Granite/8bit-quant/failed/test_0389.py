import collections
import pandas as pd
from src_0389 import task_func

def test_task_func():
    my_tuple = ('col1', 'col2', 'col3')
    path_csv_files = ['path/to/file1.csv', 'path/to/file2.csv']
    counter = task_func(my_tuple, path_csv_files)
    assert isinstance(counter, dict)
    assert all(isinstance(key, str) and isinstance(value, collections.Counter) for key, value in counter.items())
    assert all(key in my_tuple for key in counter.keys())

def test_task_func_with_empty_csv_files():
    my_tuple = ('col1', 'col2', 'col3')
    path_csv_files = ['path/to/empty_file1.csv', 'path/to/empty_file2.csv']
    counter = task_func(my_tuple, path_csv_files)
    assert all(value == collections.Counter() for value in counter.values())

def test_task_func_with_missing_column():
    my_tuple = ('col1', 'col2', 'col3')
    path_csv_files = ['path/to/file1.csv', 'path/to/file2.csv']
    counter = task_func(my_tuple, path_csv_files)
    assert 'col4' not in counter.keys()