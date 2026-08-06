import pytest
from src_0061 import task_func
import pandas as pd
import json

def test_task_func():
    result = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35}
    ]

    csv_file_path = "test.csv"
    json_file_path = "test.json"

    task_func(result, csv_file_path, json_file_path)

    assert csv_file_path.exists()
    assert json_file_path.exists()

    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(result))

    with open(json_file_path, 'r') as f:
        data = json.load(f)

    assert data == result