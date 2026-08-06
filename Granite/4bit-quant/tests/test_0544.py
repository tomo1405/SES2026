import base64
import os
import pytest

def task_func():
    float_bytes = os.urandom(4)
    encoded_str = base64.b64encode(float_bytes)

    return encoded_str.decode()

def test_task_func():
    float_bytes = os.urandom(4)
    encoded_str = base64.b64encode(float_bytes)
    expected_result = encoded_str.decode()

    actual_result = task_func()

    assert actual_result == expected_result, "task_func() returned an incorrect result"