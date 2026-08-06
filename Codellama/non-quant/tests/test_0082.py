import pytest
from src_0082 import task_func

def test_task_func():
    api_url = 'https://example.com/api'
    template_folder = 'templates'
    app = task_func(api_url, template_folder)
    assert isinstance(app, Flask)
    assert app.template_folder == template_folder
    assert isinstance(app.api, Api)
    assert isinstance(app.api.resources['/data'], DataResource)
    assert app.api.resources['/data'].get() == {'data': 'data'}