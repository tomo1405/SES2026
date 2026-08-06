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
        assert header == ['Time', 'Temperature', 'Humidity', 'Pressure']
        for row in reader:
            assert len(row) == 4
            assert row[0].isdigit()
            assert 0 <= int(row[0][:2]) < 24
            assert float(row[1]) >= -50 and float(row[1]) <= 50
            assert float(row[2]) >= 0 and float(row[2]) <= 100
            assert float(row[3]) >= 980 and float(row[3]) <= 1040