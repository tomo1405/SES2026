import pytest
from src_1040 import task_func

def test_task_func_valid_file():
    client_socket = None
    cert_file = "cert.pem"
    key_file = "key.pem"
    buffer_size = 1024
    request = "test_file.txt"
    response = task_func(client_socket, cert_file, key_file, buffer_size, request)
    assert response == "File not found"

def test_task_func_invalid_file():
    client_socket = None
    cert_file = "cert.pem"
    key_file = "key.pem"
    buffer_size = 1024
    request = "invalid_file.txt"
    response = task_func(client_socket, cert_file, key_file, buffer_size, request)
    assert response == "File not found"

def test_task_func_valid_file_with_hash():
    client_socket = None
    cert_file = "cert.pem"
    key_file = "key.pem"
    buffer_size = 1024
    request = "test_file.txt"
    response = task_func(client_socket, cert_file, key_file, buffer_size, request)
    assert response == "File not found"

def test_task_func_invalid_file_with_hash():
    client_socket = None
    cert_file = "cert.pem"
    key_file = "key.pem"
    buffer_size = 1024
    request = "invalid_file.txt"
    response = task_func(client_socket, cert_file, key_file, buffer_size, request)
    assert response == "File not found"