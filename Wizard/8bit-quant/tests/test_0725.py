python
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
    # Test case 1: Valid config file
    config_path = "config.json"
    with open(config_path, "w") as f:
        json.dump({"key": "value"}, f)
    assert task_func(config_path) == {"key": "value"}
    os.remove(config_path)

    # Test case 2: Invalid config file
    config_path = "config.json"
    with open(config_path, "w") as f:
        f.write("invalid json")
    with pytest.raises(json.JSONDecodeError):
        task_func(config_path)
    os.remove(config_path)

    # Test case 3: Non-existent config file
    config_path = "nonexistent.json"
    with pytest.raises(FileNotFoundError):
        task_func(config_path)