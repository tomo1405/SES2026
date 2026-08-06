import pandas as pd
import logging
import pytest

from src_0362 import task_func

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_task_func():
    # Test case 1: Test with valid input
    excel_file_location = "test.xlsx"
    sheet_name = "Sheet1"
    expected_column_sum = {"A": 10, "B": 20, "C": 30}

    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    df.to_excel(excel_file_location, sheet_name=sheet_name, index=False)

    result = task_func(sheet_name, excel_file_location, "test.csv")
    assert result == expected_column_sum

    # Test case 2: Test with invalid input (file not found)
    with pytest.raises(FileNotFoundError):
        task_func(sheet_name, "invalid_file.xlsx", "test.csv")

    # Test case 3: Test with invalid input (value error)
    df = pd.DataFrame({"A": [1, 2, "three"], "B": [4, 5, 6], "C": [7, 8, 9]})
    df.to_excel(excel_file_location, sheet_name=sheet_name, index=False)

    with pytest.raises(ValueError):
        task_func(sheet_name, excel_file_location, "test.csv")

if __name__ == "__main__":
    test_task_func()