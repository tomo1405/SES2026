import base64
import binascii
import hashlib

from src_0132 import task_func


def test_task_func():
    hex_str = "68656c6c6f"  # "hello" in hex
    salt_size = 16

    # Call the function
    salt_b64, hash_value = task_func(hex_str, salt_size)

    # Check that the salt is base64 encoded and has the correct length
    assert len(base64.b64decode(salt_b64)) == salt_size

    # Check that the hash value is a 64-character hexadecimal string
    assert len(hash_value) == 64
    assert all(c in '0123456789abcdef' for c in hash_value)

    # Verify that the hash is correctly computed
    salt = base64.b64decode(salt_b64)
    data = binascii.unhexlify(hex_str.replace('\\x', ''))
    salted_data = salt + data
    expected_hash = hashlib.sha256(salted_data).hexdigest()
    assert hash_value == expected_hash