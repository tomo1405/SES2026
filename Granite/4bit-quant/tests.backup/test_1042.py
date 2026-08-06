import re
import os
import pytest

def task_func(request):
    match = re.match(r"^GET /([\w\.\-]+) HTTP/1\.1$", request)
    if match:
        file_name = match.group(1)
        if os.path.exists(file_name):
            try:
                with open(file_name, "rb") as file:
                    content = file.read()
                    response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(content)}\r\n\r\n{content.decode('utf-8')}"
            except Exception:
                response = (
                    "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"
                )
        else:
            response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
    else:
        response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"

    return response

def test_task_func():
    request = "GET /index.html HTTP/1.1"
    expected_response = "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello, World!"
    assert task_func(request) == expected_response

    request = "GET /not_found.html HTTP/1.1"
    expected_response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
    assert task_func(request) == expected_response

    request = "POST /index.html HTTP/1.1"
    expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
    assert task_func(request) == expected_response

if __name__ == "__main__":
    pytest.main()