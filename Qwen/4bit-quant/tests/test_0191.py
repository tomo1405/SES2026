from io import StringIO

import pandas as pd
from src_0191 import task_func


def test_task_func_with_stringio():
    # Create a StringIO object with CSV data
    csv_data = StringIO("name,age\nAlice,30\nBob,25")
    
    # Call the function with the StringIO object
    result_df = task_func(csv_data)
    
    # Define expected DataFrame
    expected_df = pd.DataFrame({
        'name': ['Alice', 'Bob'],
        'age': ['30', '25']
    })
    
    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_file_path(tmp_path):
    # Create a temporary CSV file
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("name,age\nAlice,30\nBob,25")
    
    # Call the function with the file path
    result_df = task_func(str(csv_file))
    
    # Define expected DataFrame
    expected_df = pd.DataFrame({
        'name': ['Alice', 'Bob'],
        'age': ['30', '25']
    })
    
    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_empty_csv(tmp_path):
    # Create a temporary empty CSV file
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("")
    
    # Call the function with the file path
    result_df = task_func(str(csv_file))
    
    # Define expected DataFrame (empty)
    expected_df = pd.DataFrame(columns=['name', 'age'])
    
    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_single_row(tmp_path):
    # Create a temporary CSV file with a single row
    csv_file = tmp_path / "single_row.csv"
    csv_file.write_text("name,age\nAlice,30")
    
    # Call the function with the file path
    result_df = task_func(str(csv_file))
    
    # Define expected DataFrame
    expected_df = pd.DataFrame({
        'name': ['Alice'],
        'age': ['30']
    })
    
    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)