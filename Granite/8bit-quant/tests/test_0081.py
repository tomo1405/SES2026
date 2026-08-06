import pytest
from src_0081 import task_func

def test_task_func():
    app = task_func('/path/to/templates')
    assert app.template_folder == '/path/to/templates'
    assert app.route == '/'
    assert app.methods == ['POST']