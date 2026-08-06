import pytest
from django.http import HttpResponse
from src_0077 import task_func

def test_task_func_success(mocker):
    # Mock the random.choices to return a known value
    mocker.patch('random.choices', return_value=list('a1b2c3d4e5f6g7h8i9j0'))
    
    request = mocker.Mock()
    session_expire_time = 3600
    
    response = task_func(request, session_expire_time)
    
    assert isinstance(response, HttpResponse)
    assert response.content == b'Session key generated successfully.'
    assert response.cookies['session_key'].value == 'a1b2c3d4e5f6g7h8i9j0'
    assert response.cookies['session_key']['max-age'] == 3600

def test_task_func_invalid_session_key(mocker):
    # Mock the random.choices to return a value without digits or letters
    mocker.patch('random.choices', return_value=list('aaaaaaaaaaaaaaaaaaaa'))
    
    request = mocker.Mock()
    session_expire_time = 3600
    
    with pytest.raises(ValueError) as excinfo:
        task_func(request, session_expire_time)
    
    assert str(excinfo.value) == "Session key should contain both letters and digits"

def test_task_func_invalid_length(mocker):
    # Mock the random.choices to return a value with incorrect length
    mocker.patch('random.choices', return_value=list('a1b2c3d4e5f6g7h8i9j'))
    
    request = mocker.Mock()
    session_expire_time = 3600
    
    with pytest.raises(ValueError) as excinfo:
        task_func(request, session_expire_time)
    
    assert str(excinfo.value) == "Session key should contain both letters and digits"