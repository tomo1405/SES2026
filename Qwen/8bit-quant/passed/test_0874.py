import pytest
from src_0874 import task_func
import os
import csv

def test_task_func_with_valid_data():
    data = [
        [1, 2],
        [3, 4]
    ]
    headers = ['col1', 'col2']
    file_path = 'test_output.csv'
    
    result = task_func(data, file_path, headers)
    
    assert os.path.abspath(file_path) == result
    
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert rows == [headers, ['1', '2'], ['3', '4']]
    
    os.remove(file_path)

def test_task_func_with_missing_values():
    data = [
        [1],
        [3, 4, 5]
    ]
    headers = ['col1', 'col2', 'col3']
    file_path = 'test_output.csv'
    
    result = task_func(data, file_path, headers)
    
    assert os.path.abspath(file_path) == result
    
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert rows == [headers, ['1', '', ''], ['3', '4', '5']]
    
    os.remove(file_path)

def test_task_func_with_no_data():
    data = []
    headers = ['col1', 'col2']
    file_path = 'test_output.csv'
    
    result = task_func(data, file_path, headers)
    
    assert os.path.abspath(file_path) == result
    
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert rows == [headers]
    
    os.remove(file_path)

def test_task_func_with_invalid_file_path():
    data = [[1, 2]]
    headers = ['col1', 'col2']
    file_path = None
    
    with pytest.raises(ValueError):
        task_func(data, file_path, headers)