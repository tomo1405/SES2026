python
import json
import csv
import pytest

def task_func(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data.keys())
        writer.writerow(data.values())
    
    return csv_file

def test_task_func():
    json_file = 'data.json'
    csv_file = 'data.csv'
    result = task_func(json_file, csv_file)
    assert result == csv_file