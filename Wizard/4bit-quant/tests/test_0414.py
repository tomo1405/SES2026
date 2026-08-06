python
import os
import pytest
from flask_mail import Mail

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['MAIL_SERVER'] = 'localhost'
    app.config['MAIL_PORT'] = 25
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USERNAME'] = None
    app.config['MAIL_PASSWORD'] = None
    return app

def test_task_func(app):
    mail, config = task_func(app)
    assert mail.mail_server == app.config['MAIL_SERVER']
    assert mail.port == app.config['MAIL_PORT']
    assert mail.use_tls == app.config['MAIL_USE_TLS']
    assert mail.username == app.config['MAIL_USERNAME']
    assert mail.password == app.config['MAIL_PASSWORD']
    assert config['MAIL_SERVER'] == app.config['MAIL_SERVER']
    assert config['MAIL_PORT'] == app.config['MAIL_PORT']
    assert config['MAIL_USE_TLS'] == app.config['MAIL_USE_TLS']
    assert config['MAIL_USERNAME'] == app.config['MAIL_USERNAME']
    assert config['MAIL_PASSWORD'] == app.config['MAIL_PASSWORD']