python
import os
import shutil
import re
import pytest

from src_0827 import task_func

def test_task_func():
    source_dir = 'tests/test_data/source'
    target_dir = 'tests/test_data/target'
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    # Test case 1: source directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_dir', target_dir, file_pattern)

    # Test case 2: target directory does not exist
    os.makedirs(source_dir)
    task_func(source_dir, 'nonexistent_dir', file_pattern)
    assert os.path.exists(os.path.join(target_dir, 'test_file.txt'))

    # Test case 3: file pattern does not match any files
    os.remove(os.path.join(target_dir, 'test_file.txt'))
    os.makedirs(os.path.join(source_dir, 'subdir'))
    with open(os.path.join(source_dir, 'subdir', 'test_file.txt'), 'w') as f:
        f.write('test')
    task_func(source_dir, target_dir, r'\b[A-Za-z0-9]+\.(pdf|jpg)\b')
    assert not os.path.exists(os.path.join(target_dir, 'test_file.txt'))

    # Test case 4: file pattern matches some files
    os.remove(os.path.join(source_dir, 'subdir', 'test_file.txt'))
    os.makedirs(os.path.join(source_dir, 'subdir', 'subsubdir'))
    with open(os.path.join(source_dir, 'subdir', 'subsubdir', 'test_file.txt'), 'w') as f:
        f.write('test')
    task_func(source_dir, target_dir, file_pattern)
    assert os.path.exists(os.path.join(target_dir, 'test_file.txt'))
    assert os.path.exists(os.path.join(target_dir, 'subdir', 'subsubdir', 'test_file.txt'))