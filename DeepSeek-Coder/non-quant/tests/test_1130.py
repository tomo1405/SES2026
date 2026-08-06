import pytest
from src_1130 import task_func
import os
import json
import requests
from datetime import datetime

# Test cases for task_func

def test_task_func_basic():
    json_data = '{"url": "http://example.com"}'
    unknown_key = "url"
    save_dir = "/tmp"
    result = task_func(json_data=json_data, unknown_key=unknown_key, save_dir=save_dir)
    assert os.path.exists(result), "File should be saved"
    os.remove(result)  # Clean up

def test_task_func_invalid_url():
    json_data = '{"url": "invalid_url"}'
    unknown_key = "url"
    save_dir = "/tmp"
    with pytest.raises(requests.RequestException):
        task_func(json_data=json_data, unknown_key=unknown_key, save_dir=save_dir)

def test_task_func_save_dir_none():
    json_data = '{"url": "http://example.com"}'
    unknown_key = "url"
    save_dir = None
    result = task_func(json_data=json_data, unknown_key=unknown_key, save_dir=save_dir)
    assert os.path.exists(result), "File should be saved"
    os.remove(result)  # Clean up

def test_task_func_invalid_json():
    json_data = 'invalid_json'
    unknown_key = "url"
    save_dir = "/tmp"
    with pytest.raises(json.JSONDecodeError):
        task_func(json_data=json_data, unknown_key=unknown_key, save_dir=save_dir)