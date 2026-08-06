import pytest
from src_1113 import task_func
import os
import csv

def test_task_func_default_filename():
    # Test the default behavior of the function
    filename = task_func()
    assert filename == "data.csv"
    assert os.path.exists(filename)
    
    # Check the content of the CSV file
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        assert headers == ['Time', 'Temperature', 'Humidity', 'Pressure']
        
        rows = list(reader)
        assert len(rows) == 24
        for row in rows:
            assert row[0].endswith(':00')
            for value in row[1:]:
                assert isinstance(float(value), float)
    
    # Clean up the created file
    os.remove(filename)

def test_task_func_custom_filename():
    # Test the function with a custom filename
    custom_filename = "custom_data.csv"
    filename = task_func(custom_filename)
    assert filename == custom_filename
    assert os.path.exists(filename)
    
    # Check the content of the CSV file
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        assert headers == ['Time', 'Temperature', 'Humidity', 'Pressure']
        
        rows = list(reader)
        assert len(rows) == 24
        for row in rows:
            assert row[0].endswith(':00')
            for value in row[1:]:
                assert isinstance(float(value), float)
    
    # Clean up the created file
    os.remove(filename)