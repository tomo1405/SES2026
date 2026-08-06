import pytest
from flask import Flask
from src_0414 import task_func
import os

def test_task_func_default_values():
    app = Flask(__name__)
    mail, config = task_func(app)
    
    assert config['MAIL_SERVER'] == 'localhost'
    assert config['MAIL_PORT'] == 25
    assert config['MAIL_USE_TLS'] is False
    assert config['MAIL_USERNAME'] is None
    assert config['MAIL_PASSWORD'] is None

def test_task_func_with_env_variables(monkeypatch):
    monkeypatch.setenv('MAIL_SERVER', 'smtp.example.com')
    monkeypatch.setenv('MAIL_PORT', '587')
    monkeypatch.setenv('MAIL_USE_TLS', 'True')
    monkeypatch.setenv('MAIL_USERNAME', 'user@example.com')
    monkeypatch.setenv('MAIL_PASSWORD', 'password123')
    
    app = Flask(__name__)
    mail, config = task_func(app)
    
    assert config['MAIL_SERVER'] == 'smtp.example.com'
    assert config['MAIL_PORT'] == 587
    assert config['MAIL_USE_TLS'] is True
    assert config['MAIL_USERNAME'] == 'user@example.com'
    assert config['MAIL_PASSWORD'] == 'password123'