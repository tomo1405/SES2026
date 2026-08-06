import pytest
from src_0402 import task_func
import os
from unittest.mock import patch

def test_task_func_default_values():
    with patch.dict(os.environ, {}, clear=True):
        mail, config = task_func('test_app')
        assert config == {
            'MAIL_SERVER': 'localhost',
            'MAIL_PORT': 25,
            'MAIL_USE_TLS': False,
            'MAIL_USERNAME': None,
            'MAIL_PASSWORD': None
        }

def test_task_func_with_env_variables():
    with patch.dict(os.environ, {
        'MAIL_SERVER': 'smtp.example.com',
        'MAIL_PORT': '587',
        'MAIL_USE_TLS': 'True',
        'MAIL_USERNAME': 'user@example.com',
        'MAIL_PASSWORD': 'password'
    }):
        mail, config = task_func('test_app')
        assert config == {
            'MAIL_SERVER': 'smtp.example.com',
            'MAIL_PORT': 587,
            'MAIL_USE_TLS': True,
            'MAIL_USERNAME': 'user@example.com',
            'MAIL_PASSWORD': 'password'
        }

def test_task_func_with_partial_env_variables():
    with patch.dict(os.environ, {
        'MAIL_SERVER': 'smtp.example.com',
        'MAIL_USE_TLS': 'False'
    }):
        mail, config = task_func('test_app')
        assert config == {
            'MAIL_SERVER': 'smtp.example.com',
            'MAIL_PORT': 25,
            'MAIL_USE_TLS': False,
            'MAIL_USERNAME': None,
            'MAIL_PASSWORD': None
        }