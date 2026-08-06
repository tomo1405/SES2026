import pytest
from src_0289 import task_func
import os
import tempfile
import json

def create_temp_json_files(directory, files):
    for file_name, content in files.items():
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as f:
            json.dump(content, f)

def test_task_func_with_no_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == {}

def test_task_func_with_one_json_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_files(temp_dir, {
            'file1.json': {'key1': 'value1', 'key2': 'value2'}
        })
        result = task_func(temp_dir)
        assert result == {'key1': 1, 'key2': 1}

def test_task_func_with_multiple_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_files(temp_dir, {
            'file1.json': {'key1': 'value1', 'key2': 'value2'},
            'file2.json': {'key1': 'value3', 'key3': 'value4'},
            'file3.json': {'key2': 'value5'}
        })
        result = task_func(temp_dir)
        assert result == {'key1': 2, 'key2': 2, 'key3': 1}

def test_task_func_with_non_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_files(temp_dir, {
            'file1.json': {'key1': 'value1'},
            'file2.txt': 'This is a text file'
        })
        result = task_func(temp_dir)
        assert result == {'key1': 1}

def test_task_func_with_nested_json():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_files(temp_dir, {
            'file1.json': {'key1': {'nested_key1': 'value1'}, 'key2': 'value2'}
        })
        result = task_func(temp_dir)
        assert result == {'key1': 1, 'key2': 1}

def test_task_func_with_empty_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_json_files(temp_dir, {
            'file1.json': {},
            'file2.json': {}
        })
        result = task_func(temp_dir)
        assert result == {}