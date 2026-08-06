import csv
import os
from datetime import datetime

from src_0593 import task_func


def test_task_func():
    hours = 10
    output_dir = './output'
    FILE_PATH = os.path.join(output_dir, 'sensor_data.csv')

    # Test that the function returns the correct file path
    assert task_func(hours, output_dir) == FILE_PATH

    # Test that the file is created in the correct directory
    assert os.path.exists(FILE_PATH)

    # Test that the file contains the correct data
    with open(FILE_PATH, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    assert data[0] == ['Time'] + SENSORS
    for i in range(1, hours):
        row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')] + [randint(0, 100) for _ in SENSORS]
        assert data[i] == row