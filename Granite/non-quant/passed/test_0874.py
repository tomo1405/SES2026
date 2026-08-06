import csv
import os
import pytest
from src_0874 import task_func

def test_task_func():
    data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
    file_path = "test.csv"
    headers = ["Name", "Age"]

    expected_output = os.path.abspath(file_path)

    actual_output = task_func(data, file_path, headers)

    assert actual_output == expected_output

def test_task_func_invalid_file_path():
    data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
    file_path = None
    headers = ["Name", "Age"]

    with pytest.raises(ValueError) as excinfo:
        task_func(data, file_path, headers)

    assert "The file path is invalid." in str(excinfo.value)