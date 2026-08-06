import pytest
from src_0212 import task_func

def test_task_func():
    url = 'https://www.example.com/file.zip'
    destination_directory = 'tests/data'
    headers = {'accept': 'application/octet-stream'}

    extracted_files = task_func(url, destination_directory, headers)

    assert len(extracted_files) == 1
    assert extracted_files[0] == 'file.zip'

    with open(os.path.join(destination_directory, 'file.zip'), 'rb') as f:
        assert f.read() == b'file contents'