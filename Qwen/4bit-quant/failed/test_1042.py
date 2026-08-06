import pytest
from src_1042 import task_func
import os
import tempfile

def test_task_func_valid_request():
    # Create a temporary file and write some data to it
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, World!")
        temp_file.flush()
        file_name = temp_file.name

    # Construct a valid GET request
    request = f"GET /{file_name} HTTP/1.1"

    # Call the function
    response = task_func(request)

    # Check the response
    assert response.startswith("HTTP/1.1 200 OK")
    assert "Content-Length: 13" in response
    assert "Hello, World!" in response

    # Clean up the temporary file
    os.remove(file_name)

def test_task_func_file_not_found():
    # Construct a request for a non-existent file
    request = "GET /non_existent_file.txt HTTP/1.1"

    # Call the function
    response = task_func(request)

    # Check the response
    assert response == "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"

def test_task_func_invalid_request():
    # Construct an invalid request
    request = "POST /file.txt HTTP/1.1"

    # Call the function
    response = task_func(request)

    # Check the response
    assert response == "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"

def test_task_func_server_error():
    # Create a temporary file that cannot be read
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "unreadable_file.txt")
        with open(file_path, "wb") as file:
            file.write(b"Hello, World!")
        os.chmod(file_path, 0)  # Make the file unreadable

        # Construct a valid GET request
        request = f"GET /{os.path.basename(file_path)} HTTP/1.1"

        # Call the function
        response = task_func(request)

        # Check the response
        assert response == "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"

        # Clean up the temporary directory
        os.chmod(file_path, 0o644)  # Restore file permissions