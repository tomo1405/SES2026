import pytest
from src_0586 import task_func

def test_task_func():
    directory = 'path/to/directory'
    pub_key, zipfile_name = task_func(directory)
    assert pub_key is not None
    assert zipfile_name is not None
    assert os.path.exists(zipfile_name)
    with zipfile.ZipFile(zipfile_name, 'r') as zipf:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as f:
                    data = f.read()
                    encrypted_data = rsa.encrypt(data, pub_key)
                    assert zipf.read(filename) == b64encode(encrypted_data).decode('utf-8')