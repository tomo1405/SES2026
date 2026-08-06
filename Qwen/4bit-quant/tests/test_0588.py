import pytest
from src_0588 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary file with some content
    with tempfile.NamedTemporaryFile(delete=False, mode='w+b') as temp_file:
        temp_file.write(b'This is a test file.')
        temp_file_path = temp_file.name

    try:
        # Call the function to be tested
        pub_key, encrypted_file, encrypted_key_file = task_func(temp_file_path)

        # Check if the output files exist
        assert os.path.exists(encrypted_file)
        assert os.path.exists(encrypted_key_file)

        # Check if the public key is not None
        assert pub_key is not None

        # Read the contents of the encrypted files
        with open(encrypted_file, 'rb') as f:
            encrypted_data = f.read()

        with open(encrypted_key_file, 'rb') as f:
            encrypted_key_data = f.read()

        # Check if the encrypted data and key are not empty
        assert len(encrypted_data) > 0
        assert len(encrypted_key_data) > 0

    finally:
        # Clean up temporary files
        os.remove(temp_file_path)
        os.remove(encrypted_file)
        os.remove(encrypted_key_file)