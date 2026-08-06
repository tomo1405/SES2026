import pytest
from src_0081 import task_func

def test_task_func():
    app = task_func('/path/to/templates')
    assert app.template_folder == '/path/to/templates'

def test_handle_post():
    with app.test_request_context('/?key=value'):
        data = {'key': 'value'}
        app.logger.info(json.dumps(data))
        assert app.render_template('index.html', data=data) == 'index.html'