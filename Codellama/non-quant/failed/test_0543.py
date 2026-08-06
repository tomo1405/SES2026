import pytest
from src_0543 import task_func

def test_task_func():
    # Test with valid hex keys
    hex_keys = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
    for hex_key in hex_keys:
        hashed_float = task_func(hex_keys=[hex_key])
        assert hashed_float == hashlib.md5(str(struct.unpack('!f', bytes.fromhex(hex_key))[0]).encode()).hexdigest()

    # Test with invalid hex keys
    invalid_hex_keys = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614', 'invalid_key']
    for hex_key in invalid_hex_keys:
        with pytest.raises(ValueError):
            task_func(hex_keys=[hex_key])