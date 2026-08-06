import pytest
from src_0782 import task_func

def test_task_func():
    filepath = 'test_file.txt'
    expected_size = 100
    expected_mtime = '2022-01-01 12:00:00'

    with open(filepath, 'w') as f:
        f.write('test')

    result = task_func(filepath)

    assert result['size'] == f"{expected_size} bytes"
    assert result['last_modified'] == expected_mtime

    os.remove(filepath)