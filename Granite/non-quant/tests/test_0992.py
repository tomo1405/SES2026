import pytest
from src_0992 import task_func
import binascii
import string
import random

@pytest.mark.parametrize("length", [10, 20, 30])
def test_task_func(length):
    HEX_CHARS = string.hexdigits.lower()
    hex_string = "".join(random.choice(HEX_CHARS) for _ in range(length))
    expected_output = binascii.unhexlify(hex_string).decode("utf-8", "ignore")
    actual_output = task_func(length)
    assert actual_output == expected_output