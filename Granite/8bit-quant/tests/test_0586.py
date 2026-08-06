import pytest
from src_0586 import task_func

def test_task_func():
    directory = '/path/to/directory'
    pub_key, zipfile_name = task_func(directory)

    # Test that the public key is a tuple with two elements
    assert isinstance(pub_key, tuple) and len(pub_key) == 2

    # Test that the zipfile name is a string
    assert isinstance(zipfile_name, str)

    # Test that the zipfile exists in the specified directory
    zipfile_path = os.path.join(directory, zipfile_name)
    assert os.path.exists(zipfile_path)

    # Test that the zipfile is a valid zip file
    with zipfile.ZipFile(zipfile_path, 'r') as zipf:
        assert zipfile.is_zipfile(zipfile_path)

        # Test that each file in the zipfile can be decrypted with the private key
        for filename in zipf.namelist():
            with zipf.open(filename) as f:
                encrypted_data = f.read()
                data = rsa.decrypt(b64decode(encrypted_data), priv_key)
                assert isinstance(data, bytes)