python
import json
import logging
from flask import Flask, render_template, request
import pytest

@pytest.fixture
def app():
    app = Flask(__name__, template_folder='templates')

    @app.route('/', methods=['POST'])
    def handle_post():
        data = request.get_json()
        logging.info(json.dumps(data))
        return render_template('index.html', data=data)

    return app

def test_task_func(app):
    client = app.test_client()
    response = client.post('/', json={'name': 'John'})
    assert response.status_code == 200
    assert b'John' in response.data