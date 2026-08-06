import pytest
from src_0212 import task_func

def test_task_func():
    url = 'https://example.com/myzipfile.zip'
    destination_directory = '/path/to/destination'
    headers = {
        'accept': 'application/octet-stream'
    }

    extracted_files = task_func(url, destination_directory, headers)

    assert isinstance(extracted_files, list)
    assert len(extracted_files) > 0
    for file in extracted_files:
        assert os.path.isfile(os.path.join(destination_directory, file))