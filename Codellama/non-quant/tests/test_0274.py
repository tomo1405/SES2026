import http

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

    assert handler.send_error.call_count == 0
    assert handler.send_response.call_count == 1
    assert handler.send_header.call_count == 1
    assert handler.end_headers.call_count == 1
    assert handler.wfile.write.call_count == 1

def test_do_POST_invalid_json(mocker):
    handler = task_func()
    mocker.patch.object(handler, 'send_error')
    mocker.patch.object(handler, 'send_response')
    mocker.patch.object(handler, 'send_header')
    mocker.patch.object(handler, 'end_headers')
    mocker.patch.object(handler, 'wfile')

    handler.do_POST()

    assert handler.send_error.call_count == 1
    assert handler.send_response.call_count == 0
    assert handler.send_header.call_count == 0
    assert handler.end_headers.call_count == 0
    assert handler.wfile.write.call_count == 0

def test_do_POST_no_data_key(mocker):
    handler = task_func()
    mocker.patch.object(handler, 'send_error')
    mocker.patch.object(handler, 'send_response')
    mocker.patch.object(handler, 'send_header')
    mocker.patch.object(handler, 'end_headers')
    mocker.patch.object(handler, 'wfile')

    handler.do_POST()

    assert handler.send_error.call_count == 1
    assert handler.send_response.call_count == 0
    assert handler.send_header.call_count == 0
    assert handler.end_headers.call_count == 0
    assert handler.wfile.write.call_count == 0