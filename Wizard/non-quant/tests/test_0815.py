python
import os
import re
import shutil
import pytest

from src_0815 import task_func

def test_task_func():
    source_dir = 'tests/test_data/source'
    target_dir = 'tests/test_data/target'
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    # Test case 1: source directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('tests/test_data/nonexistent_dir', target_dir, file_pattern)

    # Test case 2: target directory does not exist
    os.makedirs(target_dir)
    assert task_func(source_dir, target_dir, file_pattern) == 0

    # Test case 3: move files
    os.makedirs(os.path.join(source_dir, 'subdir'))
    with open(os.path.join(source_dir, 'test.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(source_dir, 'test.doc'), 'w') as f:
        f.write('test')
    with open(os.path.join(source_dir, 'subdir', 'test.docx'), 'w') as f:
        f.write('test')
    assert task_func(source_dir, target_dir, file_pattern) == 3
    assert os.path.exists(os.path.join(target_dir, 'test.txt'))
    assert os.path.exists(os.path.join(target_dir, 'test.doc'))
    assert os.path.exists(os.path.join(target_dir, 'subdir', 'test.docx'))
    assert not os.path.exists(os.path.join(source_dir, 'test.txt'))
    assert not os.path.exists(os.path.join(source_dir, 'test.doc'))
    assert not os.path.exists(os.path.join(source_dir, 'subdir', 'test.docx'))