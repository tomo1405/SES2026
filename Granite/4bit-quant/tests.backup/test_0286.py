import pytest
from src_0286 import task_func

def test_task_func():
    url = 'https://example.com'
    form_id = 0
    data = {'name': 'John', 'email': 'john@example.com'}
    expected_title = 'Example Domain'

    actual_title = task_func(url, form_id, data)

    assert actual_title == expected_title, "Expected title does not match actual title"

def test_task_func_no_title():
    url = 'https://example.com'
    form_id = 0
    data = {'name': 'John', 'email': 'john@example.com'}
    expected_title = 'No Title'

    actual_title = task_func(url, form_id, data)

    assert actual_title == expected_title, "Expected title does not match actual title"