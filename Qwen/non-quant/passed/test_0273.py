import pytest
from io import BytesIO
from src_0273 import task_func

class TestPostRequestHandler:
    def test_do_POST_with_invalid_content_type(self):
        class MockRequest:
            headers = {'content-type': 'text/plain'}
            method = 'POST'
            rfile = BytesIO(b'{}')

        class MockResponse:
            def __init__(self):
                self.status_code = None
                self.headers = {}
                self.body = b''

            def send_response(self, status_code):
                self.status_code = status_code

            def send_header(self, key, value):
                self.headers[key] = value

            def end_headers(self):
                pass

            def write(self, body):
                self.body = body

        handler = task_func()(MockRequest(), MockResponse())
        assert handler.response.status_code == 400
        assert handler.response.headers['Content-type'] == 'application/json'
        response_data = json.loads(handler.response.body.decode())
        assert response_data['status'] == 'error'
        assert response_data['message'] == 'Content-Type header is not application/json'

    def test_do_POST_with_missing_data_field(self):
        class MockRequest:
            headers = {'content-type': 'application/json', 'content-length': '10'}
            method = 'POST'
            rfile = BytesIO(b'{"key": "value"}')

        class MockResponse:
            def __init__(self):
                self.status_code = None
                self.headers = {}
                self.body = b''

            def send_response(self, status_code):
                self.status_code = status_code

            def send_header(self, key, value):
                self.headers[key] = value

            def end_headers(self):
                pass

            def write(self, body):
                self.body = body

        handler = task_func()(MockRequest(), MockResponse())
        assert handler.response.status_code == 400
        assert handler.response.headers['Content-type'] == 'application/json'
        response_data = json.loads(handler.response.body.decode())
        assert response_data['status'] == 'error'
        assert response_data['message'] == 'No data received'

    def test_do_POST_with_valid_data(self):
        class MockRequest:
            headers = {'content-type': 'application/json', 'content-length': '15'}
            method = 'POST'
            rfile = BytesIO(b'{"data": "valid"}')

        class MockResponse:
            def __init__(self):
                self.status_code = None
                self.headers = {}
                self.body = b''

            def send_response(self, status_code):
                self.status_code = status_code

            def send_header(self, key, value):
                self.headers[key] = value

            def end_headers(self):
                pass

            def write(self, body):
                self.body = body

        handler = task_func()(MockRequest(), MockResponse())
        assert handler.response.status_code == 200
        assert handler.response.headers['Content-type'] == 'application/json'
        response_data = json.loads(handler.response.body.decode())
        assert response_data['status'] == 'success'
        assert response_data['message'] == 'Data received successfully.'