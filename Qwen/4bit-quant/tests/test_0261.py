import json
import os
import tempfile

from src_0261 import task_func


def create_json_file(directory, content):
    with open(os.path.join(directory, 'test.json'), 'w') as f:
        json.dump(content, f)

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == 0

def test_task_func_with_existing_key():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_json_file(temp_dir, {KEY: 'existing_value'})
        result = task_func(temp_dir)
        assert result == 0

def test_task_func_without_existing_key():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_json_file(temp_dir, {'other_key': 'other_value'})
        result = task_func(temp_dir)
        assert result == 1

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_json_file(temp_dir, {KEY: 'existing_value'})
        create_json_file(temp_dir, {'other_key': 'other_value'})
        result = task_func(temp_dir)
        assert result == 1

def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == 0

def test_task_func_non_json_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, 'test.txt'), 'w') as f:
            f.write('This is a text file.')
        result = task_func(temp_dir)
        assert result == 0