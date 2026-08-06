python
import os
import json
from collections import Counter
import pytest

def task_func(json_files_path='./json_files/', key='name'):
    key_values = []

    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_files_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if key in data:
                    key_values.append(data[key])

    return dict(Counter(key_values))

def test_task_func():
    # Test case 1: Test with default arguments
    assert task_func() == {'John': 1, 'Jane': 1, 'Bob': 1}

    # Test case 2: Test with custom arguments
    assert task_func(json_files_path='./tests/json_files/', key='age') == {'25': 1, '30': 1, '35': 1}

    # Test case 3: Test with invalid key
    with pytest.raises(KeyError):
        task_func(key='invalid_key')