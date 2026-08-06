import base64
import hashlib
import os

from src_0645 import task_func


def test_task_func():
    # Define test parameters
    filename = "test_file.txt"
    data = "Hello, World!"
    password = "secure_password"

    # Call the function
    encrypted_data = task_func(filename, data, password)

    # Check if the file was created
    assert os.path.exists(filename), "The file should be created."

    # Read the content of the file
    with open(filename, 'r') as f:
        file_content = f.read()

    # Check if the content matches the encrypted data
    assert file_content == encrypted_data, "The file content should match the encrypted data."

    # Verify encryption logic
    key = hashlib.sha256(password.encode()).digest()
    encrypted_bytes = [byte ^ key[i % len(key)] for i, byte in enumerate(data.encode())]
    expected_encrypted = base64.b64encode(bytes(encrypted_bytes)).decode()
    assert encrypted_data == expected_encrypted, "The encryption logic should produce the correct result."

    # Clean up
    os.remove(filename)

def test_task_func_directory_creation():
    # Define test parameters
    filename = "test_dir/test_file.txt"
    data = "Hello, World!"
    password = "secure_password"

    # Call the function
    task_func(filename, data, password)

    # Check if the directory was created
    directory = os.path.dirname(filename)
    assert os.path.exists(directory), "The directory should be created."

    # Clean up
    os.remove(filename)
    os.rmdir(os.path.dirname(filename))