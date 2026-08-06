python
import pytest
from src_0212 import task_func

def test_task_func():
    url = 'https://www.example.com/file.zip'
    destination_directory = '/tmp'
    headers = {
        'accept': 'application/octet-stream'
    }
    expected_files = ['file1.txt', 'file2.txt']

    # Test with headers
    extracted_files = task_func(url, destination_directory, headers)
    assert extracted_files == expected_files

    # Test without headers
    extracted_files = task_func(url, destination_directory)
    assert extracted_files == expected_files