import pytest
from src_0408 import task_func

def test_task_func():
    # Test case 1: Valid input
    file_name = "example.xlsx"
    excel_file_path = "path/to/excel"
    csv_file_path = "path/to/csv"
    expected_output = "example.csv"

    result = task_func(file_name, excel_file_path, csv_file_path)
    assert result == expected_output

    # Add more test cases as needed