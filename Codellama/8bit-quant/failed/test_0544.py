import pytest
from src_0544 import task_func

def test_task_func():
    float_bytes = os.urandom(4)
    encoded_str = base64.b64encode(float_bytes)
    assert task_func() == encoded_str.decode()