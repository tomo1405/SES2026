python
import json
import os
import glob
import pytest

# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def task_func(directory):
    files = glob.glob(os.path.join(directory, '*.json'))
    updated_files = 0

    for file in files:
        with open(file, 'r+') as f:
            data = json.load(f)
            if KEY not in data:
                data[KEY] = VALUE
                f.seek(0)
                f.truncate()
                json.dump(data, f)
                updated_files += 1

    return updated_files

def test_task_func():
    # Test case 1: Directory with no JSON files
    directory = 'test_dir'
    os.mkdir(directory)
    assert task_func(directory) == 0
    os.rmdir(directory)

    # Test case 2: Directory with JSON files, no key in any file
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'file1.json'), 'w') as f:
        json.dump({'key1': 'value1'}, f)
    with open(os.path.join(directory, 'file2.json'), 'w') as f:
        json.dump({'key2': 'value2'}, f)
    assert task_func(directory) == 0
    os.remove(os.path.join(directory, 'file1.json'))
    os.remove(os.path.join(directory, 'file2.json'))
    os.rmdir(directory)

    # Test case 3: Directory with JSON files, key in one file
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'file1.json'), 'w') as f:
        json.dump({'key1': 'value1'}, f)
    with open(os.path.join(directory, 'file2.json'), 'w') as f:
        json.dump({'key2': 'value2', KEY: 'oldvalue'}, f)
    assert task_func(directory) == 1
    with open(os.path.join(directory, 'file2.json'), 'r') as f:
        data = json.load(f)
        assert data[KEY] == VALUE
    os.remove(os.path.join(directory, 'file1.json'))
    os.remove(os.path.join(directory, 'file2.json'))
    os.rmdir(directory)

    # Test case 4: Directory with JSON files, key in all files
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'file1.json'), 'w') as f:
        json.dump({'key1': 'value1', KEY: 'oldvalue'}, f)
    with open(os.path.join(directory, 'file2.json'), 'w') as f:
        json.dump({'key2': 'value2', KEY: 'oldvalue'}, f)
    assert task_func(directory) == 2
    with open(os.path.join(directory, 'file1.json'), 'r') as f:
        data = json.load(f)
        assert data[KEY] == VALUE
    with open(os.path.join(directory, 'file2.json'), 'r') as f:
        data = json.load(f)
        assert data[KEY] == VALUE
    os.remove(os.path.join(directory, 'file1.json'))
    os.remove(os.path.join(directory, 'file2.json'))
    os.rmdir(directory)