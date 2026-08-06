import pytest
from src_0084 import task_func
from flask import Flask
from flask_mail import Mail, Message
from unittest.mock import patch, MagicMock

@pytest.fixture
def app():
    return task_func(
        smtp_server='smtp.example.com',
        smtp_port=587,
        smtp_user='user@example.com',
        smtp_password='password',
        template_folder='/path/to/templates'
    )

@pytest.fixture
def client(app):
    return app.test_client()

@patch('flask_mail.Mail.send')
def test_send_mail(mock_send, client):
    response = client.get('/send_mail')
    assert response.status_code == 200
    assert response.data == b'Mail sent!'
    mock_send.assert_called_once()

def test_app_config(app):
    assert app.config['MAIL_SERVER'] == 'smtp.example.com'
    assert app.config['MAIL_PORT'] == 587
    assert app.config['MAIL_USERNAME'] == 'user@example.com'
    assert app.config['MAIL_PASSWORD'] == 'password'
    assert app.config['MAIL_USE_TLS'] is True

def test_template_folder(app):
    assert app.template_folder == '/path/to/templates'