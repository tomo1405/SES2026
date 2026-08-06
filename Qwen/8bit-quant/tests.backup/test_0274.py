import pytest
from src_0274 import task_func
from io import BytesIO
from http.server import BaseHTTPRequestHandler

class TestPostRequestHandler:
    def test_valid_json_with_data_key(self):
        handler_class = task_func()
        request_line = b"POST / HTTP/1.1\r\n"
        headers = (
            b"Host: localhost:8000\r\n"
            b"Content-Type: application/json\r\n"
            b"Content-Length: 19\r\n"
            b"\r\n"
        )
        body = b'{"data": "some data"}'
        raw_request = request_line + headers + body

        class MockRequest:
            method = 'POST'
            headers = {}
            rfile = BytesIO(raw_request)

        class MockResponse:
            def __init__(self):
                self.status = None
                self.headers = {}
                self.wfile = BytesIO()

            def send_response(self, status):
                self.status = status

            def send_header(self, key, value):
                self.headers[key] = value

            def end_headers(self):
                pass

            def write(self, data):
                self.wfile.write(data)

        mock_response = MockResponse()
        handler = handler_class(MockRequest(), mock_response)
        handler.handle_one_request()

        assert mock_response.status == 200
        assert mock_response.headers['content-type'] == 'application/json'
        response_body = mock_response.wfile.getvalue().decode()
        assert json.loads(response_body) == {'status': 'success', 'message': 'Data received successfully.'}

    def test_invalid_content_type(self):
        handler_class = task_func()
        request_line = b"POST / HTTP/1.1\r\n"
        headers = (
            b"Host: localhost:8000\r\n"
            b"Content-Type: text/plain\r\n"
            b"Content-Length: 12\r\n"
            b"\r\n"
        )
        body = b'some data'
        raw_request = request_line + headers + body

        class MockRequest:
            method = 'POST'
            headers = {}
            rfile = BytesIO(raw_request)

        class MockResponse:
            def __init__(self):
                self.status = None
                self.headers = {}
                self.wfile = BytesIO()

            def send_response(self, status):
                self.status = status

            def send_header(self, key, value):
                self.headers[key] = value

            def end_headers(self):
                pass

            def write(self, data):
                self.wfile.write(data)

        mock_response = MockResponse()
        handler = handler_class(MockRequest(), mock_response)
        handler.handle_one_request()

        assert mock_response.status == 400
        assert mock_response.headers['content-type'] == 'text/html'
        response_body = mock_response.wfile.getvalue().decode()
        assert 'Content-Type header is not application/json' in response_body

    def test_invalid_json(self):
        handler_class = task_func()
        request_line = b"POST / HTTP/1.1\r\n"
        headers = (
            b"Host: localhost:8000\r\n"
            b"Content-Type: application/json\r\n"
            b"Content-Length: 11\r\n"
            b"\r\n"
        )
        body = b'{"data": "some data'
        raw_request = request_line + headers + body

        class MockRequest:
            method = 'POST'
            headers = {}
            rfile = BytesIO(raw_request)

        class MockResponse:
            def __init__(self):
                self.status = None
                self.headers = {}
                self.wfile = BytesIO()

            def send_response(self, status):
                self.status = status

            def send_header(self, key, value):
                self.headers[key] = value

            def end_headers(self):
                pass

            def write(self, data):
                self.wfile.write(data)

        mock_response = MockResponse()
        handler = handler_class(MockRequest(), mock_response)
        handler.handle_one_request()

        assert mock_response.status == 400
        assert mock_response.headers['content-type'] == 'text/html'
        response_body = mock_response.wfile.getvalue().decode()
        assert 'Invalid JSON' in response_body

    def test_no_data_key_in_request(self):
        handler_class = task_func()
        request_line = b"POST / HTTP/1.1\r\n"
        headers = (
            b"Host: localhost:8000\r\n"
            b"Content-Type: application/json\r\n"
            b"Content-Length: 15\r\n"
            b"\r\n"
        )
        body = b'{"key": "value"}'
        raw_request = request_line + headers + body

        class MockRequest:
            method = 'POST'
            headers = {}
            rfile = BytesIO(raw_request)

        class MockResponse:
            def __init__(self):
                self.status = None
                self.headers = {}
                self.wfile = BytesIO()

            def send_response(self, status):
                self.status = status

            def send_header(self, key, value):
                self.headers[key] = value

            def end_headers(self):
                pass

            def write(self, data):
                self.wfile.write(data)

        mock_response = MockResponse()
        handler = handler_class(MockRequest(), mock_response)
        handler.handle_one_request()

        assert mock_response.status == 400
        assert mock_response.headers['content-type'] == 'text/html'
        response_body = mock_response.wfile.getvalue().decode()
        assert 'No data key in request' in response_body