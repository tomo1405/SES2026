import pytest
from src_0061 import task_func
import pandas as pd
import os

def test_task_func():
    result = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    csv_file_path = "test_output.csv"
    json_file_path = "test_output.json"

    # Call the function
    task_func(result, csv_file_path, json_file_path)

    # Check if CSV file is created and contains correct data
    assert os.path.exists(csv_file_path)
    df = pd.read_csv(csv_file_path)
    pd.testing.assert_frame_equal(df, pd.DataFrame(result))

    # Check if JSON file is created and contains correct data
    assert os.path.exists(json_file_path)
    with open(json_file_path, 'r') as f:
        loaded_data = json.load(f)
    assert loaded_data == result

    # Clean up files
    os.remove(csv_file_path)
    os.remove(json_file_path)