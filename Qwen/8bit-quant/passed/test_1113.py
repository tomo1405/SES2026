import pytest
from src_1113 import task_func
import os
import csv

def test_task_func():
    # Test if the function returns the correct file name
    file_name = task_func()
    assert file_name == "data.csv"

    # Check if the file is created
    assert os.path.exists(file_name)

    # Read the contents of the file and validate its structure
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        assert header == ['Time', 'Temperature', 'Humidity', 'Pressure']

        for row in reader:
            assert len(row) == 4
            time, temperature, humidity, pressure = row
            assert time.endswith(':00')
            assert float(temperature) >= -50 and float(temperature) <= 50
            assert float(humidity) >= 0 and float(humidity) <= 100
            assert float(pressure) >= 980 and float(pressure) <= 1040

    # Clean up the created file
    os.remove(file_name)