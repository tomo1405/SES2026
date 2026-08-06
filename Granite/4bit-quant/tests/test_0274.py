import http
import json

import pytest
from src_0274 import task_func


class TestTaskFunc:
    def test_valid_json(self):
        """Test valid JSON request."""
        request_data = {'data': 'example'}
        request_json = json.dumps(request_data)
        handler = task_func()
        handler.rfile.read.return_value = request_json
        handler.headers = {'content-type': 'application/json', 'content-length': str(len(request_json))}
        handler.do_POST()
        assert handler.wfile.write.call_args[0][0] == json.dumps(SUCCESS_RESPONSE).encode()

    def test_invalid_json(self):
        """Test invalid JSON request."""
        request_data = 'not json'
        handler = task_func()
        handler.rfile.read.return_value = request_data
        handler.headers = {'content-type': 'application/json', 'content-length': str(len(request_data))}
        with pytest.raises(http.server.HTTPException) as exc_info:
            handler.do_POST()
        assert exc_info.value.code == 400

    def test_no_data_key(self):
        """Test request without 'data' key."""
        request_data = {}
        request_json = json.dumps(request_data)
        handler = task_func()
        handler.rfile.read.return_value = request_json
        handler.headers = {'content-type': 'application/json', 'content-length': str(len(request_json))}
        with pytest.raises(http.server.HTTPException) as exc_info:
            handler.do_POST()
        assert exc_info.value.code == 400