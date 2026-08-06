import pytest
from src_0363 import task_func
import pandas as pd
import os
import tempfile

def test_task_func_default_parameters():
    # Create a temporary directory and files
    with tempfile.TemporaryDirectory() as temp_dir:
        original_file_path = os.path.join(temp_dir, "test.xlsx")
        new_file_path = os.path.join(temp_dir, "new_test.xlsx")

        # Create a sample DataFrame and save it to the original file
        sample_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        df = pd.DataFrame(sample_data)
        df.to_excel(original_file_path, index=False)

        # Call the function
        result_df = task_func(original_file_location=original_file_path, new_file_location=new_file_path)

        # Check if the result matches the expected DataFrame
        assert result_df.equals(df)

def test_task_func_custom_sheet_name():
    # Create a temporary directory and files
    with tempfile.TemporaryDirectory() as temp_dir:
        original_file_path = os.path.join(temp_dir, "test.xlsx")
        new_file_path = os.path.join(temp_dir, "new_test.xlsx")

        # Create a sample DataFrame and save it to the original file with a custom sheet name
        sample_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        df = pd.DataFrame(sample_data)
        with pd.ExcelWriter(original_file_path) as writer:
            df.to_excel(writer, sheet_name='CustomSheet', index=False)

        # Call the function with the custom sheet name
        result_df = task_func(original_file_location=original_file_path, new_file_location=new_file_path, sheet_name='CustomSheet')

        # Check if the result matches the expected DataFrame
        assert result_df.equals(df)

def test_task_func_non_existent_file():
    with pytest.raises(FileNotFoundError):
        task_func(original_file_location="non_existent_file.xlsx")

def test_task_func_invalid_sheet_name():
    # Create a temporary directory and files
    with tempfile.TemporaryDirectory() as temp_dir:
        original_file_path = os.path.join(temp_dir, "test.xlsx")
        new_file_path = os.path.join(temp_dir, "new_test.xlsx")

        # Create a sample DataFrame and save it to the original file
        sample_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        df = pd.DataFrame(sample_data)
        df.to_excel(original_file_path, index=False)

        with pytest.raises(ValueError):
            task_func(original_file_location=original_file_path, new_file_location=new_file_path, sheet_name='NonExistentSheet')