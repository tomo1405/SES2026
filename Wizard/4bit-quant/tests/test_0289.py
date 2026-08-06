python
import collections
import json
import os
import pytest

def task_func(directory_path: str) -> dict:
    key_counts = collections.defaultdict(int)

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                for key in data.keys():
                    key_counts[key] += 1

    return dict(key_counts)

def test_task_func():
    # Test case 1: directory with no JSON files
    directory_path = 'test_dir'
    os.mkdir(directory_path)
    assert task_func(directory_path) == {}
    os.rmdir(directory_path)

    # Test case 2: directory with JSON files
    directory_path = 'test_dir'
    os.mkdir(directory_path)
    with open(os.path.join(directory_path, 'file1.json'), 'w') as f:
        json.dump({'key1': 'value1', 'key2': 'value2'}, f)
    with open(os.path.join(directory_path, 'file2.json'), 'w') as f:
        json.dump({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}, f)
    assert task_func(directory_path) == {'key1': 2, 'key2': 2, 'key3': 1}
    os.remove(os.path.join(directory_path, 'file1.json'))
    os.remove(os.path.join(directory_path, 'file2.json'))
    os.rmdir(directory_path)

    # Test case 3: directory with JSON files with invalid JSON
    directory_path = 'test_dir'
    os.mkdir(directory_path)
    with open(os.path.join(directory_path, 'file1.json'), 'w') as f:
        f.write('invalid JSON')
    with open(os.path.join(directory_path, 'file2.json'), 'w') as f:
        json.dump({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}, f)
    assert task_func(directory_path) == {'key2': 2, 'key3': 1}
    os.remove(os.path.join(directory_path, 'file1.json'))
    os.remove(os.path.join(directory_path, 'file2.json'))
    os.rmdir(directory_path)