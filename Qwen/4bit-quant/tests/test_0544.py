import base64

import pytest
from src_0544 import task_func


def test_task_func():
    result = task_func()
    assert isinstance(result, str), "The result should be a string"
    # Check if the string is a valid base64 encoded string
    try:
        base64.b64decode(result.encode())
    except Exception as e:
        pytest.fail(f"Result is not a valid base64 encoded string: {e}")