import pytest
from src_0535 import task_func

@pytest.mark.parametrize("num, from_base, to_base, private_key, alphabet, expected_output", [
    ("10", 10, 2, "private_key", "0123456789", "011010001010"),
    ("255", 10, 16, "private_key", "0123456789abcdef", "ff"),
    ("1234567890", 10, 8, "private_key", "01234567", "313233347735363730"),
])
def test_task_func(num, from_base, to_base, private_key, alphabet, expected_output):
    assert task_func(num, from_base, to_base, private_key, alphabet) == expected_output