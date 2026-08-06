import csv

import pytest
from src_0721 import task_func


def test_task_func():
    FILE_NAME = 'task_func_data/Output.txt'
    FIELDS = ['Timestamp', 'Temperature', 'Humidity']

    # Test that the function returns the correct file name
    assert task_func() == FILE_NAME

    # Test that the file exists and has the correct headers
    with open(FILE_NAME, 'r') as f:
        csv_reader = csv.reader(f)
        headers = next(csv_reader)
        assert headers == FIELDS

    # Test that the file has the correct data
    with open(FILE_NAME, 'r') as f:
        csv_reader = csv.reader(f)
        data = next(csv_reader)
        assert data[0] == 'Timestamp'
        assert data[1] == 'Temperature'
        assert data[2] == 'Humidity'

    # Test that the function raises an error if the file already exists
    with pytest.raises(FileExistsError):
        task_func()