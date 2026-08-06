import pytest
from src_0082 import task_func

def test_task_func():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    template_folder = "path/to/templates"
    app = task_func(api_url, template_folder)
    assert app is not None
    assert app.template_folder == "path/to/templates"
    assert app.root_path == "path/to/templates"
    assert app.name == "__main__"
    assert app.config["TESTING"] == True
    assert app.config["DEBUG"] == False
    assert app.config["PROPAGATE_EXCEPTIONS"] == True