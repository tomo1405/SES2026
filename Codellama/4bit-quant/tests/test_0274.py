import pytest
from src_0274 import task_func

def test_do_POST_valid_json():
    request_handler = task_func()
    request_handler.headers = {'content-type': 'application/json'}
    request_handler.rfile = b'{"data": "test"}'
    request_handler.do_POST()
    assert request_handler.wfile.getvalue() == b'{"status": "success", "message": "Data received successfully."}'

def test_do_POST_invalid_json():
    request_handler = task_func()
    request_handler.headers = {'content-type': 'application/json'}
    request_handler.rfile = b'{"data": "test"'
    request_handler.do_POST()
    assert request_handler.wfile.getvalue() == b'{"status": "error", "message": "Invalid JSON"}'

def test_do_POST_no_data_key():
    request_handler = task_func()
    request_handler.headers = {'content-type': 'application/json'}
    request_handler.rfile = b'{"test": "test"}'
    request_handler.do_POST()
    assert request_handler.wfile.getvalue() == b'{"status": "error", "message": "No data key in request"}'

def test_do_POST_invalid_content_type():
    request_handler = task_func()
    request_handler.headers = {'content-type': 'text/plain'}
    request_handler.rfile = b'{"data": "test"}'
    request_handler.do_POST()
    assert request_handler.wfile.getvalue() == b'{"status": "error", "message": "Content-Type header is not application/json"}'