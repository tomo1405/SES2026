import pytest
from src_0207 import task_func
import os
import csv
import json
import tempfile

def test_task_func_with_valid_csv():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv', mode='w', newline='') as temp_csv:
        writer = csv.writer(temp_csv)
        writer.writerow(['name', 'age'])
        writer.writerow(['Alice', 30])
        writer.writerow(['Bob', 25])

    # Call the function
    json_file_name = task_func(temp_csv.name)

    # Check if the JSON file was created
    assert os.path.exists(json_file_name)

    # Read the JSON file and check its content
    with open(json_file_name, 'r') as json_file:
        data = json.load(json_file)
        assert data == [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]

    # Clean up
    os.remove(temp_csv.name)
    os.remove(json_file_name)

def test_task_func_with_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent.csv')

def test_task_func_with_empty_csv():
    # Create a temporary empty CSV file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv', mode='w', newline='') as temp_csv:
        pass

    # Call the function
    json_file_name = task_func(temp_csv.name)

    # Check if the JSON file was created
    assert os.path.exists(json_file_name)

    # Read the JSON file and check its content
    with open(json_file_name, 'r') as json_file:
        data = json.load(json_file)
        assert data == []

    # Clean up
    os.remove(temp_csv.name)
    os.remove(json_file_name)