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
    task_func(json_file, csv_file)
    assert csv_file.endswith('.csv')
    assert csv_file.startswith('data')
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        values = next(reader)
        assert header == list(data.keys())
        assert values == list(data.values())