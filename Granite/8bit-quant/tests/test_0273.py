import pytest
from src_0273 import task_func

def test_task_func():
    request_handler = task_func()
    assert request_handler.do_POST() == None

def test_do_POST_with_invalid_content_type():
    request_handler = task_func()
    request_handler.headers['content-type'] = 'text/html'
    assert request_handler.do_POST() == None

def test_do_POST_with_no_data():
    request_handler = task_func()
    request_handler.headers['content-type'] = 'application/json'
    request_handler.rfile.read = lambda x: b''
    assert request_handler.do_POST() == None

def test_do_POST_with_valid_data():
    request_handler = task_func()
    request_handler.headers['content-type'] = 'application/json'
    request_handler.headers['content-length'] = '100'
    request_handler.rfile.read = lambda x: b'{"data": "example"}'
    assert request_handler.do_POST() == None