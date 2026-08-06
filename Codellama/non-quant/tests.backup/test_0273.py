import pytest
from src_0273 import task_func

def test_do_POST_with_valid_json_data():
    request_handler = task_func()
    request_handler.headers = {'Content-Type': 'application/json'}
    request_handler.rfile = b'{"data": "test data"}'
    request_handler.do_POST()
    assert request_handler.wfile.getvalue() == b'{"status": "success", "message": "Data received successfully."}'

def test_do_POST_with_invalid_json_data():
    request_handler = task_func()
    request_handler.headers = {'Content-Type': 'application/json'}
    request_handler.rfile = b'{"data": "test data"'
    request_handler.do_POST()
    assert request_handler.wfile.getvalue() == b'{"status": "error", "message": "Invalid JSON data received."}'

def test_do_POST_with_no_data():
    request_handler = task_func()
    request_handler.headers = {'Content-Type': 'application/json'}
    request_handler.rfile = b'{}'
    request_handler.do_POST()
    assert request_handler.wfile.getvalue() == b'{"status": "error", "message": "No data received."}'

def test_do_POST_with_invalid_content_type():
    request_handler = task_func()
    request_handler.headers = {'Content-Type': 'text/plain'}
    request_handler.rfile = b'{"data": "test data"}'
    request_handler.do_POST()
    assert request_handler.wfile.getvalue() == b'{"status": "error", "message": "Content-Type header is not application/json."}'