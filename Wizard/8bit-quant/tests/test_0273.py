python
import pytest
from src_0273 import task_func

def test_post_request_handler_do_post_success():
    # Test successful POST request
    request_handler = task_func()
    request_handler.path = '/api/data'
    request_handler.headers = {'content-type': 'application/json'}
    request_handler.rfile = BytesIO(json.dumps({'data': 'some data'}).encode())
    request_handler.wfile = BytesIO()
    request_handler.do_POST()
    assert request_handler.wfile.getvalue().decode() == '{"status": "success", "message": "Data received successfully."}'

def test_post_request_handler_do_post_no_data():
    # Test POST request with no data
    request_handler = task_func()
    request_handler.path = '/api/data'
    request_handler.headers = {'content-type': 'application/json'}
    request_handler.rfile = BytesIO(json.dumps({}).encode())
    request_handler.wfile = BytesIO()
    request_handler.do_POST()
    assert request_handler.wfile.getvalue().decode() == '{"status": "error", "message": "No data received"}'

def test_post_request_handler_do_post_invalid_content_type():
    # Test POST request with invalid content type
    request_handler = task_func()
    request_handler.path = '/api/data'
    request_handler.headers = {'content-type': 'text/plain'}
    request_handler.rfile = BytesIO(json.dumps({'data': 'some data'}).encode())
    request_handler.wfile = BytesIO()
    request_handler.do_POST()
    assert request_handler.wfile.getvalue().decode() == '{"status": "error", "message": "Content-Type header is not application/json"}'