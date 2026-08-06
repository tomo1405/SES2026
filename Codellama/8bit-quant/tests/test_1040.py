import pytest
from src_1040 import task_func

def test_task_func_valid_file():
    client_socket = None
    cert_file = "cert.pem"
    key_file = "key.pem"
    buffer_size = 1024
    request = "test_file.txt"
    response = "098f6bcd4621d373cade4e832627b4f6"

    with pytest.raises(Exception) as e:
        task_func(client_socket, cert_file, key_file, buffer_size)

    assert e.value.args[0] == "Error: File not found"

def test_task_func_invalid_file():
    client_socket = None
    cert_file = "cert.pem"
    key_file = "key.pem"
    buffer_size = 1024
    request = "invalid_file.txt"
    response = "Error: File not found"

    with pytest.raises(Exception) as e:
        task_func(client_socket, cert_file, key_file, buffer_size)

    assert e.value.args[0] == response