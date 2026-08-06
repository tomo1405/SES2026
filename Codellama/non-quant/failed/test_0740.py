import pytest
from src_0740 import task_func

def test_task_func():
    # Test with a valid hex key
    hex_key = '470FC614'
    expected_result = 123.45
    assert task_func(hex_key) == expected_result

    # Test with a random hex key
    hex_key = random.choice(KEYS)
    expected_result = round(struct.unpack('!f', bytes.fromhex(hex_key))[0], 2)
    assert task_func(hex_key) == expected_result

    # Test with a None hex key
    hex_key = None
    expected_result = round(struct.unpack('!f', bytes.fromhex(random.choice(KEYS)))[0], 2)
    assert task_func(hex_key) == expected_result