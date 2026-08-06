import pytest
from src_0712 import task_func

def test_task_func():
    json_file = 'test.json'
    csv_file = 'test.csv'
    expected_csv_file = 'test.csv'

    with open(json_file, 'w') as f:
        f.write('{"name": "John", "age": 30}')

    result = task_func(json_file, csv_file)

    assert result == expected_csv_file
    assert open(csv_file).read() == 'name,age\nJohn,30\n'