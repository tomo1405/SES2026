import json
import os

from src_0672 import task_func


def test_task_func_creates_directory():
    directory = task_func('test_directory', 10)
    assert os.path.exists(directory)

def test_task_func_creates_files():
    directory = task_func('test_directory', 10)
    for i in range(10):
        filename = str(i) + ".json"
        filepath = os.path.join(directory, filename)
        assert os.path.exists(filepath)

def test_task_func_writes_json_data():
    directory = task_func('test_directory', 10)
    for i in range(10):
        filename = str(i) + ".json"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            assert data['number'] >= 1 and data['number'] <= 100