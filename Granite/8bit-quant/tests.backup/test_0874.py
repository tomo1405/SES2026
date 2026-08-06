import csv
import os
import pytest
from src_0874 import task_func

def test_task_func():
    data = [("Name", "Age", "Gender"), ("Alice", 25, "Female"), ("Bob", 30, "Male")]
    file_path = "test.csv"
    headers = ["Name", "Age", "Gender"]

    expected_output = os.path.abspath(file_path)

    actual_output = task_func(data, file_path, headers)

    assert actual_output == expected_output