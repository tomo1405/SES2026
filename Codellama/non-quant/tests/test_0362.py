import pytest
from src_0362 import task_func

def test_task_func_valid_input():
    # Test with valid input
    sheet_name = "Sheet1"
    excel_file_location = "test.xlsx"
    csv_file_location = "test.csv"
    expected_output = {"Column1": 10, "Column2": 20, "Column3": 30}

    # Call the function with valid input
    output = task_func(sheet_name, excel_file_location, csv_file_location)

    # Assert that the output is correct
    assert output == expected_output

def test_task_func_invalid_input():
    # Test with invalid input
    sheet_name = "Sheet1"
    excel_file_location = "test.xlsx"
    csv_file_location = "test.csv"
    expected_output = {"Column1": 10, "Column2": 20, "Column3": 30}

    # Call the function with invalid input
    output = task_func(sheet_name, excel_file_location, csv_file_location)

    # Assert that the output is correct
    assert output == expected_output

def test_task_func_invalid_file():
    # Test with invalid file
    sheet_name = "Sheet1"
    excel_file_location = "test.xlsx"
    csv_file_location = "test.csv"
    expected_output = {"Column1": 10, "Column2": 20, "Column3": 30}

    # Call the function with invalid file
    output = task_func(sheet_name, excel_file_location, csv_file_location)

    # Assert that the output is correct
    assert output == expected_output

def test_task_func_invalid_sheet():
    # Test with invalid sheet
    sheet_name = "Sheet1"
    excel_file_location = "test.xlsx"
    csv_file_location = "test.csv"
    expected_output = {"Column1": 10, "Column2": 20, "Column3": 30}

    # Call the function with invalid sheet
    output = task_func(sheet_name, excel_file_location, csv_file_location)

    # Assert that the output is correct
    assert output == expected_output