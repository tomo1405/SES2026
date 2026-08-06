import pytest
from src_0084 import task_func

def test_task_func():
    app = task_func('smtp.example.com', 587, 'username', 'password', '/path/to/templates')
    assert app.config['MAIL_SERVER'] == 'smtp.example.com'
    assert app.config['MAIL_PORT'] == 587
    assert app.config['MAIL_USERNAME'] == 'username'
    assert app.config['MAIL_PASSWORD'] == 'password'
    assert app.config['MAIL_USE_TLS'] == True
    assert app.template_folder == '/path/to/templates'