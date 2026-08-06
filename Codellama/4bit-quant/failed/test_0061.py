import pytest
from src_0061 import task_func
import pandas as pd
import json

def test_task_func():
    result = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    csv_file_path = "test.csv"
    json_file_path = "test.json"
    task_func(result, csv_file_path, json_file_path)

    # Test CSV file
    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(result))

    # Test JSON file
    with open(json_file_path, 'r') as f:
        json_data = json.load(f)
    assert json_data == result

    # Clean up
    os.remove(csv_file_path)
    os.remove(json_file_path)