import os
import glob
import csv
import pytest
from src_0906 import task_func

def test_task_func():
    directory_path = '/path/to/directory'
    file_extension = '.csv'
    expected_output = {
        'file1': [['row1', 'col1'], ['row2', 'col2']],
        'file2': [['row3', 'col3'], ['row4', 'col4']]
    }

    data = task_func(directory_path, file_extension)

    assert data == expected_output