import json
import os
import tempfile

from src_0261 import task_func


def create_temp_json_file(directory, content):
    file_path = os.path.join(directory, 'temp.json')
    with open(file_path, 'w') as f:
        json.dump(content, f)
    return file_path

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == 0

def test_task_func_with_existing_key():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_file(temp_dir, {KEY: "old_value"})
        result = task_func(temp_dir)
        assert result == 0

def test_task_func_without_key():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_file(temp_dir, {"other_key": "other_value"})
        result = task_func(temp_dir)
        assert result == 1

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_file(temp_dir, {KEY: "old_value"})
        create_temp_json_file(temp_dir, {"other_key": "other_value"})
        create_temp_json_file(temp_dir, {})
        result = task_func(temp_dir)
        assert result == 2

def test_task_func_nested_directories():
    with tempfile.TemporaryDirectory() as temp_dir:
        sub_dir = os.path.join(temp_dir, 'subdir')
        os.makedirs(sub_dir)
        create_temp_json_file(sub_dir, {"other_key": "other_value"})
        result = task_func(temp_dir)
        assert result == 1

def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == 0