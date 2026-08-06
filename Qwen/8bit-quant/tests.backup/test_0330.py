import pytest
from src_0330 import task_func
import os
import json
import tempfile

def test_task_func_with_default_pattern():
    # Create a temporary JSON file
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
        temp_file.write(json.dumps({'key1': 'value1', 'key2': 'value2'}))
        temp_file_path = temp_file.name

    try:
        result = task_func(temp_file_path)
        expected_result = {os.path.basename(temp_file_path): ['value1', 'value2']}
        assert result == expected_result
    finally:
        os.remove(temp_file_path)

def test_task_func_with_custom_pattern():
    # Create a temporary JSON file
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
        temp_file.write(json.dumps({'key1': 'hello world', 'key2': 'foo bar'}))
        temp_file_path = temp_file.name

    try:
        custom_pattern = r'\b\w+\b'
        result = task_func(temp_file_path, regex_pattern=custom_pattern)
        expected_result = {os.path.basename(temp_file_path): ['hello', 'world', 'foo', 'bar']}
        assert result == expected_result
    finally:
        os.remove(temp_file_path)

def test_task_func_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_file.json')

def test_task_func_empty_json_file():
    # Create a temporary empty JSON file
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
        temp_file_path = temp_file.name

    try:
        result = task_func(temp_file_path)
        expected_result = {os.path.basename(temp_file_path): []}
        assert result == expected_result
    finally:
        os.remove(temp_file_path)

def test_task_func_invalid_json_file():
    # Create a temporary invalid JSON file
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
        temp_file.write('{invalid json}')
        temp_file_path = temp_file.name

    try:
        with pytest.raises(json.JSONDecodeError):
            task_func(temp_file_path)
    finally:
        os.remove(temp_file_path)