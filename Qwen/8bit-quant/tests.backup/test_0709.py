import pytest
from src_0709 import task_func
import os
import base64
import json

def test_task_func(tmpdir):
    # Create a temporary directory for the output
    output_dir = tmpdir.strpath

    # Sample data
    raw_string = base64.b64encode(json.dumps({"name": "John", "age": 30}).encode('utf-8')).decode('utf-8')
    filename = "test_data"

    # Call the function
    result = task_func(raw_string, filename, output_dir)

    # Check if the file was created in the correct location
    expected_file_path = os.path.join(output_dir, f"{filename}.csv")
    assert result == expected_file_path
    assert os.path.exists(expected_file_path)

    # Check the contents of the CSV file
    with open(expected_file_path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows == [["name", "John"], ["age", "30"]]