import pytest
from src_0402 import task_func
import os

@pytest.fixture
def mock_env_vars():
    os.environ['MAIL_SERVER'] = 'smtp.example.com'
    os.environ['MAIL_PORT'] = '587'
    os.environ['MAIL_USE_TLS'] = 'True'
    os.environ['MAIL_USERNAME'] = 'user@example.com'
    os.environ['MAIL_PASSWORD'] = 'password123'

@pytest.fixture
def default_env_vars():
    os.environ.pop('MAIL_SERVER', None)
    os.environ.pop('MAIL_PORT', None)
    os.environ.pop('MAIL_USE_TLS', None)
    os.environ.pop('MAIL_USERNAME', None)
    os.environ.pop('MAIL_PASSWORD', None)

def test_task_func_with_mock_env_vars(mock_env_vars):
    mail, config = task_func('test_app')
    assert config == {
        'MAIL_SERVER': 'smtp.example.com',
        'MAIL_PORT': 587,
        'MAIL_USE_TLS': True,
        'MAIL_USERNAME': 'user@example.com',
        'MAIL_PASSWORD': 'password123'
    }

def test_task_func_with_default_env_vars(default_env_vars):
    mail, config = task_func('test_app')
    assert config == {
        'MAIL_SERVER': 'localhost',
        'MAIL_PORT': 25,
        'MAIL_USE_TLS': False,
        'MAIL_USERNAME': None,
        'MAIL_PASSWORD': None
    }