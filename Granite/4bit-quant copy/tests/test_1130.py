import json
import requests
import os
from datetime import datetime
from src_1130 import task_func
import pytest

def test_task_func():
    json_data = '{"key1": "https://example.com", "key2": "https://test.com"}'
    unknown_key = "key1"
    save_dir = "/path/to/save/directory"
    
    file_path = task_func(json_data, unknown_key, save_dir)
    
    assert file_path.startswith(save_dir)  # Check if the file path starts with the specified save directory
    assert file_path.endswith(".txt")  # Check if the file path ends with ".txt"
    assert os.path.exists(file_path)  # Check if the file exists at the given file path
    
    with open(file_path, 'rb') as f:
        content = f.read()
        assert content == requests.get(json.loads(json_data)[unknown_key]).content  # Check if the content of the file matches the content of the URL