import base64
import hashlib
import os

from src_0645 import task_func


def test_task_func():
    filename = "test_file.txt"
    data = "test data"
    password = "test password"

    encrypted = task_func(filename, data, password)

    assert encrypted  # Check if the function returned a non-empty value

    # Check if the file was created and written to
    directory = os.path.dirname(filename)
    assert os.path.exists(filename)

    # Check if the file contains the expected encrypted data
    with open(filename, 'r') as f:
        file_data = f.read()

    key = hashlib.sha256(password.encode()).digest()
    encrypted_bytes = [byte ^ key[i % len(key)] for i, byte in enumerate(data.encode())]
    expected_encrypted = base64.b64encode(bytes(encrypted_bytes)).decode()

    assert file_data == expected_encrypted