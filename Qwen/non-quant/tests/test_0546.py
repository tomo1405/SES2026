import codecs
import struct

from src_0546 import task_func


def test_task_func():
    # Test that the function returns a byte string
    result = task_func()
    assert isinstance(result, bytes)

    # Test that the function returns one of the possible encoded float values
    possible_values = [struct.unpack('!f', bytes.fromhex(key))[0] for key in KEYS]
    possible_encoded_values = {codecs.encode(str(value), 'utf-8') for value in possible_values}
    assert result in possible_encoded_values

    # Test that the function returns a different value each time it is called
    results = set()
    for _ in range(10):
        result = task_func()
        results.add(result)
        assert isinstance(result, bytes)
    assert len(results) > 1  # Ensure at least two different values were returned