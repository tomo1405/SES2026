python
import os
import pytest
from flask_mail import Mail

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app

def test_task_func(app):
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'localhost')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 25))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', False) == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', None)
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', None)
    
    mail = Mail(app)
    
    assert mail.app == app
    assert mail.mail_server == app.config['MAIL_SERVER']
    assert mail.mail_port == app.config['MAIL_PORT']
    assert mail.use_tls == app.config['MAIL_USE_TLS']
    assert mail.username == app.config['MAIL_USERNAME']
    assert mail.password == app.config['MAIL_PASSWORD']