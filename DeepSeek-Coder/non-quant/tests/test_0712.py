import pytest
from src_0712 import task_func
import json
import csv

def test_task_func():
    # Create a temporary JSON file
    json_data = {'key1': 'value1', 'key2': 'value2'}
    json_file = 'test_data.json'
    with open(json_file, 'w') as f:
        json.dump(json_data, f)

    # Call the function
    csv_file = task_func(json_file, 'test_output.csv')

    # Read the generated CSV file and check the content
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows == [['key1', 'key2'], ['value1', 'value2']]

    # Clean up
    import os
    os.remove(json_file)
    os.remove(csv_file)