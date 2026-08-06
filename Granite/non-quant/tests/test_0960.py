import pytest
from src_0960 import task_func
import string
import random

def test_task_func():
    # Test case 1: Test with a string and a seed
    text = "Hello, World!"
    seed = 42
    random.seed(seed)
    expected_output = "".join(random.choice(string.ascii_letters) for c in text)
    actual_output = task_func(text, seed)
    assert actual_output == expected_output

    # Test case 2: Test with an empty string and a seed
    text = ""
    seed = 123
    random.seed(seed)
    expected_output = "".join(random.choice(string.ascii_letters) for c in text)
    actual_output = task_func(text, seed)
    assert actual_output == expected_output

    # Test case 3: Test with a string and no seed
    text = "Python is great!"
    expected_output = "".join(random.choice(string.ascii_letters) for c in text)
    actual_output = task_func(text)
    assert actual_output == expected_output