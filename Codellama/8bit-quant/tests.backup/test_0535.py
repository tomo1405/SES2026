import pytest
from src_0535 import task_func

def test_task_func():
    num = "1234567890"
    from_base = 10
    to_base = 36
    private_key = "private_key"
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"

    expected_result = "base64_encoded_string"

    result = task_func(num, from_base, to_base, private_key, alphabet)

    assert result == expected_result