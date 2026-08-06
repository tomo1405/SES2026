import pytest
from src_0286 import task_func

def test_task_func():
    url = 'https://example.com'
    form_id = 0
    data = {'username': 'john', 'password': '123456'}
    expected_title = 'Welcome, John'

    actual_title = task_func(url, form_id, data)

    assert actual_title == expected_title, "Expected title does not match actual title"