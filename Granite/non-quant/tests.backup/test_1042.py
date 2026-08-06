import pytest
from src_1042 import task_func

def test_task_func():
    request = "GET /index.html HTTP/1.1"
    expected_response = "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello, world!"
    assert task_func(request) == expected_response

def test_task_func_file_not_found():
    request = "GET /nonexistent.html HTTP/1.1"
    expected_response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
    assert task_func(request) == expected_response

def test_task_func_bad_request():
    request = "POST /index.html HTTP/1.1"
    expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
    assert task_func(request) == expected_response