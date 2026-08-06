python
import pytest
from src_0155 import task_func

def test_task_func():
    directory = 'test_dir'
    file_pattern = '*.txt'
    suffix = '.txt'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'test1.txt'), 'w') as f:
        f.write('test1')
    with open(os.path.join(directory, 'test2.txt'), 'w') as f:
        f.write('test2')
    with open(os.path.join(directory, 'test3.jpg'), 'w') as f:
        f.write('test3')
    file_types = task_func(directory, file_pattern, suffix)
    assert file_types == {'test1.txt': 'text/plain', 'test2.txt': 'text/plain'}