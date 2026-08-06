python
import cgi
import http.server
import json
import pytest

def task_func():
    class PostRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            
            # Define error response directly within the method
            error_response = {
                'status': 'error',
                'message': ''  # This will be modified based on the error condition
            }
            
            if ctype != 'application/json':
                self.send_response(400)
                self.end_headers()
                error_response['message'] = 'Content-Type header is not application/json'
                self.wfile.write(json.dumps(error_response).encode())
                return

            length = int(self.headers.get('content-length'))
            message = json.loads(self.rfile.read(length))
            
            if 'data' not in message:
                self.send_response(400)
                self.end_headers()
                error_response['message'] = 'No data received'
                self.wfile.write(json.dumps(error_response).encode())
                return

            # Define success response directly within the method
            success_response = {
                'status': 'success',
                'message': 'Data received successfully.'
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(success_response).encode())

    return PostRequestHandler

def test_task_func():
    # Test case 1: Valid JSON data
    request_handler = task_func()()
    request_handler.rfile = BytesIO(json.dumps({'data': 'test data'}).encode())
    request_handler.headers = {'content-type': 'application/json'}
    request_handler.handle_one_request()
    assert request_handler.wfile.getvalue().decode() == '{"status": "success", "message": "Data received successfully."}\n'

    # Test case 2: Invalid JSON data
    request_handler = task_func()()
    request_handler.rfile = BytesIO(json.dumps({'not_data': 'test data'}).encode())
    request_handler.headers = {'content-type': 'application/json'}
    request_handler.handle_one_request()
    assert request_handler.wfile.getvalue().decode() == '{"status": "error", "message": "No data received"}\n'

    # Test case 3: Invalid Content-Type header
    request_handler = task_func()()
    request_handler.rfile = BytesIO(json.dumps({'data': 'test data'}).encode())
    request_handler.headers = {'content-type': 'text/plain'}
    request_handler.handle_one_request()
    assert request_handler.wfile.getvalue().decode() == '{"status": "error", "message": "Content-Type header is not application/json"}\n'