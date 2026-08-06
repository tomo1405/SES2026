import pytest
from src_0273 import task_func

def test_task_func():
    request_handler = task_func()()
    assert request_handler.do_POST() == None

def test_task_func_content_type_error():
    request_handler = task_func()()
    request_handler.headers['content-type'] = 'text/html'
    assert request_handler.do_POST() == None

def test_task_func_no_data_error():
    request_handler = task_func()()
    request_handler.headers['content-type'] = 'application/json'
    request_handler.rfile.read = lambda x: b''
    assert request_handler.do_POST() == None

def test_task_func_success():
    request_handler = task_func()()
    request_handler.headers['content-type'] = 'application/json'
    request_handler.rfile.read = lambda x: b'{"data": "example"}'
    assert request_handler.do_POST() == None