import pytest
from src_1043 import task_func

def test_task_func():
    client_socket = ...  # create a mock client socket
    task_func(client_socket)
    assert client_socket.recv.called_once_with(BUFFER_SIZE)
    assert client_socket.send.called_once_with(response.encode("utf-8"))
    assert client_socket.close.called_once()