import pytest
from src_0274 import task_func
import json
from io import BytesIO
from http.server import BaseHTTPRequestHandler

class TestPostRequestHandler:
    @pytest.fixture
    def handler(self):
        class Request(BaseHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                self.rfile = BytesIO()
                self.wfile = BytesIO()
                super().__init__(*args, **kwargs)

        return Request

    def test_valid_json_data(self, handler):
        handler_instance = handler()
        handler_instance.headers = {'content-type': 'application/json', 'content-length': '18'}
        handler_instance.rfile.write(b'{"data": "some data"}')
        handler_instance.rfile.seek(0)

        PostRequestHandler = task_func()
        post_request_handler = PostRequestHandler(handler_instance)
        post_request_handler.do_POST()

        handler_instance.wfile.seek(0)
        response = json.load(handler_instance.wfile)
        assert response == {'status': 'success', 'message': 'Data received successfully.'}

    def test_invalid_content_type(self, handler):
        handler_instance = handler()
        handler_instance.headers = {'content-type': 'text/plain', 'content-length': '18'}
        handler_instance.rfile.write(b'{"data": "some data"}')
        handler_instance.rfile.seek(0)

        PostRequestHandler = task_func()
        post_request_handler = PostRequestHandler(handler_instance)
        post_request_handler.do_POST()

        assert handler_instance.wfile.getvalue() == b''

    def test_invalid_json(self, handler):
        handler_instance = handler()
        handler_instance.headers = {'content-type': 'application/json', 'content-length': '18'}
        handler_instance.rfile.write(b'{"data": "some data"')
        handler_instance.rfile.seek(0)

        PostRequestHandler = task_func()
        post_request_handler = PostRequestHandler(handler_instance)
        post_request_handler.do_POST()

        assert handler_instance.wfile.getvalue() == b''

    def test_no_data_key(self, handler):
        handler_instance = handler()
        handler_instance.headers = {'content-type': 'application/json', 'content-length': '13'}
        handler_instance.rfile.write(b'{"key": "value"}')
        handler_instance.rfile.seek(0)

        PostRequestHandler = task_func()
        post_request_handler = PostRequestHandler(handler_instance)
        post_request_handler.do_POST()

        assert handler_instance.wfile.getvalue() == b''