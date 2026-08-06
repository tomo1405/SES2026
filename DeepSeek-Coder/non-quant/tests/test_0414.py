import pytest
from src_0414 import task_func

def test_task_func():
    # Mock the necessary imports and setup
    from unittest.mock import patch
    from flask import Flask
    from flask_mail import Mail

    app = Flask(__name__)
    mail, config = task_func(app)

    # Assertions to verify the output
    assert isinstance(mail, Mail)
    assert isinstance(config, dict)
    assert 'MAIL_SERVER' in config
    assert 'MAIL_PORT' in config
    assert 'MAIL_USE_TLS' in config
    assert 'MAIL_USERNAME' in config
    assert 'MAIL_PASSWORD' in config