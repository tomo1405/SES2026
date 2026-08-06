import os
import glob
import csv
from src_0906 import task_func

def test_task_func():
    directory_path = '/path/to/directory'
    file_extension = '.csv'
    data = task_func(directory_path, file_extension)
    assert isinstance(data, dict)
    for filename, rows in data.items():
        assert isinstance(filename, str)
        assert isinstance(rows, list)
        for row in rows:
            assert isinstance(row, list)