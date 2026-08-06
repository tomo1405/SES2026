import pytest
from src_0960 import task_func
import string
import random

def test_task_func():
    text = "Hello, World!"
    seed = 42
    random.seed(seed)
    expected_output = "".join(random.choice(string.ascii_letters) if c.isalpha() else c for c in text)
    actual_output = task_func(text, seed)
    assert actual_output == expected_output, "Task function output does not match expected output"

def test_task_func_without_seed():
    text = "Python is great!"
    expected_output = "".join(random.choice(string.ascii_letters) if c.isalpha() else c for c in text)
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function output does not match expected output"

def test_task_func_with_empty_string():
    text = ""
    expected_output = ""
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function output does not match expected output"