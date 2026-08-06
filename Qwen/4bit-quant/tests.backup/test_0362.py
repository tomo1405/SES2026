import pytest
from src_0362 import task_func
import pandas as pd
import os

@pytest.fixture
def setup_test_files(tmp_path):
    # Create a test Excel file with some data
    excel_file = tmp_path / "test.xlsx"
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False, sheet_name='Sheet1')

    # Define the CSV file path
    csv_file = tmp_path / "test.csv"

    return excel_file, csv_file

def test_task_func(setup_test_files):
    excel_file, csv_file = setup_test_files
    result = task_func(sheet_name='Sheet1', excel_file_location=str(excel_file), csv_file_location=str(csv_file))

    # Check if the CSV file was created
    assert os.path.exists(csv_file), "CSV file was not created."

    # Check if the result is correct
    expected_result = {'A': 6, 'B': 15}
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(sheet_name='Sheet1', excel_file_location='non_existent_file.xlsx')
    assert "Excel file not found at non_existent_file.xlsx" in str(excinfo.value)

def test_task_func_value_error():
    with pytest.raises(ValueError) as excinfo:
        task_func(sheet_name='NonExistentSheet', excel_file_location='test.xlsx')
    assert "Error in processing Excel file:" in str(excinfo.value)