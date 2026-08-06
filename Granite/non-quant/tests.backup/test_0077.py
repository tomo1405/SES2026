import pytest
from src_0077 import task_func

def test_task_func():
    request = # mock the request object
    session_expire_time = # set a valid session expire time
    response = task_func(request, session_expire_time)
    
    assert response.status_code == 200
    assert 'Session key generated successfully.' in response.content.decode('utf-8')
    assert 'session_key' in response.cookies
    assert response.cookies['session_key'] == session_key