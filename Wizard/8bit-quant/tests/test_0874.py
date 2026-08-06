python
import csv
import os
import pytest

from src_0874 import task_func

def test_task_func_valid_input():
    data = [
        ['John', 'Doe', '123 Main St', '123-456-7890'],
        ['Jane', 'Doe', '456 Oak Ave', '555-555-5555'],
        ['Bob', 'Smith', '789 Elm St', '555-555-5555']
    ]
    file_path = 'test.csv'
    headers = ['First Name', 'Last Name', 'Address', 'Phone']
    expected_output = os.path.abspath(file_path)

    assert task_func(data, file_path, headers) == expected_output

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]

    assert rows == [headers] + data

    os.remove(file_path)

def test_task_func_invalid_file_path():
    data = [
        ['John', 'Doe', '123 Main St', '123-456-7890'],
        ['Jane', 'Doe', '456 Oak Ave', '555-555-5555'],
        ['Bob', 'Smith', '789 Elm St', '555-555-5555']
    ]
    file_path = None
    headers = ['First Name', 'Last Name', 'Address', 'Phone']

    with pytest.raises(ValueError):
        task_func(data, file_path, headers)