python
import os
import pytest
from flask_mail import Mail

def task_func(app):

    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'localhost')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 25))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', False) == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', None)
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', None)
    
    mail = Mail(app)
    
    return mail, {
        'MAIL_SERVER': app.config['MAIL_SERVER'],
        'MAIL_PORT': app.config['MAIL_PORT'],
        'MAIL_USE_TLS': app.config['MAIL_USE_TLS'],
        'MAIL_USERNAME': app.config['MAIL_USERNAME'],
        'MAIL_PASSWORD': app.config['MAIL_PASSWORD']
    }

def test_task_func():
    app = {}
    mail, config = task_func(app)
    assert mail.app == app
    assert config == {
        'MAIL_SERVER': 'localhost',
        'MAIL_PORT': 25,
        'MAIL_USE_TLS': False,
        'MAIL_USERNAME': None,
        'MAIL_PASSWORD': None
    }