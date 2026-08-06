import os
import hashlib
import pytest
from src_1051 import task_func

DIRECTORY = "./hashed_files"

def test_task_func():
    input_string = "Hello\nWorld\nPython\nTesting"
    expected_output = [
        os.path.join(DIRECTORY, "185f8db32271fe25f561a6fc938b2e26.txt"),
        os.path.join(DIRECTORY, "7509e5bda0c762d2bac7f90d758b5b22.txt"),
        os.path.join(DIRECTORY, "c2d51904f0b0c5d2d70e494106f82e95.txt"),
        os.path.join(DIRECTORY, "45b951a00062f39626659a0052ce99e6.txt"),
    ]
    output = task_func(input_string)
    assert output == expected_output

def test_task_func_with_empty_input():
    input_string = ""
    expected_output = []
    output = task_func(input_string)
    assert output == expected_output

def test_task_func_with_one_line_input():
    input_string = "Single line input"
    expected_output = [
        os.path.join(DIRECTORY, "01ba4719c80b6fe911b091a7c05124b6.txt"),
    ]
    output = task_func(input_string)
    assert output == expected_output