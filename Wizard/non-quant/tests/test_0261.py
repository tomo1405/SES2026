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
    # Test case 1: directory with no JSON files
    directory = 'test_dir'
    os.mkdir(directory)
    assert task_func(directory) == 0
    os.rmdir(directory)

    # Test case 2: directory with one JSON file
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'test.json'), 'w') as f:
        json.dump({'key1': 'value1'}, f)
    assert task_func(directory) == 1
    os.remove(os.path.join(directory, 'test.json'))
    os.rmdir(directory)

    # Test case 3: directory with multiple JSON files
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'test1.json'), 'w') as f:
        json.dump({'key1': 'value1'}, f)
    with open(os.path.join(directory, 'test2.json'), 'w') as f:
        json.dump({'key2': 'value2'}, f)
    with open(os.path.join(directory, 'test3.json'), 'w') as f:
        json.dump({'key3': 'value3'}, f)
    assert task_func(directory) == 3
    os.remove(os.path.join(directory, 'test1.json'))
    os.remove(os.path.join(directory, 'test2.json'))
    os.remove(os.path.join(directory, 'test3.json'))
    os.rmdir(directory)

    # Test case 4: directory with JSON file that already has the key
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'test.json'), 'w') as f:
        json.dump({KEY: 'value1'}, f)
    assert task_func(directory) == 0
    os.remove(os.path.join(directory, 'test.json'))
    os.rmdir(directory)

    # Test case 5: directory with JSON file that has invalid JSON format
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'test.json'), 'w') as f:
        f.write('invalid json format')
    with pytest.raises(json.JSONDecodeError):
        task_func(directory)
    os.remove(os.path.join(directory, 'test.json'))
    os.rmdir(directory)