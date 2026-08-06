import base64

import pytest
from src_0544 import task_func


def test_task_func_output_type():
    result = task_func()
    assert isinstance(result, str), "The function should return a string."

def test_task_func_output_length():
    result = task_func()
    # Base64 encoding of 4 bytes results in a string of length 6 (since 4*8/6 = 5.33, rounded up to 6)
    assert len(result) == 6, "The length of the encoded string should be 6."

def test_task_func_output_valid_base64():
    result = task_func()
    try:
        base64.b64decode(result)
    except Exception as e:
        pytest.fail(f"The output is not a valid base64 encoded string: {e}")

def test_task_func_reproducibility():
    # Since os.urandom is used, we cannot predict the exact output,
    # but we can check that multiple calls produce different results.
    result1 = task_func()
    result2 = task_func()
    assert result1 != result2, "The function should produce different results on different calls."