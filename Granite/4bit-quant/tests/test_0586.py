import pytest
from src_0586 import task_func

def test_task_func():
    directory = '/path/to/directory'
    pub_key, zipfile_name = task_func(directory)

    # Test if the public key is a tuple with two elements
    assert isinstance(pub_key, tuple) and len(pub_key) == 2

    # Test if the zipfile exists
    assert os.path.exists(zipfile_name)

    # Test if the zipfile contains encrypted files
    with zipfile.ZipFile(zipfile_name, 'r') as zipf:
        encrypted_files = zipf.namelist()
        assert len(encrypted_files) > 0