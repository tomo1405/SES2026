import pytest
from src_0402 import task_func

def test_task_func():
    app_name = 'test_app'
    mail, config = task_func(app_name)
    assert isinstance(mail, Mail)
    assert config['MAIL_SERVER'] == 'localhost'
    assert config['MAIL_PORT'] == 25
    assert config['MAIL_USE_TLS'] == False
    assert config['MAIL_USERNAME'] == None
    assert config['MAIL_PASSWORD'] == None