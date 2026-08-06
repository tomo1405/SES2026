import json
import os
import tempfile

import pytest
from src_0261 import task_func


def create_temp_json_file(directory, content):
    file_path = os.path.join(directory, 'temp.json')
    with open(file_path, 'w') as f:
        json.dump(content, f)
    return file_path

def test_task_func_no_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == 0

def test_task_func_existing_key():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_file(temp_dir, {KEY: 'oldvalue'})
        result = task_func(temp_dir)
        assert result == 0

def test_task_func_missing_key():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_file(temp_dir, {'otherkey': 'othervalue'})
        result = task_func(temp_dir)
        assert result == 1

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_file(temp_dir, {'otherkey': 'othervalue'})
        create_temp_json_file(temp_dir, {'yetanotherkey': 'yetanothervalue'})
        result = task_func(temp_dir)
        assert result == 2

def test_task_func_mixed_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_file(temp_dir, {KEY: 'oldvalue'})
        create_temp_json_file(temp_dir, {'otherkey': 'othervalue'})
        result = task_func(temp_dir)
        assert result == 1

def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == 0

def test_task_func_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_directory')