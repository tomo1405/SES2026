python
import pytest
from src_1107 import task_func

def test_task_func():
    # Test valid file path
    assert task_func('test_file.txt') == '2022-01-01 00:00:00'

    # Test invalid file path
    with pytest.raises(FileNotFoundError):
        task_func('invalid_file.txt')