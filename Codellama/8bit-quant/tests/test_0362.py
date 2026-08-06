from unittest.mock import patch

import pytest
from src_0362 import task_func


def test_task_func_valid_input():
    # Test with valid input
    sheet_name = "Sheet1"
    excel_file_location = "test.xlsx"
    csv_file_location = "test.csv"
    expected_output = {"Column1": 10, "Column2": 20, "Column3": 30}

    # Mock the pandas.read_excel and pandas.to_csv functions
    with patch("pandas.read_excel") as mock_read_excel, patch("pandas.to_csv") as mock_to_csv:
        # Set the return value of the mock functions
        mock_read_excel.return_value = pd.DataFrame({"Column1": [1, 2, 3], "Column2": [4, 5, 6], "Column3": [7, 8, 9]})
        mock_to_csv.return_value = None

        # Call the function with the valid input
        output = task_func(sheet_name, excel_file_location, csv_file_location)

        # Assert that the output is correct
        assert output == expected_output

def test_task_func_invalid_input():
    # Test with invalid input
    sheet_name = "Sheet1"
    excel_file_location = "test.xlsx"
    csv_file_location = "test.csv"

    # Mock the pandas.read_excel and pandas.to_csv functions
    with patch("pandas.read_excel") as mock_read_excel, patch("pandas.to_csv") as mock_to_csv:
        # Set the return value of the mock functions
        mock_read_excel.side_effect = FileNotFoundError("Excel file not found")
        mock_to_csv.return_value = None

        # Call the function with the invalid input
        with pytest.raises(FileNotFoundError):
            task_func(sheet_name, excel_file_location, csv_file_location)

def test_task_func_error_in_processing():
    # Test with error in processing
    sheet_name = "Sheet1"
    excel_file_location = "test.xlsx"
    csv_file_location = "test.csv"

    # Mock the pandas.read_excel and pandas.to_csv functions
    with patch("pandas.read_excel") as mock_read_excel, patch("pandas.to_csv") as mock_to_csv:
        # Set the return value of the mock functions
        mock_read_excel.return_value = pd.DataFrame({"Column1": [1, 2, 3], "Column2": [4, 5, 6], "Column3": [7, 8, 9]})
        mock_to_csv.side_effect = ValueError("Error in processing Excel file")

        # Call the function with the invalid input
        with pytest.raises(ValueError):
            task_func(sheet_name, excel_file_location, csv_file_location)