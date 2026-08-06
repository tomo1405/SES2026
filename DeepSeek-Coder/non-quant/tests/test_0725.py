import pytest
from src_0725 import task_func

def test_file_exists():
    config_path = "test_config.json"
    with open(config_path, 'w') as f:
        f.write('{"key": "value"}')
    try:
        result = task_func(config_path)
        assert result == {"key": "value"}
    finally:
        os.remove(config_path)

def test_file_does_not_exist():
    config_path = "nonexistent_file.json"
    with pytest.raises(FileNotFoundError):
        task_func(config_path)