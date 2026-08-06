import json
import os

import pandas as pd
from src_0061 import task_func


def test_task_func():
    result = [
        {"name": "John", "age": 30},
        {"name": "Jane", "age": 25},
        {"name": "Jim", "age": 35}
    ]
    csv_file_path = "test_csv.csv"
    json_file_path = "test_json.json"

    task_func(result, csv_file_path, json_file_path)

    # Test CSV file
    df = pd.read_csv(csv_file_path)
    assert df.shape == (3, 2)
    assert df["name"][0] == "John"
    assert df["age"][0] == 30
    assert df["name"][1] == "Jane"
    assert df["age"][1] == 25
    assert df["name"][2] == "Jim"
    assert df["age"][2] == 35

    # Test JSON file
    with open(json_file_path, "r") as f:
        data = json.load(f)
    assert data == result

    # Clean up
    os.remove(csv_file_path)
    os.remove(json_file_path)