import pytest
from src_0845 import task_func

def test_task_func_num_rows_positive():
    file_path = 'test_file.csv'
    num_rows = 10
    random_seed = 42
    task_func(file_path, num_rows, random_seed)
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        assert header == ['Name', 'Age', 'Address', 'Email']
        for row in reader:
            assert len(row) == 4
            assert row[0] == 'Name'
            assert row[1] == 'Age'
            assert row[2] == 'Address'
            assert row[3] == 'Email'

def test_task_func_num_rows_negative():
    file_path = 'test_file.csv'
    num_rows = -1
    random_seed = 42
    with pytest.raises(ValueError):
        task_func(file_path, num_rows, random_seed)

def test_task_func_num_rows_not_integer():
    file_path = 'test_file.csv'
    num_rows = 10.5
    random_seed = 42
    with pytest.raises(ValueError):
        task_func(file_path, num_rows, random_seed)

def test_task_func_random_seed():
    file_path = 'test_file.csv'
    num_rows = 10
    random_seed = 42
    task_func(file_path, num_rows, random_seed)
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        assert header == ['Name', 'Age', 'Address', 'Email']
        for row in reader:
            assert len(row) == 4
            assert row[0] == 'Name'
            assert row[1] == 'Age'
            assert row[2] == 'Address'
            assert row[3] == 'Email'

def test_task_func_random_seed_not_integer():
    file_path = 'test_file.csv'
    num_rows = 10
    random_seed = '42'
    with pytest.raises(ValueError):
        task_func(file_path, num_rows, random_seed)