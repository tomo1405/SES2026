import pytest
from src_0586 import task_func
import os
import zipfile
import rsa
import tempfile

def test_task_func():
    # Create a temporary directory and add some files to it
    temp_dir = tempfile.mkdtemp()
    file_paths = [
        os.path.join(temp_dir, 'file1.txt'),
        os.path.join(temp_dir, 'file2.txt')
    ]
    with open(file_paths[0], 'wb') as f:
        f.write(b'This is the content of file1.')
    with open(file_paths[1], 'wb') as f:
        f.write(b'This is the content of file2.')

    # Call the function
    pub_key, zipfile_name = task_func(temp_dir)

    # Check if the public key is generated correctly
    assert isinstance(pub_key, rsa.PublicKey)

    # Check if the zipfile exists
    assert os.path.exists(zipfile_name)

    # Check if the zipfile contains the correct number of files
    with zipfile.ZipFile(zipfile_name, 'r') as zipf:
        assert len(zipf.namelist()) == 2

    # Clean up
    os.remove(zipfile_name)
    os.rmdir(temp_dir)

# Run the test
if __name__ == '__main__':
    pytest.main()