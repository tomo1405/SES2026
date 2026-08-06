import pytest
from unittest.mock import patch, MagicMock
from src_1041 import task_func

@pytest.fixture
def mock_socket():
    with patch('src_1041.socket') as mock_socket:
        yield mock_socket

@pytest.fixture
def mock_select():
    with patch('src_1041.select') as mock_select:
        yield mock_select

@pytest.fixture
def mock_datetime():
    with patch('src_1041.datetime') as mock_datetime:
        yield mock_datetime

def test_task_func_basic(mock_socket, mock_select, mock_datetime):
    mock_datetime.now.return_value = datetime(2023, 1, 1, 12, 0, 0)
    mock_datetime.now.return_value + timedelta(seconds=5) = datetime(2023, 1, 1, 12, 0, 5)

    mock_server = MagicMock()
    mock_socket.socket.return_value = mock_server
    mock_server.setblocking.return_value = None
    mock_server.bind.return_value = None
    mock_server.listen.return_value = None
    mock_server.accept.return_value = (MagicMock(), ("client_address", 12346))

    mock_select.select.side_effect = [
        ([mock_server], [], []),
        ([mock_server], [], []),
        ([], [], []),
        ([], [], [])
    ]

    result = task_func(server_address="localhost", server_port=12345, buffer_size=1024, run_duration=5)

    assert result == "Server started on localhost:12345. Ran for 5 seconds."

def test_task_func_client_connection(mock_socket, mock_select, mock_datetime):
    mock_datetime.now.return_value = datetime(2023, 1, 1, 12, 0, 0)
    mock_datetime.now.return_value + timedelta(seconds=5) = datetime(2023, 1, 1, 12, 0, 5)

    mock_server = MagicMock()
    mock_socket.socket.return_value = mock_server
    mock_server.setblocking.return_value = None
    mock_server.bind.return_value = None
    mock_server.listen.return_value = None
    mock_server.accept.return_value = (MagicMock(), ("client_address", 12346))

    mock_client = MagicMock()
    mock_server.accept.return_value = (mock_client, ("client_address", 12346))
    mock_client.recv.return_value = b"test_message"

    mock_select.select.side_effect = [
        ([mock_server], [], []),
        ([mock_client], [], []),
        ([], [], []),
        ([], [], [])
    ]

    result = task_func(server_address="localhost", server_port=12345, buffer_size=1024, run_duration=5)

    assert result == "Server started on localhost:12345. Ran for 5 seconds."
    mock_client.sendall.assert_called_once_with(b'2023-01-01 12:00:00: test_message')

def test_task_func_client_disconnection(mock_socket, mock_select, mock_datetime):
    mock_datetime.now.return_value = datetime(2023, 1, 1, 12, 0, 0)
    mock_datetime.now.return_value + timedelta(seconds=5) = datetime(2023, 1, 1, 12, 0, 5)

    mock_server = MagicMock()
    mock_socket.socket.return_value = mock_server
    mock_server.setblocking.return_value = None
    mock_server.bind.return_value = None
    mock_server.listen.return_value = None
    mock_server.accept.return_value = (MagicMock(), ("client_address", 12346))

    mock_client = MagicMock()
    mock_server.accept.return_value = (mock_client, ("client_address", 12346))
    mock_client.recv.return_value = b""

    mock_select.select.side_effect = [
        ([mock_server], [], []),
        ([mock_client], [], []),
        ([], [], []),
        ([], [], [])
    ]

    result = task_func(server_address="localhost", server_port=12345, buffer_size=1024, run_duration=5)

    assert result == "Server started on localhost:12345. Ran for 5 seconds."
    mock_client.close.assert_called_once()