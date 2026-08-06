import pytest
from src_1129 import task_func
import json
import os
import hashlib
import base64
import time

def test_task_func():
    file_path = "test_data.json"
    unknown_key = "example_key"
    with open(file_path, 'w') as f:
        json.dump({"A": {unknown_key: {"maindata": [{"Info": "example_value"}]}}}", f)
    
    new_file_path = task_func(file_path, unknown_key)
    assert os.path.exists(new_file_path)
    
    with open(new_file_path, 'r') as f:
        data = f.read()
    
    hashed_str = data.encode()
    hashed_value = base64.b64decode(hashed_str)
    value = hashlib.sha256(hashed_value).hexdigest()
    
    assert value == "example_value"
    
    os.remove(file_path)
    os.remove(new_file_path)