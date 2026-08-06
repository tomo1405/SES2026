python
import os
import pandas as pd
import pytest

from src_0363 import task_func

def test_task_func_valid_input():
    # Test with valid input
    original_file_location = "test.xlsx"
    new_file_location = "new_test.xlsx"
    sheet_name = "Sheet1"
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    # Create test Excel file
    expected_df.to_excel(original_file_location, index=False)

    # Call task_func function
    actual_df = task_func(original_file_location, new_file_location, sheet_name)

    # Check if the actual DataFrame is equal to the expected DataFrame
    assert actual_df.equals(expected_df)

    # Check if the new Excel file was created
    assert os.path.exists(new_file_location)

    # Remove the test Excel file
    os.remove(original_file_location)
    os.remove(new_file_location)

def test_task_func_invalid_input():
    # Test with invalid input
    original_file_location = "invalid_file.xlsx"
    new_file_location = "new_test.xlsx"
    sheet_name = "Sheet1"

    # Call task_func function
    with pytest.raises(FileNotFoundError):
        task_func(original_file_location, new_file_location, sheet_name)