import pytest
from src_0077 import task_func

def test_task_func_valid_session_key():
    request = None
    session_expire_time = 1000
    response = task_func(request, session_expire_time)
    assert response.status_code == 200
    assert response.content == b'Session key generated successfully.'
    assert response.cookies['session_key'] == session_key

def test_task_func_invalid_session_key():
    request = None
    session_expire_time = 1000
    response = task_func(request, session_expire_time)
    assert response.status_code == 400
    assert response.content == b'Session key should contain both letters and digits'
    assert 'session_key' not in response.cookies