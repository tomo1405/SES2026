python
import csv
import random
import pytest

# Constants
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}

def task_func(file_name="data.csv"):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time'] + DATA)
        
        for hour in range(24):
            row = [f'{hour}:00']
            for data_type in DATA:
                min_val, max_val = RANGE[data_type]
                row.append(random.uniform(min_val, max_val))
            writer.writerow(row)

    return file_name

def test_task_func():
    file_name = task_func()
    assert file_name == "data.csv"
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        assert header == ['Time'] + DATA
        for row in reader:
            assert len(row) == len(DATA) + 1
            time = row[0]
            assert time.endswith(':00')
            for i in range(1, len(row)):
                val = float(row[i])
                assert RANGE[DATA[i-1]][0] <= val <= RANGE[DATA[i-1]][1]