import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from src_1041 import task_func

@patch('src_1041.socket')
@patch('src_1041.select.select')
@patch('src_1041.queue.Queue')
def test_task_func(mock_queue, mock_select, mock_socket):
    # Mock the socket behavior
    mock_server = MagicMock(spec=socket.socket)
    mock_server.getsockname.return_value = ("localhost", 12345)
    mock_socket.socket.return_value = mock_server

    # Mock the select behavior
    mock_readable = [mock_server]
    mock_writable = []
    mock_select.return_value = (mock_readable, mock_writable, [])

    # Mock the queue behavior
    mock_queue_instance = MagicMock(spec=queue.Queue)
    mock_queue.return_value = mock_queue_instance

    # Call the function
    result = task_func()

    # Assertions
    mock_socket.socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
    mock_server.setblocking.assert_called_once_with(0)
    mock_server.bind.assert_called_once_with(("localhost", 12345))
    mock_server.listen.assert_called_once_with(5)
    mock_select.assert_called_once_with([mock_server], [], [mock_server], 1)
    assert result == "Server started on localhost:12345. Ran for 5 seconds."

@patch('src_1041.socket')
@patch('src_1041.select.select')
@patch('src_1041.queue.Queue')
def test_task_func_with_client_connection(mock_queue, mock_select, mock_socket):
    # Mock the socket behavior
    mock_server = MagicMock(spec=socket.socket)
    mock_server.getsockname.return_value = ("localhost", 12345)
    mock_socket.socket.return_value = mock_server

    mock_connection = MagicMock(spec=socket.socket)
    mock_server.accept.return_value = (mock_connection, None)

    # Mock the select behavior
    mock_readable = [mock_server, mock_connection]
    mock_writable = []
    mock_select.return_value = (mock_readable, mock_writable, [])

    # Mock the queue behavior
    mock_queue_instance = MagicMock(spec=queue.Queue)
    mock_queue.return_value = mock_queue_instance

    # Mock the recv behavior
    mock_connection.recv.return_value = b"Hello, World!"

    # Call the function
    with patch('src_1041.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime(2023, 1, 1, 12, 0, 0)
        result = task_func(run_duration=0)

    # Assertions
    mock_server.accept.assert_called_once()
    mock_connection.setblocking.assert_called_once_with(0)
    mock_connection.recv.assert_called_once_with(1024)
    mock_queue_instance.put.assert_called_once_with("2023-01-01 12:00:00: Hello, World!")
    assert result == "Server started on localhost:12345. Ran for 0 seconds."