import csv
import os

import pytest
from src_0712 import task_func


@pytest.fixture
def temp_files(tmpdir):
    json_content = '{"name": "John", "age": 30, "city": "New York"}'
    json_file = tmpdir.join('data.json')
    json_file.write(json_content)

    csv_file = tmpdir.join('output.csv')
    return str(json_file), str(csv_file)

def test_task_func(temp_files):
    json_file, csv_file = temp_files
    result = task_func(json_file, csv_file)
    assert result == csv_file

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    expected_keys = ['name', 'age', 'city']
    expected_values = ['John', '30', 'New York']
    
    assert rows[0] == expected_keys
    assert rows[1] == expected_values

def test_task_func_with_empty_json(temp_files):
    json_file, csv_file = temp_files
    os.remove(json_file)
    with open(json_file, 'w') as f:
        f.write('{}')

    result = task_func(json_file, csv_file)
    assert result == csv_file

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    expected_keys = []
    expected_values = []
    
    assert rows[0] == expected_keys
    assert rows[1] == expected_values

def test_task_func_with_nonexistent_json(temp_files):
    json_file, csv_file = temp_files
    os.remove(json_file)
    
    with pytest.raises(FileNotFoundError):
        task_func(json_file, csv_file)