import os
from unittest.mock import patch

import pytest
from src_0402 import task_func


def test_task_func_default_values():
    with patch.dict(os.environ, {}, clear=True):
        mail, config = task_func("test_app")
        assert config == {
            'MAIL_SERVER': 'localhost',
            'MAIL_PORT': 25,
            'MAIL_USE_TLS': False,
            'MAIL_USERNAME': None,
            'MAIL_PASSWORD': None
        }

def test_task_func_custom_values():
    with patch.dict(os.environ, {
        'MAIL_SERVER': 'smtp.example.com',
        'MAIL_PORT': '587',
        'MAIL_USE_TLS': 'True',
        'MAIL_USERNAME': 'user@example.com',
        'MAIL_PASSWORD': 'password'
    }, clear=True):
        mail, config = task_func("test_app")
        assert config == {
            'MAIL_SERVER': 'smtp.example.com',
            'MAIL_PORT': 587,
            'MAIL_USE_TLS': True,
            'MAIL_USERNAME': 'user@example.com',
            'MAIL_PASSWORD': 'password'
        }

def test_task_func_invalid_mail_port():
    with patch.dict(os.environ, {
        'MAIL_PORT': 'invalid_port'
    }, clear=True):
        with pytest.raises(ValueError):
            task_func("test_app")

def test_task_func_mail_use_tls_not_boolean():
    with patch.dict(os.environ, {
        'MAIL_USE_TLS': 'not_a_boolean'
    }, clear=True):
        mail, config = task_func("test_app")
        assert config['MAIL_USE_TLS'] == False