import pytest
from src_0721 import task_func
import os
import csv
from datetime import datetime

def test_task_func():
    # Call the function
    file_name = task_func()
    
    # Check if the file was created in the correct directory
    assert os.path.exists(file_name), f"File {file_name} does not exist"
    
    # Read the contents of the file
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # Check if the header is correct
    assert rows[0] == ['Timestamp', 'Temperature', 'Humidity'], "Header row is incorrect"
    
    # Check if the data row has the correct number of columns
    assert len(rows[1]) == 3, "Data row does not have 3 columns"
    
    # Check if the timestamp is a valid datetime object
    timestamp_str = rows[1][0]
    try:
        datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        pytest.fail("Timestamp is not in the correct format")
    
    # Check if the temperature is between 20 and 30
    temperature = float(rows[1][1])
    assert 20 <= temperature <= 30, f"Temperature {temperature} is out of range"
    
    # Check if the humidity is between 50 and 60
    humidity = float(rows[1][2])
    assert 50 <= humidity <= 60, f"Humidity {humidity} is out of range"

# Run the tests
if __name__ == "__main__":
    pytest.main()