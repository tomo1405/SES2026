import pytest
from src_0593 import task_func
import os
import csv

def test_task_func_output_file_exists():
    hours = 1
    output_dir = './test_output'
    file_path = task_func(hours, output_dir)
    assert os.path.exists(file_path), f"File {file_path} does not exist"

def test_task_func_output_file_content():
    hours = 1
    output_dir = './test_output'
    file_path = task_func(hours, output_dir)
    
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert len(rows) == hours + 1, "Number of rows in the CSV file is incorrect"
    assert rows[0] == ['Time'] + ['Temperature', 'Humidity', 'Pressure'], "Header row is incorrect"
    
    for row in rows[1:]:
        assert len(row) == 4, "Each data row should have 4 elements"
        assert isinstance(row[0], str), "Time should be a string"
        for value in row[1:]:
            assert isinstance(value, int), "Sensor values should be integers"
            assert 0 <= value <= 100, "Sensor values should be between 0 and 100"

def test_task_func_directory_creation():
    hours = 1
    output_dir = './non_existent_dir'
    task_func(hours, output_dir)
    assert os.path.exists(output_dir), f"Directory {output_dir} was not created"

def test_task_func_default_output_dir():
    hours = 1
    default_output_dir = './output'
    file_path = task_func(hours)
    assert file_path.startswith(default_output_dir), f"File path {file_path} does not start with the default output directory {default_output_dir}"

def teardown_module(module):
    # Clean up test directories
    test_dirs = ['./test_output', './non_existent_dir']
    for dir_path in test_dirs:
        if os.path.exists(dir_path):
            for root, dirs, files in os.walk(dir_path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(dir_path)