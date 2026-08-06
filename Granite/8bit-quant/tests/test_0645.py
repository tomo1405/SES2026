import os

import pytest
from src_0645 import task_func


def test_task_func():
    filename = "test.txt"
    data = "This is a test"
    password = "password"

    encrypted = task_func(filename, data, password)

    assert encrypted == "encrypted_data"  # Replace with the expected encrypted data

def test_file_created(tmpdir):
    filename = str(tmpdir.join("test.txt"))
    data = "This is a test"
    password = "password"

    task_func(filename, data, password)

    assert os.path.exists(filename)

def test_invalid_password():
    filename = "test.txt"
    data = "This is a test"
    password = "wrong_password"

    with pytest.raises(ValueError) as excinfo:
        task_func(filename, data, password)

    assert "Invalid password" in str(excinfo.value)