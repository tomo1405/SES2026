import pytest
from src_1042 import task_func
import os
import tempfile

def test_task_func_valid_request():
    # Create a temporary file and write some data to it
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, World!")
        temp_file_name = temp_file.name

    # Construct a valid HTTP GET request
    request = f"GET {temp_file_name} HTTP/1.1"

    # Call the function with the request
    response = task_func(request)

    # Check that the response is correct
    expected_response = (
        f"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!"
    )
    assert response == expected_response

    # Clean up the temporary file
    os.remove(temp_file_name)

def test_task_func_file_not_found():
    # Construct a request for a non-existent file
    request = "GET non_existent_file.txt HTTP/1.1"

    # Call the function with the request
    response = task_func(request)

    # Check that the response is correct
    expected_response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
    assert response == expected_response

def test_task_func_invalid_request():
    # Construct an invalid HTTP request
    request = "POST /file.txt HTTP/1.1"

    # Call the function with the request
    response = task_func(request)

    # Check that the response is correct
    expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
    assert response == expected_response

def test_task_func_internal_server_error():
    # Create a temporary file that cannot be read
    temp_file_name = "/path/to/non_readable_file"

    # Construct a valid HTTP GET request
    request = f"GET {temp_file_name} HTTP/1.1"

    # Call the function with the request
    response = task_func(request)

    # Check that the response is correct
    expected_response = (
        "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"
    )
    assert response == expected_response