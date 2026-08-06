import pytest
from src_0077 import task_func
from django.http import HttpResponse
from django.test import RequestFactory

@pytest.fixture
def request_factory():
    return RequestFactory()

def test_task_func_success(request_factory):
    request = request_factory.get('/')
    session_expire_time = 3600
    response = task_func(request, session_expire_time)
    assert isinstance(response, HttpResponse)
    assert response.content == b'Session key generated successfully.'
    assert 'session_key' in response.cookies
    session_key = response.cookies['session_key'].value
    assert len(session_key) == 20
    assert any(char.isdigit() for char in session_key)
    assert any(char.isalpha() for char in session_key)

def test_task_func_invalid_session_key(request_factory):
    request = request_factory.get('/')
    session_expire_time = 3600
    with pytest.raises(ValueError) as excinfo:
        task_func(request, session_expire_time)
    assert "Session key should contain both letters and digits" in str(excinfo.value)