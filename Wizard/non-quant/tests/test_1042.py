python
import pytest
from src_1042 import task_func

def test_task_func():
    request = "GET /index.html HTTP/1.1"
    response = task_func(request)
    assert response == "HTTP/1.1 200 OK\r\nContent-Length: 123\r\n\r\n<html>...</html>"

    request = "GET /nonexistent.html HTTP/1.1"
    response = task_func(request)
    assert response == "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"

    request = "POST /index.html HTTP/1.1"
    response = task_func(request)
    assert response == "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"