import pytest
from src_0709 import task_func
import os
import base64
import json

def test_task_func(tmpdir):
    # Prepare test data
    raw_string = base64.b64encode(json.dumps({"name": "John", "age": 30}).encode('utf-8')).decode('utf-8')
    filename = "test_file"
    output_dir = str(tmpdir)

    # Call the function
    result = task_func(raw_string, filename, output_dir)

    # Check if the file was created
    assert os.path.exists(result)

    # Read the content of the CSV file
    with open(result, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Check the content of the CSV file
    assert rows == [['name', 'John'], ['age', '30']]

def test_task_func_nonexistent_directory(tmpdir):
    # Prepare test data
    raw_string = base64.b64encode(json.dumps({"name": "John", "age": 30}).encode('utf-8')).decode('utf-8')
    filename = "test_file"
    output_dir = str(tmpdir.join("nonexistent_dir"))

    # Call the function
    result = task_func(raw_string, filename, output_dir)

    # Check if the file was created
    assert os.path.exists(result)

    # Read the content of the CSV file
    with open(result, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Check the content of the CSV file
    assert rows == [['name', 'John'], ['age', '30']]