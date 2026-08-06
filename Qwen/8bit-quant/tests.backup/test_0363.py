import pytest
from src_0363 import task_func
import pandas as pd
import os

def test_task_func_default_parameters(tmpdir):
    # Create a temporary directory
    temp_dir = tmpdir.mkdir("temp")
    original_file_path = temp_dir.join("test.xlsx")
    new_file_path = temp_dir.join("new_test.xlsx")

    # Create a sample DataFrame and save it to the original file
    sample_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(sample_data)
    df.to_excel(original_file_path, index=False)

    # Call the function with default parameters
    result_df = task_func(str(original_file_path), str(new_file_path))

    # Check if the result matches the original data
    assert result_df.equals(df)

def test_task_func_custom_sheet_name(tmpdir):
    # Create a temporary directory
    temp_dir = tmpdir.mkdir("temp")
    original_file_path = temp_dir.join("test.xlsx")
    new_file_path = temp_dir.join("new_test.xlsx")

    # Create a sample DataFrame and save it to the original file with a custom sheet name
    sample_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(sample_data)
    df.to_excel(original_file_path, sheet_name="CustomSheet", index=False)

    # Call the function with a custom sheet name
    result_df = task_func(str(original_file_path), str(new_file_path), sheet_name="CustomSheet")

    # Check if the result matches the original data
    assert result_df.equals(df)

def test_task_func_file_not_found():
    # Call the function with a non-existent file path
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_file.xlsx")

    # Check if the correct error message is raised
    assert str(excinfo.value) == "No file found at non_existent_file.xlsx"

def test_task_func_invalid_sheet_name(tmpdir):
    # Create a temporary directory
    temp_dir = tmpdir.mkdir("temp")
    original_file_path = temp_dir.join("test.xlsx")
    new_file_path = temp_dir.join("new_test.xlsx")

    # Create a sample DataFrame and save it to the original file
    sample_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(sample_data)
    df.to_excel(original_file_path, index=False)

    # Call the function with an invalid sheet name
    with pytest.raises(ValueError) as excinfo:
        task_func(str(original_file_path), str(new_file_path), sheet_name="InvalidSheet")

    # Check if the correct error message is raised
    assert str(excinfo.value).startswith("Error reading sheet:")