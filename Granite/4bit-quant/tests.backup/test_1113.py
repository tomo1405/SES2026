import csv
import random
import pytest
from src_1113 import task_func

# Constants
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}

def test_task_func():
    file_name = task_func()
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        assert header == ['Time'] + DATA
        for hour in range(24):
            row = next(reader)
            assert row[0] == f'{hour}:00'
            for data_type, (min_val, max_val) in RANGE.items():
                value = float(row[DATA.index(data_type) + 1])
                assert min_val <= value <= max_val

def test_task_func_with_custom_file_name():
    file_name = 'custom_data.csv'
    custom_file_name = task_func(file_name)
    assert custom_file_name == file_name