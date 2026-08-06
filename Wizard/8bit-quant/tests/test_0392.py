python
import os
import glob
import shutil
import pytest

def task_func(directory, archive_dir='archive'):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    json_files = glob.glob(os.path.join(directory, '*.json'))
    error_messages = []

    for json_file in json_files:
        try:
            shutil.move(json_file, archive_dir)
        except Exception as e:
            error_message = f'Unable to move {json_file} due to {str(e)}'
            error_messages.append(error_message)

    return (len(error_messages) == 0, error_messages)

def test_task_func():
    # Test case 1: Move all JSON files successfully
    directory = 'data'
    archive_dir = 'archive'
    os.makedirs(directory, exist_ok=True)
    for i in range(5):
        with open(os.path.join(directory, f'file{i}.json'), 'w') as f:
            f.write('test')
    assert task_func(directory, archive_dir) == (True, [])
    assert len(os.listdir(directory)) == 0
    assert len(os.listdir(archive_dir)) == 5

    # Test case 2: Move some JSON files successfully, some fail
    directory = 'data'
    archive_dir = 'archive'
    os.makedirs(directory, exist_ok=True)
    for i in range(5):
        with open(os.path.join(directory, f'file{i}.json'), 'w') as f:
            f.write('test')
    with open(os.path.join(directory, 'file5.txt'), 'w') as f:
        f.write('test')
    assert task_func(directory, archive_dir) == (False, ['Unable to move data/file5.txt due to [Errno 2] No such file or directory: '])
    assert len(os.listdir(directory)) == 1
    assert len(os.listdir(archive_dir)) == 5

    # Test case 3: Move no JSON files
    directory = 'data'
    archive_dir = 'archive'
    os.makedirs(directory, exist_ok=True)
    assert task_func(directory, archive_dir) == (True, [])
    assert len(os.listdir(directory)) == 0
    assert len(os.listdir(archive_dir)) == 0

    # Test case 4: Move JSON files to non-existent directory
    directory = 'data'
    archive_dir = 'nonexistent'
    os.makedirs(directory, exist_ok=True)
    for i in range(5):
        with open(os.path.join(directory, f'file{i}.json'), 'w') as f:
            f.write('test')
    assert task_func(directory, archive_dir) == (False, ['Unable to move data/file0.json due to [Errno 2] No such file or directory: '])
    assert len(os.listdir(directory)) == 5
    assert len(os.listdir(archive_dir)) == 0