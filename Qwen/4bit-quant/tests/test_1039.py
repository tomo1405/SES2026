import json
from datetime import datetime
from unittest.mock import Mock

from src_1039 import task_func


def test_task_func_sends_correct_response():
    # Create a mock socket
    mock_socket = Mock()
    
    # Call the function with the mock socket
    task_func(mock_socket)
    
    # Check that the send method was called with the correct data
    expected_response = json.dumps({"message": "Hello", "time": str(datetime.now())}) + "\n"
    mock_socket.send.assert_called_once_with(expected_response.encode("utf-8"))
    
    # Check that the close method was called
    mock_socket.close.assert_called_once()

def test_task_func_closes_socket():
    # Create a mock socket
    mock_socket = Mock()
    
    # Call the function with the mock socket
    task_func(mock_socket)
    
    # Check that the close method was called
    mock_socket.close.assert_called_once()