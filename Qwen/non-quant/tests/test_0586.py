import pytest
from src_0586 import task_func
import rsa
import os
import zipfile
from base64 import b64decode

def test_task_func(tmpdir):
    # Create a temporary directory and add some files to it
    temp_dir = tmpdir.mkdir("temp")
    file1 = temp_dir.join("test1.txt")
    file1.write("Hello, World!")
    file2 = temp_dir.join("test2.txt")
    file2.write("This is a test.")

    # Call the function
    pub_key, zipfile_name = task_func(str(temp_dir))

    # Check if the zipfile exists
    assert os.path.exists(zipfile_name)

    # Open the zipfile and check its contents
    with zipfile.ZipFile(zipfile_name, 'r') as zipf:
        # Check if all files are in the zipfile
        assert set(zipf.namelist()) == {'test1.txt', 'test2.txt'}

        # Decrypt and read the contents of each file
        for filename in zipf.namelist():
            with zipf.open(filename) as f:
                encrypted_data = f.read().encode('utf-8')
                decrypted_data = rsa.decrypt(b64decode(encrypted_data), pub_key)
                original_content = open(os.path.join(str(temp_dir), filename), 'rb').read()
                assert decrypted_data == original_content

    # Clean up the zipfile
    os.remove(zipfile_name)