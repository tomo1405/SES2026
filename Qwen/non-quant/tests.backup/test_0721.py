import pytest
from src_0721 import task_func
import os
import csv
from datetime import datetime

def test_task_func_directory_creation():
    # Run the function to create the directory and file
    task_func()
    
    # Check if the directory exists
    assert os.path.exists('task_func_data')

def test_task_func_file_creation():
    # Run the function to create the file
    file_name = task_func()
    
    # Check if the file exists
    assert os.path.isfile(file_name)

def test_task_func_headers():
    # Run the function to create the file with headers
    file_name = task_func()
    
    # Read the file and check if the headers are correct
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert headers == ['Timestamp', 'Temperature', 'Humidity']

def test_task_func_data_append():
    # Run the function twice to append data
    file_name1 = task_func()
    file_name2 = task_func()
    
    # Read the file and check if two rows of data are appended
    with open(file_name1, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip headers
        data_rows = list(reader)
        assert len(data_rows) == 2

def test_task_func_data_format():
    # Run the function to append data
    file_name = task_func()
    
    # Read the file and check if the data format is correct
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip headers
        data_row = next(reader)
        assert isinstance(data_row[0], str)  # Timestamp should be a string
        assert 20 <= float(data_row[1]) <= 30  # Temperature should be between 20 and 30
        assert 50 <= float(data_row[2]) <= 60  # Humidity should be between 50 and 60

def test_task_func_timestamp():
    # Run the function to append data
    file_name = task_func()
    
    # Read the file and check if the timestamp is in the correct format
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip headers
        data_row = next(reader)
        timestamp = datetime.strptime(data_row[0], '%Y-%m-%d %H:%M:%S.%f')
        assert isinstance(timestamp, datetime)