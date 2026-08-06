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
    test_directory_path = '/path/to/test/directory'
    test_file_extension = '.csv'
    expected_output = {
        'file1': [['data1', 'data2'], ['data3', 'data4']],
        'file2': [['data5', 'data6'], ['data7', 'data8']]
    }

    actual_output = task_func(test_directory_path, test_file_extension)

    assert actual_output == expected_output