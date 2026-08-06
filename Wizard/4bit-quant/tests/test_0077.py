python
import random
import string
import pytest
from django.http import HttpResponse

def task_func(request, session_expire_time):
    session_key = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    
    has_digit = any(char.isdigit() for char in session_key)
    has_letter = any(char.isalpha() for char in session_key)
    if not (has_digit and has_letter or len(session_key)!=20):
        raise ValueError("Session key should contain both letters and digits")

    response = HttpResponse('Session key generated successfully.')
    response.set_cookie('session_key', session_key, max_age=session_expire_time)
    return response

def test_task_func():
    request = None
    session_expire_time = 600
    response = task_func(request, session_expire_time)
    assert response.cookies['session_key'].value is not None
    assert response.cookies['session_key']['max-age'] == session_expire_time
    assert response.content == b'Session key generated successfully.'