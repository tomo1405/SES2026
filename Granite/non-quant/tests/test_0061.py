import json
import os

import pandas as pd
from src_0061 import task_func


def test_task_func():
    result = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Jane", "age": 25, "city": "Los Angeles"},
        {"name": "Bob", "age": 40, "city": "Chicago"}
    ]

    csv_file_path = "test.csv"
    json_file_path = "test.json"

    task_func(result, csv_file_path, json_file_path)

    # Check if the CSV file was created
    assert os.path.exists(csv_file_path)

    # Check if the JSON file was created
    assert os.path.exists(json_file_path)

    # Read the CSV file and check if it contains the expected data
    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(result))

    # Read the JSON file and check if it contains the expected data
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    assert data == result