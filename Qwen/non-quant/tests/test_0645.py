import base64
import hashlib
import os

from src_0645 import task_func


def test_task_func():
    # Test data
    filename = "test_file.txt"
    data = "Hello, World!"
    password = "securepassword"

    # Call the function
    result = task_func(filename, data, password)

    # Check if the file was created
    assert os.path.exists(filename)

    # Read the content of the file
    with open(filename, 'r') as f:
        file_content = f.read()

    # Check if the file content matches the encrypted result
    assert file_content == result

    # Verify the encryption process
    key = hashlib.sha256(password.encode()).digest()
    encrypted_bytes = [byte ^ key[i % len(key)] for i, byte in enumerate(data.encode())]
    expected_encrypted = base64.b64encode(bytes(encrypted_bytes)).decode()

    assert result == expected_encrypted

    # Clean up
    os.remove(filename)