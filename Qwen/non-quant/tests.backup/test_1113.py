import pytest
from src_1113 import task_func
import os
import csv

def test_task_func_default_filename():
    # Test with default filename
    file_name = task_func()
    assert file_name == "data.csv"
    assert os.path.exists(file_name)

    # Clean up
    os.remove(file_name)

def test_task_func_custom_filename():
    # Test with custom filename
    custom_filename = "test_data.csv"
    file_name = task_func(custom_filename)
    assert file_name == custom_filename
    assert os.path.exists(file_name)

    # Clean up
    os.remove(file_name)

def test_task_func_file_content():
    # Test file content
    file_name = task_func("test_content.csv")
    assert os.path.exists(file_name)

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Check header
    assert rows[0] == ['Time', 'Temperature', 'Humidity', 'Pressure']

    # Check each row has 5 elements
    for row in rows[1:]:
        assert len(row) == 5

    # Clean up
    os.remove(file_name)

def test_task_func_random_values():
    # Test random values within range
    file_name = task_func("test_random.csv")
    assert os.path.exists(file_name)

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows[1:]:
        time, temperature, humidity, pressure = row
        assert float(temperature) >= RANGE['Temperature'][0] and float(temperature) <= RANGE['Temperature'][1]
        assert float(humidity) >= RANGE['Humidity'][0] and float(humidity) <= RANGE['Humidity'][1]
        assert float(pressure) >= RANGE['Pressure'][0] and float(pressure) <= RANGE['Pressure'][1]

    # Clean up
    os.remove(file_name)