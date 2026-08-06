import pytest
from src_0845 import task_func
import os
import csv

@pytest.fixture
def temp_file_path(tmpdir):
    return str(tmpdir.join("temp.csv"))

def test_task_func_with_valid_input(temp_file_path):
    num_rows = 5
    random_seed = 42
    result_path = task_func(temp_file_path, num_rows, random_seed)
    
    assert result_path == temp_file_path
    
    with open(result_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert len(rows) == num_rows + 1  # +1 for the header row
    for row in rows[1:]:
        assert len(row) == 4
        name, age, address, email = row
        assert isinstance(name, str)
        assert isinstance(age, str) and age.isdigit() and 20 <= int(age) <= 60
        assert isinstance(address, str)
        assert isinstance(email, str)

def test_task_func_with_zero_rows(temp_file_path):
    num_rows = 0
    random_seed = 42
    result_path = task_func(temp_file_path, num_rows, random_seed)
    
    assert result_path == temp_file_path
    
    with open(result_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert len(rows) == 1  # Only the header row

def test_task_func_with_negative_rows(temp_file_path):
    num_rows = -1
    with pytest.raises(ValueError) as excinfo:
        task_func(temp_file_path, num_rows)
    assert str(excinfo.value) == 'num_rows should be an integer >=0.'

def test_task_func_with_non_integer_rows(temp_file_path):
    num_rows = "five"
    with pytest.raises(ValueError) as excinfo:
        task_func(temp_file_path, num_rows)
    assert str(excinfo.value) == 'num_rows should be an integer >=0.'

def test_task_func_with_no_random_seed(temp_file_path):
    num_rows = 5
    result_path = task_func(temp_file_path, num_rows)
    
    assert result_path == temp_file_path
    
    with open(result_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert len(rows) == num_rows + 1  # +1 for the header row
    for row in rows[1:]:
        assert len(row) == 4
        name, age, address, email = row
        assert isinstance(name, str)
        assert isinstance(age, str) and age.isdigit() and 20 <= int(age) <= 60
        assert isinstance(address, str)
        assert isinstance(email, str)

def test_task_func_with_same_random_seed(temp_file_path):
    num_rows = 5
    random_seed = 42
    task_func(temp_file_path, num_rows, random_seed)
    
    with open(temp_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows1 = list(reader)
    
    os.remove(temp_file_path)
    task_func(temp_file_path, num_rows, random_seed)
    
    with open(temp_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows2 = list(reader)
    
    assert rows1 == rows2