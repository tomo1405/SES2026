import pytest
from src_0274 import task_func
import io
import json
from http.server import BaseHTTPRequestHandler

class TestPostRequestHandler:
    @pytest.fixture
    def handler_instance(self):
        class MockServer:
            def __init__(self):
                self.response = None

            def send_error(self, code, message):
                self.response = {'code': code, 'message': message}

            def send_response(self, code):
                self.response = {'code': code}

            def send_header(self, key, value):
                if not hasattr(self, 'headers'):
                    self.headers = {}
                self.headers[key] = value

            def end_headers(self):
                pass

            def wfile_write(self, data):
                self.response_data = data.decode()

        mock_server = MockServer()
        handler_class = task_func()
        handler_instance = handler_class(mock_server, None)
        handler_instance.rfile = io.BytesIO(b'{"data": "test"}')
        handler_instance.headers = {'content-type': 'application/json', 'content-length': '18'}
        return handler_instance, mock_server

    def test_do_POST_success(self, handler_instance):
        handler, server = handler_instance
        handler.do_POST()
        assert server.response == {'code': 200}
        assert server.headers['content-type'] == 'application/json'
        assert json.loads(server.response_data) == {'status': 'success', 'message': 'Data received successfully.'}

    def test_do_POST_invalid_content_type(self, handler_instance):
        handler, server = handler_instance
        handler.headers['content-type'] = 'text/plain'
        handler.do_POST()
        assert server.response == {'code': 400, 'message': 'Content-Type header is not application/json'}

    def test_do_POST_invalid_json(self, handler_instance):
        handler, server = handler_instance
        handler.rfile = io.BytesIO(b'invalid json')
        handler.do_POST()
        assert server.response == {'code': 400, 'message': 'Invalid JSON'}

    def test_do_POST_no_data_key(self, handler_instance):
        handler, server = handler_instance
        handler.rfile = io.BytesIO(b'{}')
        handler.do_POST()
        assert server.response == {'code': 400, 'message': 'No data key in request'}