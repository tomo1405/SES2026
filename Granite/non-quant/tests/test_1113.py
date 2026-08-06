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
            assert len(row) == len(header)
            time, *data = row
            assert time == f'{hour}:00'
            for data_type, (min_val, max_val) in RANGE.items():
                value = float(data[DATA.index(data_type)])
                assert min_val <= value <= max_val