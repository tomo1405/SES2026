import pytest
from src_1042 import task_func

def test_task_func():
    # Test case 1: valid request
    request = "GET /index.html HTTP/1.1"
    expected_response = "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello, world!"
    assert task_func(request) == expected_response

    # Test case 2: invalid request
    request = "GET / HTTP/1.1"
    expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
    assert task_func(request) == expected_response

    # Test case 3: file not found
    request = "GET /not_found.html HTTP/1.1"
    expected_response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
    assert task_func(request) == expected_response

    # Test case 4: internal server error
    request = "GET /error.html HTTP/1.1"
    expected_response = "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"
    assert task_func(request) == expected_response