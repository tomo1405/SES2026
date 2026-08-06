import pytest
from src_0084 import task_func

def test_task_func():
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_user = 'user@example.com'
    smtp_password = 'password'
    template_folder = 'templates'

    app = task_func(smtp_server, smtp_port, smtp_user, smtp_password, template_folder)

    with app.test_client() as client:
        response = client.get('/send_mail')
        assert response.status_code == 200
        assert response.data == b'Mail sent!'