import os

from src_0501 import task_func


def test_task_func():
    values = [
        {'ID': 1, 'Name': 'Alice', 'Age': 25},
        {'ID': 2, 'Name': 'Bob', 'Age': 30},
        {'ID': 3, 'Name': 'Charlie', 'Age': 35}
    ]
    filename = 'output.xls'

    result = task_func(values, filename)

    assert result == os.path.abspath(filename)
    assert os.path.exists(filename)

    with open(filename, 'rb') as f:
        data = f.read()
        assert b'ID' in data
        assert b'Name' in data
        assert b'Age' in data
        assert b'1' in data
        assert b'Alice' in data
        assert b'25' in data
        assert b'2' in data
        assert b'Bob' in data
        assert b'30' in data
        assert b'3' in data
        assert b'Charlie' in data
        assert b'35' in data

    os.remove(filename)