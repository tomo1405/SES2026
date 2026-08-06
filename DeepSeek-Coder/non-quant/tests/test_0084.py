import pytest
from src_0084 import task_func

def test_task_func():
    # Test the function
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "user@example.com"
    smtp_password = "password"
    template_folder = "templates"

    app = task_func(smtp_server=smtp_server, smtp_port=smtp_port, smtp_user=smtp_user, smtp_password=smtp_password, template_folder=template_folder)

    assert app is not None
    assert app.config['MAIL_SERVER'] == smtp_server
    assert app.config['MAIL_PORT'] == smtp_port
    assert app.config['MAIL_USERNAME'] == smtp_user
    assert app.config['MAIL_PASSWORD'] == smtp_password
    assert app.config['MAIL_USE_TLS'] is True

    # Add more assertions to test the send_mail route if possible