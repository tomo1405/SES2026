import pytest
from src_0586 import task_func
import rsa
import os
import zipfile
from base64 import b64decode

# Mocking rsa and os modules
class MockRSA:
    @staticmethod
    def newkeys(size):
        return "public_key", "private_key"

    @staticmethod
    def encrypt(data, pub_key):
        return b"encrypted_data"

class MockOS:
    @staticmethod
    def listdir(directory):
        return ["file1.txt", "file2.txt"]

    @staticmethod
    def path.join(directory, filename):
        return os.path.join(directory, filename)

    @staticmethod
    def path.isfile(filepath):
        return True

# Patching the modules
rsa = MockRSA()
os = MockOS()

def test_task_func(tmpdir):
    # Create temporary files
    file1_path = tmpdir.join("file1.txt")
    file2_path = tmpdir.join("file2.txt")
    file1_path.write("content1")
    file2_path.write("content2")

    # Call the function
    pub_key, zipfile_name = task_func(str(tmpdir))

    # Check if the public key is correct
    assert pub_key == "public_key"

    # Check if the zipfile exists
    assert os.path.exists(zipfile_name)

    # Open the zipfile and check its contents
    with zipfile.ZipFile(zipfile_name, 'r') as zipf:
        file_names = zipf.namelist()
        assert set(file_names) == {"file1.txt", "file2.txt"}

        for file_name in file_names:
            with zipf.open(file_name) as f:
                content = f.read()
                decrypted_data = rsa.decrypt(b64decode(content), "private_key")
                if file_name == "file1.txt":
                    assert decrypted_data == b"content1"
                elif file_name == "file2.txt":
                    assert decrypted_data == b"content2"