import pytest
from src_0712 import task_func

def test_task_func():
    json_file = 'test_data.json'
    csv_file = 'test_data.csv'
    with open(json_file, 'w') as f:
        json.dump({'key1': 'value1', 'key2': 'value2'}, f)

    task_func(json_file, csv_file)

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ['key1', 'key2']

        data = next(reader)
        assert data == ['value1', 'value2']