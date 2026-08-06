import pytest
from src_1039 import task_func
from unittest.mock import Mock, patch
import json
from datetime import datetime

@pytest.fixture
def mock_client_socket():
    return Mock()

def test_task_func_sends_correct_response(mock_client_socket):
    # Arrange
    expected_message = "Hello"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expected_response = json.dumps({"message": expected_message, "time": current_time}) + "\n"
    
    # Act
    task_func(mock_client_socket)
    
    # Assert
    mock_client_socket.send.assert_called_once_with(expected_response.encode("utf-8"))
    mock_client_socket.close.assert_called_once()

@patch('src_1039.datetime')
def test_task_func_includes_current_time(mock_datetime, mock_client_socket):
    # Arrange
    mock_now = Mock()
    mock_datetime.now.return_value = mock_now
    expected_time_str = mock_now.strftime.return_value
    expected_response = json.dumps({"message": "Hello", "time": expected_time_str}) + "\n"
    
    # Act
    task_func(mock_client_socket)
    
    # Assert
    mock_datetime.now.assert_called_once()
    mock_now.strftime.assert_called_once_with("%Y-%m-%d %H:%M:%S")
    mock_client_socket.send.assert_called_once_with(expected_response.encode("utf-8"))
    mock_client_socket.close.assert_called_once()