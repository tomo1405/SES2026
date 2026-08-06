import pytest
from src_0709 import task_func
import os
import json
import base64
import csv

# Mock data for testing
raw_string = "eyJrZXkxIjogImFyZWFsb25nIiwgImtleTIiOiAiY29tbWEifQ=="
filename = "test_file"
output_dir = "test_output"

def test_task_func():
    # Call the function with the mock data
    result = task_func(raw_string, filename, output_dir)

    # Check if the file was created and has the correct content
    file_path = os.path.join(output_dir, f"{filename}.csv")
    assert os.path.exists(file_path), "File was not created"

    # Read the file and check its content
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows == [['key1', 'value1'], ['key2', 'value2']]

    # Clean up the test file
    os.remove(file_path)
    os.rmdir(output_dir)