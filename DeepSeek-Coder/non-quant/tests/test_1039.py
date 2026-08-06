import pytest
from unittest.mock import patch
from src_1039 import task_func

@pytest.fixture
def mock_client_socket():
    class MockSocket:
        def __init__(self):
            self.sent_data = b''

        def send(self, data):
            self.sent_data = data

        def close(self):
            pass

    return MockSocket()

@pytest.fixture
def mock_client_socket():
    return mock_client_socket()

def test_task_func(mock_client_socket):
    client_socket = mock_client_socket
    task_func(client_socket)
    assert client_socket.sent_data == b'{"message": "Hello", "time": "2023-04-14T00:00:00"}\n'