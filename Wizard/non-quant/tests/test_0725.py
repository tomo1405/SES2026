python
import os
import json
import pytest

from src_0725 import task_func

def test_task_func():
    # Test case 1: Valid config file
    config_path = "config.json"
    with open(config_path, "w") as f:
        json.dump({"key": "value"}, f)
    assert task_func(config_path) == {"key": "value"}
    os.remove(config_path)
    
    # Test case 2: Invalid config file
    with pytest.raises(FileNotFoundError):
        task_func("invalid_config.json")