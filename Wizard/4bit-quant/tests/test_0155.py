python
import pytest
from src_0155 import task_func

def test_task_func():
    directory = 'test_dir'
    file_pattern = '*.txt'
    suffix = '.txt'
    expected_result = {'test_dir/test1.txt': 'text/plain', 'test_dir/test2.txt': 'text/plain'}

    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'test1.txt'), 'w') as f:
        f.write('test1')
    with open(os.path.join(directory, 'test2.txt'), 'w') as f:
        f.write('test2')

    result = task_func(directory, file_pattern, suffix)

    assert result == expected_result

    os.remove(os.path.join(directory, 'test1.txt'))
    os.remove(os.path.join(directory, 'test2.txt'))
    os.rmdir(directory)