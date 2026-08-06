from unittest.mock import MagicMock, patch

from src_0204 import task_func


@patch('src_0204.smtplib.SMTP')
def test_task_func_valid_input(mock_smtp):
    input_data = '{"recipient": "test@example.com", "names": ["Alice", "Bob"]}'
    expected_output = ["Alice", "Bob"]
    
    mock_smtp_instance = MagicMock()
    mock_smtp.return_value = mock_smtp_instance
    mock_smtp_instance.starttls.return_value = None
    mock_smtp_instance.login.return_value = None
    mock_smtp_instance.sendmail.return_value = None
    mock_smtp_instance.quit.return_value = None
    
    result = task_func(input_data)
    
    assert result == expected_output
    mock_smtp.assert_called_once_with(SMTP_SERVER, SMTP_PORT)
    mock_smtp_instance.starttls.assert_called_once()
    mock_smtp_instance.login.assert_called_once_with(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mock_smtp_instance.sendmail.assert_called_once_with(EMAIL_ADDRESS, "test@example.com", 'Subject: Extracted Names\n\nAlice\nBob')
    mock_smtp_instance.quit.assert_called_once()

@patch('src_0204.smtplib.SMTP')
def test_task_func_invalid_json(mock_smtp):
    input_data = '{"recipient": "test@example.com", "names": [1, 2]}'
    expected_output = []
    
    result = task_func(input_data)
    
    assert result == expected_output
    mock_smtp.assert_not_called()

def test_task_func_no_recipient(mock_smtp):
    input_data = '{"names": ["Alice", "Bob"]}'
    expected_output = []
    
    result = task_func(input_data)
    
    assert result == expected_output
    mock_smtp.assert_not_called()

def test_task_func_no_names(mock_smtp):
    input_data = '{"recipient": "test@example.com"}'
    expected_output = []
    
    result = task_func(input_data)
    
    assert result == expected_output
    mock_smtp.assert_not_called()

def test_task_func_empty_input(mock_smtp):
    input_data = None
    expected_output = []
    
    result = task_func(input_data)
    
    assert result == expected_output
    mock_smtp.assert_not_called()