python
import os
import glob
import csv
import pytest

def task_func(directory_path, file_extension='.csv'):
    data = {}

    for file in glob.glob(os.path.join(directory_path, '*' + file_extension)):
        filename = os.path.splitext(os.path.basename(file))[0]
        with open(file, 'r') as f:
            reader = csv.reader(f)
            data[filename] = list(reader)

    return data

def test_task_func():
    # Test case 1: Valid directory path and file extension
    directory_path = 'tests/data'
    file_extension = '.csv'
    expected_data = {'test1': [['1', '2', '3'], ['4', '5', '6']], 'test2': [['7', '8', '9'], ['10', '11', '12']]}
    assert task_func(directory_path, file_extension) == expected_data

    # Test case 2: Invalid directory path
    directory_path = 'invalid_directory'
    file_extension = '.csv'
    with pytest.raises(FileNotFoundError):
        task_func(directory_path, file_extension)

    # Test case 3: Invalid file extension
    directory_path = 'tests/data'
    file_extension = '.txt'
    with pytest.raises(FileNotFoundError):
        task_func(directory_path, file_extension)