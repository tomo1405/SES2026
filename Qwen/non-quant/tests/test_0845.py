import pytest
from src_0845 import task_func
import os
import csv

@pytest.fixture
def temp_file_path(tmpdir):
    return str(tmpdir.join("test_file.csv"))

def test_task_func_invalid_num_rows(temp_file_path):
    with pytest.raises(ValueError):
        task_func(temp_file_path, -1)

def test_task_func_non_integer_num_rows(temp_file_path):
    with pytest.raises(ValueError):
        task_func(temp_file_path, "abc")

def test_task_func_zero_rows(temp_file_path):
    result_path = task_func(temp_file_path, 0)
    assert os.path.exists(result_path)
    with open(result_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    assert len(rows) == 1  # Only header row

def test_task_func_positive_rows(temp_file_path):
    num_rows = 5
    result_path = task_func(temp_file_path, num_rows)
    assert os.path.exists(result_path)
    with open(result_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    assert len(rows) == num_rows + 1  # Header row plus data rows

def test_task_func_with_random_seed(temp_file_path):
    seed = 42
    task_func(temp_file_path, 5, seed)
    with open(temp_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    # Assuming the first data row is used for comparison
    first_row = rows[1]
    assert first_row[0] == 'Evelyn Moore'  # Name
    assert int(first_row[1]) == 33  # Age
    assert first_row[2] == '97895 Lillian Rue Apt. 353, East Daphne, MI 50313'  # Address
    assert first_row[3] == 'evelynmoore@swift.com'  # Email

def test_task_func_file_creation(temp_file_path):
    result_path = task_func(temp_file_path, 3)
    assert os.path.exists(result_path)