python
import pytest
from src_0373 import task_func

def test_task_func():
    directory_path = 'test_files'
    processed_files = task_func(directory_path)
    assert processed_files == 2