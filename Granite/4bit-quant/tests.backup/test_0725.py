import os
import json
import pytest

def task_func(config_path: str) -> dict:
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"The configuration file {config_path} does not exist.")
    
    with open(config_path) as f:
        config = json.load(f)
    
    return config

def test_task_func():
    config_path = "path/to/config.json"
    with open(config_path, "w") as f:
        json.dump({"key": "value"}, f)
    
    result = task_func(config_path)
    assert result == {"key": "value"}
    
    os.remove(config_path)

def test_task_func_file_not_found():
    config_path = "path/to/nonexistent.json"
    with pytest.raises(FileNotFoundError):
        task_func(config_path)