python
import csv
import os
from datetime import datetime
from random import randint
import pytest

# Constants
SENSORS = ['Temperature', 'Humidity', 'Pressure']
OUTPUT_DIR = './output'

def task_func(hours, output_dir=OUTPUT_DIR):
    FILE_PATH = os.path.join(output_dir, 'sensor_data.csv')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = [['Time'] + SENSORS]
    for i in range(hours):
        row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')] + [randint(0, 100) for _ in SENSORS]
        data.append(row)

    with open(FILE_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    return FILE_PATH

def test_task_func():
    # Test with default output directory
    file_path = task_func(hours=2)
    assert os.path.exists(file_path)
    os.remove(file_path)

    # Test with custom output directory
    file_path = task_func(hours=2, output_dir='./custom_output')
    assert os.path.exists(file_path)
    os.remove(file_path)

    # Test with invalid hours parameter
    with pytest.raises(ValueError):
        task_func(hours=-1)

    # Test with invalid output directory parameter
    with pytest.raises(NotADirectoryError):
        task_func(hours=2, output_dir='./invalid_output')