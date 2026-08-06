import pytest
from src_1042 import task_func
import os
import tempfile

def test_valid_get_request():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, World!")
        temp_file_name = temp_file.name

    request = f"GET {temp_file_name} HTTP/1.1"
    expected_response = (
        f"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!"
    )
    assert task_func(request) == expected_response

    os.unlink(temp_file_name)

def test_file_not_found():
    request = "GET non_existent_file.txt HTTP/1.1"
    expected_response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
    assert task_func(request) == expected_response

def test_invalid_request():
    request = "POST /file.txt HTTP/1.1"
    expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
    assert task_func(request) == expected_response

def test_internal_server_error():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_name = temp_file.name

    request = f"GET {temp_file_name} HTTP/1.1"
    expected_response = (
        "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"
    )

    # Simulate an error by renaming the file
    os.rename(temp_file_name, temp_file_name + ".bak")

    assert task_func(request) == expected_response

    # Clean up
    os.remove(temp_file_name + ".bak")