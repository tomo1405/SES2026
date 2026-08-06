import json
from datetime import datetime
from unittest.mock import MagicMock

from src_1039 import task_func


def test_task_func():
    # Mock the client_socket
    client_socket = MagicMock()

    # Call the function with the mock socket
    task_func(client_socket)

    # Get the current time and format it as a string
    current_time = str(datetime.now())

    # Create the expected response
    expected_response_data = {"message": "Hello", "time": current_time}
    expected_response = json.dumps(expected_response_data) + "\n"

    # Encode the expected response to bytes
    expected_response_bytes = expected_response.encode("utf-8")

    # Assert that the send method was called with the correct data
    client_socket.send.assert_called_once_with(expected_response_bytes)

    # Assert that the close method was called
    client_socket.close.assert_called_once()