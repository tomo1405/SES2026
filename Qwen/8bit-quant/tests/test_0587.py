import os
import tempfile

import rsa
from src_0587 import task_func


def test_task_func():
    # Create a temporary file with some content
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, World!")
        temp_file_path = temp_file.name

    try:
        # Call the function with the temporary file path
        pub_key, encrypted_file, encrypted_key_file = task_func(temp_file_path)

        # Check if the encrypted file exists and is not empty
        assert os.path.exists(encrypted_file)
        assert os.path.getsize(encrypted_file) > 0

        # Check if the encrypted key file exists and is not empty
        assert os.path.exists(encrypted_key_file)
        assert os.path.getsize(encrypted_key_file) > 0

        # Check if the public key is of the correct type
        assert isinstance(pub_key, rsa.PublicKey)

    finally:
        # Clean up the temporary files
        os.remove(temp_file_path)
        os.remove(encrypted_file)
        os.remove(encrypted_key_file)