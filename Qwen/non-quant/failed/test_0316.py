import pytest
from src_0316 import task_func
from unittest.mock import patch, MagicMock

@patch('os.listdir')
@patch('sendgrid.SendGridAPIClient')
def test_task_func_success(mock_sendgrid_client, mock_listdir):
    # Arrange
    dir = '/test/dir'
    api_key = 'test_api_key'
    recipient_email = 'test@example.com'
    mock_listdir.return_value = ['file1.txt', 'file2.txt']
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_sendgrid_client.return_value.send.return_value = mock_response

    # Act
    result = task_func(dir, api_key, recipient_email)

    # Assert
    assert result is True
    mock_listdir.assert_called_once_with(dir)
    mock_sendgrid_client.assert_called_once_with(api_key)
    mock_sendgrid_client.return_value.send.assert_called_once()

@patch('os.listdir')
def test_task_func_directory_not_found(mock_listdir):
    # Arrange
    dir = '/nonexistent/dir'
    api_key = 'test_api_key'
    recipient_email = 'test@example.com'
    mock_listdir.side_effect = FileNotFoundError()

    # Act & Assert
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(dir, api_key, recipient_email)
    assert str(excinfo.value) == f"Directory '{dir}' does not exist."

@patch('os.listdir')
@patch('sendgrid.SendGridAPIClient')
def test_task_func_http_error(mock_sendgrid_client, mock_listdir):
    # Arrange
    dir = '/test/dir'
    api_key = 'test_api_key'
    recipient_email = 'test@example.com'
    mock_listdir.return_value = ['file1.txt', 'file2.txt']
    mock_sendgrid_client.return_value.send.side_effect = HTTPError("HTTP Error")

    # Act & Assert
    with pytest.raises(HTTPError) as excinfo:
        task_func(dir, api_key, recipient_email)
    assert str(excinfo.value) == "HTTP Error"

@patch('os.listdir')
@patch('sendgrid.SendGridAPIClient')
def test_task_func_general_exception(mock_sendgrid_client, mock_listdir):
    # Arrange
    dir = '/test/dir'
    api_key = 'test_api_key'
    recipient_email = 'test@example.com'
    mock_listdir.return_value = ['file1.txt', 'file2.txt']
    mock_sendgrid_client.return_value.send.side_effect = Exception("General Error")

    # Act & Assert
    with pytest.raises(Exception) as excinfo:
        task_func(dir, api_key, recipient_email)
    assert str(excinfo.value) == "General Error"