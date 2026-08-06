import pytest
from src_0119 import task_func
import os
import shutil

def test_task_func():
    # Create a temporary directory for testing
    test_dir = 'test_directory'
    test_backup_dir = 'test_backup_directory'
    
    # Create a sample file in the test directory
    os.makedirs(os.path.join(test_dir, 'subdir'))
    with open(os.path.join(test_dir, 'test_file.json'), 'w') as f:
        f.write('test content')

    # Call the function
    result = task_func(test_dir, test_backup_dir)

    # Assertions
    assert os.path.exists(os.path.join(test_backup_dir, 'test_file.json'))
    assert len(result) == 1
    assert os.path.exists(result[0])

    # Clean up
    shutil.rmtree(test_dir)
    shutil.rmtree(test_backup_dir)