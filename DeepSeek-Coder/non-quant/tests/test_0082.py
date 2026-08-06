import pytest
from src_0082 import task_func

def test_task_func():
    api_url = "https://api.example.com/data"
    template_folder = "templates"
    app = task_func(api_url, template_folder)
    
    assert app is not None
    assert callable(app)