import pytest
from src_1043 import task_func

def test_task_func():
    client_socket = pytest.fixture.socket()
    request = "Hello, World!"
    client_socket.send(request.encode("utf-8"))
    task_func(client_socket)
    response = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    assert response == "Message sent."
    client_socket.close()