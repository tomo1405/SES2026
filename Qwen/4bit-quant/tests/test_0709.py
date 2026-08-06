import base64
import csv
import json
import os

from src_0709 import task_func


def test_task_func():
    # Prepare test data
    raw_string = base64.b64encode(json.dumps({"name": "John", "age": 30}).encode('utf-8')).decode('utf-8')
    filename = "test_data"
    output_dir = "test_output"

    # Call the function
    result = task_func(raw_string, filename, output_dir)

    # Check if the file was created
    expected_file_path = os.path.join(output_dir, f'{filename}.csv')
    assert os.path.exists(expected_file_path), "The CSV file was not created."

    # Check if the content of the file is correct
    with open(expected_file_path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert len(rows) == 2, "The CSV file does not contain the correct number of rows."
        assert ["name", "John"] in rows, "The CSV file does not contain the correct data."
        assert ["age", "30"] in rows, "The CSV file does not contain the correct data."

    # Clean up
    os.remove(expected_file_path)
    os.rmdir(output_dir)