import pytest
from io import BytesIO
from http.server import BaseHTTPRequestHandler
from src_0273 import task_func

class TestPostRequestHandler:
    @pytest.fixture
    def handler_class(self):
        return task_func()

    @pytest.fixture
    def make_request(self, handler_class):
        def _make_request(body, content_type='application/json'):
            request = BytesIO(body.encode('utf-8'))
            request.seek(0)
            headers = {'Content-Length': str(len(body)), 'Content-Type': content_type}
            environ = {
                'REQUEST_METHOD': 'POST',
                'wsgi.input': request,
                'CONTENT_LENGTH': str(len(body)),
                'CONTENT_TYPE': content_type
            }
            return handler_class(), environ
        return _make_request

    def test_valid_json_request(self, make_request):
        body = '{"data": "some data"}'
        handler, environ = make_request(body)

        response = BytesIO()
        handler.do_POST(environ, response)

        assert response.getvalue().decode('utf-8') == '{"status": "success", "message": "Data received successfully."}'

    def test_invalid_content_type(self, make_request):
        body = '{"data": "some data"}'
        handler, environ = make_request(body, content_type='text/plain')

        response = BytesIO()
        handler.do_POST(environ, response)

        expected_error = '{"status": "error", "message": "Content-Type header is not application/json"}'
        assert response.getvalue().decode('utf-8') == expected_error

    def test_missing_data_key(self, make_request):
        body = '{"not_data": "some data"}'
        handler, environ = make_request(body)

        response = BytesIO()
        handler.do_POST(environ, response)

        expected_error = '{"status": "error", "message": "No data received"}'
        assert response.getvalue().decode('utf-8') == expected_error

    def test_empty_request_body(self, make_request):
        body = ''
        handler, environ = make_request(body)

        response = BytesIO()
        handler.do_POST(environ, response)

        expected_error = '{"status": "error", "message": "No data received"}'
        assert response.getvalue().decode('utf-8') == expected_error