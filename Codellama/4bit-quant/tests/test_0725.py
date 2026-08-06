import pytest
from src_0725 import task_func

def test_task_func_valid_config():
    config_path = "path/to/config.json"
    config = task_func(config_path)
    assert isinstance(config, dict)

def test_task_func_invalid_config():
    config_path = "path/to/invalid_config.json"
    with pytest.raises(FileNotFoundError):
        task_func(config_path)