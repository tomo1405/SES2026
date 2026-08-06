import pytest
from src_0535 import task_func

@pytest.mark.parametrize("num, from_base, to_base, private_key, alphabet, expected_output", [
    ("10", 10, 2, "private_key", "0123456789", "0110100010"),
    ("255", 10, 16, "private_key", "0123456789abcdef", "ff"),
    ("1234567890", 10, 8, "private_key", "01234567", "31323334773566372031"),
])
def test_task_func(num, from_base, to_base, private_key, alphabet, expected_output):
    assert task_func(num, from_base, to_base, private_key, alphabet) == expected_output