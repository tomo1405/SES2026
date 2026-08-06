import pytest
from src_0275 import task_func

def test_task_func():
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'username'
    smtp_password = 'password'
    expected_result = EmailRequestHandler

    result = task_func(smtp_server, smtp_port, smtp_username, smtp_password)

    assert result == expected_result