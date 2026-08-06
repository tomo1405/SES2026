import pytest
from src_0204 import task_func

def test_task_func_no_input():
    assert task_func() == []

def test_task_func_invalid_json():
    assert task_func(input_data="invalid json") == []

def test_task_func_missing_recipient():
    assert task_func(input_data='{"names": ["Alice", "Bob"]}') == []

def test_task_func_missing_names():
    assert task_func(input_data='{"recipient": "test@example.com"}') == []

def test_task_func_empty_names():
    assert task_func(input_data='{"recipient": "test@example.com", "names": []}') == []

def test_task_func_valid_input(mocker):
    mock_smtp = mocker.patch('src_0204.smtplib.SMTP')
    input_data = '{"recipient": "test@example.com", "names": ["Alice", "Bob"]}'
    result = task_func(input_data=input_data)
    assert result == ["Alice", "Bob"]
    mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
    mock_smtp_instance = mock_smtp.return_value
    mock_smtp_instance.starttls.assert_called_once()
    mock_smtp_instance.login.assert_called_once_with("your.email@gmail.com", "your.password")
    mock_smtp_instance.sendmail.assert_called_once_with("your.email@gmail.com", "test@example.com", 'Subject: Extracted Names\n\nAlice\nBob')
    mock_smtp_instance.quit.assert_called_once()

def test_task_func_custom_smtp(mocker):
    mock_smtp = mocker.patch('src_0204.smtp')
    input_data = '{"recipient": "test@example.com", "names": ["Alice", "Bob"]}'
    result = task_func(input_data=input_data, smtp=mock_smtp)
    assert result == ["Alice", "Bob"]
    mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
    mock_smtp_instance = mock_smtp.return_value
    mock_smtp_instance.starttls.assert_called_once()
    mock_smtp_instance.login.assert_called_once_with("your.email@gmail.com", "your.password")
    mock_smtp_instance.sendmail.assert_called_once_with("your.email@gmail.com", "test@example.com", 'Subject: Extracted Names\n\nAlice\nBob')
    mock_smtp_instance.quit.assert_called_once()