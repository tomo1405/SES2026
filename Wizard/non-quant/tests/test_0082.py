python
import pytest
from src_0082 import task_func

def test_task_func():
    app = task_func('https://jsonplaceholder.typicode.com/todos/1', 'templates')
    assert app.name == 'src_0082'
    assert app.template_folder == 'templates'
    assert len(app.url_map._rules) == 1
    assert app.url_map._rules[0].rule == '/data'
    assert app.url_map._rules[0].endpoint == 'data'
    assert app.url_map._rules[0].methods == {'GET'}