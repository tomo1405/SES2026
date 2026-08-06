import pytest
from src_1042 import task_func

def test_task_func_valid_request():
    request = "GET /example.txt HTTP/1.1"
    expected_response = "HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n"
    assert task_func(request) == expected_response

def test_task_func_invalid_request():
    request = "GET /nonexistent.txt HTTP/1.1"
    expected_response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
    assert task_func(request) == expected_response

def test_task_func_bad_request():
    request = "GET /invalidrequest HTTP/1.1"
    expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
    assert task_func(request) == expected_response

def test_task_func_internal_error():
    request = "GET /nonexistent.txt HTTP/1.1"
    expected_response = "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"
    assert task_func(request) == expected_response