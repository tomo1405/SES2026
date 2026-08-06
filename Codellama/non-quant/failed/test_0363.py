import pytest
from src_0363 import task_func

def test_task_func_valid_input():
    original_file_location = "test.xlsx"
    new_file_location = "new_test.xlsx"
    sheet_name = "Sheet1"

    # Test with valid input
    result = task_func(original_file_location, new_file_location, sheet_name)
    assert result is not None
    assert isinstance(result, pd.DataFrame)

def test_task_func_invalid_input():
    original_file_location = "test.xlsx"
    new_file_location = "new_test.xlsx"
    sheet_name = "Sheet1"

    # Test with invalid input
    with pytest.raises(FileNotFoundError):
        task_func(original_file_location, new_file_location, sheet_name)

def test_task_func_invalid_sheet_name():
    original_file_location = "test.xlsx"
    new_file_location = "new_test.xlsx"
    sheet_name = "Sheet2"

    # Test with invalid sheet name
    with pytest.raises(ValueError):
        task_func(original_file_location, new_file_location, sheet_name)