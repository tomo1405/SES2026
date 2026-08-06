import pytest
from src_0193 import task_func
import re
import smtplib

# Mocking the SMTP class to avoid actual email sending
class MockSMTP:
    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.sent_messages = []

    def starttls(self):
        pass

    def login(self, email_address, email_password):
        pass

    def sendmail(self, from_addr, to_addrs, msg):
        self.sent_messages.append(msg)

    def quit(self):
        pass

def test_task_func():
    # Arrange
    text = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
    expected_names = ["Josie Smith", "Mugsy Dog Smith"]
    mock_smtp = MockSMTP("smtp.gmail.com", 587)

    # Act
    result = task_func(text=text, smtp=MockSMTP)

    # Assert
    assert result == expected_names
    assert len(mock_smtp.sent_messages) == 1
    assert "Extracted Names" in mock_smtp.sent_messages[0]
    for name in expected_names:
        assert name in mock_smtp.sent_messages[0]

def test_task_func_no_names():
    # Arrange
    text = "No names here"
    expected_names = []
    mock_smtp = MockSMTP("smtp.gmail.com", 587)

    # Act
    result = task_func(text=text, smtp=MockSMTP)

    # Assert
    assert result == expected_names
    assert len(mock_smtp.sent_messages) == 1
    assert "Extracted Names" in mock_smtp.sent_messages[0]
    for name in expected_names:
        assert name not in mock_smtp.sent_messages[0]

def test_task_func_empty_text():
    # Arrange
    text = ""
    expected_names = []
    mock_smtp = MockSMTP("smtp.gmail.com", 587)

    # Act
    result = task_func(text=text, smtp=MockSMTP)

    # Assert
    assert result == expected_names
    assert len(mock_smtp.sent_messages) == 1
    assert "Extracted Names" in mock_smtp.sent_messages[0]
    for name in expected_names:
        assert name not in mock_smtp.sent_messages[0]