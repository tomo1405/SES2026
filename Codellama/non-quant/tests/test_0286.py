import pytest
from src_0286 import task_func

def test_task_func():
    url = 'https://www.example.com'
    form_id = 0
    data = {'username': 'test_user', 'password': 'test_pass'}

    title = task_func(url, form_id, data)

    assert title == 'Example Domain'