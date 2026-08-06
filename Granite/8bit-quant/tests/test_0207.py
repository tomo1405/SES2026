import csv
import json
import os
import pytest
from src_0207 import task_func

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv")

def test_task_func_valid_csv_file():
    csv_data = "name,age,city\nJohn,25,New York\nJane,30,San Francisco"
    with open("test_file.csv", "w") as f:
        f.write(csv_data)
    json_file_name = task_func("test_file.csv")
    with open(json_file_name) as f:
        json_data = json.load(f)
    assert json_data == [{"name": "John", "age": "25", "city": "New York"}, {"name": "Jane", "age": "30", "city": "San Francisco"}]
    os.remove("test_file.csv")
    os.remove(json_file_name)