import pytest
from src_0146 import task_func

def test_task_func():
    ip_range = '192.168.1.0/24'
    csv_path = 'test.csv'

    result = task_func(ip_range, csv_path)

    assert result == csv_path

    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        assert reader.fieldnames == ['IP Address']

        for row in reader:
            assert row['IP Address'] in IPv4Network(ip_range)