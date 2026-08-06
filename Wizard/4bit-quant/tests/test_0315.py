python
import socket
import ssl
import http.client
import pytest

def task_func(SERVER_NAME, SERVER_PORT, path):
    context = ssl.create_default_context()

    with socket.create_connection((SERVER_NAME, SERVER_PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=SERVER_NAME) as ssock:
            conn = http.client.HTTPSConnection(SERVER_NAME, SERVER_PORT, context=context)
            conn.request('GET', path)
            response = conn.getresponse()
            return response.read().decode()

def test_task_func():
    # Test case 1: Valid input
    response = task_func('www.google.com', 443, '/')
    assert response.startswith('<!doctype html>')

    # Test case 2: Invalid input
    with pytest.raises(ValueError):
        task_func('www.google.com', 443, 'invalid_path')