import pytest
from src_1113 import task_func

def test_task_func():
    file_name = 'test_data.csv'
    result = task_func(file_name)
    assert result == file_name

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        assert header == ['Time'] + DATA

        for row in reader:
            time, temperature, humidity, pressure = row
            assert time in range(24)
            assert temperature in range(RANGE['Temperature'])
            assert humidity in range(RANGE['Humidity'])
            assert pressure in range(RANGE['Pressure'])

    os.remove(file_name)