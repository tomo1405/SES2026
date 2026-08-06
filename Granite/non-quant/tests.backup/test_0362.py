import pytest
from src_0362 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    expected_output = {'column1': 10, 'column2': 20, 'column3': 30}
    actual_output = task_func('Sheet1')
    assert actual_output == expected_output, "Test case 1 failed"

    # Test case 2: Test with invalid input (file not found)
    with pytest.raises(FileNotFoundError):
        task_func('Sheet1', excel_file_location='invalid_file.xlsx')

    # Test case 3: Test with invalid input (value error)
    with pytest.raises(ValueError):
        task_func('Sheet1', excel_file_location='test.xlsx', csv_file_location='invalid_file.csv')