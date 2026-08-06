import pytest
from src_0212 import task_func
import os
import requests

@pytest.fixture
def setup():
    url = "http://example.com/file.zip"
    destination_directory = "./test_directory"
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    return url, destination_directory

def test_task_func(setup):
    url, destination_directory = setup
    result = task_func(url, destination_directory)
    assert isinstance(result, list), "The result should be a list"
    assert len(result) > 0, "The result should contain files"
    for file in result:
        assert os.path.isfile(os.path.join(destination_directory, file)), f"File {file} does not exist"

    # Clean up
    for file in result:
        os.remove(os.path.join(destination_directory, file))
    os.rmdir(destination_directory)