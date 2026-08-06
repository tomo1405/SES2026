import pytest
from src_0402 import task_func

def test_task_func():
    app_name = 'MyApp'
    mail, config = task_func(app_name)
    assert mail is not None
    assert config is not None
    assert isinstance(config, dict)
    assert 'MAIL_SERVER' in config
    assert 'MAIL_PORT' in config
    assert 'MAIL_USE_TLS' in config
    assert 'MAIL_USERNAME' in config
    assert 'MAIL_PASSWORD' in config