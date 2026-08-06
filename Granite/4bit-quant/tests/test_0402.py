import os

from src_0402 import task_func


def test_task_func():
    app_name = "MyApp"
    mail, config = task_func(app_name)
    assert mail is not None
    assert config['MAIL_SERVER'] == os.getenv('MAIL_SERVER', 'localhost')
    assert config['MAIL_PORT'] == int(os.getenv('MAIL_PORT', 25))
    assert config['MAIL_USE_TLS'] == os.getenv('MAIL_USE_TLS', False) == 'True'
    assert config['MAIL_USERNAME'] == os.getenv('MAIL_USERNAME', None)
    assert config['MAIL_PASSWORD'] == os.getenv('MAIL_PASSWORD', None)