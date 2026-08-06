import csv
import json

from src_0712 import task_func


def test_task_func():
    json_file = 'test_data.json'
    csv_file = 'test_data.csv'
    with open(json_file, 'w') as f:
        json.dump({'a': 1, 'b': 2}, f)

    task_func(json_file, csv_file)

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        assert reader.next() == ['a', 'b']
        assert reader.next() == [1, 2]