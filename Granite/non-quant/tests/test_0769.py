import re
import os
import glob
import pytest
from src_0769 import task_func

def test_task_func():
    dir_path = "/path/to/directory"
    result = task_func(dir_path)
    assert isinstance(result, dict)
    for file_path, count in result.items():
        assert isinstance(file_path, str)
        assert isinstance(count, int)
        assert count >= 0

def test_task_func_with_invalid_directory():
    dir_path = "/path/to/invalid/directory"
    with pytest.raises(ValueError):
        task_func(dir_path)