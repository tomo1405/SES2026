python
import base64
import os
import pytest

def task_func():
    float_bytes = os.urandom(4)
    encoded_str = base64.b64encode(float_bytes)

    return encoded_str.decode()

def test_task_func():
    assert isinstance(task_func(), str)
    assert len(task_func()) == 8