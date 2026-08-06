import pytest
from flask import Flask
from flask_mail import Mail, Message
from src_0084 import task_func

@pytest.fixture
def app():
    return task_func(
        smtp_server='smtp.example.com',
        smtp_port=587,
        smtp_user='user@example.com',
        smtp_password='password',
        template_folder='/path/to/templates'
    )

def test_task_func_initialization(app):
    assert isinstance(app, Flask)
    assert app.config['MAIL_SERVER'] == 'smtp.example.com'
    assert app.config['MAIL_PORT'] == 587
    assert app.config['MAIL_USERNAME'] == 'user@example.com'
    assert app.config['MAIL_PASSWORD'] == 'password'
    assert app.config['MAIL_USE_TLS'] is True

def test_send_mail_route(app, monkeypatch):
    # Mocking the mail.send method to avoid sending actual emails
    def mock_send_message(message):
        pass

    monkeypatch.setattr(Mail, 'send', mock_send_message)

    with app.test_client() as client:
        response = client.get('/send_mail')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'Mail sent!'