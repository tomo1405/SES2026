import os
import pathlib
import pytest

from src_0973 import task_func

def test_task_func():
    path = "C:/Users/John/Documents/myfile.txt"
    expected_output = ["C:", "Users", "John", "Documents", "myfile.txt"]
    assert task_func(path) == expected_output

def test_task_func_with_empty_path():
    path = ""
    expected_output = []
    assert task_func(path) == expected_output

def test_task_func_with_invalid_chars():
    path = "C:/Users/John<Documents/myfile.txt"
    expected_output = []
    assert task_func(path) == expected_output

def test_task_func_with_delimiter():
    path = "C:/Users/John/Documents/myfile.txt"
    delimiter = "/"
    expected_output = ["C:", "Users", "John", "Documents", "myfile.txt"]
    assert task_func(path, delimiter) == expected_output