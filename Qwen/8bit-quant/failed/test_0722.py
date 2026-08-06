import pytest
from src_0722 import task_func
import os
import tempfile
import csv

def test_task_func_nonexistent_file():
    assert task_func("nonexistent_file.csv") is None

def test_task_func_empty_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.close()
        assert task_func(temp_file.name) is None
    os.remove(temp_file.name)

def test_task_func_single_row():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerow(['apple', 'banana', 'apple'])
        temp_file.close()
        assert task_func(temp_file.name) == ('apple', 2)
    os.remove(temp_file.name)

def test_task_func_multiple_rows():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerow(['apple', 'banana'])
        writer.writerow(['apple', 'orange', 'banana'])
        temp_file.close()
        assert task_func(temp_file.name) == ('apple', 2)
    os.remove(temp_file.name)

def test_task_func_case_insensitivity():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerow(['Apple', 'Banana', 'apple'])
        temp_file.close()
        assert task_func(temp_file.name) == ('apple', 2)
    os.remove(temp_file.name)

def test_task_func_whitespace_handling():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerow(['  apple  ', 'banana', 'apple '])
        temp_file.close()
        assert task_func(temp_file.name) == ('apple', 2)
    os.remove(temp_file.name)