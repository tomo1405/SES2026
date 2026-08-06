import csv
import os

from src_0712 import task_func


def test_task_func():
    json_file = 'test.json'
    csv_file = 'test.csv'
    expected_csv_file = 'test.csv'

    with open(json_file, 'w') as f:
        f.write('{}')

    result = task_func(json_file, csv_file)

    assert result == expected_csv_file
    assert os.path.isfile(csv_file)

    with open(csv_file, 'r') as f:
        data = csv.reader(f)
        rows = list(data)
        assert rows == [['']]

    os.remove(json_file)
    os.remove(csv_file)