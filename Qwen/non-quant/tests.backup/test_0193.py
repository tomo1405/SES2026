import pytest
from src_0193 import task_func
import smtplib
from unittest.mock import Mock, patch

@pytest.fixture
def mock_smtp():
    with patch('smtplib.SMTP') as mock_smtp:
        yield mock_smtp

def test_task_func(mock_smtp):
    # Arrange
    text = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
    expected_names = ["Josie Smith", "Mugsy Dog Smith"]
    
    # Act
    names = task_func(text=text, smtp=Mock())
    
    # Assert
    assert names == expected_names
    mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
    mock_smtp.return_value.starttls.assert_called_once()
    mock_smtp.return_value.login.assert_called_once_with("your.email@gmail.com", "your.password")
    mock_smtp.return_value.sendmail.assert_called_once_with("your.email@gmail.com", "names@gmail.com", 'Subject: Extracted Names\n\nJosie Smith\nMugsy Dog Smith')
    mock_smtp.return_value.quit.assert_called_once()

def test_task_func_no_names(mock_smtp):
    # Arrange
    text = "[3996 COLLEGE AVENUE, SOMETOWN, MD 21003]"
    expected_names = []
    
    # Act
    names = task_func(text=text, smtp=Mock())
    
    # Assert
    assert names == expected_names
    mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
    mock_smtp.return_value.starttls.assert_called_once()
    mock_smtp.return_value.login.assert_called_once_with("your.email@gmail.com", "your.password")
    mock_smtp.return_value.sendmail.assert_called_once_with("your.email@gmail.com", "names@gmail.com", 'Subject: Extracted Names\n\n')
    mock_smtp.return_value.quit.assert_called_once()

def test_task_func_empty_text(mock_smtp):
    # Arrange
    text = ""
    expected_names = []
    
    # Act
    names = task_func(text=text, smtp=Mock())
    
    # Assert
    assert names == expected_names
    mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
    mock_smtp.return_value.starttls.assert_called_once()
    mock_smtp.return_value.login.assert_called_once_with("your.email@gmail.com", "your.password")
    mock_smtp.return_value.sendmail.assert_called_once_with("your.email@gmail.com", "names@gmail.com", 'Subject: Extracted Names\n\n')
    mock_smtp.return_value.quit.assert_called_once()