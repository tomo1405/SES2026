python
import pytest
from src_0848 import task_func

def test_task_func():
    input_string = "Hello, World!\nHow are you?\nI'm doing great."
    file_paths = task_func(input_string)
    assert len(file_paths) == 3
    for filepath in file_paths:
        assert os.path.isfile(filepath)
        with open(filepath, 'r') as file:
            assert file.read() in input_string.split('\n')