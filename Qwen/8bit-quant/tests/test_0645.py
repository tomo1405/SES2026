import base64
import hashlib
import os

from src_0645 import task_func


def test_task_func():
    # Test data
    filename = "test_file.txt"
    data = "Hello, World!"
    password = "secret"

    # Call the function
    encrypted_data = task_func(filename, data, password)

    # Verify the file exists
    assert os.path.exists(filename)

    # Read the content of the file
    with open(filename, 'r') as f:
        file_content = f.read()

    # Verify the content matches the encrypted data
    assert file_content == encrypted_data

    # Verify the encryption process
    key = hashlib.sha256(password.encode()).digest()
    encrypted_bytes = [byte ^ key[i % len(key)] for i, byte in enumerate(data.encode())]
    expected_encrypted = base64.b64encode(bytes(encrypted_bytes)).decode()
    assert encrypted_data == expected_encrypted

    # Clean up
    os.remove(filename)
    assert not os.path.exists(filename)

def test_task_func_directory_creation():
    # Test data
    filename = "new_directory/test_file.txt"
    data = "Hello, World!"
    password = "secret"

    # Call the function
    task_func(filename, data, password)

    # Verify the directory exists
    directory = os.path.dirname(filename)
    assert os.path.exists(directory)

    # Clean up
    os.remove(filename)
    os.rmdir(directory)
    assert not os.path.exists(directory)