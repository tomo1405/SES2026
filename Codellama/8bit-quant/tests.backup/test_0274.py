import pytest
from src_0274 import task_func

def test_task_func():
    handler = task_func()
    assert isinstance(handler, http.server.BaseHTTPRequestHandler)

def test_do_POST_valid_json(mocker):
    handler = task_func()
    mocker.patch.object(handler, 'send_error')
    mocker.patch.object(handler, 'send_response')
    mocker.patch.object(handler, 'send_header')
    mocker.patch.object(handler, 'end_headers')
    mocker.patch.object(handler, 'wfile')

    handler.do_POST()

    handler.send_error.assert_not_called()
    handler.send_response.assert_called_once_with(200)
    handler.send_header.assert_called_once_with('content-type', 'application/json')
    handler.end_headers.assert_called_once()
    handler.wfile.write.assert_called_once_with(json.dumps(SUCCESS_RESPONSE).encode())

def test_do_POST_invalid_json(mocker):
    handler = task_func()
    mocker.patch.object(handler, 'send_error')
    mocker.patch.object(handler, 'send_response')
    mocker.patch.object(handler, 'send_header')
    mocker.patch.object(handler, 'end_headers')
    mocker.patch.object(handler, 'wfile')

    handler.do_POST()

    handler.send_error.assert_called_once_with(400, 'Invalid JSON')
    handler.send_response.assert_not_called()
    handler.send_header.assert_not_called()
    handler.end_headers.assert_not_called()
    handler.wfile.write.assert_not_called()

def test_do_POST_no_data_key(mocker):
    handler = task_func()
    mocker.patch.object(handler, 'send_error')
    mocker.patch.object(handler, 'send_response')
    mocker.patch.object(handler, 'send_header')
    mocker.patch.object(handler, 'end_headers')
    mocker.patch.object(handler, 'wfile')

    handler.do_POST()

    handler.send_error.assert_called_once_with(400, 'No data key in request')
    handler.send_response.assert_not_called()
    handler.send_header.assert_not_called()
    handler.end_headers.assert_not_called()
    handler.wfile.write.assert_not_called()