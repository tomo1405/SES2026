python
import hashlib
import base64
import os
import pytest

def task_func(filename, data, password):
    # Ensure the file exists
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)
    if not os.path.exists(filename):
        open(filename, 'a').close()

    # Encrypt the data using simple XOR operation with password hash as key
    key = hashlib.sha256(password.encode()).digest()
    encrypted_bytes = [byte ^ key[i % len(key)] for i, byte in enumerate(data.encode())]
    encrypted = base64.b64encode(bytes(encrypted_bytes)).decode()

    # Write to the file
    with open(filename, 'w') as f:
        f.write(encrypted)

    return encrypted

def test_task_func():
    # Test case 1: Valid input
    filename = 'test.txt'
    data = 'Hello, world!'
    password = 'password'
    expected_output = 'SGVsbG8sIHdvcmxkIQ=='
    assert task_func(filename, data, password) == expected_output

    # Test case 2: Invalid input (empty filename)
    with pytest.raises(ValueError):
        task_func('', data, password)

    # Test case 3: Invalid input (empty data)
    with pytest.raises(ValueError):
        task_func(filename, '', password)

    # Test case 4: Invalid input (empty password)
    with pytest.raises(ValueError):
        task_func(filename, data, '')