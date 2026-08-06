python
import os
import re
import shutil
import pytest

# Constants
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def task_func():
    for filename in os.listdir(SOURCE_DIR):
        match = FILE_PATTERN.match(filename)
        if match is not None:
            prefix = match.group(1)
            new_filename = f'{prefix}.json'
            shutil.move(os.path.join(SOURCE_DIR, filename), os.path.join(TARGET_DIR, new_filename))

def test_task_func():
    # Test case 1
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(TARGET_DIR, exist_ok=True)
    with open(os.path.join(SOURCE_DIR, 'file1-123.json'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file2-456.json'), 'w') as f:
        f.write('test')
    task_func()
    assert os.path.exists(os.path.join(TARGET_DIR, 'file1.json'))
    assert os.path.exists(os.path.join(TARGET_DIR, 'file2.json'))
    assert not os.path.exists(os.path.join(SOURCE_DIR, 'file1-123.json'))
    assert not os.path.exists(os.path.join(SOURCE_DIR, 'file2-456.json'))

    # Test case 2
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(TARGET_DIR, exist_ok=True)
    with open(os.path.join(SOURCE_DIR, 'file1-123.json'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file2-456.json'), 'w') as f:
        f.write('test')
    with pytest.raises(Exception):
        task_func()
    assert os.path.exists(os.path.join(SOURCE_DIR, 'file1-123.json'))
    assert os.path.exists(os.path.join(SOURCE_DIR, 'file2-456.json'))
    assert not os.path.exists(os.path.join(TARGET_DIR, 'file1.json'))
    assert not os.path.exists(os.path.join(TARGET_DIR, 'file2.json'))