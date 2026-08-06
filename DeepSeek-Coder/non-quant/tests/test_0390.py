import pytest
from src_0390 import task_func
import os
import shutil
import re

def test_task_func():
    # Create a temporary directory for testing
    test_dir = 'test_dir'
    os.makedirs(test_dir)
    
    # Create some test files
    with open(os.path.join(test_dir, 'file1.txt'), 'w') as f:
        f.write('like this')
    with open(os.path.join(test_dir, 'file2.txt'), 'w') as f:
        f.write('what about this')
    with open(os.path.join(test_dir, 'file3.txt'), 'w') as f:
        f.write('nothing to see here')

    # Call the function
    result = task_func(test_dir)

    # Check the results
    assert os.path.exists(os.path.join(test_dir, 'Interesting Files'))
    assert len(os.listdir(os.path.join(test_dir, 'Interesting Files'))) == 2
    assert 'file1.txt' in os.listdir(os.path.join(test_dir, 'Interesting Files'))
    assert 'file2.txt' in os.listdir(os.path.join(test_dir, 'Interesting Files'))

    # Clean up
    shutil.rmtree(test_dir)