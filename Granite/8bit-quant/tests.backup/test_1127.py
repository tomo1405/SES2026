import re
import hashlib
import pytest

from src_1127 import task_func

def test_task_func():
    input_str = "Hello, World!"
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str)
    hashed_str = hashlib.sha256(cleaned_str.encode()).hexdigest()
    expected_output = hashed_str

    actual_output = task_func(input_str)

    assert actual_output == expected_output, "Task function output does not match expected output"