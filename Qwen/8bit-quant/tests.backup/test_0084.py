import pytest
from flask import Flask, request
from flask_mail import Mail, Message
from src_0084 import task_func

@pytest.fixture
def app():
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_user = 'user@example.com'
    smtp_password = 'password'
    template_folder = 'templates'
    app = task_func(smtp_server, smtp_port, smtp_user, smtp_password, template_folder)
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

def test_send_mail(client):
    response = client.get('/send_mail')
    assert response.status_code == 200
    assert response.data == b'Mail sent!'