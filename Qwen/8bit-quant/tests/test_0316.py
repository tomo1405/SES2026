from unittest.mock import MagicMock, patch

import pytest
from src_0316 import task_func


# Mocking the SendGridAPIClient and Mail classes
class MockSendGridAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def send(self, message):
        mock_response = MagicMock()
        mock_response.status_code = 200
        return mock_response

class MockMail:
    def __init__(self, from_email, to_emails, subject, plain_text_content):
        self.from_email = from_email
        self.to_emails = to_emails
        self.subject = subject
        self.plain_text_content = plain_text_content

@pytest.fixture
def mock_sendgrid_client():
    with patch('src_0316.SendGridAPIClient', new=MockSendGridAPIClient) as mock_client:
        yield mock_client

@pytest.fixture
def mock_mail():
    with patch('src_0316.Mail', new=MockMail) as mock_mail:
        yield mock_mail

def test_task_func_success(tmp_path, mock_sendgrid_client, mock_mail):
    # Create a temporary directory and add some files to it
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / "file1.txt").touch()
    (dir_path / "file2.txt").touch()

    api_key = "fake_api_key"
    recipient_email = "test@example.com"

    result = task_func(str(dir_path), api_key, recipient_email)

    assert result is True
    mock_sendgrid_client.assert_called_once_with(api_key)
    mock_mail.assert_called_once_with(
        from_email='from_email@example.com',
        to_emails=recipient_email,
        subject=f'Directory Listing for {str(dir_path)}',
        plain_text_content='file1.txt, file2.txt'
    )

def test_task_func_directory_not_exists(mock_sendgrid_client, mock_mail):
    dir_path = "/nonexistent_directory"
    api_key = "fake_api_key"
    recipient_email = "test@example.com"

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(dir_path, api_key, recipient_email)

    assert str(excinfo.value) == f"Directory '{dir_path}' does not exist."

def test_task_func_sendgrid_error(tmp_path, mock_sendgrid_client, mock_mail):
    # Create a temporary directory and add some files to it
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / "file1.txt").touch()
    (dir_path / "file2.txt").touch()

    api_key = "fake_api_key"
    recipient_email = "test@example.com"

    # Simulate an HTTP error
    mock_sendgrid_client.return_value.send.side_effect = HTTPError(response="Simulated HTTP Error")

    with pytest.raises(HTTPError) as excinfo:
        task_func(str(dir_path), api_key, recipient_email)

    assert str(excinfo.value) == "Simulated HTTP Error"