import os
import hashlib
import pytest
from src_1051 import task_func

# Constants
DIRECTORY = "./hashed_files"

def test_task_func():
    input_string = "Hello\nWorld"
    expected_output = [os.path.join(DIRECTORY, "64ec88ca9867e5661673548b6c0325b0.txt"),
                       os.path.join(DIRECTORY, "1b9a5ee740f4d4d1224b184cd095f3f1.txt")]

    output = task_func(input_string)

    assert output == expected_output

def test_task_func_with_empty_input():
    input_string = ""
    expected_output = []

    output = task_func(input_string)

    assert output == expected_output

def test_task_func_with_one_line_input():
    input_string = "Hello"
    expected_output = [os.path.join(DIRECTORY, "64ec88ca98.txt")]

    output = task_func(input_string)

    assert output == expected_output