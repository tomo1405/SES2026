import pytest
from src_0730 import task_func
import os
import pickle
import random
import string

def test_task_func():
    # Test with a list of strings
    strings = ["string1", "string2", "string3"]
    result = task_func(strings)
    assert result == strings

    # Test with a specific filename
    filename = "test_file.pkl"
    result = task_func(strings, filename)
    assert result == strings
    assert os.path.exists(filename)
    os.remove(filename)

    # Test with a random filename
    filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".pkl"
    result = task_func(strings, filename)
    assert result == strings
    assert os.path.exists(filename)
    os.remove(filename)