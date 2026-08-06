import pytest
from src_0273 import task_func
import json
from io import BytesIO
from http.server import BaseHTTPRequestHandler

class TestPostRequestHandler:
    @pytest.fixture
    def request_handler(self):
        class Request:
            headers = {}
            rfile = None

        class Response:
            status_code = None
            headers = {}
            body = None

        class MockServer:
            def handle_error(self, request, client_address):
                pass

        request = Request()
        response = Response()

        def write(data):
            response.body = data

        def send_response(code):
            response.status_code = code

        def send_header(key, value):
            response.headers[key] = value

        def end_headers():
            pass

        request_handler_class = task_func()
        handler = request_handler_class(request, None, MockServer())
        handler.send_response = send_response
        handler.send_header = send_header
        handler.end_headers = end_headers
        handler.wfile = BytesIO()
        handler.wfile.write = write

        return handler, request, response

    def test_non_json_content_type(self, request_handler):
        handler, request, response = request_handler
        request.headers['content-type'] = 'text/plain'

        handler.do_POST()

        assert response.status_code == 400
        assert response.headers['Content-type'] == 'application/json'
        response_body = json.loads(response.body.decode())
        assert response_body['status'] == 'error'
        assert response_body['message'] == 'Content-Type header is not application/json'

    def test_no_data_received(self, request_handler):
        handler, request, response = request_handler
        request.headers['content-type'] = 'application/json'
        request.headers['content-length'] = '0'

        handler.do_POST()

        assert response.status_code == 400
        assert response.headers['Content-type'] == 'application/json'
        response_body = json.loads(response.body.decode())
        assert response_body['status'] == 'error'
        assert response_body['message'] == 'No data received'

    def test_successful_data_received(self, request_handler):
        handler, request, response = request_handler
        request.headers['content-type'] = 'application/json'
        request.headers['content-length'] = '15'
        request.rfile = BytesIO(b'{"data": "test"}')

        handler.do_POST()

        assert response.status_code == 200
        assert response.headers['Content-type'] == 'application/json'
        response_body = json.loads(response.body.decode())
        assert response_body['status'] == 'success'
        assert response_body['message'] == 'Data received successfully.'