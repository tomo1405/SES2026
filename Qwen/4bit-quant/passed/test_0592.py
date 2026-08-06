import pytest
from src_0592 import task_func
import pandas as pd
import os

def test_task_func():
    hours = 5
    file_path, ax = task_func(hours)
    
    # Check if the file was created
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    # Check if the file is not empty
    assert os.path.getsize(file_path) > 0, f"File {file_path} is empty"
    
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['Time', 'Temperature', 'Category']
    assert list(df.columns) == expected_columns, f"DataFrame columns do not match expected columns: {expected_columns}"
    
    # Check if the number of rows is equal to the number of hours
    assert len(df) == hours, f"Number of rows in DataFrame does not match the number of hours: {hours}"
    
    # Check if the Category column values are within the expected categories
    expected_categories = ['Cold', 'Normal', 'Hot']
    assert all(category in expected_categories for category in df['Category']), "Category values contain unexpected categories"
    
    # Check if the Time column values are in the correct format
    assert all(isinstance(time, str) and time.count(':') == 2 for time in df['Time']), "Time values are not in the correct format"
    
    # Clean up: remove the created file
    os.remove(file_path)

# Run the test
if __name__ == "__main__":
    pytest.main()