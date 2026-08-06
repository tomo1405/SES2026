import pytest
from src_0204 import task_func
import json

def test_task_func_no_input():
    assert task_func() == []

def test_task_func_invalid_json():
    assert task_func('{"invalid": json}') == []

def test_task_func_missing_recipient():
    assert task_func('{"names": ["Alice", "Bob"]}') == []

def test_task_func_missing_names():
    assert task_func('{"recipient": "test@example.com"}') == []

def test_task_func_empty_names():
    assert task_func('{"recipient": "test@example.com", "names": []}') == []

def test_task_func_valid_input(mocker):
    mock_smtp = mocker.patch('src_0204.smtplib.SMTP')
    mock_server = mock_smtp.return_value
    mock_server.starttls.return_value = None
    mock_server.login.return_value = None
    mock_server.sendmail.return_value = None
    mock_server.quit.return_value = None

    input_data = '{"recipient": "test@example.com", "names": ["Alice", "Bob"]}'
    result = task_func(input_data)

    assert result == ["Alice", "Bob"]
    mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
    mock_server.starttls.assert_called_once()
    mock_server.login.assert_called_once_with("your.email@gmail.com", "your.password")
    mock_server.sendmail.assert_called_once_with("your.email@gmail.com", "test@example.com", 'Subject: Extracted Names\n\nAlice\nBob')
    mock_server.quit.assert_called_once()

def test_task_func_custom_smtp(mocker):
    def custom_smtp(server, port):
        return smtplib.SMTP(server, port)

    mock_smtp = mocker.patch('src_0204.smtplib.SMTP')
    mock_server = mock_smtp.return_value
    mock_server.starttls.return_value = None
    mock_server.login.return_value = None
    mock_server.sendmail.return_value = None
    mock_server.quit.return_value = None

    input_data = '{"recipient": "test@example.com", "names": ["Alice", "Bob"]}'
    result = task_func(input_data, smtp=custom_smtp)

    assert result == ["Alice", "Bob"]
    mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
    mock_server.starttls.assert_called_once()
    mock_server.login.assert_called_once_with("your.email@gmail.com", "your.password")
    mock_server.sendmail.assert_called_once_with("your.email@gmail.com", "test@example.com", 'Subject: Extracted Names\n\nAlice\nBob')
    mock_server.quit.assert_called_once()