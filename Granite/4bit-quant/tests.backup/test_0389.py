import pytest
from src_0389 import task_func

def test_task_func():
    my_tuple = ('col1', 'col2', 'col3')
    path_csv_files = ['path/to/file1.csv', 'path/to/file2.csv']
    expected_output = {'col1': collections.Counter({'a': 2, 'b': 1}),
                       'col2': collections.Counter({'c': 3, 'd': 2}),
                       'col3': collections.Counter({'e': 1, 'f': 1})}

    actual_output = task_func(my_tuple, path_csv_files)

    assert actual_output == expected_output