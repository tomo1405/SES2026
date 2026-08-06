import csv
import os
from datetime import datetime
from random import randint
from src_0593 import task_func
import pytest

# Constants
SENSORS = ['Temperature', 'Humidity', 'Pressure']
OUTPUT_DIR = './output'

def test_task_func():
    hours = 10
    file_path = task_func(hours)
    assert file_path == os.path.join(OUTPUT_DIR, 'sensor_data.csv')
    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    assert len(data) == hours + 1  # +1 for the header row
    for row in data[1:]:  # Skip the header row
        assert len(row) == len(SENSORS) + 1  # +1 for the 'Time' column
        assert datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')  # Check if the 'Time' column is a valid datetime
        for sensor_value in row[1:]:  # Skip the 'Time' column
            assert int(sensor_value) >= 0 and int(sensor_value) <= 100  # Check if the sensor values are within the expected range

def test_task_func_with_custom_output_dir():
    hours = 5
    custom_output_dir = '/tmp/sensor_data'
    file_path = task_func(hours, output_dir=custom_output_dir)
    assert file_path == os.path.join(custom_output_dir, 'sensor_data.csv')

def test_task_func_with_invalid_hours():
    with pytest.raises(ValueError, match='hours must be a positive integer'):
        task_func(-1)
    with pytest.raises(ValueError, match='hours must be a positive integer'):
        task_func('abc')