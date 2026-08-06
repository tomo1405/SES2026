import pytest
from src_0740 import task_func

def test_task_func():
    # Test with a valid hex key
    hex_key = '470FC614'
    expected_result = 1.23
    assert task_func(hex_key) == expected_result

    # Test with a valid hex key and a different expected result
    hex_key = '4A0FC614'
    expected_result = 2.34
    assert task_func(hex_key) == expected_result

    # Test with a valid hex key and a different expected result
    hex_key = '4B9FC614'
    expected_result = 3.45
    assert task_func(hex_key) == expected_result

    # Test with a valid hex key and a different expected result
    hex_key = '4C8FC614'
    expected_result = 4.56
    assert task_func(hex_key) == expected_result

    # Test with a valid hex key and a different expected result
    hex_key = '4D7FC614'
    expected_result = 5.67
    assert task_func(hex_key) == expected_result

    # Test with a random hex key
    hex_key = random.choice(KEYS)
    expected_result = round(struct.unpack('!f', bytes.fromhex(hex_key))[0], 2)
    assert task_func(hex_key) == expected_result

    # Test with a random hex key and a different expected result
    hex_key = random.choice(KEYS)
    expected_result = round(struct.unpack('!f', bytes.fromhex(hex_key))[0], 2) + 1
    assert task_func(hex_key) == expected_result

    # Test with a random hex key and a different expected result
    hex_key = random.choice(KEYS)
    expected_result = round(struct.unpack('!f', bytes.fromhex(hex_key))[0], 2) - 1
    assert task_func(hex_key) == expected_result