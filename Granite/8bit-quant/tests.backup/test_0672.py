import os
import random
import json
import pytest
from src_0672 import task_func

def test_task_func():
    directory = "test_directory"
    n = 5
    expected_output = "test_directory"
    expected_files = ["0.json", "1.json", "2.json", "3.json", "4.json"]

    output = task_func(directory, n)

    assert output == expected_output
    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == n
    for filename in expected_files:
        assert filename in os.listdir(directory)

def test_task_func_with_invalid_directory():
    directory = 123
    n = 5

    with pytest.raises(TypeError):
        task_func(directory, n)

def test_task_func_with_invalid_n():
    directory = "test_directory"
    n = "five"

    with pytest.raises(TypeError):
        task_func(directory, n)