import pytest
from src_0207 import task_func

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv")

def test_valid_file():
    result = task_func("test_file.csv")
    assert os.path.exists(result)
    os.remove(result)  # Clean up the created JSON file