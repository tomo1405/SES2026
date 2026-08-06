import pytest
from src_0729 import task_func

def test_task_func():
    filename = 'example.csv'
    from_encoding = 'cp1251'
    to_encoding = 'utf8'
    delimiter = ','

    data, converted_csv = task_func(filename, from_encoding, to_encoding, delimiter)

    assert isinstance(data, list)
    assert isinstance(converted_csv, str)
    assert converted_csv.count('\n') == len(data) + 1  # +1 for the header row