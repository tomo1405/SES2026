import pytest
from src_0845 import task_func
import os
import csv

def test_task_func_invalid_num_rows():
    with pytest.raises(ValueError):
        task_func('test.csv', -1)

def test_task_func_non_integer_num_rows():
    with pytest.raises(ValueError):
        task_func('test.csv', 'not an integer')

def test_task_func_zero_rows():
    file_path = task_func('test.csv', 0)
    assert os.path.exists(file_path)
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    assert len(data) == 1  # Only the header row should exist
    os.remove(file_path)

def test_task_func_positive_rows():
    file_path = task_func('test.csv', 5, random_seed=42)
    assert os.path.exists(file_path)
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    assert len(data) == 6  # Header row + 5 data rows
    os.remove(file_path)

def test_task_func_with_random_seed():
    file_path1 = task_func('test1.csv', 3, random_seed=42)
    file_path2 = task_func('test2.csv', 3, random_seed=42)
    with open(file_path1, newline='') as csvfile1:
        reader1 = csv.reader(csvfile1)
        data1 = list(reader1)
    with open(file_path2, newline='') as csvfile2:
        reader2 = csv.reader(csvfile2)
        data2 = list(reader2)
    assert data1 == data2  # Both files should have identical content
    os.remove(file_path1)
    os.remove(file_path2)