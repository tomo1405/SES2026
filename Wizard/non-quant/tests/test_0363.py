python
import os
import pandas as pd
import pytest

from src_0363 import task_func

def test_task_func_valid_file():
    # Test with valid file
    original_file_location = "test.xlsx"
    new_file_location = "new_test.xlsx"
    sheet_name = "Sheet1"
    task_func(original_file_location, new_file_location, sheet_name)
    assert os.path.exists(new_file_location)

def test_task_func_invalid_file():
    # Test with invalid file
    original_file_location = "invalid_file.xlsx"
    new_file_location = "new_test.xlsx"
    sheet_name = "Sheet1"
    with pytest.raises(FileNotFoundError):
        task_func(original_file_location, new_file_location, sheet_name)

def test_task_func_invalid_sheet():
    # Test with invalid sheet name
    original_file_location = "test.xlsx"
    new_file_location = "new_test.xlsx"
    sheet_name = "Invalid Sheet"
    with pytest.raises(ValueError):
        task_func(original_file_location, new_file_location, sheet_name)