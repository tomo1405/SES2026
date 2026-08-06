import pytest
from src_0586 import task_func

def test_task_func():
    directory = '/path/to/directory'
    pub_key, zipfile_name = task_func(directory)

    # Test that the public key is a tuple with the correct length
    assert isinstance(pub_key, tuple)
    assert len(pub_key) == 2

    # Test that the zipfile was created and is a valid zip file
    assert os.path.isfile(zipfile_name)
    with zipfile.ZipFile(zipfile_name, 'r') as zipf:
        assert zipf.namelist() != []

    # Test that the files in the directory were encrypted and the zip file contains the correct number of files
    num_files_encrypted = 0
    with zipfile.ZipFile(zipfile_name, 'r') as zipf:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as f:
                    data = f.read()
                    encrypted_data = rsa.encrypt(data, pub_key)
                    encrypted_data_b64 = b64encode(encrypted_data).decode('utf-8')
                    assert zipf.getinfo(filename).filename == filename
                    assert zipf.read(filename).decode('utf-8') == encrypted_data_b64
                    num_files_encrypted += 1
    assert num_files_encrypted == len(os.listdir(directory))