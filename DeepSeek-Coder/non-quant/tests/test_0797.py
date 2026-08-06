import pytest
from src_0797 import task_func
import os

def test_task_func():
    # Test case 1: Normal case with a directory containing files with brackets
    test_dir = 'test_directory'
    os.makedirs(test_dir)
    with open(os.path.join(test_dir, 'file1.txt'), 'w') as f:
        f.write('{}[]')
    with open(os.path.join(test_dir, 'file2.txt'), 'w') as f:
        f.write('test')
    
    result = task_func(test_dir)
    assert len(result) == 2
    os.rmdir(test_dir)

    # Add more test cases as needed

pytest.main()