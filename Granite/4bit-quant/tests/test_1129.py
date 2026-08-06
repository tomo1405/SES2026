import json
import os
import hashlib
import base64
import time
import pytest

from src_1129 import task_func

def test_task_func():
    file_path = "path/to/test/file.json"
    unknown_key = "some_key"
    new_file_path = task_func(file_path, unknown_key)
    assert new_file_path.endswith(".txt")
    assert os.path.exists(new_file_path)
    with open(new_file_path, "r") as f:
        content = f.read()
        assert content == "hashed_value"

def test_task_func_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        task_func("invalid_file_path", "some_key")

def test_task_func_invalid_key():
    file_path = "path/to/test/file.json"
    with pytest.raises(KeyError):
        task_func(file_path, "invalid_key")