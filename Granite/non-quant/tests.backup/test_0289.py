import pytest
from src_0289 import task_func
import os
import json

def test_task_func():
    directory_path = '/path/to/directory'
    key_counts = task_func(directory_path)
    assert isinstance(key_counts, dict)
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                for key in data.keys():
                    assert key in key_counts
                    key_counts[key] -= 1
    for key, count in key_counts.items():
        assert count == 0