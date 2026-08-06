python
import os
import re
import shutil
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
    task_func(source_dir, target_dir, r'\b[A-Za-z0-9]+\.(jpg|png)\b')
    assert not os.path.exists(os.path.join(target_dir, 'test_file.txt'))

    # Test case 4: file pattern matches multiple files
    os.remove(os.path.join(target_dir, 'test_file.txt'))
    os.makedirs(os.path.join(source_dir, 'subdir'))
    with open(os.path.join(source_dir, 'test_file.txt'), 'w') as f:
        f.write('test content')
    with open(os.path.join(source_dir, 'subdir', 'test_file.txt'), 'w') as f:
        f.write('test content')
    task_func(source_dir, target_dir, file_pattern)
    assert os.path.exists(os.path.join(target_dir, 'test_file.txt'))
    assert os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.txt'))
    assert os.path.exists(os.path.join(target_dir, 'test_file.doc'))
    assert os.path.exists(os.path.join(target_dir, 'test_file.docx'))
    assert os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.doc'))
    assert os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.docx'))
    assert os.path.exists(os.path.join(target_dir, 'test_file.jpg'))
    assert os.path.exists(os.path.join(target_dir, 'test_file.png'))
    assert os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.jpg'))
    assert os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.png'))
    assert os.path.exists(os.path.join(target_dir, 'test_file.pdf')) == False
    assert os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.pdf')) == False

    # Test case 5: file pattern matches no files
    os.remove(os.path.join(target_dir, 'test_file.txt'))
    os.remove(os.path.join(target_dir, 'subdir', 'test_file.txt'))
    os.remove(os.path.join(target_dir, 'test_file.doc'))
    os.remove(os.path.join(target_dir, 'test_file.docx'))
    os.remove(os.path.join(target_dir, 'subdir', 'test_file.doc'))
    os.remove(os.path.join(target_dir, 'subdir', 'test_file.docx'))
    os.remove(os.path.join(target_dir, 'test_file.jpg'))
    os.remove(os.path.join(target_dir, 'test_file.png'))
    os.remove(os.path.join(target_dir, 'subdir', 'test_file.jpg'))
    os.remove(os.path.join(target_dir, 'subdir', 'test_file.png'))
    task_func(source_dir, target_dir, r'\b[A-Za-z0-9]+\.(pdf)\b')
    assert not os.path.exists(os.path.join(target_dir, 'test_file.txt'))
    assert not os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.txt'))
    assert not os.path.exists(os.path.join(target_dir, 'test_file.doc'))
    assert not os.path.exists(os.path.join(target_dir, 'test_file.docx'))
    assert not os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.doc'))
    assert not os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.docx'))
    assert not os.path.exists(os.path.join(target_dir, 'test_file.jpg'))
    assert not os.path.exists(os.path.join(target_dir, 'test_file.png'))
    assert not os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.jpg'))
    assert not os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.png'))
    assert not os.path.exists(os.path.join(target_dir, 'test_file.pdf'))
    assert not os.path.exists(os.path.join(target_dir, 'subdir', 'test_file.pdf'))