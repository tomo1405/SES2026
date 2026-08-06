import pytest
from src_0505 import task_func

def test_task_func():
    file_path = 'test_file.txt'
    with open(file_path, 'w') as f:
        f.write('Hello, world!')

    signature = task_func(file_path)

    assert signature == 'dGVzdCBzdHJpbmc='