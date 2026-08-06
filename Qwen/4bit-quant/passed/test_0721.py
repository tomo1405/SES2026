import pytest
from src_0721 import task_func
import os
import csv
import random
from datetime import datetime

def test_task_func_directory_creation():
    task_func()
    assert os.path.exists('task_func_data'), "Directory 'task_func_data' should be created"

def test_task_func_file_creation():
    file_name = task_func()
    assert os.path.isfile(file_name), f"File '{file_name}' should be created"

def test_task_func_headers_written():
    file_name = task_func()
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
    assert headers == ['Timestamp', 'Temperature', 'Humidity'], "Headers should match ['Timestamp', 'Temperature', 'Humidity']"

def test_task_func_data_appended():
    file_name = task_func()
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    assert len(rows) > 1, "At least one row of data should be appended to the file"

def test_task_func_temperature_range():
    file_name = task_func()
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip headers
        temperature = float(next(reader)[1])
    assert 20 <= temperature <= 30, "Temperature should be between 20 and 30"

def test_task_func_humidity_range():
    file_name = task_func()
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip headers
        humidity = float(next(reader)[2])
    assert 50 <= humidity <= 60, "Humidity should be between 50 and 60"

def test_task_func_timestamp_format():
    file_name = task_func()
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip headers
        timestamp_str = next(reader)[0]
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
    assert isinstance(timestamp, datetime), "Timestamp should be in the correct format"