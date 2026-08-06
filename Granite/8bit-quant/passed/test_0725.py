import os
import json
import pytest
from src_0725 import task_func

def test_task_func():
    config_path = "path/to/config.json"
    with open(config_path, "w") as f:
        json.dump({}, f)
    
    result = task_func(config_path)
    assert result == {}
    
    os.remove(config_path)

def test_task_func_file_not_found():
    config_path = "path/to/nonexistent.json"
    with pytest.raises(FileNotFoundError):
        task_func(config_path)