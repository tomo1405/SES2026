python
import pytest
from src_0275 import task_func

def test_task_func():
    # Test with valid input
    request_handler = task_func('smtp.gmail.com', 587, 'username', 'password')
    assert isinstance(request_handler, http.server.BaseHTTPRequestHandler)

    # Test with invalid input
    with pytest.raises(TypeError):
        task_func(123, '587', 'username', 'password')
    with pytest.raises(TypeError):
        task_func('smtp.gmail.com', '587', 'username', 'password')
    with pytest.raises(TypeError):
        task_func('smtp.gmail.com', 587, 123, 'password')
    with pytest.raises(TypeError):
        task_func('smtp.gmail.com', 587, 'username', 123)
    with pytest.raises(ValueError):
        task_func('smtp.gmail.com', 587, 'username', '')
    with pytest.raises(ValueError):
        task_func('smtp.gmail.com', 587, '', 'password')
    with pytest.raises(ValueError):
        task_func('', 587, 'username', 'password')
    with pytest.raises(ValueError):
        task_func('smtp.gmail.com', '', 'username', 'password')
    with pytest.raises(ValueError):
        task_func('smtp.gmail.com', 587, '', '')
    with pytest.raises(ValueError):
        task_func('', '', '', '')