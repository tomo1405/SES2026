import re
import os
import string
import random
import pytest
from src_0848 import task_func
def test_task_func():
    input_string = "Hello, world!\nThis is a test line."
    file_paths = task_func(input_string)
    for file_path in file_paths:
        assert os.path.exists(file_path)
        with open(file_path, 'r') as file:
            content = file.read()
            assert content in input_string
    assert len(file_paths) == 2