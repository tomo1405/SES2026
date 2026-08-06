import pandas as pd
import pytest
from src_0363 import task_func


def test_task_func_default_parameters(tmp_path):
    # Create a temporary directory and a sample Excel file
    original_file = tmp_path / "test.xlsx"
    new_file = tmp_path / "new_test.xlsx"
    
    # Sample data to write into the Excel file
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    df.to_excel(original_file, index=False)
    
    # Call the function
    result_df = task_func(str(original_file), str(new_file))
    
    # Check if the result matches the original data
    assert result_df.equals(df)

def test_task_func_custom_sheet_name(tmp_path):
    # Create a temporary directory and a sample Excel file with multiple sheets
    original_file = tmp_path / "test.xlsx"
    new_file = tmp_path / "new_test.xlsx"
    
    # Sample data to write into the Excel file
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    with pd.ExcelWriter(original_file) as writer:
        df.to_excel(writer, sheet_name='CustomSheet', index=False)
    
    # Call the function with a custom sheet name
    result_df = task_func(str(original_file), str(new_file), sheet_name='CustomSheet')
    
    # Check if the result matches the original data
    assert result_df.equals(df)

def test_task_func_file_not_found():
    # Test the case where the original file does not exist
    with pytest.raises(FileNotFoundError, match="No file found at non_existent_file.xlsx"):
        task_func("non_existent_file.xlsx")

def test_task_func_invalid_sheet_name(tmp_path):
    # Create a temporary directory and a sample Excel file
    original_file = tmp_path / "test.xlsx"
    new_file = tmp_path / "new_test.xlsx"
    
    # Sample data to write into the Excel file
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    df.to_excel(original_file, index=False)
    
    # Call the function with an invalid sheet name
    with pytest.raises(ValueError, match="Error reading sheet:"):
        task_func(str(original_file), str(new_file), sheet_name='NonExistentSheet')