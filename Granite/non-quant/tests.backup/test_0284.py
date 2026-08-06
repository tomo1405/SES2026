import os
import json
from collections import Counter
from src_0284 import task_func
import pytest

def test_task_func():
    json_files_path = './json_files/'
    key = 'name'
    key_values = []

    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_files_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if key in data:
                    key_values.append(data[key])

    expected_result = dict(Counter(key_values))
    actual_result = task_func(json_files_path, key)
    assert actual_result == expected_result