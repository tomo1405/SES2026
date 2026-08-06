import pytest
from src_0363 import task_func
import pandas as pd
import os

@pytest.fixture
def setup_and_teardown():
    # Create a temporary test file for testing
    test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    test_file_path = "test.xlsx"
    test_sheet_name = "Sheet1"
    test_new_file_path = "new_test.xlsx"

    test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    test_data.to_excel(test_file_path, index=False)

    yield test_file_path, test_new_file_path, test_sheet_name

    # Clean up: remove the test file after the test
    os.remove(test_file_path)
    os.remove(test_new_file_path)

def test_task_func(setup_and_teardown):
    test_file_path, test_new_file_path, test_sheet_name = setup_and_teardown

    # Call the function with the test data
    result = task_func(original_file_location=test_file_path, new_file_location=test_new_file_path, sheet_name=test_sheet_name)

    # Check the output
    assert result.equals(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}))