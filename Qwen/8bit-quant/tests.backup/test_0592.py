import pytest
from src_0592 import task_func
from datetime import datetime
import pandas as pd

def test_task_func():
    hours = 5
    file_path = 'test_custom_data.csv'
    
    # Call the function
    result_file_path, ax = task_func(hours, file_path)
    
    # Check if the returned file path is correct
    assert result_file_path == file_path
    
    # Check if the file exists and can be read
    df = pd.read_csv(file_path)
    assert not df.empty
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['Time', 'Temperature', 'Category']
    assert list(df.columns) == expected_columns
    
    # Check if the number of rows is equal to the number of hours
    assert len(df) == hours
    
    # Check if the 'Time' column contains valid datetime strings
    for time_str in df['Time']:
        try:
            datetime.strptime(time_str, '%H:%M:%S.%f')
        except ValueError:
            pytest.fail(f"Invalid datetime format: {time_str}")
    
    # Check if the 'Temperature' values are within the expected range
    for temp in df['Temperature']:
        assert -10 <= temp <= 40
    
    # Check if the 'Category' values are correct based on the 'Temperature' values
    for temp, category in zip(df['Temperature'], df['Category']):
        if temp < 0:
            assert category == 'Cold'
        elif temp > 25:
            assert category == 'Hot'
        else:
            assert category == 'Normal'

# To run the tests, use the following command in the terminal:
# pytest -v test_task_func.py