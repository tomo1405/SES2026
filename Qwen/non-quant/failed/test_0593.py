import pytest
from src_0593 import task_func
import os
import csv
from datetime import datetime

def test_task_func_output_directory_creation():
    # Test if the output directory is created
    output_dir = './test_output'
    file_path = task_func(1, output_dir)
    assert os.path.exists(output_dir)
    os.rmdir(output_dir)  # Clean up

def test_task_func_file_creation():
    # Test if the CSV file is created
    output_dir = './test_output'
    file_path = task_func(1, output_dir)
    assert os.path.isfile(file_path)
    os.remove(file_path)  # Clean up
    os.rmdir(output_dir)  # Clean up

def test_task_func_file_content():
    # Test if the CSV file contains the correct number of rows and columns
    output_dir = './test_output'
    hours = 3
    file_path = task_func(hours, output_dir)
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    assert len(rows) == hours + 1  # Header + data rows
    for row in rows[1:]:
        assert len(row) == 4  # Time + 3 sensor values
    os.remove(file_path)  # Clean up
    os.rmdir(output_dir)  # Clean up

def test_task_func_file_header():
    # Test if the CSV file has the correct header
    output_dir = './test_output'
    file_path = task_func(1, output_dir)
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
    assert header == ['Time', 'Temperature', 'Humidity', 'Pressure']
    os.remove(file_path)  # Clean up
    os.rmdir(output_dir)  # Clean up