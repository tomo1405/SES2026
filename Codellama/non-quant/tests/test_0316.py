import pytest
from src_0316 import task_func


def test_task_func_valid_dir():
    dir = 'test_dir'
    api_key = 'test_api_key'
    recipient_email = 'test@example.com'
    file_list = ['file1.txt', 'file2.txt']

    with pytest.raises(FileNotFoundError):
        task_func(dir, api_key, recipient_email)

    with pytest.raises(HTTPError):
        task_func(dir, api_key, recipient_email)

    with pytest.raises(Exception):
        task_func(dir, api_key, recipient_email)