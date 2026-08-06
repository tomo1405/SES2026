import pytest
from src_0077 import task_func

def test_task_func_valid_session_key():
    request = HttpRequest()
    session_expire_time = 3600
    response = task_func(request, session_expire_time)
    assert response.status_code == 200
    assert response.cookies['session_key'] == ''.join(random.choices(string.ascii_letters + string.digits, k=20))

def test_task_func_invalid_session_key():
    request = HttpRequest()
    session_expire_time = 3600
    response = task_func(request, session_expire_time)
    assert response.status_code == 400
    assert response.cookies['session_key'] == ''