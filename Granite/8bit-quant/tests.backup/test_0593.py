import csv
import os
from datetime import datetime
from random import randint
from src_0593 import task_func
import pytest

def test_task_func():
    hours = 10
    file_path = task_func(hours)
    assert file_path == os.path.join('./output', 'sensor_data.csv')
    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    assert len(data) == hours + 1  # +1 for the header row
    for row in data[1:]:  # Skip the header row
        assert len(row) == len(SENSORS) + 1  # +1 for the 'Time' column
        assert datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')  # Check if the 'Time' column is a valid datetime string
        for sensor_value in row[1:]:  # Check if the sensor values are integers between 0 and 100
            assert sensor_value.isdigit() and 0 <= int(sensor_value) <= 100

def test_task_func_with_custom_output_dir():
    hours = 5
    output_dir = '/tmp/sensor_data'
    file_path = task_func(hours, output_dir)
    assert file_path == os.path.join(output_dir, 'sensor_data.csv')
    assert os.path.exists(output_dir)  # Check if the custom output directory was created

def test_task_func_with_invalid_hours():
    with pytest.raises(ValueError) as exc_info:
        task_func(-1)
    assert str(exc_info.value) == 'hours must be a positive integer'